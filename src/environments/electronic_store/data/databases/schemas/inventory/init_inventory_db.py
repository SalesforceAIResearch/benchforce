from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import List, Tuple


# -------------------------------------------------------------------
# 1) Schema creation
# -------------------------------------------------------------------

def create_inventory_schema(cursor: sqlite3.Cursor) -> None:
    """Create all tables for the electronics inventory database."""

    cursor.execute("""
        CREATE TABLE categories (
            category_id    TEXT PRIMARY KEY,
            category_code  TEXT NOT NULL UNIQUE,
            category_name  TEXT NOT NULL,
            description    TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE brands (
            brand_id       TEXT PRIMARY KEY,
            brand_code     TEXT NOT NULL UNIQUE,
            brand_name     TEXT NOT NULL,
            country_origin TEXT,
            is_flagship    INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE branches (
            branch_id    TEXT PRIMARY KEY,
            branch_code  TEXT NOT NULL UNIQUE,
            branch_name  TEXT NOT NULL,
            city         TEXT,
            state        TEXT,
            ZIP_code     TEXT,
            phone        TEXT NOT NULL UNIQUE,
            manager_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE products (
            product_id      TEXT PRIMARY KEY,
            barcode         TEXT NOT NULL,
            model_number    TEXT NOT NULL,       
            category_id     TEXT NOT NULL,
            brand_id        TEXT NOT NULL,
            branch_id       TEXT NOT NULL,
            product_name    TEXT NOT NULL,
            description     TEXT,
            year_of_release TEXT NOT NULL,  -- ISO date string
            quantity        INTEGER NOT NULL,
            warranty_Months INTEGER NOT NULL,
            price           NUMERIC NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(category_id),
            FOREIGN KEY (brand_id)    REFERENCES brands(brand_id),
            FOREIGN KEY (branch_id)   REFERENCES branches(branch_id)
        )
    """)

    cursor.execute("""
        CREATE TABLE lenders_type (
            lender_type_id   TEXT PRIMARY KEY,
            lender_type_code TEXT NOT NULL,
            lender_name      TEXT NOT NULL,
            lender_type      TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE lenders (
            lender_id        TEXT PRIMARY KEY,
            lender_code      INTEGER NOT NULL,
            lender_type_id   TEXT NOT NULL,
            contact_name     TEXT NOT NULL,
            contact_phone    TEXT NOT NULL,
            contact_email    TEXT NOT NULL,
            min_credit_score INTEGER NOT NULL,
            max_term_months  INTEGER NOT NULL,
            FOREIGN KEY (lender_type_id) REFERENCES lenders_type(lender_type_id)
        )
    """)

    # Helpful indexes
    cursor.execute("CREATE INDEX idx_products_category ON products(category_id)")
    cursor.execute("CREATE INDEX idx_products_brand    ON products(brand_id)")
    cursor.execute("CREATE INDEX idx_products_branch   ON products(branch_id)")
    cursor.execute("CREATE INDEX idx_lenders_type      ON lenders(lender_type_id)")


# -------------------------------------------------------------------
# 2) Data population
# -------------------------------------------------------------------

def populate_data(cursor: sqlite3.Cursor) -> None:
    """Insert seed data for all tables (including 200 products)."""

    # -------------------------
    # Categories
    # -------------------------
    categories_data: List[Tuple[str, str, str, str]] = [
        ("CAT110", "CAT001_SMARTPHONES", "Smartphones",
         "Smartphones used for calls, messaging, social media, photography, and mobile internet on the go."),
        ("CAT120", "CAT_002_TABLETS", "Tablets",
         "Portable touch-screen devices ideal for media consumption, light productivity, and studying."),
        ("CAT200", "CAT_003_DESKTOPS", "desktops",
         "Stationary desktop computers for home, office, and gaming with upgradeable components."),
        ("CAT210", "CAT_004_LAPTOPS", "Laptops",
         "Portable computers for work, study, and entertainment with built-in screen and battery."),
        ("CAT220", "CAT_005_MONITORS", "Monitors",
         "External displays used with desktops and laptops for work, gaming, and content creation."),
        ("CAT300", "CAT_006_WEARABLES", "Wearables",
             "Smartwatches and fitness bands that track health, notifications, and daily activity."),
        ("CAT400", "CAT_007_AUDIO", "Audio",
         "Headphones, earbuds, and speakers for music, calls, gaming, and home audio setups."),
        ("CAT500", "CAT_008_TV_HT", "TV & Home Theater",
         "Televisions and home theater equipment for high-quality movies, streaming, and gaming."),
        ("CAT600", "CAT_009_GAMING", "Gaming",
         "Gaming consoles and accessories designed for video games and interactive entertainment."),
        ("CAT700", "CAT_010_NETWORKING", "Networking",
         "Routers and network devices that provide wired and wireless internet connectivity."),
        ("CAT701", "CAT_011_HOME_APPLIANCES", "Home Appliances",
         "Smart home appliances used for everyday household tasks."),
    ]
    cursor.executemany(
        "INSERT INTO categories (category_id, category_code, category_name, description) "
        "VALUES (?, ?, ?, ?)",
        categories_data,
    )

    # -------------------------
    # Brands 
    # -------------------------
    brands_data: List[Tuple[str, str, str, str, int]] = [
        ("BR001", "APPLE", "Apple", "USA", 1),
        ("BR002", "SMSG", "Samsung", "South Korea", 1),
        ("BR003", "XIAO", "Xiaomi", "China", 0),
        ("BR004", "HUA", "Huawei", "China", 0),
        ("BR005", "LEN", "Lenovo", "China", 0),
        ("BR006", "DELL", "Dell", "USA", 0),
        ("BR007", "HP", "HP", "USA", 0),
        ("BR008", "ASUS", "Asus", "Taiwan", 0),
        ("BR009", "SONY", "Sony", "Japan", 1),
        ("BR010", "LG", "LG", "South Korea", 0),
        ("BR011", "MSFT", "Microsoft", "USA", 0),
        ("BR012", "BOSE", "Bose", "USA", 0),
        ("BR013", "LOGI", "Logitech", "Switzerland", 0),
        ("BR014", "NINT", "Nintendo", "Japan", 1),
        ("BR015", "TPLK", "TP-Link", "China", 0),
        ("BR016", "INTC", "Intel", "USA", 0),
        ("BR017", "GOOG", "Google", "USA", 1),
        ("BR018", "QLCM", "Qualcomm", "USA", 0),
    ]
    cursor.executemany(
        "INSERT INTO brands (brand_id, brand_code, brand_name, country_origin, is_flagship) "
        "VALUES (?, ?, ?, ?, ?)",
        brands_data,
    )

    # -------------------------
    # Branches
    # -------------------------
   # (branch_id, branch_code, branch_name, city, state, ZIP_code, phone, manager_name)
    branches_data = [
    ("BRC001", "BRN_NY_MAIN",  "New York Main Branch",       "New York",    "NY", "10001", "+1-212-000-0001", "Store Manager A"),
    ("BRC002", "BRN_CA_LA",    "Los Angeles City Branch",    "Los Angeles", "CA", "90001", "+1-310-000-0002", "Store Manager B"),
    ("BRC003", "BRN_IL_CHI",   "Chicago Downtown Branch",    "Chicago",     "IL", "60601", "+1-312-000-0003", "Store Manager C"),
] 

    cursor.executemany(
        "INSERT INTO branches (branch_id, branch_code, branch_name, city, state, ZIP_code, phone, manager_name) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        branches_data,
    )

    # -------------------------
    # Lender types + lenders
    # -------------------------
    lender_types_data: List[Tuple[str, str, str, str]] = [
        ("LT001", "BANK", "Local Bank Partner", "Bank"),
        ("LT002", "FINTECH", "Fintech Installments", "Fintech"),
        ("LT003", "STORE", "In-store Financing", "In-house"),
    ]
    cursor.executemany(
        "INSERT INTO lenders_type (lender_type_id, lender_type_code, lender_name, lender_type) "
        "VALUES (?, ?, ?, ?)",
        lender_types_data,
    )

    lenders_data: List[Tuple[str, int, str, str, str, str, int, int]] = [
        ("L001", 1001, "LT001", "Bank Sales Team", "+962-6-555-1001", "bank-finance@example.com", 650, 36),
        ("L002", 2001, "LT002", "Fintech Partner", "+962-6-555-2001", "fintech@example.com", 600, 24),
        ("L003", 3001, "LT003", "In-Store Finance Desk", "+962-6-555-3001", "store-finance@example.com", 580, 18),
    ]
    cursor.executemany(
        "INSERT INTO lenders (lender_id, lender_code, lender_type_id, contact_name, contact_phone, "
        "contact_email, min_credit_score, max_term_months) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        lenders_data,
    )

