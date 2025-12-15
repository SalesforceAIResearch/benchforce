from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import List, Tuple, Optional


# Small helpers

def _db_now_iso() -> str:
    """Return current timestamp in ISO format (seconds precision)."""
    import datetime as _dt
    return _dt.datetime.now().isoformat(timespec="seconds")


# -------------------------------------------------------------------
# 1) Schema creation
# -------------------------------------------------------------------

def create_customer_schema(cursor: sqlite3.Cursor) -> None:
    """Create all customer-related tables."""

    # Branches
    cursor.execute(
        """
        CREATE TABLE branches (
            branch_id    TEXT PRIMARY KEY,
            branch_name  TEXT NOT NULL,
            city         TEXT NOT NULL,
            state        TEXT NOT NULL,
            ZIP_code     TEXT NOT NULL,
            phone        TEXT NOT NULL UNIQUE,
            manager_name TEXT NOT NULL,
            branch_code  TEXT NOT NULL UNIQUE
        )
        """
    )

    # Customers
    cursor.execute(
        """
        CREATE TABLE customers (
            customer_id     TEXT PRIMARY KEY,
            branch_id       TEXT NOT NULL,
            ssn             TEXT NOT NULL UNIQUE,
            customer_name   TEXT NOT NULL,
            customer_email  TEXT NOT NULL UNIQUE,
            customer_phone  TEXT NOT NULL UNIQUE,
            annual_income   INTEGER NOT NULL,
            credit_limit    INTEGER NOT NULL,
            FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
        )
        """
    )

    # Customer addresses
    cursor.execute(
        """
        CREATE TABLE customer_addresses (
            address_id   TEXT PRIMARY KEY,
            customer_id  TEXT NOT NULL,
            city         TEXT NOT NULL,
            street       TEXT NOT NULL,
            postal_code  TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
        """
    )

    # Orders (order_items stored as JSON TEXT representing an array)
    cursor.execute(
        """
        CREATE TABLE orders (
            order_id       TEXT PRIMARY KEY,
            customer_id    TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            order_items    TEXT NOT NULL,
            order_date     TEXT NOT NULL,
            total_price    REAL NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
        """
    )

    # Finance applications
    cursor.execute(
        """
        CREATE TABLE finance_applications (
            application_id     TEXT PRIMARY KEY,
            customer_id        TEXT NOT NULL,
            branch_id          TEXT NOT NULL,
            application_date   TEXT NOT NULL,
            requested_amount   REAL NOT NULL,
            approved_amount    REAL NOT NULL,
            application_status INTEGER NOT NULL, -- stored as 0/1 for False/True
            credit_limit       INTEGER NOT NULL,
            annual_income      INTEGER NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (branch_id)   REFERENCES branches(branch_id)
        )
        """
    )

    # Customer complaints
    cursor.execute(
        """
        CREATE TABLE customer_complaints (
            complaint_id     TEXT PRIMARY KEY,
            customer_id      TEXT NOT NULL,
            order_id         TEXT NOT NULL,
            branch_id        TEXT NOT NULL,
            complaint_type   TEXT NOT NULL,
            complaint_text   TEXT NOT NULL,
            status           TEXT NOT NULL,
            created_at       TEXT NOT NULL,
            resolved_at      TEXT,
            resolution_notes TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (order_id)    REFERENCES orders(order_id),
            FOREIGN KEY (branch_id)   REFERENCES branches(branch_id)
        )
        """
    )



