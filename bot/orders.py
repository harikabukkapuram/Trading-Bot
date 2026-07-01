# Order logic placeholder
from bot.client import BinanceClient
from bot.validators import validate_inputs
from bot.logging_config import logger


class OrderManager:
    """
    Handles order validation and placement.
    """

    def __init__(self):
        self.client = BinanceClient()

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None,
    ):
        """
        Validate user input and place the order.
        """

        data = validate_inputs(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print("\n" + "=" * 50)
        print("ORDER REQUEST")
        print("=" * 50)
        print(f"Symbol     : {data['symbol']}")
        print(f"Side       : {data['side']}")
        print(f"Type       : {data['type']}")
        print(f"Quantity   : {data['quantity']}")

        if data["type"] == "LIMIT":
            print(f"Price      : {data['price']}")

        print("=" * 50)

        logger.info(
            "Submitting %s order for %s",
            data["type"],
            data["symbol"],
        )

        if data["type"] == "MARKET":

            response = self.client.place_market_order(
                symbol=data["symbol"],
                side=data["side"],
                quantity=data["quantity"],
            )

        else:

            response = self.client.place_limit_order(
                symbol=data["symbol"],
                side=data["side"],
                quantity=data["quantity"],
                price=data["price"],
            )

        self.print_response(response)

        return response

    def print_response(self, response):
        """
        Pretty-print Binance response.
        """

        print("\n" + "=" * 50)
        print("ORDER RESPONSE")
        print("=" * 50)

        print(
            f"Order ID        : {response.get('orderId', '-')}"
        )

        print(
            f"Status          : {response.get('status', '-')}"
        )

        print(
            f"Executed Qty    : {response.get('executedQty', '-')}"
        )

        avg_price = (
            response.get("avgPrice")
            or response.get("price")
            or "-"
        )

        print(f"Average Price   : {avg_price}")

        print("=" * 50)
        print("✅ ORDER PLACED SUCCESSFULLY")
        print("=" * 50)

        logger.info(
            "Order Successful | ID=%s | Status=%s",
            response.get("orderId"),
            response.get("status"),
        )