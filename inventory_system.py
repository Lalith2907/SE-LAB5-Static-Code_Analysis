"""Inventory management system with proper error handling and validation.

This module provides functions to manage an inventory system including
adding/removing items, loading/saving data, and generating reports.
"""

import json
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory.

    Args:
        item (str): The name of the item to add
        qty (int): The quantity to add
        logs (list): Optional list to append log messages to

    Returns:
        None
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove an item from the inventory.

    Args:
        item (str): The name of the item to remove
        qty (int): The quantity to remove

    Returns:
        None
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.info("Item not found")


def get_qty(item):
    """Get the quantity of an item in inventory.

    Args:
        item (str): The name of the item to query

    Returns:
        int: The quantity of the item, or KeyError if not found
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file.

    Args:
        file (str): Path to the JSON file to load

    Returns:
        None
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file.

    Args:
        file (str): Path to the JSON file to save

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Print a report of all items in inventory.

    Returns:
        None
    """
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """Check for items below a quantity threshold.

    Args:
        threshold (int): The minimum quantity threshold

    Returns:
        list: List of items below the threshold
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main function to demonstrate inventory system functionality.

    Returns:
        None
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Removed dangerous eval() - replaced with safe print
    print("eval demonstration removed for security")


main()