# -------------------------
# Products
# -------------------------
   
    products_data: List[Tuple[str, str, str, str, str, str, str, str, str, int, int, float]] = [
        ('PRD001', 'SPH000001', 'MDL-SPH-000001', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Black 128GB', 'Apple iPhone 15 Pro in Black with 128GB storage.', '2023-09-01', 7, 24, 999.0),
        ('PRD002', 'SPH000002', 'MDL-SPH-000002', 'CAT110', 'BR001', 'BRC002', 'Apple iPhone 15 Pro Black 256GB', 'Apple iPhone 15 Pro in Black with 256GB storage.', '2023-09-01', 6, 24, 1139.8),
        ('PRD003', 'SPH000003', 'MDL-SPH-000003', 'CAT110', 'BR001', 'BRC003', 'Apple iPhone 15 Pro Black 512GB', 'Apple iPhone 15 Pro in Black with 512GB storage.', '2023-09-01', 9, 24, 1421.4),
        ('PRD004', 'SPH000004', 'MDL-SPH-000004', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Blue 128GB', 'Apple iPhone 15 Pro in Blue with 128GB storage.', '2023-09-01', 6, 24, 999.0),
        ('PRD005', 'SPH000005', 'MDL-SPH-000005', 'CAT110', 'BR001', 'BRC002', 'Apple iPhone 15 Pro Blue 256GB', 'Apple iPhone 15 Pro in Blue with 256GB storage.', '2023-09-01', 12, 24, 1139.8),
        ('PRD006', 'SPH000006', 'MDL-SPH-000006', 'CAT110', 'BR001', 'BRC003', 'Apple iPhone 15 Pro Blue 512GB', 'Apple iPhone 15 Pro in Blue with 512GB storage.', '2023-09-01', 9, 24, 1421.4),
        ('PRD007', 'SPH000007', 'MDL-SPH-000007', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Silver 128GB', 'Apple iPhone 15 Pro in Silver with 128GB storage.', '2023-09-01', 8, 24, 999.0),
        ('PRD008', 'SPH000008', 'MDL-SPH-000008', 'CAT110', 'BR001', 'BRC002', 'Apple iPhone 15 Pro Silver 256GB', 'Apple iPhone 15 Pro in Silver with 256GB storage.', '2023-09-01', 8, 24, 1139.8),
        ('PRD009', 'SPH000009', 'MDL-SPH-000009', 'CAT110', 'BR001', 'BRC003', 'Apple iPhone 15 Pro Silver 512GB', 'Apple iPhone 15 Pro in Silver with 512GB storage.', '2023-09-01', 12, 24, 1421.4),
        ('PRD010', 'SPH000010', 'MDL-SPH-000010', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Gold 128GB', 'Apple iPhone 15 Pro in Gold with 128GB storage.', '2023-09-01', 11, 24, 999.0),
        ('PRD011', 'SPH000011', 'MDL-SPH-000011', 'CAT110', 'BR001', 'BRC002', 'Apple iPhone 15 Pro Gold 256GB', 'Apple iPhone 15 Pro in Gold with 256GB storage.', '2023-09-01', 5, 24, 1139.8),
        ('PRD012', 'SPH000012', 'MDL-SPH-000012', 'CAT110', 'BR001', 'BRC003', 'Apple iPhone 15 Pro Gold 512GB', 'Apple iPhone 15 Pro in Gold with 512GB storage.', '2023-09-01', 5, 24, 1421.4),
        ('PRD013', 'SPH000013', 'MDL-SPH-000013', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Green 128GB', 'Apple iPhone 15 Pro in Green with 128GB storage.', '2023-09-01', 11, 24, 999.0),
        ('PRD014', 'SPH000014', 'MDL-SPH-000014', 'CAT110', 'BR001', 'BRC002', 'Apple iPhone 15 Pro Green 256GB', 'Apple iPhone 15 Pro in Green with 256GB storage.', '2023-09-01', 5, 24, 1139.8),
        ('PRD015', 'SPH000015', 'MDL-SPH-000015', 'CAT110', 'BR001', 'BRC003', 'Apple iPhone 15 Pro Green 512GB', 'Apple iPhone 15 Pro in Green with 512GB storage.', '2023-09-01', 8, 24, 1421.4),
        ('PRD016', 'SPH000016', 'MDL-SPH-000016', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Black 128GB', 'Apple iPhone 15 Pro in Black with 128GB storage.', '2023-09-01', 8, 24, 999.0),
        ('PRD017', 'SPH000017', 'MDL-SPH-000017', 'CAT110', 'BR001', 'BRC002', 'Apple iPhone 15 Pro Black 256GB', 'Apple iPhone 15 Pro in Black with 256GB storage.', '2023-09-01', 8, 24, 1139.8),
        ('PRD018', 'SPH000018', 'MDL-SPH-000018', 'CAT110', 'BR001', 'BRC003', 'Apple iPhone 15 Pro Black 512GB', 'Apple iPhone 15 Pro in Black with 512GB storage.', '2023-09-01', 10, 24, 1421.4),
        ('PRD019', 'SPH000019', 'MDL-SPH-000019', 'CAT110', 'BR001', 'BRC001', 'Apple iPhone 15 Pro Blue 128GB', 'Apple iPhone 15 Pro in Blue with 128GB storage.', '2023-09-01', 11, 24, 999.0),

        ('PRD020', 'TAB000020', 'MDL-TAB-000020', 'CAT120', 'BR001', 'BRC002', 'Apple iPad Air 5 Space Gray 64GB', 'Apple iPad Air 5 tablet, Space Gray, 64GB.', '2022-03-01', 4, 24, 599.0),
        ('PRD021', 'TAB000021', 'MDL-TAB-000021', 'CAT120', 'BR001', 'BRC003', 'Apple iPad Air 5 Space Gray 128GB', 'Apple iPad Air 5 tablet, Space Gray, 128GB.', '2022-03-01', 8, 24, 659.8),
        ('PRD022', 'TAB000022', 'MDL-TAB-000022', 'CAT120', 'BR001', 'BRC001', 'Apple iPad Air 5 Space Gray 256GB', 'Apple iPad Air 5 tablet, Space Gray, 256GB.', '2022-03-01', 4, 24, 781.4),
        ('PRD023', 'TAB000023', 'MDL-TAB-000023', 'CAT120', 'BR001', 'BRC002', 'Apple iPad Air 5 Silver 64GB', 'Apple iPad Air 5 tablet, Silver, 64GB.', '2022-03-01', 8, 24, 599.0),
        ('PRD024', 'TAB000024', 'MDL-TAB-000024', 'CAT120', 'BR001', 'BRC003', 'Apple iPad Air 5 Silver 128GB', 'Apple iPad Air 5 tablet, Silver, 128GB.', '2022-03-01', 7, 24, 659.8),
        ('PRD025', 'TAB000025', 'MDL-TAB-000025', 'CAT120', 'BR001', 'BRC001', 'Apple iPad Air 5 Silver 256GB', 'Apple iPad Air 5 tablet, Silver, 256GB.', '2022-03-01', 10, 24, 781.4),
        ('PRD026', 'TAB000026', 'MDL-TAB-000026', 'CAT120', 'BR001', 'BRC002', 'Apple iPad Air 5 Graphite 64GB', 'Apple iPad Air 5 tablet, Graphite, 64GB.', '2022-03-01', 7, 24, 599.0),
        ('PRD027', 'TAB000027', 'MDL-TAB-000027', 'CAT120', 'BR001', 'BRC003', 'Apple iPad Air 5 Graphite 128GB', 'Apple iPad Air 5 tablet, Graphite, 128GB.', '2022-03-01', 6, 24, 659.8),
        ('PRD028', 'TAB000028', 'MDL-TAB-000028', 'CAT120', 'BR001', 'BRC001', 'Apple iPad Air 5 Graphite 256GB', 'Apple iPad Air 5 tablet, Graphite, 256GB.', '2022-03-01', 5, 24, 781.4),
        ('PRD029', 'TAB000029', 'MDL-TAB-000029', 'CAT120', 'BR002', 'BRC002', 'Samsung Galaxy Tab S9 Space Gray 64GB', 'Samsung Galaxy Tab S9 tablet, Space Gray, 64GB.', '2023-08-01', 10, 24, 799.0),
        ('PRD030', 'TAB000030', 'MDL-TAB-000030', 'CAT120', 'BR002', 'BRC003', 'Samsung Galaxy Tab S9 Space Gray 128GB', 'Samsung Galaxy Tab S9 tablet, Space Gray, 128GB.', '2023-08-01', 9, 24, 859.8),
        ('PRD031', 'TAB000031', 'MDL-TAB-000031', 'CAT120', 'BR002', 'BRC001', 'Samsung Galaxy Tab S9 Space Gray 256GB', 'Samsung Galaxy Tab S9 tablet, Space Gray, 256GB.', '2023-08-01', 6, 24, 981.4),
        ('PRD032', 'TAB000032', 'MDL-TAB-000032', 'CAT120', 'BR002', 'BRC002', 'Samsung Galaxy Tab S9 Silver 64GB', 'Samsung Galaxy Tab S9 tablet, Silver, 64GB.', '2023-08-01', 9, 24, 799.0),
        ('PRD033', 'TAB000033', 'MDL-TAB-000033', 'CAT120', 'BR002', 'BRC003', 'Samsung Galaxy Tab S9 Silver 128GB', 'Samsung Galaxy Tab S9 tablet, Silver, 128GB.', '2023-08-01', 6, 24, 859.8),
        ('PRD034', 'TAB000034', 'MDL-TAB-000034', 'CAT120', 'BR002', 'BRC001', 'Samsung Galaxy Tab S9 Silver 256GB', 'Samsung Galaxy Tab S9 tablet, Silver, 256GB.', '2023-08-01', 6, 24, 981.4),
        ('PRD035', 'TAB000035', 'MDL-TAB-000035', 'CAT120', 'BR005', 'BRC002', 'Lenovo Tab P12 Space Gray 64GB', 'Lenovo Tab P12 tablet, Space Gray, 64GB.', '2023-05-01', 6, 24, 429.0),
        ('PRD036', 'TAB000036', 'MDL-TAB-000036', 'CAT120', 'BR005', 'BRC003', 'Lenovo Tab P12 Space Gray 128GB', 'Lenovo Tab P12 tablet, Space Gray, 128GB.', '2023-05-01', 7, 24, 489.8),
        ('PRD037', 'TAB000037', 'MDL-TAB-000037', 'CAT120', 'BR005', 'BRC001', 'Lenovo Tab P12 Space Gray 256GB', 'Lenovo Tab P12 tablet, Space Gray, 256GB.', '2023-05-01', 10, 24, 611.4),

        ('PRD038', 'DST000038', 'MDL-DST-000038', 'CAT200', 'BR006', 'BRC002', 'Dell OptiPlex 7010 SFF i5 16GB', 'Dell OptiPlex 7010 SFF desktop with i5 and 16GB RAM.', '2023-01-01', 6, 24, 899.0),
        ('PRD039', 'DST000039', 'MDL-DST-000039', 'CAT200', 'BR006', 'BRC003', 'Dell OptiPlex 7010 SFF i5 32GB', 'Dell OptiPlex 7010 SFF desktop with i5 and 32GB RAM.', '2023-01-01', 6, 24, 1459.0),
        ('PRD040', 'DST000040', 'MDL-DST-000040', 'CAT200', 'BR006', 'BRC001', 'Dell OptiPlex 7010 SFF i7 16GB', 'Dell OptiPlex 7010 SFF desktop with i7 and 16GB RAM.', '2023-01-01', 2, 24, 1049.0),
        ('PRD041', 'DST000041', 'MDL-DST-000041', 'CAT200', 'BR006', 'BRC002', 'Dell OptiPlex 7010 SFF i7 32GB', 'Dell OptiPlex 7010 SFF desktop with i7 and 32GB RAM.', '2023-01-01', 2, 24, 1609.0),
        ('PRD042', 'DST000042', 'MDL-DST-000042', 'CAT200', 'BR007', 'BRC003', 'HP Pavilion Gaming Desktop i5 16GB', 'HP Pavilion Gaming Desktop desktop with i5 and 16GB RAM.', '2023-02-01', 3, 24, 1099.0),
        ('PRD043', 'DST000043', 'MDL-DST-000043', 'CAT200', 'BR007', 'BRC001', 'HP Pavilion Gaming Desktop i5 32GB', 'HP Pavilion Gaming Desktop desktop with i5 and 32GB RAM.', '2023-02-01', 2, 24, 1659.0),
        ('PRD044', 'DST000044', 'MDL-DST-000044', 'CAT200', 'BR007', 'BRC002', 'HP Pavilion Gaming Desktop i7 16GB', 'HP Pavilion Gaming Desktop desktop with i7 and 16GB RAM.', '2023-02-01', 5, 24, 1249.0),
        ('PRD045', 'DST000045', 'MDL-DST-000045', 'CAT200', 'BR007', 'BRC003', 'HP Pavilion Gaming Desktop i7 32GB', 'HP Pavilion Gaming Desktop desktop with i7 and 32GB RAM.', '2023-02-01', 8, 24, 1809.0),
        ('PRD046', 'DST000046', 'MDL-DST-000046', 'CAT200', 'BR005', 'BRC001', 'Lenovo IdeaCentre Tower 5 i5 16GB', 'Lenovo IdeaCentre Tower 5 desktop with i5 and 16GB RAM.', '2022-05-01', 5, 24, 799.0),
        ('PRD047', 'DST000047', 'MDL-DST-000047', 'CAT200', 'BR005', 'BRC002', 'Lenovo IdeaCentre Tower 5 i5 32GB', 'Lenovo IdeaCentre Tower 5 desktop with i5 and 32GB RAM.', '2022-05-01', 5, 24, 1359.0),
        ('PRD048', 'DST000048', 'MDL-DST-000048', 'CAT200', 'BR005', 'BRC003', 'Lenovo IdeaCentre Tower 5 i7 16GB', 'Lenovo IdeaCentre Tower 5 desktop with i7 and 16GB RAM.', '2022-05-01', 2, 24, 949.0),
        ('PRD049', 'DST000049', 'MDL-DST-000049', 'CAT200', 'BR005', 'BRC001', 'Lenovo IdeaCentre Tower 5 i7 32GB', 'Lenovo IdeaCentre Tower 5 desktop with i7 and 32GB RAM.', '2022-05-01', 6, 24, 1509.0),
        ('PRD050', 'DST000050', 'MDL-DST-000050', 'CAT200', 'BR001', 'BRC002', 'Apple iMac 24-inch M3 i5 16GB', 'Apple iMac 24-inch M3 desktop with i5 and 16GB RAM.', '2023-11-01', 3, 24, 1299.0),
        ('PRD051', 'DST000051', 'MDL-DST-000051', 'CAT200', 'BR001', 'BRC003', 'Apple iMac 24-inch M3 i5 32GB', 'Apple iMac 24-inch M3 desktop with i5 and 32GB RAM.', '2023-11-01', 8, 24, 1859.0),
        ('PRD052', 'DST000052', 'MDL-DST-000052', 'CAT200', 'BR001', 'BRC001', 'Apple iMac 24-inch M3 i7 16GB', 'Apple iMac 24-inch M3 desktop with i7 and 16GB RAM.', '2023-11-01', 7, 24, 1449.0),
        ('PRD053', 'DST000053', 'MDL-DST-000053', 'CAT200', 'BR001', 'BRC002', 'Apple iMac 24-inch M3 i7 32GB', 'Apple iMac 24-inch M3 desktop with i7 and 32GB RAM.', '2023-11-01', 5, 24, 2009.0),
        ('PRD054', 'DST000054', 'MDL-DST-000054', 'CAT200', 'BR008', 'BRC003', 'Asus ExpertCenter Mini PC i5 16GB', 'Asus ExpertCenter Mini PC desktop with i5 and 16GB RAM.', '2022-10-01', 8, 24, 699.0),
        ('PRD055', 'DST000055', 'MDL-DST-000055', 'CAT200', 'BR008', 'BRC001', 'Asus ExpertCenter Mini PC i5 32GB', 'Asus ExpertCenter Mini PC desktop with i5 and 32GB RAM.', '2022-10-01', 5, 24, 1259.0),

        ('PRD056', 'LTP000056', 'MDL-LTP-000056', 'CAT210', 'BR001', 'BRC002', 'MacBook Air M2 13-inch Gray 8GB RAM 512GB SSD', 'MacBook Air M2 13-inch laptop in Gray with 8GB RAM and 512GB SSD.', '2022-07-01', 7, 24, 1199.0),
        ('PRD057', 'LTP000057', 'MDL-LTP-000057', 'CAT210', 'BR001', 'BRC003', 'MacBook Air M2 13-inch Gray 8GB RAM 1024GB SSD', 'MacBook Air M2 13-inch laptop in Gray with 8GB RAM and 1024GB SSD.', '2022-07-01', 3, 24, 1506.2),
        ('PRD058', 'LTP000058', 'MDL-LTP-000058', 'CAT210', 'BR001', 'BRC001', 'MacBook Air M2 13-inch Gray 16GB RAM 512GB SSD', 'MacBook Air M2 13-inch laptop in Gray with 16GB RAM and 512GB SSD.', '2022-07-01', 7, 24, 1879.0),
        ('PRD059', 'LTP000059', 'MDL-LTP-000059', 'CAT210', 'BR001', 'BRC002', 'MacBook Air M2 13-inch Gray 16GB RAM 1024GB SSD', 'MacBook Air M2 13-inch laptop in Gray with 16GB RAM and 1024GB SSD.', '2022-07-01', 4, 24, 2186.2),
        ('PRD060', 'LTP000060', 'MDL-LTP-000060', 'CAT210', 'BR001', 'BRC003', 'MacBook Air M2 13-inch Black 8GB RAM 512GB SSD', 'MacBook Air M2 13-inch laptop in Black with 8GB RAM and 512GB SSD.', '2022-07-01', 3, 24, 1199.0),
        ('PRD061', 'LTP000061', 'MDL-LTP-000061', 'CAT210', 'BR001', 'BRC001', 'MacBook Air M2 13-inch Black 8GB RAM 1024GB SSD', 'MacBook Air M2 13-inch laptop in Black with 8GB RAM and 1024GB SSD.', '2022-07-01', 2, 24, 1506.2),
        ('PRD062', 'LTP000062', 'MDL-LTP-000062', 'CAT210', 'BR001', 'BRC002', 'MacBook Air M2 13-inch Black 16GB RAM 512GB SSD', 'MacBook Air M2 13-inch laptop in Black with 16GB RAM and 512GB SSD.', '2022-07-01', 5, 24, 1879.0),
        ('PRD063', 'LTP000063', 'MDL-LTP-000063', 'CAT210', 'BR001', 'BRC003', 'MacBook Air M2 13-inch Black 16GB RAM 1024GB SSD', 'MacBook Air M2 13-inch laptop in Black with 16GB RAM and 1024GB SSD.', '2022-07-01', 7, 24, 2186.2),
        ('PRD064', 'LTP000064', 'MDL-LTP-000064', 'CAT210', 'BR001', 'BRC001', 'MacBook Pro 14-inch M3 Gray 8GB RAM 512GB SSD', 'MacBook Pro 14-inch M3 laptop in Gray with 8GB RAM and 512GB SSD.', '2023-10-01', 2, 24, 1999.0),
        ('PRD065', 'LTP000065', 'MDL-LTP-000065', 'CAT210', 'BR001', 'BRC002', 'MacBook Pro 14-inch M3 Gray 8GB RAM 1024GB SSD', 'MacBook Pro 14-inch M3 laptop in Gray with 8GB RAM and 1024GB SSD.', '2023-10-01', 3, 24, 2306.2),
        ('PRD066', 'LTP000066', 'MDL-LTP-000066', 'CAT210', 'BR001', 'BRC003', 'MacBook Pro 14-inch M3 Gray 16GB RAM 512GB SSD', 'MacBook Pro 14-inch M3 laptop in Gray with 16GB RAM and 512GB SSD.', '2023-10-01', 6, 24, 2679.0),
        ('PRD067', 'LTP000067', 'MDL-LTP-000067', 'CAT210', 'BR001', 'BRC001', 'MacBook Pro 14-inch M3 Gray 16GB RAM 1024GB SSD', 'MacBook Pro 14-inch M3 laptop in Gray with 16GB RAM and 1024GB SSD.', '2023-10-01', 5, 24, 2986.2),
        ('PRD068', 'LTP000068', 'MDL-LTP-000068', 'CAT210', 'BR006', 'BRC002', 'Dell XPS 13 Plus Gray 8GB RAM 512GB SSD', 'Dell XPS 13 Plus laptop in Gray with 8GB RAM and 512GB SSD.', '2023-01-01', 5, 24, 1399.0),
        ('PRD069', 'LTP000069', 'MDL-LTP-000069', 'CAT210', 'BR006', 'BRC003', 'Dell XPS 13 Plus Gray 8GB RAM 1024GB SSD', 'Dell XPS 13 Plus laptop in Gray with 8GB RAM and 1024GB SSD.', '2023-01-01', 2, 24, 1706.2),
        ('PRD070', 'LTP000070', 'MDL-LTP-000070', 'CAT210', 'BR006', 'BRC001', 'Dell XPS 13 Plus Gray 16GB RAM 512GB SSD', 'Dell XPS 13 Plus laptop in Gray with 16GB RAM and 512GB SSD.', '2023-01-01', 6, 24, 2079.0),
        ('PRD071', 'LTP000071', 'MDL-LTP-000071', 'CAT210', 'BR006', 'BRC002', 'Dell XPS 13 Plus Gray 16GB RAM 1024GB SSD', 'Dell XPS 13 Plus laptop in Gray with 16GB RAM and 1024GB SSD.', '2023-01-01', 6, 24, 2386.2),
        ('PRD072', 'LTP000072', 'MDL-LTP-000072', 'CAT210', 'BR007', 'BRC003', 'HP Spectre x360 14 Gray 8GB RAM 512GB SSD', 'HP Spectre x360 14 laptop in Gray with 8GB RAM and 512GB SSD.', '2023-03-01', 3, 24, 1499.0),
        ('PRD073', 'LTP000073', 'MDL-LTP-000073', 'CAT210', 'BR007', 'BRC001', 'HP Spectre x360 14 Gray 8GB RAM 1024GB SSD', 'HP Spectre x360 14 laptop in Gray with 8GB RAM and 1024GB SSD.', '2023-03-01', 2, 24, 1806.2),
        ('PRD074', 'LTP000074', 'MDL-LTP-000074', 'CAT210', 'BR007', 'BRC002', 'HP Spectre x360 14 Gray 16GB RAM 512GB SSD', 'HP Spectre x360 14 laptop in Gray with 16GB RAM and 512GB SSD.', '2023-03-01', 2, 24, 2179.0),

        ('PRD075', 'MON000075', 'MDL-MON-000075', 'CAT220', 'BR006', 'BRC003', 'Dell UltraSharp 27" 4K IPS (24in FHD)', 'Dell UltraSharp 27" 4K IPS monitor, 24-inch, FHD resolution.', '2022-04-01', 11, 24, 549.0),
        ('PRD076', 'MON000076', 'MDL-MON-000076', 'CAT220', 'BR006', 'BRC001', 'Dell UltraSharp 27" 4K IPS (24in QHD)', 'Dell UltraSharp 27" 4K IPS monitor, 24-inch, QHD resolution.', '2022-04-01', 12, 24, 599.0),
        ('PRD077', 'MON000077', 'MDL-MON-000077', 'CAT220', 'BR006', 'BRC002', 'Dell UltraSharp 27" 4K IPS (27in FHD)', 'Dell UltraSharp 27" 4K IPS monitor, 27-inch, FHD resolution.', '2022-04-01', 9, 24, 570.0),
        ('PRD078', 'MON000078', 'MDL-MON-000078', 'CAT220', 'BR006', 'BRC003', 'Dell UltraSharp 27" 4K IPS (27in QHD)', 'Dell UltraSharp 27" 4K IPS monitor, 27-inch, QHD resolution.', '2022-04-01', 9, 24, 620.0),
        ('PRD079', 'MON000079', 'MDL-MON-000079', 'CAT220', 'BR006', 'BRC001', 'Dell UltraSharp 27" 4K IPS (32in FHD)', 'Dell UltraSharp 27" 4K IPS monitor, 32-inch, FHD resolution.', '2022-04-01', 7, 24, 605.0),
        ('PRD080', 'MON000080', 'MDL-MON-000080', 'CAT220', 'BR006', 'BRC002', 'Dell UltraSharp 27" 4K IPS (32in QHD)', 'Dell UltraSharp 27" 4K IPS monitor, 32-inch, QHD resolution.', '2022-04-01', 11, 24, 655.0),
        ('PRD081', 'MON000081', 'MDL-MON-000081', 'CAT220', 'BR010', 'BRC003', 'LG UltraGear 32" QHD 165Hz (24in FHD)', 'LG UltraGear 32" QHD 165Hz monitor, 24-inch, FHD resolution.', '2023-05-01', 7, 24, 499.0),
        ('PRD082', 'MON000082', 'MDL-MON-000082', 'CAT220', 'BR010', 'BRC001', 'LG UltraGear 32" QHD 165Hz (24in QHD)', 'LG UltraGear 32" QHD 165Hz monitor, 24-inch, QHD resolution.', '2023-05-01', 6, 24, 549.0),
        ('PRD083', 'MON000083', 'MDL-MON-000083', 'CAT220', 'BR010', 'BRC002', 'LG UltraGear 32" QHD 165Hz (27in FHD)', 'LG UltraGear 32" QHD 165Hz monitor, 27-inch, FHD resolution.', '2023-05-01', 6, 24, 520.0),
        ('PRD084', 'MON000084', 'MDL-MON-000084', 'CAT220', 'BR010', 'BRC003', 'LG UltraGear 32" QHD 165Hz (27in QHD)', 'LG UltraGear 32" QHD 165Hz monitor, 27-inch, QHD resolution.', '2023-05-01', 5, 24, 570.0),
        ('PRD085', 'MON000085', 'MDL-MON-000085', 'CAT220', 'BR010', 'BRC001', 'LG UltraGear 32" QHD 165Hz (32in FHD)', 'LG UltraGear 32" QHD 165Hz monitor, 32-inch, FHD resolution.', '2023-05-01', 4, 24, 555.0),
        ('PRD086', 'MON000086', 'MDL-MON-000086', 'CAT220', 'BR010', 'BRC002', 'LG UltraGear 32" QHD 165Hz (32in QHD)', 'LG UltraGear 32" QHD 165Hz monitor, 32-inch, QHD resolution.', '2023-05-01', 10, 24, 605.0),
        ('PRD087', 'MON000087', 'MDL-MON-000087', 'CAT220', 'BR002', 'BRC003', 'Samsung Odyssey G7 27" QHD (24in FHD)', 'Samsung Odyssey G7 27" QHD monitor, 24-inch, FHD resolution.', '2022-08-01', 4, 24, 599.0),
        ('PRD088', 'MON000088', 'MDL-MON-000088', 'CAT220', 'BR002', 'BRC001', 'Samsung Odyssey G7 27" QHD (24in QHD)', 'Samsung Odyssey G7 27" QHD monitor, 24-inch, QHD resolution.', '2022-08-01', 11, 24, 649.0),
        ('PRD089', 'MON000089', 'MDL-MON-000089', 'CAT220', 'BR002', 'BRC002', 'Samsung Odyssey G7 27" QHD (27in FHD)', 'Samsung Odyssey G7 27" QHD monitor, 27-inch, FHD resolution.', '2022-08-01', 5, 24, 620.0),
        ('PRD090', 'MON000090', 'MDL-MON-000090', 'CAT220', 'BR002', 'BRC003', 'Samsung Odyssey G7 27" QHD (27in QHD)', 'Samsung Odyssey G7 27" QHD monitor, 27-inch, QHD resolution.', '2022-08-01', 4, 24, 670.0),
        ('PRD091', 'MON000091', 'MDL-MON-000091', 'CAT220', 'BR002', 'BRC001', 'Samsung Odyssey G7 27" QHD (32in FHD)', 'Samsung Odyssey G7 27" QHD monitor, 32-inch, FHD resolution.', '2022-08-01', 4, 24, 655.0),
        ('PRD092', 'MON000092', 'MDL-MON-000092', 'CAT220', 'BR002', 'BRC002', 'Samsung Odyssey G7 27" QHD (32in QHD)', 'Samsung Odyssey G7 27" QHD monitor, 32-inch, QHD resolution.', '2022-08-01', 7, 24, 705.0),

        ('PRD093', 'WRB000093', 'MDL-WRB-000093', 'CAT300', 'BR001', 'BRC003', 'Apple Watch Series 9 GPS 45mm Black', 'Apple Watch Series 9 GPS 45mm in Black, health tracking and notifications.', '2023-09-01', 15, 12, 429.0),
        ('PRD094', 'WRB000094', 'MDL-WRB-000094', 'CAT300', 'BR001', 'BRC001', 'Apple Watch Series 9 GPS 45mm Silver', 'Apple Watch Series 9 GPS 45mm in Silver, health tracking and notifications.', '2023-09-01', 6, 12, 449.0),
        ('PRD095', 'WRB000095', 'MDL-WRB-000095', 'CAT300', 'BR001', 'BRC002', 'Apple Watch Series 9 GPS 45mm Green', 'Apple Watch Series 9 GPS 45mm in Green, health tracking and notifications.', '2023-09-01', 12, 12, 429.0),
        ('PRD096', 'WRB000096', 'MDL-WRB-000096', 'CAT300', 'BR002', 'BRC003', 'Samsung Galaxy Watch 6 Classic 47mm Black', 'Samsung Galaxy Watch 6 Classic 47mm in Black, health tracking and notifications.', '2023-08-01', 18, 12, 399.0),
        ('PRD097', 'WRB000097', 'MDL-WRB-000097', 'CAT300', 'BR002', 'BRC001', 'Samsung Galaxy Watch 6 Classic 47mm Silver', 'Samsung Galaxy Watch 6 Classic 47mm in Silver, health tracking and notifications.', '2023-08-01', 16, 12, 419.0),
        ('PRD098', 'WRB000098', 'MDL-WRB-000098', 'CAT300', 'BR002', 'BRC002', 'Samsung Galaxy Watch 6 Classic 47mm Green', 'Samsung Galaxy Watch 6 Classic 47mm in Green, health tracking and notifications.', '2023-08-01', 11, 12, 399.0),
        ('PRD099', 'WRB000099', 'MDL-WRB-000099', 'CAT300', 'BR003', 'BRC003', 'Xiaomi Smart Band 8 Black', 'Xiaomi Smart Band 8 in Black, health tracking and notifications.', '2023-04-01', 10, 12, 59.0),
        ('PRD100', 'WRB000100', 'MDL-WRB-000100', 'CAT300', 'BR003', 'BRC001', 'Xiaomi Smart Band 8 Silver', 'Xiaomi Smart Band 8 in Silver, health tracking and notifications.', '2023-04-01', 7, 12, 79.0),
        ('PRD101', 'WRB000101', 'MDL-WRB-000101', 'CAT300', 'BR003', 'BRC002', 'Xiaomi Smart Band 8 Green', 'Xiaomi Smart Band 8 in Green, health tracking and notifications.', '2023-04-01', 12, 12, 59.0),
        ('PRD102', 'WRB000102', 'MDL-WRB-000102', 'CAT300', 'BR004', 'BRC003', 'Huawei Watch GT 4 Black', 'Huawei Watch GT 4 in Black, health tracking and notifications.', '2023-10-01', 9, 12, 299.0),
        ('PRD103', 'WRB000103', 'MDL-WRB-000103', 'CAT300', 'BR004', 'BRC001', 'Huawei Watch GT 4 Silver', 'Huawei Watch GT 4 in Silver, health tracking and notifications.', '2023-10-01', 16, 12, 319.0),
        ('PRD104', 'WRB000104', 'MDL-WRB-000104', 'CAT300', 'BR004', 'BRC002', 'Huawei Watch GT 4 Green', 'Huawei Watch GT 4 in Green, health tracking and notifications.', '2023-10-01', 11, 12, 299.0),
        ('PRD105', 'WRB000105', 'MDL-WRB-000105', 'CAT300', 'BR017', 'BRC003', 'Google Pixel Watch 2 Black', 'Google Pixel Watch 2 in Black, health tracking and notifications.', '2023-10-01', 11, 12, 349.0),
        ('PRD106', 'WRB000106', 'MDL-WRB-000106', 'CAT300', 'BR017', 'BRC001', 'Google Pixel Watch 2 Silver', 'Google Pixel Watch 2 in Silver, health tracking and notifications.', '2023-10-01', 5, 12, 369.0),
        ('PRD107', 'WRB000107', 'MDL-WRB-000107', 'CAT300', 'BR017', 'BRC002', 'Google Pixel Watch 2 Green', 'Google Pixel Watch 2 in Green, health tracking and notifications.', '2023-10-01', 7, 12, 349.0),
        ('PRD108', 'WRB000108', 'MDL-WRB-000108', 'CAT300', 'BR009', 'BRC003', 'Sony LinkBuds S Fitness Tracker Black', 'Sony LinkBuds S Fitness Tracker in Black, health tracking and notifications.', '2022-05-01', 18, 12, 199.0),
        ('PRD109', 'WRB000109', 'MDL-WRB-000109', 'CAT300', 'BR009', 'BRC001', 'Sony LinkBuds S Fitness Tracker Silver', 'Sony LinkBuds S Fitness Tracker in Silver, health tracking and notifications.', '2022-05-01', 5, 12, 219.0),
        ('PRD110', 'WRB000110', 'MDL-WRB-000110', 'CAT300', 'BR009', 'BRC002', 'Sony LinkBuds S Fitness Tracker Green', 'Sony LinkBuds S Fitness Tracker in Green, health tracking and notifications.', '2022-05-01', 15, 12, 199.0),

        ('PRD111', 'AUD000111', 'MDL-AUD-000111', 'CAT400', 'BR009', 'BRC003', 'Sony WH-1000XM5 Wireless Headphones Black', 'Sony WH-1000XM5 Wireless Headphones in Black, high-quality audio for music and calls.', '2022-05-01', 13, 12, 399.0),
        ('PRD112', 'AUD000112', 'MDL-AUD-000112', 'CAT400', 'BR009', 'BRC001', 'Sony WH-1000XM5 Wireless Headphones White', 'Sony WH-1000XM5 Wireless Headphones in White, high-quality audio for music and calls.', '2022-05-01', 13, 12, 409.0),
        ('PRD113', 'AUD000113', 'MDL-AUD-000113', 'CAT400', 'BR012', 'BRC002', 'Bose QuietComfort 45 Black', 'Bose QuietComfort 45 in Black, high-quality audio for music and calls.', '2021-09-01', 7, 12, 329.0),
        ('PRD114', 'AUD000114', 'MDL-AUD-000114', 'CAT400', 'BR012', 'BRC003', 'Bose QuietComfort 45 White', 'Bose QuietComfort 45 in White, high-quality audio for music and calls.', '2021-09-01', 7, 12, 339.0),
        ('PRD115', 'AUD000115', 'MDL-AUD-000115', 'CAT400', 'BR001', 'BRC001', 'Apple AirPods Pro 2 USB-C Black', 'Apple AirPods Pro 2 USB-C in Black, high-quality audio for music and calls.', '2022-09-01', 18, 12, 249.0),
        ('PRD116', 'AUD000116', 'MDL-AUD-000116', 'CAT400', 'BR001', 'BRC002', 'Apple AirPods Pro 2 USB-C White', 'Apple AirPods Pro 2 USB-C in White, high-quality audio for music and calls.', '2022-09-01', 8, 12, 259.0),
        ('PRD117', 'AUD000117', 'MDL-AUD-000117', 'CAT400', 'BR009', 'BRC003', 'Sony WF-1000XM5 Earbuds Black', 'Sony WF-1000XM5 Earbuds in Black, high-quality audio for music and calls.', '2023-07-01', 8, 12, 299.0),
        ('PRD118', 'AUD000118', 'MDL-AUD-000118', 'CAT400', 'BR009', 'BRC001', 'Sony WF-1000XM5 Earbuds White', 'Sony WF-1000XM5 Earbuds in White, high-quality audio for music and calls.', '2023-07-01', 19, 12, 309.0),
        ('PRD119', 'AUD000119', 'MDL-AUD-000119', 'CAT400', 'BR013', 'BRC002', 'Logitech G Pro X Gaming Headset Black', 'Logitech G Pro X Gaming Headset in Black, high-quality audio for music and calls.', '2020-08-01', 11, 12, 129.0),
        ('PRD120', 'AUD000120', 'MDL-AUD-000120', 'CAT400', 'BR013', 'BRC003', 'Logitech G Pro X Gaming Headset White', 'Logitech G Pro X Gaming Headset in White, high-quality audio for music and calls.', '2020-08-01', 10, 12, 139.0),
        ('PRD121', 'AUD000121', 'MDL-AUD-000121', 'CAT400', 'BR002', 'BRC001', 'Samsung Galaxy Buds2 Pro Black', 'Samsung Galaxy Buds2 Pro in Black, high-quality audio for music and calls.', '2022-08-01', 14, 12, 229.0),
        ('PRD122', 'AUD000122', 'MDL-AUD-000122', 'CAT400', 'BR002', 'BRC002', 'Samsung Galaxy Buds2 Pro White', 'Samsung Galaxy Buds2 Pro in White, high-quality audio for music and calls.', '2022-08-01', 14, 12, 239.0),
        ('PRD123', 'AUD000123', 'MDL-AUD-000123', 'CAT400', 'BR010', 'BRC003', 'LG XBOOM Go PL7 Speaker Black', 'LG XBOOM Go PL7 Speaker in Black, high-quality audio for music and calls.', '2021-03-01', 16, 12, 149.0),
        ('PRD124', 'AUD000124', 'MDL-AUD-000124', 'CAT400', 'BR010', 'BRC001', 'LG XBOOM Go PL7 Speaker White', 'LG XBOOM Go PL7 Speaker in White, high-quality audio for music and calls.', '2021-03-01', 10, 12, 159.0),
        ('PRD125', 'AUD000125', 'MDL-AUD-000125', 'CAT400', 'BR012', 'BRC002', 'Bose SoundLink Revolve+ II Black', 'Bose SoundLink Revolve+ II Black for music, calls, and everyday listening.', '2021-04-01', 12, 12, 239.0),
        ('PRD126', 'AUD000126', 'MDL-AUD-000126', 'CAT400', 'BR009', 'BRC003', 'Sony SRS-XG300 Portable Speaker Black', 'Sony SRS-XG300 Portable Speaker Black for music, calls, and everyday listening.', '2022-07-01', 19, 12, 349.0),
        ('PRD127', 'AUD000127', 'MDL-AUD-000127', 'CAT400', 'BR001', 'BRC001', 'Apple HomePod mini White', 'Apple HomePod mini White for music, calls, and everyday listening.', '2020-11-01', 7, 12, 99.0),
        ('PRD128', 'AUD000128', 'MDL-AUD-000128', 'CAT400', 'BR002', 'BRC002', 'Samsung Galaxy Buds FE White', 'Samsung Galaxy Buds FE White for music, calls, and everyday listening.', '2023-10-01', 17, 12, 99.0),

        ('PRD129', 'TVH000129', 'MDL-TVH-000129', 'CAT500', 'BR010', 'BRC003', 'LG OLED C3 55" 4K Smart TV (55-inch)', 'LG OLED C3 55" 4K Smart TV home theater product, 55-inch class.', '2023-03-01', 7, 24, 1499.0),
        ('PRD130', 'TVH000130', 'MDL-TVH-000130', 'CAT500', 'BR010', 'BRC001', 'LG OLED C3 55" 4K Smart TV (65-inch)', 'LG OLED C3 55" 4K Smart TV home theater product, 65-inch class.', '2023-03-01', 5, 24, 1699.0),
        ('PRD131', 'TVH000131', 'MDL-TVH-000131', 'CAT500', 'BR002', 'BRC002', 'Samsung QLED Q80C 65" 4K Smart TV (55-inch)', 'Samsung QLED Q80C 65" 4K Smart TV home theater product, 55-inch class.', '2023-04-01', 4, 24, 1599.0),
        ('PRD132', 'TVH000132', 'MDL-TVH-000132', 'CAT500', 'BR002', 'BRC003', 'Samsung QLED Q80C 65" 4K Smart TV (65-inch)', 'Samsung QLED Q80C 65" 4K Smart TV home theater product, 65-inch class.', '2023-04-01', 9, 24, 1799.0),
        ('PRD133', 'TVH000133', 'MDL-TVH-000133', 'CAT500', 'BR009', 'BRC001', 'Sony BRAVIA XR A80L 55" OLED (55-inch)', 'Sony BRAVIA XR A80L 55" OLED home theater product, 55-inch class.', '2023-05-01', 4, 24, 1699.0),
        ('PRD134', 'TVH000134', 'MDL-TVH-000134', 'CAT500', 'BR009', 'BRC002', 'Sony BRAVIA XR A80L 55" OLED (65-inch)', 'Sony BRAVIA XR A80L 55" OLED home theater product, 65-inch class.', '2023-05-01', 9, 24, 1899.0),
        ('PRD135', 'TVH000135', 'MDL-TVH-000135', 'CAT500', 'BR010', 'BRC003', 'LG NanoCell 50" 4K TV (55-inch)', 'LG NanoCell 50" 4K TV home theater product, 55-inch class.', '2022-10-01', 4, 24, 799.0),
        ('PRD136', 'TVH000136', 'MDL-TVH-000136', 'CAT500', 'BR010', 'BRC001', 'LG NanoCell 50" 4K TV (65-inch)', 'LG NanoCell 50" 4K TV home theater product, 65-inch class.', '2022-10-01', 8, 24, 999.0),
        ('PRD137', 'TVH000137', 'MDL-TVH-000137', 'CAT500', 'BR002', 'BRC002', 'Samsung The Frame 55" QLED (55-inch)', 'Samsung The Frame 55" QLED home theater product, 55-inch class.', '2022-06-01', 6, 24, 1399.0),
        ('PRD138', 'TVH000138', 'MDL-TVH-000138', 'CAT500', 'BR002', 'BRC003', 'Samsung The Frame 55" QLED (65-inch)', 'Samsung The Frame 55" QLED home theater product, 65-inch class.', '2022-06-01', 6, 24, 1599.0),
        ('PRD139', 'TVH000139', 'MDL-TVH-000139', 'CAT500', 'BR009', 'BRC001', 'Sony HT-A3000 Soundbar (55-inch)', 'Sony HT-A3000 Soundbar home theater product, 55-inch class.', '2022-02-01', 5, 24, 699.0),
        ('PRD140', 'TVH000140', 'MDL-TVH-000140', 'CAT500', 'BR009', 'BRC002', 'Sony HT-A3000 Soundbar (65-inch)', 'Sony HT-A3000 Soundbar home theater product, 65-inch class.', '2022-02-01', 8, 24, 899.0),
        ('PRD141', 'TVH000141', 'MDL-TVH-000141', 'CAT500', 'BR012', 'BRC003', 'Bose Smart Soundbar 600 (55-inch)', 'Bose Smart Soundbar 600 home theater product, 55-inch class.', '2022-09-01', 4, 24, 499.0),
        ('PRD142', 'TVH000142', 'MDL-TVH-000142', 'CAT500', 'BR012', 'BRC001', 'Bose Smart Soundbar 600 (65-inch)', 'Bose Smart Soundbar 600 home theater product, 65-inch class.', '2022-09-01', 9, 24, 699.0),
        ('PRD143', 'TVH000143', 'MDL-TVH-000143', 'CAT500', 'BR010', 'BRC002', 'LG OLED C3 65" 4K Smart TV (65-inch)', 'LG OLED C3 65" 4K Smart TV (65-inch) home theater upgrade for movies and gaming.', '2023-03-01', 3, 24, 1899.0),
        ('PRD144', 'TVH000144', 'MDL-TVH-000144', 'CAT500', 'BR002', 'BRC003', 'Samsung HW-Q990C Dolby Atmos Soundbar (65-inch)', 'Samsung HW-Q990C Dolby Atmos Soundbar (65-inch) home theater upgrade for movies and gaming.', '2023-02-01', 4, 24, 1599.0),
        ('PRD145', 'TVH000145', 'MDL-TVH-000145', 'CAT500', 'BR009', 'BRC001', 'Sony BRAVIA X90L 65" 4K Full Array (65-inch)', 'Sony BRAVIA X90L 65" 4K Full Array (65-inch) home theater upgrade for movies and gaming.', '2023-04-01', 7, 24, 1499.0),
        ('PRD146', 'TVH000146', 'MDL-TVH-000146', 'CAT500', 'BR012', 'BRC002', 'Bose Bass Module 700 Black (55-inch)', 'Bose Bass Module 700 Black (55-inch) home theater upgrade for movies and gaming.', '2020-09-01', 6, 24, 799.0),

        ('PRD147', 'GAM000147', 'MDL-GAM-000147', 'CAT600', 'BR009', 'BRC003', 'PlayStation 5 Standard Edition Standard', 'PlayStation 5 Standard Edition Standard for gaming and accessories.', '2020-11-01', 6, 12, 499.0),
        ('PRD148', 'GAM000148', 'MDL-GAM-000148', 'CAT600', 'BR009', 'BRC001', 'PlayStation 5 Standard Edition Bundle', 'PlayStation 5 Standard Edition Bundle for gaming and accessories.', '2020-11-01', 12, 12, 529.0),
        ('PRD149', 'GAM000149', 'MDL-GAM-000149', 'CAT600', 'BR011', 'BRC002', 'Xbox Series X 1TB Standard', 'Xbox Series X 1TB Standard for gaming and accessories.', '2020-11-01', 6, 12, 499.0),
        ('PRD150', 'GAM000150', 'MDL-GAM-000150', 'CAT600', 'BR011', 'BRC003', 'Xbox Series X 1TB Bundle', 'Xbox Series X 1TB Bundle for gaming and accessories.', '2020-11-01', 3, 12, 529.0),
        ('PRD151', 'GAM000151', 'MDL-GAM-000151', 'CAT600', 'BR014', 'BRC001', 'Nintendo Switch OLED Standard', 'Nintendo Switch OLED Standard for gaming and accessories.', '2021-10-01', 11, 12, 349.0),
        ('PRD152', 'GAM000152', 'MDL-GAM-000152', 'CAT600', 'BR014', 'BRC002', 'Nintendo Switch OLED Bundle', 'Nintendo Switch OLED Bundle for gaming and accessories.', '2021-10-01', 15, 12, 379.0),
        ('PRD153', 'GAM000153', 'MDL-GAM-000153', 'CAT600', 'BR009', 'BRC003', 'PlayStation DualSense Controller Standard', 'PlayStation DualSense Controller Standard for gaming and accessories.', '2020-11-01', 12, 12, 69.0),
        ('PRD154', 'GAM000154', 'MDL-GAM-000154', 'CAT600', 'BR009', 'BRC001', 'PlayStation DualSense Controller Bundle', 'PlayStation DualSense Controller Bundle for gaming and accessories.', '2020-11-01', 9, 12, 99.0),
        ('PRD155', 'GAM000155', 'MDL-GAM-000155', 'CAT600', 'BR011', 'BRC002', 'Xbox Wireless Controller Standard', 'Xbox Wireless Controller Standard for gaming and accessories.', '2021-02-01', 11, 12, 69.0),
        ('PRD156', 'GAM000156', 'MDL-GAM-000156', 'CAT600', 'BR011', 'BRC003', 'Xbox Wireless Controller Bundle', 'Xbox Wireless Controller Bundle for gaming and accessories.', '2021-02-01', 7, 12, 99.0),
        ('PRD157', 'GAM000157', 'MDL-GAM-000157', 'CAT600', 'BR013', 'BRC001', 'Logitech G923 Racing Wheel Standard', 'Logitech G923 Racing Wheel Standard for gaming and accessories.', '2020-08-01', 9, 12, 399.0),
        ('PRD158', 'GAM000158', 'MDL-GAM-000158', 'CAT600', 'BR013', 'BRC002', 'Logitech G923 Racing Wheel Bundle', 'Logitech G923 Racing Wheel Bundle for gaming and accessories.', '2020-08-01', 4, 12, 429.0),
        ('PRD159', 'GAM000159', 'MDL-GAM-000159', 'CAT600', 'BR009', 'BRC003', 'Sony Pulse 3D Wireless Headset Standard', 'Sony Pulse 3D Wireless Headset Standard for gaming and accessories.', '2020-11-01', 10, 12, 99.0),
        ('PRD160', 'GAM000160', 'MDL-GAM-000160', 'CAT600', 'BR009', 'BRC001', 'Sony Pulse 3D Wireless Headset Bundle', 'Sony Pulse 3D Wireless Headset Bundle for gaming and accessories.', '2020-11-01', 3, 12, 129.0),
        ('PRD161', 'GAM000161', 'MDL-GAM-000161', 'CAT600', 'BR014', 'BRC002', 'Nintendo Pro Controller Standard', 'Nintendo Pro Controller Standard for gaming and accessories.', '2017-03-01', 5, 12, 69.0),
        ('PRD162', 'GAM000162', 'MDL-GAM-000162', 'CAT600', 'BR014', 'BRC003', 'Nintendo Pro Controller Bundle', 'Nintendo Pro Controller Bundle for gaming and accessories.', '2017-03-01', 11, 12, 99.0),
        ('PRD163', 'GAM000163', 'MDL-GAM-000163', 'CAT600', 'BR014', 'BRC001', 'Nintendo Switch Lite Standard', 'Nintendo Switch Lite Standard gaming product for consoles and accessories.', '2019-09-01', 11, 12, 199.0),
        ('PRD164', 'GAM000164', 'MDL-GAM-000164', 'CAT600', 'BR009', 'BRC002', 'PlayStation VR2 Bundle', 'PlayStation VR2 Bundle gaming product for consoles and accessories.', '2023-02-01', 6, 12, 549.0),

        ('PRD165', 'NET000165', 'MDL-NET-000165', 'CAT700', 'BR015', 'BRC003', 'TP-Link Archer AX73 Wi-Fi 6 Router Single', 'TP-Link Archer AX73 Wi-Fi 6 Router networking device (Single) for fast, stable connectivity.', '2021-03-01', 5, 24, 179.0),
        ('PRD166', 'NET000166', 'MDL-NET-000166', 'CAT700', 'BR015', 'BRC001', 'TP-Link Archer AX73 Wi-Fi 6 Router 2-Pack', 'TP-Link Archer AX73 Wi-Fi 6 Router networking device (2-Pack) for fast, stable connectivity.', '2021-03-01', 6, 24, 239.0),
        ('PRD167', 'NET000167', 'MDL-NET-000167', 'CAT700', 'BR017', 'BRC002', 'Google Nest Wi-Fi Pro 3-Pack Single', 'Google Nest Wi-Fi Pro 3-Pack networking device (Single) for fast, stable connectivity.', '2022-10-01', 17, 24, 399.0),
        ('PRD168', 'NET000168', 'MDL-NET-000168', 'CAT700', 'BR017', 'BRC003', 'Google Nest Wi-Fi Pro 3-Pack 2-Pack', 'Google Nest Wi-Fi Pro 3-Pack networking device (2-Pack) for fast, stable connectivity.', '2022-10-01', 13, 24, 459.0),
        ('PRD169', 'NET000169', 'MDL-NET-000169', 'CAT700', 'BR015', 'BRC001', 'TP-Link Deco X50 Mesh 2-Pack Single', 'TP-Link Deco X50 Mesh 2-Pack networking device (Single) for fast, stable connectivity.', '2022-06-01', 5, 24, 259.0),
        ('PRD170', 'NET000170', 'MDL-NET-000170', 'CAT700', 'BR015', 'BRC002', 'TP-Link Deco X50 Mesh 2-Pack 2-Pack', 'TP-Link Deco X50 Mesh 2-Pack networking device (2-Pack) for fast, stable connectivity.', '2022-06-01', 9, 24, 319.0),
        ('PRD171', 'NET000171', 'MDL-NET-000171', 'CAT700', 'BR008', 'BRC003', 'ASUS RT-AX88U Gaming Router Single', 'ASUS RT-AX88U Gaming Router networking device (Single) for fast, stable connectivity.', '2020-09-01', 9, 24, 299.0),
        ('PRD172', 'NET000172', 'MDL-NET-000172', 'CAT700', 'BR008', 'BRC001', 'ASUS RT-AX88U Gaming Router 2-Pack', 'ASUS RT-AX88U Gaming Router networking device (2-Pack) for fast, stable connectivity.', '2020-09-01', 10, 24, 359.0),
        ('PRD173', 'NET000173', 'MDL-NET-000173', 'CAT700', 'BR004', 'BRC002', 'Huawei WiFi AX3 Router Single', 'Huawei WiFi AX3 Router networking device (Single) for fast, stable connectivity.', '2020-05-01', 17, 24, 99.0),
        ('PRD174', 'NET000174', 'MDL-NET-000174', 'CAT700', 'BR004', 'BRC003', 'Huawei WiFi AX3 Router 2-Pack', 'Huawei WiFi AX3 Router networking device (2-Pack) for fast, stable connectivity.', '2020-05-01', 5, 24, 159.0),
        ('PRD175', 'NET000175', 'MDL-NET-000175', 'CAT700', 'BR002', 'BRC001', 'Samsung SmartThings Wi-Fi Single', 'Samsung SmartThings Wi-Fi networking device (Single) for fast, stable connectivity.', '2019-09-01', 15, 24, 199.0),
        ('PRD176', 'NET000176', 'MDL-NET-000176', 'CAT700', 'BR002', 'BRC002', 'Samsung SmartThings Wi-Fi 2-Pack', 'Samsung SmartThings Wi-Fi networking device (2-Pack) for fast, stable connectivity.', '2019-09-01', 13, 24, 259.0),
        ('PRD177', 'NET000177', 'MDL-NET-000177', 'CAT700', 'BR016', 'BRC003', 'Intel Wi-Fi 6E AX210 Card Single', 'Intel Wi-Fi 6E AX210 Card networking device (Single) for fast, stable connectivity.', '2020-01-01', 17, 24, 39.0),
        ('PRD178', 'NET000178', 'MDL-NET-000178', 'CAT700', 'BR016', 'BRC001', 'Intel Wi-Fi 6E AX210 Card 2-Pack', 'Intel Wi-Fi 6E AX210 Card networking device (2-Pack) for fast, stable connectivity.', '2020-01-01', 12, 24, 99.0),
        ('PRD179', 'NET000179', 'MDL-NET-000179', 'CAT700', 'BR015', 'BRC002', 'TP-Link TL-SG108 8-Port Gigabit Switch Single', 'TP-Link TL-SG108 8-Port Gigabit Switch Single networking device for home or small office.', '2021-01-01', 12, 24, 29.0),
        ('PRD180', 'NET000180', 'MDL-NET-000180', 'CAT700', 'BR008', 'BRC003', 'Asus ZenWiFi XT8 Mesh 2-Pack', 'Asus ZenWiFi XT8 Mesh 2-Pack networking device for home or small office.', '2020-08-01', 9, 24, 349.0),
        ('PRD181', 'NET000181', 'MDL-NET-000181', 'CAT700', 'BR017', 'BRC001', 'Google Nest Wi-Fi Router Single', 'Google Nest Wi-Fi Router Single networking device for home or small office.', '2019-10-01', 14, 24, 149.0),
        ('PRD182', 'NET000182', 'MDL-NET-000182', 'CAT700', 'BR004', 'BRC002', 'Huawei 5G CPE Pro 2 Single', 'Huawei 5G CPE Pro 2 Single networking device for home or small office.', '2021-06-01', 13, 24, 399.0),

        ('PRD183', 'HAP000183', 'MDL-HAP-000183', 'CAT701', 'BR010', 'BRC003', 'Smart Air Purifier with HEPA Filter Black', 'Smart Air Purifier with HEPA Filter in Black, smart home appliance with app control.', '2022-01-01', 10, 24, 249.0),
        ('PRD184', 'HAP000184', 'MDL-HAP-000184', 'CAT701', 'BR010', 'BRC001', 'Smart Air Purifier with HEPA Filter White', 'Smart Air Purifier with HEPA Filter in White, smart home appliance with app control.', '2022-01-01', 5, 24, 249.0),
        ('PRD185', 'HAP000185', 'MDL-HAP-000185', 'CAT701', 'BR002', 'BRC002', 'Smart Microwave Oven 30L Inverter Black', 'Smart Microwave Oven 30L Inverter in Black, smart home appliance with app control.', '2021-09-01', 2, 24, 199.0),
        ('PRD186', 'HAP000186', 'MDL-HAP-000186', 'CAT701', 'BR002', 'BRC003', 'Smart Microwave Oven 30L Inverter White', 'Smart Microwave Oven 30L Inverter in White, smart home appliance with app control.', '2021-09-01', 7, 24, 199.0),
        ('PRD187', 'HAP000187', 'MDL-HAP-000187', 'CAT701', 'BR017', 'BRC001', 'Smart Robot Vacuum with Mapping Black', 'Smart Robot Vacuum with Mapping in Black, smart home appliance with app control.', '2022-11-01', 7, 24, 399.0),
        ('PRD188', 'HAP000188', 'MDL-HAP-000188', 'CAT701', 'BR017', 'BRC002', 'Smart Robot Vacuum with Mapping White', 'Smart Robot Vacuum with Mapping in White, smart home appliance with app control.', '2022-11-01', 10, 24, 399.0),
        ('PRD189', 'HAP000189', 'MDL-HAP-000189', 'CAT701', 'BR003', 'BRC003', 'Smart Kettle with Temperature Control Black', 'Smart Kettle with Temperature Control in Black, smart home appliance with app control.', '2023-02-01', 11, 24, 89.0),
        ('PRD190', 'HAP000190', 'MDL-HAP-000190', 'CAT701', 'BR003', 'BRC001', 'Smart Kettle with Temperature Control White', 'Smart Kettle with Temperature Control in White, smart home appliance with app control.', '2023-02-01', 12, 24, 89.0),
        ('PRD191', 'HAP000191', 'MDL-HAP-000191', 'CAT701', 'BR010', 'BRC002', 'LG Smart Washer 10kg Black', 'LG Smart Washer 10kg in Black, smart home appliance with app control.', '2022-08-01', 9, 24, 699.0),
        ('PRD192', 'HAP000192', 'MDL-HAP-000192', 'CAT701', 'BR010', 'BRC003', 'LG Smart Washer 10kg White', 'LG Smart Washer 10kg in White, smart home appliance with app control.', '2022-08-01', 12, 24, 699.0),
        ('PRD193', 'HAP000193', 'MDL-HAP-000193', 'CAT701', 'BR002', 'BRC001', 'Samsung Smart Refrigerator 550L Black', 'Samsung Smart Refrigerator 550L in Black, smart home appliance with app control.', '2023-01-01', 12, 24, 1299.0),
        ('PRD194', 'HAP000194', 'MDL-HAP-000194', 'CAT701', 'BR002', 'BRC002', 'Samsung Smart Refrigerator 550L White', 'Samsung Smart Refrigerator 550L in White, smart home appliance with app control.', '2023-01-01', 5, 24, 1299.0),
        ('PRD195', 'HAP000195', 'MDL-HAP-000195', 'CAT701', 'BR003', 'BRC003', 'Xiaomi Smart Standing Fan 2 Black', 'Xiaomi Smart Standing Fan 2 in Black, smart home appliance with app control.', '2021-05-01', 7, 24, 119.0),
        ('PRD196', 'HAP000196', 'MDL-HAP-000196', 'CAT701', 'BR003', 'BRC001', 'Xiaomi Smart Standing Fan 2 White', 'Xiaomi Smart Standing Fan 2 in White, smart home appliance with app control.', '2021-05-01', 5, 24, 119.0),
        ('PRD197', 'HAP000197', 'MDL-HAP-000197', 'CAT701', 'BR004', 'BRC002', 'Huawei Smart Home Hub Black', 'Huawei Smart Home Hub in Black, smart home appliance with app control.', '2020-10-01', 6, 24, 129.0),
        ('PRD198', 'HAP000198', 'MDL-HAP-000198', 'CAT701', 'BR004', 'BRC003', 'Huawei Smart Home Hub White', 'Huawei Smart Home Hub in White, smart home appliance with app control.', '2020-10-01', 10, 24, 129.0),
        ('PRD199', 'HAP000199', 'MDL-HAP-000199', 'CAT701', 'BR017', 'BRC001', 'Google Nest Thermostat Black', 'Google Nest Thermostat in Black, smart home appliance with app control.', '2021-10-01', 8, 24, 129.0),
        ('PRD200', 'HAP000200', 'MDL-HAP-000200', 'CAT701', 'BR017', 'BRC002', 'Google Nest Thermostat White', 'Google Nest Thermostat in White, smart home appliance with app control.', '2021-10-01', 9, 24, 129.0),
    ]

    assert len(products_data) == 200, f"Expected 200 products, got {len(products_data)}"

    cursor.executemany(
        """INSERT INTO products
           (product_id, barcode, model_number, category_id, brand_id, branch_id,
            product_name, description, year_of_release, quantity,
            warranty_Months, price)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        products_data,
    )


    print("[OK] Inserted:")
    print(f"  categories    : {len(categories_data)}")
    print(f"  brands        : {len(brands_data)}")
    print(f"  branches      : {len(branches_data)}")
    print(f"  lender types  : {len(lender_types_data)}")
    print(f"  lenders       : {len(lenders_data)}")
    print(f"  products      : {len(products_data)} (should be 200)")


# -------------------------------------------------------------------
# 3) DB initializer
# -------------------------------------------------------------------

def init_inventory_db() -> None:
    """Create inventory.db, build schema, and seed data."""

    db_path = Path(__file__).parent / "inventory.db"

    if db_path.exists():
        os.remove(db_path)
        print(f"Removed existing database: {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        create_inventory_schema(cursor)
        print("[OK] Created schema")

        populate_data(cursor)

        conn.commit()
        print(f"\n[OK] inventory.db initialized at: {db_path}\n")

        # Quick counts
        for table in ["categories", "brands", "branches", "lenders_type", "lenders", "products"]:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"{table:.<20} {count:>5} rows")

    except Exception as exc:
        conn.rollback()
        print(f"[ERROR] Failed to initialize DB: {exc}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    init_inventory_db()
