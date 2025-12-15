"""
Data Access Utilities for Electronic Store

Functions should use these utilities instead of accessing data structures directly.
"""

import sqlite3
from pathlib import Path
from typing import Dict, Any, Optional, List
from contextlib import contextmanager


@contextmanager
def get_database_connection(data: Dict[str, Any], db_name: str):
    """
    Get a database connection for the specified database.

    Args:
        data: The data dictionary from function parameters
        db_name: Database name ('customers' or 'inventory')

    Yields:
        sqlite3.Connection: Database connection with row factory set
    """

    database_paths = data.get("database_paths", {})
    if db_name not in database_paths:
        raise KeyError(f"Database path not found for: {db_name}")

    db_path = database_paths[db_name]
    if not Path(db_path).exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def execute_sql_query(data: Dict[str, Any], db_name: str, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
    """
    Execute a SQL query and return results as list of dictionaries.

    Args:
        data: The data dictionary
        db_name: Database name ('customers' or 'inventory')
        query: SQL query string
        params: Optional parameters for parameterized queries

    Returns:
        List of dictionaries representing rows
    """
    with get_database_connection(data, db_name) as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        rows = cursor.fetchall()
        return [dict(row) for row in rows]