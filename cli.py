import argparse
import sys

from colorama import Fore, Style, init

from bot.orders import OrderManager
from bot.exceptions import (
    ValidationError,
    TradingBotError,
)

init(autoreset=True)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit price (required for LIMIT)"
    )

    return parser


def main():

    parser = build_parser()

    args = parser.parse_args()

    if args.type == "LIMIT" and args.price is None:
        parser.error("--price is required for LIMIT orders.")

    manager = OrderManager()

    try:

        manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )

        print(
            Fore.GREEN +
            "\nOrder completed successfully."
        )

    except ValidationError as e:

        print(
            Fore.RED +
            f"\nValidation Error: {e}"
        )

        sys.exit(1)

    except TradingBotError as e:

        print(
            Fore.RED +
            f"\nTrading Bot Error: {e}"
        )

        sys.exit(1)

    except Exception as e:

        print(
            Fore.RED +
            f"\nUnexpected Error: {e}"
        )

        sys.exit(1)


if __name__ == "__main__":
    main()