import json
import unittest
from unittest.mock import patch

from src.environments.electronic_store.functions.process_exchange_request import ProcessExchangeRequest


class TestProcessExchangeRequest(unittest.TestCase):

    def setUp(self):
        self.base_data = {"customer_id": "CUST001"}
        self.order_id = "ORD001"
        self.old_product_id = "PRD001"
        self.new_product_id = "PRD002"


    @patch("src.environments.electronic_store.functions.process_exchange_request.execute_sql_query")
    def test_exchange_allowed(self, mock_execute):
        mock_execute.side_effect = [
            # Orders query
            [{"order_items": json.dumps([self.old_product_id])}],
            # Old product price
            [{"price": 500.0}],
            # New product price & quantity
            [{"price": 600.0, "quantity": 3}],
        ]

        result = ProcessExchangeRequest.apply(
            data=self.base_data,
            order_id=self.order_id,
            exchanged_product_id=self.old_product_id,
            barcode=self.new_product_id,
            reason_for_exchange="defective",
        )

        self.assertTrue(result["allowed"])
        self.assertIn("processed", result["message"].lower())

    def test_exchange_fails_invalid_reason(self):
        result = ProcessExchangeRequest.apply(
            data=self.base_data,
            order_id=self.order_id,
            exchanged_product_id=self.old_product_id,
            barcode=self.new_product_id,
            reason_for_exchange="invalid",
        )

        self.assertFalse(result["allowed"])
        self.assertIn("policy", result["message"].lower())

    @patch(
        "src.environments.electronic_store.functions.process_exchange_request.execute_sql_query"
    )
    def test_exchange_fails_order_not_found(self, mock_execute):
        mock_execute.side_effect = [[]]

        result = ProcessExchangeRequest.apply(
            data=self.base_data,
            order_id="ORD404",
            exchanged_product_id=self.old_product_id,
            barcode=self.new_product_id,
            reason_for_exchange="defective",
        )

        self.assertFalse(result["allowed"])
        self.assertIn("order", result["message"].lower())

    @patch(
        "src.environments.electronic_store.functions.process_exchange_request.execute_sql_query"
    )
    def test_exchange_fails_product_not_in_order(self, mock_execute):
        mock_execute.side_effect = [
            [{"order_items": json.dumps(["PRD999"])}],
        ]

        result = ProcessExchangeRequest.apply(
            data=self.base_data,
            order_id=self.order_id,
            exchanged_product_id=self.old_product_id,
            barcode=self.new_product_id,
            reason_for_exchange="defective",
        )

        self.assertFalse(result["allowed"])
        self.assertIn("not part", result["message"].lower())

    @patch(
    "src.environments.electronic_store.functions.process_exchange_request.execute_sql_query"
)
    def test_exchange_fails_out_of_stock(self, mock_execute):
        mock_execute.side_effect = [
            [{"order_items": json.dumps([self.old_product_id])}],
            [{"price": 500.0}],
            [{"price": 600.0, "quantity": 0}],
        ]

        result = ProcessExchangeRequest.apply(
            data=self.base_data,
            order_id=self.order_id,
            exchanged_product_id=self.old_product_id,
            barcode=self.new_product_id,
            reason_for_exchange="wrong item",
        )

        self.assertFalse(result["allowed"])
        self.assertIn("out of stock", result["message"].lower())


    @patch(
    "src.environments.electronic_store.functions.process_exchange_request.execute_sql_query"
)
    def test_exchange_fails_price_lower(self, mock_execute):
        mock_execute.side_effect = [
            [{"order_items": json.dumps([self.old_product_id])}],
            [{"price": 500.0}],
            [{"price": 400.0, "quantity": 5}],
        ]

        result = ProcessExchangeRequest.apply(
            data=self.base_data,
            order_id=self.order_id,
            exchanged_product_id=self.old_product_id,
            barcode=self.new_product_id,
            reason_for_exchange="changed mind",
        )

        self.assertFalse(result["allowed"])
        self.assertIn("same price or higher", result["message"].lower())



if __name__ == "__main__":
    unittest.main(verbosity=2)