def populate_customer_data(cursor: sqlite3.Cursor) -> None:
    """Insert seed data for branches, customers, addresses, orders, finance apps, complaints."""

    
    # Branches 
    branches_data: List[Tuple[str, str, str, str, str, str, str, str]] = [
        (
            "BRC001",
            "New York Main Branch",
            "New York",
            "NY",
            "10001",
            "1-212-000-0001",
            "Michael Thompson",
            "BRN_NY_MAIN",
        ),
        (
            "BRC002",
            "Los Angeles City Branch",
            "Los Angeles",
            "CA",
            "90001",
            "1-212-000-0002",
            "Jessica Miller",
            "BRN_CA_LA",
        ),
        (
            "BRC003",
            "Chicago Downtown Branch",
            "Chicago",
            "IL",
            "60601",
            "1-212-000-0003",
            "Brian Anderson",
            "BRN_IL_CHI",
        ),
    ]

    cursor.executemany(
        """
        INSERT INTO branches
            (branch_id, branch_name, city, state, ZIP_code, phone, manager_name, branch_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        branches_data,
    )

    # Customers 
    customers_data: List[Tuple[str, str, str, str, str, str, int, int]] = [
        ("CUST001", "BRC001", "400-00-0001", "James Smith",        "james.smith1@example.com",        "+1-555-0001", 50000, 15000),
        ("CUST002", "BRC002", "400-00-0002", "Mary Johnson",       "mary.johnson2@example.com",       "+1-555-0002", 50000, 15000),
        ("CUST003", "BRC003", "400-00-0003", "Robert Williams",    "robert.williams3@example.com",    "+1-555-0003", 50000, 15000),
        ("CUST004", "BRC001", "400-00-0004", "Patricia Brown",     "patricia.brown4@example.com",     "+1-555-0004", 50000, 15000),
        ("CUST005", "BRC002", "400-00-0005", "John Jones",         "john.jones5@example.com",         "+1-555-0005", 50000, 15000),
        ("CUST006", "BRC003", "400-00-0006", "Jennifer Garcia",    "jennifer.garcia6@example.com",    "+1-555-0006", 50000, 15000),
        ("CUST007", "BRC001", "400-00-0007", "Michael Miller",     "michael.miller7@example.com",     "+1-555-0007", 50000, 15000),
        ("CUST008", "BRC002", "400-00-0008", "Linda Davis",        "linda.davis8@example.com",        "+1-555-0008", 50000, 15000),
        ("CUST009", "BRC003", "400-00-0009", "William Rodriguez",  "william.rodriguez9@example.com",  "+1-555-0009", 50000, 15000),
        ("CUST010", "BRC001", "400-00-0010", "Elizabeth Martinez", "elizabeth.martinez10@example.com","+1-555-0010", 50000, 15000),

        ("CUST011", "BRC002", "400-00-0011", "James Smith",        "james.smith11@example.com",       "+1-555-0011", 60000, 20000),
        ("CUST012", "BRC003", "400-00-0012", "Mary Johnson",       "mary.johnson12@example.com",      "+1-555-0012", 60000, 20000),
        ("CUST013", "BRC001", "400-00-0013", "Robert Williams",    "robert.williams13@example.com",   "+1-555-0013", 60000, 20000),
        ("CUST014", "BRC002", "400-00-0014", "Patricia Brown",     "patricia.brown14@example.com",    "+1-555-0014", 60000, 20000),
        ("CUST015", "BRC003", "400-00-0015", "John Jones",         "john.jones15@example.com",        "+1-555-0015", 60000, 20000),
        ("CUST016", "BRC001", "400-00-0016", "Jennifer Garcia",    "jennifer.garcia16@example.com",   "+1-555-0016", 60000, 20000),
        ("CUST017", "BRC002", "400-00-0017", "Michael Miller",     "michael.miller17@example.com",    "+1-555-0017", 60000, 20000),
        ("CUST018", "BRC003", "400-00-0018", "Linda Davis",        "linda.davis18@example.com",       "+1-555-0018", 60000, 20000),
        ("CUST019", "BRC001", "400-00-0019", "William Rodriguez",  "william.rodriguez19@example.com", "+1-555-0019", 60000, 20000),
        ("CUST020", "BRC002", "400-00-0020", "Elizabeth Martinez", "elizabeth.martinez20@example.com","+1-555-0020", 60000, 20000),

        ("CUST021", "BRC003", "400-00-0021", "James Smith",        "james.smith21@example.com",       "+1-555-0021", 70000, 25000),
        ("CUST022", "BRC001", "400-00-0022", "Mary Johnson",       "mary.johnson22@example.com",      "+1-555-0022", 70000, 25000),
        ("CUST023", "BRC002", "400-00-0023", "Robert Williams",    "robert.williams23@example.com",   "+1-555-0023", 70000, 25000),
        ("CUST024", "BRC003", "400-00-0024", "Patricia Brown",     "patricia.brown24@example.com",    "+1-555-0024", 70000, 25000),
        ("CUST025", "BRC001", "400-00-0025", "John Jones",         "john.jones25@example.com",        "+1-555-0025", 70000, 25000),
        ("CUST026", "BRC002", "400-00-0026", "Jennifer Garcia",    "jennifer.garcia26@example.com",   "+1-555-0026", 70000, 25000),
        ("CUST027", "BRC003", "400-00-0027", "Michael Miller",     "michael.miller27@example.com",    "+1-555-0027", 70000, 25000),
        ("CUST028", "BRC001", "400-00-0028", "Linda Davis",        "linda.davis28@example.com",       "+1-555-0028", 70000, 25000),
        ("CUST029", "BRC002", "400-00-0029", "William Rodriguez",  "william.rodriguez29@example.com", "+1-555-0029", 70000, 25000),
        ("CUST030", "BRC003", "400-00-0030", "Elizabeth Martinez", "elizabeth.martinez30@example.com","+1-555-0030", 70000, 25000),

        ("CUST031", "BRC001", "400-00-0031", "James Smith",        "james.smith31@example.com",       "+1-555-0031", 80000, 30000),
        ("CUST032", "BRC002", "400-00-0032", "Mary Johnson",       "mary.johnson32@example.com",      "+1-555-0032", 80000, 30000),
        ("CUST033", "BRC003", "400-00-0033", "Robert Williams",    "robert.williams33@example.com",   "+1-555-0033", 80000, 30000),
        ("CUST034", "BRC001", "400-00-0034", "Patricia Brown",     "patricia.brown34@example.com",    "+1-555-0034", 80000, 30000),
        ("CUST035", "BRC002", "400-00-0035", "John Jones",         "john.jones35@example.com",        "+1-555-0035", 80000, 30000),
        ("CUST036", "BRC003", "400-00-0036", "Jennifer Garcia",    "jennifer.garcia36@example.com",   "+1-555-0036", 80000, 30000),
        ("CUST037", "BRC001", "400-00-0037", "Michael Miller",     "michael.miller37@example.com",    "+1-555-0037", 80000, 30000),
        ("CUST038", "BRC002", "400-00-0038", "Linda Davis",        "linda.davis38@example.com",       "+1-555-0038", 80000, 30000),
        ("CUST039", "BRC003", "400-00-0039", "William Rodriguez",  "william.rodriguez39@example.com", "+1-555-0039", 80000, 30000),
        ("CUST040", "BRC001", "400-00-0040", "Elizabeth Martinez", "elizabeth.martinez40@example.com","+1-555-0040", 80000, 30000),
    ]

    cursor.executemany(
        """
        INSERT INTO customers
            (customer_id, branch_id, ssn, customer_name, customer_email,
             customer_phone, annual_income, credit_limit)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        customers_data,
    )

    
    # Customer addresses 
    customer_addresses_data: List[Tuple[str, str, str, str, str]] = [
        ("ADDR001", "CUST001", "New York",      "101 5th Ave",          "10001"),
        ("ADDR002", "CUST002", "Los Angeles",   "202 Sunset Blvd",      "90001"),
        ("ADDR003", "CUST003", "Chicago",       "303 Michigan Ave",     "60601"),
        ("ADDR004", "CUST004", "New York",      "104 Madison Ave",      "10001"),
        ("ADDR005", "CUST005", "Los Angeles",   "205 Hollywood Blvd",   "90001"),
        ("ADDR006", "CUST006", "Chicago",       "306 Wacker Dr",        "60601"),
        ("ADDR007", "CUST007", "New York",      "107 Broadway",         "10001"),
        ("ADDR008", "CUST008", "Los Angeles",   "208 Vine St",          "90001"),
        ("ADDR009", "CUST009", "Chicago",       "309 State St",         "60601"),
        ("ADDR010", "CUST010", "New York",      "110 Lexington Ave",    "10001"),

        ("ADDR011", "CUST011", "Los Angeles",   "211 Melrose Ave",      "90001"),
        ("ADDR012", "CUST012", "Chicago",       "312 Lake Shore Dr",    "60601"),
        ("ADDR013", "CUST013", "New York",      "113 Park Ave",         "10001"),
        ("ADDR014", "CUST014", "Los Angeles",   "214 Pico Blvd",        "90001"),
        ("ADDR015", "CUST015", "Chicago",       "315 Clark St",         "60601"),
        ("ADDR016", "CUST016", "New York",      "116 West End Ave",     "10001"),
        ("ADDR017", "CUST017", "Los Angeles",   "217 Olympic Blvd",     "90001"),
        ("ADDR018", "CUST018", "Chicago",       "318 Dearborn St",      "60601"),
        ("ADDR019", "CUST019", "New York",      "119 Columbus Ave",     "10001"),
        ("ADDR020", "CUST020", "Los Angeles",   "220 Beverly Dr",       "90001"),

        ("ADDR021", "CUST021", "Chicago",       "321 Randolph St",      "60601"),
        ("ADDR022", "CUST022", "New York",      "122 7th Ave",          "10001"),
        ("ADDR023", "CUST023", "Los Angeles",   "223 Wilshire Blvd",    "90001"),
        ("ADDR024", "CUST024", "Chicago",       "324 Monroe St",        "60601"),
        ("ADDR025", "CUST025", "New York",      "125 8th Ave",          "10001"),
        ("ADDR026", "CUST026", "Los Angeles",   "226 Fairfax Ave",      "90001"),
        ("ADDR027", "CUST027", "Chicago",       "327 LaSalle St",       "60601"),
        ("ADDR028", "CUST028", "New York",      "128 Amsterdam Ave",    "10001"),
        ("ADDR029", "CUST029", "Los Angeles",   "229 Highland Ave",     "90001"),
        ("ADDR030", "CUST030", "Chicago",       "330 Wells St",         "60601"),

        ("ADDR031", "CUST031", "New York",      "131 9th Ave",          "10001"),
        ("ADDR032", "CUST032", "Los Angeles",   "232 Figueroa St",      "90001"),
        ("ADDR033", "CUST033", "Chicago",       "333 Jackson Blvd",     "60601"),
        ("ADDR034", "CUST034", "New York",      "134 10th Ave",         "10001"),
        ("ADDR035", "CUST035", "Los Angeles",   "235 Olympic Way",      "90001"),
        ("ADDR036", "CUST036", "Chicago",       "336 Franklin St",      "60601"),
        ("ADDR037", "CUST037", "New York",      "137 Riverside Dr",     "10001"),
        ("ADDR038", "CUST038", "Los Angeles",   "238 Sunset Plaza",     "90001"),
        ("ADDR039", "CUST039", "Chicago",       "339 Polk St",          "60601"),
        ("ADDR040", "CUST040", "New York",      "140 West 34th St",     "10001"),
    ]

    cursor.executemany(
        """
        INSERT INTO customer_addresses
            (address_id, customer_id, city, street, postal_code)
        VALUES (?, ?, ?, ?, ?)
        """,
        customer_addresses_data,
    )

    # -------------------------
    # Orders 
    orders_data: List[Tuple[str, str, str, str, str, float]] = [
        ("ORD001", "CUST001", "james.smith1@example.com",        '["PRD001"]',                      "2024-02-01T10:00:00", 199.99),
        ("ORD002", "CUST002", "mary.johnson2@example.com",       '["PRD002","PRD003"]',             "2024-02-02T10:15:00", 499.99),
        ("ORD003", "CUST003", "robert.williams3@example.com",    '["PRD003"]',                      "2024-02-03T11:00:00", 249.99),
        ("ORD004", "CUST004", "patricia.brown4@example.com",     '["PRD004","PRD005"]',             "2024-02-04T11:30:00", 549.99),
        ("ORD005", "CUST005", "john.jones5@example.com",         '["PRD005"]',                      "2024-02-05T12:00:00", 179.99),
        ("ORD006", "CUST006", "jennifer.garcia6@example.com",    '["PRD006","PRD007"]',             "2024-02-06T09:45:00", 529.99),
        ("ORD007", "CUST007", "michael.miller7@example.com",     '["PRD007"]',                      "2024-02-07T10:20:00", 299.99),
        ("ORD008", "CUST008", "linda.davis8@example.com",        '["PRD008","PRD009"]',             "2024-02-08T14:10:00", 459.99),
        ("ORD009", "CUST009", "william.rodriguez9@example.com",  '["PRD009"]',                      "2024-02-09T15:05:00", 219.99),
        ("ORD010", "CUST010", "elizabeth.martinez10@example.com",'["PRD010","PRD001"]',             "2024-02-10T16:30:00", 599.99),

        ("ORD011", "CUST011", "james.smith11@example.com",       '["PRD002"]',                      "2024-02-11T10:00:00", 209.99),
        ("ORD012", "CUST012", "mary.johnson12@example.com",      '["PRD003","PRD004"]',             "2024-02-12T11:15:00", 489.99),
        ("ORD013", "CUST013", "robert.williams13@example.com",   '["PRD004"]',                      "2024-02-13T12:40:00", 259.99),
        ("ORD014", "CUST014", "patricia.brown14@example.com",    '["PRD005","PRD006"]',             "2024-02-14T13:25:00", 519.99),
        ("ORD015", "CUST015", "john.jones15@example.com",        '["PRD006"]',                      "2024-02-15T09:35:00", 189.99),
        ("ORD016", "CUST016", "jennifer.garcia16@example.com",   '["PRD007","PRD008"]',             "2024-02-16T10:50:00", 539.99),
        ("ORD017", "CUST017", "michael.miller17@example.com",    '["PRD008"]',                      "2024-02-17T11:05:00", 229.99),
        ("ORD018", "CUST018", "linda.davis18@example.com",       '["PRD009","PRD010"]',             "2024-02-18T14:55:00", 569.99),
        ("ORD019", "CUST019", "william.rodriguez19@example.com", '["PRD010"]',                      "2024-02-19T15:20:00", 279.99),
        ("ORD020", "CUST020", "elizabeth.martinez20@example.com",'["PRD001","PRD002"]',             "2024-02-20T16:45:00", 609.99),

        ("ORD021", "CUST021", "james.smith21@example.com",       '["PRD003"]',                      "2024-02-21T09:15:00", 219.99),
        ("ORD022", "CUST022", "mary.johnson22@example.com",      '["PRD004","PRD005"]',             "2024-02-22T10:25:00", 499.99),
        ("ORD023", "CUST023", "robert.williams23@example.com",   '["PRD005"]',                      "2024-02-23T11:45:00", 239.99),
        ("ORD024", "CUST024", "patricia.brown24@example.com",    '["PRD006","PRD007"]',             "2024-02-24T12:35:00", 529.99),
        ("ORD025", "CUST025", "john.jones25@example.com",        '["PRD007"]',                      "2024-02-25T13:05:00", 249.99),
        ("ORD026", "CUST026", "jennifer.garcia26@example.com",   '["PRD008","PRD009"]',             "2024-02-26T09:55:00", 559.99),
        ("ORD027", "CUST027", "michael.miller27@example.com",    '["PRD009"]',                      "2024-02-27T10:40:00", 269.99),
        ("ORD028", "CUST028", "linda.davis28@example.com",       '["PRD010","PRD001"]',             "2024-02-28T11:20:00", 589.99),
        ("ORD029", "CUST029", "william.rodriguez29@example.com", '["PRD001"]',                      "2024-02-29T14:05:00", 259.99),
        ("ORD030", "CUST030", "elizabeth.martinez30@example.com",'["PRD002","PRD003"]',             "2024-03-01T15:10:00", 519.99),

        ("ORD031", "CUST031", "james.smith31@example.com",       '["PRD004"]',                      "2024-03-02T10:30:00", 229.99),
        ("ORD032", "CUST032", "mary.johnson32@example.com",      '["PRD005","PRD006"]',             "2024-03-03T11:10:00", 549.99),
        ("ORD033", "CUST033", "robert.williams33@example.com",   '["PRD006"]',                      "2024-03-04T12:25:00", 239.99),
        ("ORD034", "CUST034", "patricia.brown34@example.com",    '["PRD007","PRD008"]',             "2024-03-05T13:15:00", 569.99),
        ("ORD035", "CUST035", "john.jones35@example.com",        '["PRD008"]',                      "2024-03-06T09:40:00", 249.99),
        ("ORD036", "CUST036", "jennifer.garcia36@example.com",   '["PRD009","PRD010"]',             "2024-03-07T10:35:00", 579.99),
        ("ORD037", "CUST037", "michael.miller37@example.com",    '["PRD010"]',                      "2024-03-08T11:50:00", 269.99),
        ("ORD038", "CUST038", "linda.davis38@example.com",       '["PRD001","PRD002"]',             "2024-03-09T14:30:00", 599.99),
        ("ORD039", "CUST039", "william.rodriguez39@example.com", '["PRD003"]',                      "2024-03-10T15:25:00", 219.99),
        ("ORD040", "CUST040", "elizabeth.martinez40@example.com",'["PRD004","PRD005"]',             "2024-03-11T16:05:00", 529.99),
    ]

    cursor.executemany(
        """
        INSERT INTO orders
            (order_id, customer_id, customer_email, order_items, order_date, total_price)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        orders_data,
    )

    # Finance applications 
    finance_applications_data: List[Tuple[str, str, str, str, float, float, int, int, int]] = [
        ("FAPP001", "CUST001", "BRC001", "2024-03-15T09:00:00", 12000.0, 12000.0, 1, 15000, 50000),
        ("FAPP002", "CUST002", "BRC002", "2024-03-16T09:10:00", 12000.0,  8000.0, 0, 15000, 50000),
        ("FAPP003", "CUST003", "BRC003", "2024-03-17T09:20:00", 12000.0, 12000.0, 1, 15000, 50000),
        ("FAPP004", "CUST004", "BRC001", "2024-03-18T09:30:00", 12000.0,  9000.0, 0, 15000, 50000),
        ("FAPP005", "CUST005", "BRC002", "2024-03-19T09:40:00", 12000.0, 12000.0, 1, 15000, 50000),
        ("FAPP006", "CUST006", "BRC003", "2024-03-20T09:50:00", 12000.0,  7000.0, 0, 15000, 50000),
        ("FAPP007", "CUST007", "BRC001", "2024-03-21T10:00:00", 12000.0, 12000.0, 1, 15000, 50000),
        ("FAPP008", "CUST008", "BRC002", "2024-03-22T10:10:00", 12000.0,  9000.0, 0, 15000, 50000),
        ("FAPP009", "CUST009", "BRC003", "2024-03-23T10:20:00", 12000.0, 12000.0, 1, 15000, 50000),
        ("FAPP010", "CUST010", "BRC001", "2024-03-24T10:30:00", 12000.0,  9500.0, 0, 15000, 50000),

        ("FAPP011", "CUST011", "BRC002", "2024-03-25T09:00:00", 16000.0, 16000.0, 1, 20000, 60000),
        ("FAPP012", "CUST012", "BRC003", "2024-03-26T09:10:00", 16000.0, 10000.0, 0, 20000, 60000),
        ("FAPP013", "CUST013", "BRC001", "2024-03-27T09:20:00", 16000.0, 16000.0, 1, 20000, 60000),
        ("FAPP014", "CUST014", "BRC002", "2024-03-28T09:30:00", 16000.0, 11000.0, 0, 20000, 60000),
        ("FAPP015", "CUST015", "BRC003", "2024-03-29T09:40:00", 16000.0, 16000.0, 1, 20000, 60000),
        ("FAPP016", "CUST016", "BRC001", "2024-03-30T09:50:00", 16000.0,  9500.0, 0, 20000, 60000),
        ("FAPP017", "CUST017", "BRC002", "2024-03-31T10:00:00", 16000.0, 16000.0, 1, 20000, 60000),
        ("FAPP018", "CUST018", "BRC003", "2024-04-01T10:10:00", 16000.0, 10500.0, 0, 20000, 60000),
        ("FAPP019", "CUST019", "BRC001", "2024-04-02T10:20:00", 16000.0, 16000.0, 1, 20000, 60000),
        ("FAPP020", "CUST020", "BRC002", "2024-04-03T10:30:00", 16000.0, 12000.0, 0, 20000, 60000),

        ("FAPP021", "CUST021", "BRC003", "2024-04-04T09:00:00", 20000.0, 20000.0, 1, 25000, 70000),
        ("FAPP022", "CUST022", "BRC001", "2024-04-05T09:10:00", 20000.0, 13000.0, 0, 25000, 70000),
        ("FAPP023", "CUST023", "BRC002", "2024-04-06T09:20:00", 20000.0, 20000.0, 1, 25000, 70000),
        ("FAPP024", "CUST024", "BRC003", "2024-04-07T09:30:00", 20000.0, 14000.0, 0, 25000, 70000),
        ("FAPP025", "CUST025", "BRC001", "2024-04-08T09:40:00", 20000.0, 20000.0, 1, 25000, 70000),
        ("FAPP026", "CUST026", "BRC002", "2024-04-09T09:50:00", 20000.0, 15000.0, 0, 25000, 70000),
        ("FAPP027", "CUST027", "BRC003", "2024-04-10T10:00:00", 20000.0, 20000.0, 1, 25000, 70000),
        ("FAPP028", "CUST028", "BRC001", "2024-04-11T10:10:00", 20000.0, 16000.0, 0, 25000, 70000),
        ("FAPP029", "CUST029", "BRC002", "2024-04-12T10:20:00", 20000.0, 20000.0, 1, 25000, 70000),
        ("FAPP030", "CUST030", "BRC003", "2024-04-13T10:30:00", 20000.0, 17000.0, 0, 25000, 70000),

        ("FAPP031", "CUST031", "BRC001", "2024-04-14T09:00:00", 24000.0, 24000.0, 1, 30000, 80000),
        ("FAPP032", "CUST032", "BRC002", "2024-04-15T09:10:00", 24000.0, 18000.0, 0, 30000, 80000),
        ("FAPP033", "CUST033", "BRC003", "2024-04-16T09:20:00", 24000.0, 24000.0, 1, 30000, 80000),
        ("FAPP034", "CUST034", "BRC001", "2024-04-17T09:30:00", 24000.0, 19000.0, 0, 30000, 80000),
        ("FAPP035", "CUST035", "BRC002", "2024-04-18T09:40:00", 24000.0, 24000.0, 1, 30000, 80000),
        ("FAPP036", "CUST036", "BRC003", "2024-04-19T09:50:00", 24000.0, 20000.0, 0, 30000, 80000),
        ("FAPP037", "CUST037", "BRC001", "2024-04-20T10:00:00", 24000.0, 24000.0, 1, 30000, 80000),
        ("FAPP038", "CUST038", "BRC002", "2024-04-21T10:10:00", 24000.0, 21000.0, 0, 30000, 80000),
        ("FAPP039", "CUST039", "BRC003", "2024-04-22T10:20:00", 24000.0, 24000.0, 1, 30000, 80000),
        ("FAPP040", "CUST040", "BRC001", "2024-04-23T10:30:00", 24000.0, 22000.0, 0, 30000, 80000),
    ]

    cursor.executemany(
        """
        INSERT INTO finance_applications
            (application_id, customer_id, branch_id, application_date,
             requested_amount, approved_amount, application_status,
             credit_limit, annual_income)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        finance_applications_data,
    )

    # Customer complaints 
    customer_complaints_data: List[Tuple[str, str, str, str, str, str, str, str, Optional[str], Optional[str]]] = [
        (
            "CMP001",
            "CUST001",
            "ORD001",
            "BRC001",
            "product",
            "Customer reported a defect in the smartphone screen.",
            "open",
            "2024-05-01T11:00:00",
            None,
            "Awaiting technician inspection.",
        ),
        (
            "CMP002",
            "CUST003",
            "ORD003",
            "BRC003",
            "order",
            "Order arrived later than the estimated delivery date.",
            "in_progress",
            "2024-05-02T12:15:00",
            None,
            "Investigation with shipping provider is ongoing.",
        ),
        (
            "CMP003",
            "CUST005",
            "ORD005",
            "BRC002",
            "billing",
            "Customer claims an incorrect charge on the invoice.",
            "resolved",
            "2024-05-03T09:45:00",
            "2024-05-06T10:00:00",
            "Invoice adjusted and partial refund issued.",
        ),
        (
            "CMP004",
            "CUST007",
            "ORD007",
            "BRC001",
            "tech",
            "Difficulty pairing the wireless headphones with device.",
            "closed",
            "2024-05-04T10:30:00",
            "2024-05-07T11:10:00",
            "Provided step-by-step guide and in-store assistance.",
        ),
        (
            "CMP005",
            "CUST009",
            "ORD009",
            "BRC003",
            "refund",
            "Customer requested a refund within the return window.",
            "resolved",
            "2024-05-05T14:20:00",
            "2024-05-08T15:00:00",
            "Full refund processed to original payment method.",
        ),
        (
            "CMP006",
            "CUST011",
            "ORD011",
            "BRC002",
            "product",
            "Reported dead pixels on the newly purchased monitor.",
            "in_progress",
            "2024-05-06T13:05:00",
            None,
            "Replacement monitor being arranged with supplier.",
        ),
        (
            "CMP007",
            "CUST013",
            "ORD013",
            "BRC001",
            "order",
            "Wrong color variant of the laptop was delivered.",
            "resolved",
            "2024-05-07T11:50:00",
            "2024-05-10T09:30:00",
            "Correct color shipped and old unit collected.",
        ),
        (
            "CMP008",
            "CUST015",
            "ORD015",
            "BRC003",
            "billing",
            "Customer was not informed about activation fee.",
            "closed",
            "2024-05-08T16:00:00",
            "2024-05-11T10:15:00",
            "Fee waived as goodwill and policy clarified.",
        ),
        (
            "CMP009",
            "CUST017",
            "ORD017",
            "BRC002",
            "tech",
            "Smartwatch not syncing with mobile app.",
            "resolved",
            "2024-05-09T10:25:00",
            "2024-05-12T11:40:00",
            "Firmware updated and pairing reconfigured successfully.",
        ),
        (
            "CMP010",
            "CUST019",
            "ORD019",
            "BRC001",
            "refund",
            "Customer changed mind and requested store credit.",
            "resolved",
            "2024-05-10T12:10:00",
            "2024-05-13T13:20:00",
            "Store credit issued after product inspection.",
        ),
        (
            "CMP011",
            "CUST021",
            "ORD021",
            "BRC003",
            "product",
            "Speaker has intermittent audio drop issues.",
            "open",
            "2024-05-11T09:55:00",
            None,
            "Product scheduled for diagnostic testing.",
        ),
        (
            "CMP012",
            "CUST023",
            "ORD023",
            "BRC002",
            "order",
            "Customer received incomplete accessories in the box.",
            "in_progress",
            "2024-05-12T15:35:00",
            None,
            "Warehouse notified to ship missing accessories.",
        ),
        (
            "CMP013",
            "CUST025",
            "ORD025",
            "BRC001",
            "billing",
            "Extended warranty was added without explicit consent.",
            "resolved",
            "2024-05-13T10:05:00",
            "2024-05-16T09:45:00",
            "Warranty removed and extra cost refunded.",
        ),
        (
            "CMP014",
            "CUST027",
            "ORD027",
            "BRC003",
            "tech",
            "Game console overheating during normal use.",
            "closed",
            "2024-05-14T11:20:00",
            "2024-05-17T12:30:00",
            "Unit replaced and airflow guidance provided.",
        ),
        (
            "CMP015",
            "CUST029",
            "ORD029",
            "BRC002",
            "other",
            "Customer requested follow-up on loyalty program points.",
            "resolved",
            "2024-05-15T13:40:00",
            "2024-05-18T14:10:00",
            "Points manually adjusted and confirmation emailed.",
        ),
    ]

    cursor.executemany(
        """
        INSERT INTO customer_complaints
            (complaint_id, customer_id, order_id, branch_id, complaint_type,
             complaint_text, status, created_at, resolved_at, resolution_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        customer_complaints_data,
    )

    print("[OK] Populated customer database: 3 branches, 40 customers, 40 addresses, 40 orders, 40 finance apps, 15 complaints.")


# 3) DB initializer

def init_customer_db() -> None:
    """
    Initialize the SQLite database for customer-related data.

    Steps:
    - Remove existing DB if present
    - Create schema
    - Insert seed data
    - Print record counts
    """
    db_path = Path(__file__).parent / "customers.db"

    if db_path.exists():
        os.remove(db_path)
        print(f"Removed existing database: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        create_customer_schema(cursor)
        print("[OK] Created customer-related schema")

        populate_customer_data(cursor)

        conn.commit()
        print(f"\n[OK] Successfully initialized customer database: {db_path}\n")

        tables = [
            "branches",
            "customers",
            "customer_addresses",
            "orders",
            "finance_applications",
            "customer_complaints",
        ]

        print("=" * 60)
        print("CUSTOMER DATABASE - RECORD COUNTS")
        print("=" * 60)
        for t in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {t}")
            count = cursor.fetchone()[0]
            print(f"  {t:.<40} {count:>6} records")
        print("=" * 60)

    except Exception as e:
        conn.rollback()
        print(f"[ERROR] Error initializing customer DB: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    init_customer_db()
