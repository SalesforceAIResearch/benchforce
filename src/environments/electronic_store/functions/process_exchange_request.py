from src.classes.function import Function
from typing import Dict, Any, Optional
import json
from src.environments.electronic_store.utils.data_utils import execute_sql_query

class ProcessExchangeRequest(Function):

    ALLOWED_REASONS = {"defective", "wrong item", "changed mind"}

    @staticmethod
    def apply(data: Dict[str, Any], order_id:str, exchanged_product_id: str, barcode: str, reason_for_exchange: Optional[str]) -> Dict[str, Any]:
        """
        Determines whether a customer is eligible for a product exchange.
        The function performs the following checks: 

        1. Validate the exchanged_product_id exists in the user's purchase history to ensure that the product being exchanged was actually purchased from the store.
        2. Validate the barcode is available in inventory, if new product is out of stock, deny the exchange.
        3. Check if the reason_for_exchange is valid.
        4. Check if the price of the new product is equal to or greater than the exchanged product, otherwise deny the exchange.
        5. If the exchange is valid, returns True, otherwise returns False.

        Args:
            data (Dict[str, Any]): Environment data dictionary.
            order_id (str): The ID of the order containing the originally purchased product.
            exchanged_product_id (str): The ID of the product to be exchanged.
            barcode (str): The code of the new product to exchange for.
            reason_for_exchange (optional str): The reason for the exchange.
        Returns:
            Dict[str, Any]: A decision object containing:
                - allowed (bool): Whether the exchange is permitted
                - message (str): User-friendly explanation

        """
        customer_id = data.get("customer_id")

        if not customer_id:
            return {
                "allowed": False,
                "message": "Customer information is missing."
            }

        if reason_for_exchange not in ProcessExchangeRequest.ALLOWED_REASONS:
            return {
            "allowed": False,
            "message": "This exchange reason is not eligible under our policy."
        }
        
        try:
            orders = execute_sql_query(
                data=data,
                db_name="customers",
                query="""
                    SELECT order_items
                    FROM orders
                    WHERE order_id = ? AND customer_id = ?
                """,
                params=(order_id, customer_id),
            )

            if not orders:
                return {
                    "allowed": False,
                    "message": "We couldn’t find this order in our system."
                }

            order_items = json.loads(orders[0]["order_items"])
            if exchanged_product_id not in order_items:
                return {
                    "allowed": False,
                    "message": "The selected product was not part of this order."
                }

        except Exception:
            return {
                "allowed": False,
                "message": "We’re unable to verify your order right now."
            }

        try:
            old_products = execute_sql_query(
                data=data,
                db_name="inventory",
                query="""
                    SELECT price
                    FROM products
                    WHERE product_id = ?
                """,
                params=(exchanged_product_id,),
            )

            if not old_products:
                return {
                    "allowed": False,
                    "message": "The original product could not be verified."
                }

            old_price = old_products[0]["price"]

        except Exception:
            return {
                "allowed": False,
                "message": "We’re unable to verify the original product."
            }

        try:
            new_products = execute_sql_query(
                data=data,
                db_name="inventory",
                query="""
                    SELECT price, quantity
                    FROM products
                    WHERE product_id = ?
                """,
                params=(barcode,),
            )

            if not new_products:
                return {
                    "allowed": False,
                    "message": "The replacement product could not be found."
                }

            new_price = new_products[0]["price"]
            new_quantity = new_products[0]["quantity"]

            if new_quantity <= 0:
                return {
                    "allowed": False,
                    "message": "The requested replacement item is currently out of stock."
                }

            if new_price < old_price:
                return {
                    "allowed": False,
                    "message": "The replacement item must be the same price or higher."
                }

        except Exception:
            return {
                "allowed": False,
                "message": "We’re unable to check product availability right now."
            }

        return {
            "allowed": True,
            "message": "This exchange meets our policy and can be processed at the counter."
        }



    def get_metadata() -> dict:
        return {
            "name": "ProcessExchangeRequest",
            "description": "Checks whether a customer is eligible for a product exchange based on store policy.",
            "parameters": {
                "order_id": {
                    "type": "string",
                    "description": "Order containing the originally purchased product",
                },
                "exchanged_product_id": {
                    "type": "string",
                    "description": "Previously purchased product ID",
                },
                "barcode": {
                    "type": "string",
                    "description": "Replacement product ID",
                },
                "reason_for_exchange": {
                    "type": "string",
                    "enum": ["defective", "wrong item", "changed mind"],
                },
            },
            "required": ["order_id", "exchanged_product_id", "barcode", "reason_for_exchange"],
        }

