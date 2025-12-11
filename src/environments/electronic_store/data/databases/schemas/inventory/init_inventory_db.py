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
            category_code  TEXT NOT NULL,
            category_name  TEXT NOT NULL,
            description    TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE brands (
            brand_id       TEXT PRIMARY KEY,
            brand_code     TEXT NOT NULL,
            brand_name     TEXT NOT NULL,
            country_origin TEXT,
            is_flagship    INTEGER NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE branches (
            branch_id    TEXT PRIMARY KEY,
            branch_code  TEXT NOT NULL,
            branch_name  TEXT NOT NULL,
            city         TEXT,
            state        TEXT,
            ZIP_code     TEXT,
            phone        TEXT,
            manager_name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE products (
            product_id      TEXT PRIMARY KEY,
            barcode         TEXT NOT NULL,
            category_id     TEXT NOT NULL,
            brand_id        TEXT NOT NULL,
            branch_id       TEXT NOT NULL,
            product_name    TEXT NOT NULL,
            description     TEXT,
            year_of_release TEXT NOT NULL,  -- ISO date string
            quantity        INTEGER NOT NULL,
            warranty_Months INTEGER NOT NULL,
            price           REAL NOT NULL,
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

    products_data: List[Tuple[str, str, str, str, str, str, str, str, int, int, float]] = []

    def add_product(
        product_counter: int,
        category_id: str,
        brand_id: str,
        branch_id: str,
        product_name: str,
        description: str,
        year_of_release: str,
        quantity: int,
        warranty_months: int,
        price: float,
        barcode_prefix: str,
    ) -> None:
        product_id = f"PRD{product_counter:03d}"
        barcode = f"{barcode_prefix}{product_counter:06d}"
        products_data.append(
            (
                product_id,
                barcode,
                category_id,
                brand_id,
                branch_id,
                product_name,
                description,
                year_of_release,
                quantity,
                warranty_months,
                price,
            )
        )

    branches_ids = [b[0] for b in branches_data]

    product_counter = 1

    # --- Smartphones (CAT110) ---
    smartphone_models = [
        ("Apple iPhone 15 Pro", "BR001", "2023-09-01", 999.0),
        ("Apple iPhone 15", "BR001", "2023-09-01", 899.0),
        ("Samsung Galaxy S24 Ultra", "BR002", "2024-02-01", 1199.0),
        ("Samsung Galaxy A55", "BR002", "2024-03-01", 399.0),
        ("Xiaomi Redmi Note 13 Pro", "BR003", "2023-11-01", 349.0),
        ("Huawei P60 Pro", "BR004", "2023-06-01", 949.0),
    ]
    sp_colors = ["Black", "Blue", "Silver", "Gold"]
    sp_storages = [128, 256, 512]

    for model_name, brand_id, year_str, base_price in smartphone_models:
        for color in sp_colors:
            for storage in sp_storages:
                if product_counter > 200:
                    break
                branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
                name = f"{model_name} {color} {storage}GB"
                desc = f"{model_name} in {color} with {storage}GB storage, premium smartphone for everyday use."
                price = base_price + (storage - 128) * 1.2
                qty = 5 + (product_counter % 6)  # 5–10 units
                add_product(
                    product_counter,
                    "CAT110",
                    brand_id,
                    branch_id,
                    name,
                    desc,
                    year_str,
                    qty,
                    24,
                    round(price, 2),
                    "SPH",
                )
                product_counter += 1
            if product_counter > 200:
                break
        if product_counter > 200:
            break

    # --- Tablets (CAT120) ---
    tablet_models = [
        ("Apple iPad Air 5", "BR001", "2022-03-01", 599.0),
        ("Samsung Galaxy Tab S9", "BR002", "2023-08-01", 799.0),
        ("Lenovo Tab P12", "BR005", "2023-05-01", 429.0),
    ]
    tab_storages = [64, 128, 256]
    tab_colors = ["Space Gray", "Silver"]

    for model_name, brand_id, year_str, base_price in tablet_models:
        for color in tab_colors:
            for storage in tab_storages:
                if product_counter > 200:
                    break
                branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
                name = f"{model_name} {color} {storage}GB"
                desc = f"{model_name} tablet in {color} with {storage}GB storage, ideal for study and entertainment."
                price = base_price + (storage - 64) * 1.0
                qty = 3 + (product_counter % 5)  # 3–7 units
                add_product(
                    product_counter,
                    "CAT120",
                    brand_id,
                    branch_id,
                    name,
                    desc,
                    year_str,
                    qty,
                    24,
                    round(price, 2),
                    "TAB",
                )
                product_counter += 1
            if product_counter > 200:
                break
        if product_counter > 200:
            break

    # --- Laptops (CAT210) ---
    laptop_models = [
        ("MacBook Air M2 13\"", "BR001", "2022-07-01", 1199.0),
        ("Dell XPS 13 Plus", "BR006", "2023-01-01", 1399.0),
        ("HP Spectre x360 14", "BR007", "2023-03-01", 1499.0),
        ("Asus ROG Zephyrus G14", "BR008", "2023-02-01", 1799.0),
        ("Lenovo ThinkPad X1 Carbon", "BR005", "2022-01-01", 1599.0),
        ("Xiaomi Mi Notebook Pro 16", "BR003", "2022-10-01", 1099.0),
    ]
    laptop_rams = [8, 16]
    laptop_storages = [512, 1024]
    laptop_colors = ["Gray", "Black"]

    for model_name, brand_id, year_str, base_price in laptop_models:
        for ram in laptop_rams:
            for storage in laptop_storages:
                for color in laptop_colors:
                    if product_counter > 200:
                        break
                    branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
                    name = f"{model_name} {color} {ram}GB RAM {storage}GB SSD"
                    desc = (
                        f"{model_name} laptop in {color} with {ram}GB RAM and {storage}GB SSD, "
                        f"suitable for productivity and content creation."
                    )
                    price = base_price + (ram - 8) * 80 + (storage - 512) * 0.7
                    qty = 2 + (product_counter % 4)  # 2–5 units
                    add_product(
                        product_counter,
                        "CAT210",
                        brand_id,
                        branch_id,
                        name,
                        desc,
                        year_str,
                        qty,
                        24,
                        round(price, 2),
                        "LTP",
                    )
                    product_counter += 1
                if product_counter > 200:
                    break
            if product_counter > 200:
                break
        if product_counter > 200:
            break

    # --- Desktops (CAT200) & Monitors (CAT220) ---
    desktop_models = [
        ("Intel Core i7 Gaming Desktop", "BR016", "2023-01-01", 1299.0),
        ("Office Desktop i5 Small Form Factor", "BR006", "2022-09-01", 799.0),
    ]
    for model_name, brand_id, year_str, base_price in desktop_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} tower with dedicated graphics and SSD storage for fast performance."
        qty = 3 + (product_counter % 4)
        add_product(
            product_counter,
            "CAT200",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            24,
            base_price,
            "DST",
        )
        product_counter += 1

    monitor_models = [
        ("Dell UltraSharp 27\" 4K IPS", "BR006", "2022-04-01", 549.0),
        ("LG UltraGear 32\" QHD 165Hz", "BR010", "2023-05-01", 499.0),
        ("Samsung Odyssey G7 27\" QHD", "BR002", "2022-08-01", 599.0),
    ]
    for model_name, brand_id, year_str, base_price in monitor_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} gaming and productivity monitor with high refresh rate and wide color gamut."
        qty = 4 + (product_counter % 5)
        add_product(
            product_counter,
            "CAT220",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            24,
            base_price,
            "MON",
        )
        product_counter += 1

    # --- Wearables (CAT300) ---
    wearable_models = [
        ("Apple Watch Series 9 GPS 45mm", "BR001", "2023-09-01", 429.0),
        ("Samsung Galaxy Watch 6 Classic 47mm", "BR002", "2023-08-01", 399.0),
        ("Xiaomi Smart Band 8", "BR003", "2023-04-01", 59.0),
        ("Huawei Watch GT 4", "BR004", "2023-10-01", 299.0),
    ]
    wear_colors = ["Black", "Silver", "Green"]
    for model_name, brand_id, year_str, base_price in wearable_models:
        for color in wear_colors:
            if product_counter > 200:
                break
            branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
            name = f"{model_name} {color}"
            desc = f"{model_name} in {color}, tracks heart rate, sleep, workouts, and notifications."
            qty = 6 + (product_counter % 6)
            add_product(
                product_counter,
                "CAT300",
                brand_id,
                branch_id,
                name,
                desc,
                year_str,
                qty,
                12,
                base_price,
                "WRB",
            )
            product_counter += 1
        if product_counter > 200:
            break

    # --- Audio (CAT400) ---
    audio_models = [
        ("Sony WH-1000XM5 Wireless Headphones", "BR009", "2022-05-01", 399.0),
        ("Bose QuietComfort 45", "BR012", "2021-09-01", 329.0),
        ("Apple AirPods Pro 2 USB-C", "BR001", "2022-09-01", 249.0),
        ("Sony WF-1000XM5 Earbuds", "BR009", "2023-07-01", 299.0),
        ("Logitech G Pro X Gaming Headset", "BR013", "2020-08-01", 129.0),
    ]
    for model_name, brand_id, year_str, base_price in audio_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} with high-quality sound and comfortable design for long listening sessions."
        qty = 8 + (product_counter % 8)
        add_product(
            product_counter,
            "CAT400",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            12,
            base_price,
            "AUD",
        )
        product_counter += 1

    # --- TV & Home Theater (CAT500) ---
    tv_models = [
        ("LG OLED C3 55\" 4K Smart TV", "BR010", "2023-03-01", 1499.0),
        ("Samsung QLED Q80C 65\" 4K Smart TV", "BR002", "2023-04-01", 1599.0),
        ("Sony BRAVIA XR A80L 55\" OLED", "BR009", "2023-05-01", 1699.0),
        ("LG NanoCell 50\" 4K TV", "BR010", "2022-10-01", 799.0),
    ]
    for model_name, brand_id, year_str, base_price in tv_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} with smart apps, HDR support, and excellent picture quality for movies and gaming."
        qty = 3 + (product_counter % 4)
        add_product(
            product_counter,
            "CAT500",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            24,
            base_price,
            "TVH",
        )
        product_counter += 1

    # --- Gaming (CAT600) ---
    gaming_models = [
        ("PlayStation 5 Standard Edition", "BR009", "2020-11-01", 499.0),
        ("Xbox Series X 1TB", "BR011", "2020-11-01", 499.0),
        ("Nintendo Switch OLED", "BR014", "2021-10-01", 349.0),
        ("Xbox Wireless Controller Shock Blue", "BR011", "2021-02-01", 69.0),
        ("PlayStation DualSense Controller", "BR009", "2020-11-01", 69.0),
    ]
    for model_name, brand_id, year_str, base_price in gaming_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} for next-generation gaming and smooth online multiplayer experiences."
        qty = 5 + (product_counter % 7)
        add_product(
            product_counter,
            "CAT600",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            12,
            base_price,
            "GAM",
        )
        product_counter += 1

    # --- Networking (CAT700) ---
    networking_models = [
        ("TP-Link Archer AX73 Wi-Fi 6 Router", "BR015", "2021-03-01", 179.0),
        ("Google Nest Wi-Fi Pro 3-Pack", "BR017", "2022-10-01", 399.0),
        ("TP-Link Deco X50 Mesh 2-Pack", "BR015", "2022-06-01", 259.0),
        ("ASUS RT-AX88U Gaming Router", "BR008", "2020-09-01", 299.0),
    ]
    for model_name, brand_id, year_str, base_price in networking_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} high-performance router for fast and stable home or office Wi-Fi."
        qty = 4 + (product_counter % 5)
        add_product(
            product_counter,
            "CAT700",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            24,
            base_price,
            "NET",
        )
        product_counter += 1

    # --- Home Appliances (CAT701) ---
    home_appliance_models = [
        ("Smart Air Purifier with HEPA Filter", "BR010", "2022-01-01", 249.0),
        ("Smart Microwave Oven 30L Inverter", "BR002", "2021-09-01", 199.0),
        ("Smart Robot Vacuum with Mapping", "BR017", "2022-11-01", 399.0),
        ("Smart Kettle with Temperature Control", "BR003", "2023-02-01", 89.0),
    ]
    for model_name, brand_id, year_str, base_price in home_appliance_models:
        if product_counter > 200:
            break
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        name = model_name
        desc = f"{model_name} suitable for modern smart homes with app control and energy-efficient design."
        qty = 3 + (product_counter % 6)
        add_product(
            product_counter,
            "CAT701",
            brand_id,
            branch_id,
            name,
            desc,
            year_str,
            qty,
            24,
            base_price,
            "HAP",
        )
        product_counter += 1

    # If still not 200, fill with generic extra smartphones (same structure)
    while product_counter <= 200:
        branch_id = branches_ids[(product_counter - 1) % len(branches_ids)]
        storage = 128 + ((product_counter % 3) * 64)  # 128 / 192 / 256
        color = ["Black", "Blue", "Starlight"][product_counter % 3]
        name = f"Generic Smartphone Model {product_counter} {color} {storage}GB"
        desc = f"Mid-range smartphone {color} with {storage}GB storage for daily communication and apps."
        price = 299.0 + (product_counter % 5) * 20
        qty = 4 + (product_counter % 5)
        add_product(
            product_counter,
            "CAT110",
            "BR003",
            branch_id,
            name,
            desc,
            "2023-01-01",
            qty,
            24,
            price,
            "SPH",
        )
        product_counter += 1

    assert len(products_data) == 200, f"Expected 200 products, got {len(products_data)}"

    cursor.executemany(
        """INSERT INTO products
           (product_id, barcode, category_id, brand_id, branch_id,
            product_name, description, year_of_release, quantity,
            warranty_Months, price)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
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
