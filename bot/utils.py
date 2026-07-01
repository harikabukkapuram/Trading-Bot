# Utilities placeholder
from datetime import datetime


def separator(length=60):
    return "=" * length


def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_order(order):
    """
    Return only the most important order details.
    """

    return {
        "orderId": order.get("orderId"),
        "symbol": order.get("symbol"),
        "side": order.get("side"),
        "type": order.get("type"),
        "status": order.get("status"),
        "price": order.get("price"),
        "executedQty": order.get("executedQty"),
        "avgPrice": order.get("avgPrice"),
    }


def print_title(title):
    print("\n" + separator())
    print(title)
    print(separator())