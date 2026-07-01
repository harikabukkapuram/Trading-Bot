# Binance client wrapper placeholder
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.config import API_KEY, API_SECRET, validate_config
from bot.logging_config import logger


class BinanceClient:
    """
    Wrapper class for Binance Futures Testnet.
    """

    def __init__(self):
        validate_config()

        try:
            self.client = Client(
                api_key=API_KEY,
                api_secret=API_SECRET,
                testnet=True
            )

            # Force Futures Testnet URL
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

            logger.info("Connected to Binance Futures Testnet.")

        except Exception as e:
            logger.exception("Failed to initialize Binance client.")
            raise

    def place_market_order(
        self,
        symbol,
        side,
        quantity,
    ):
        """
        Place a MARKET order.
        """

        try:

            logger.info(
                f"MARKET ORDER | {symbol} | {side} | Qty={quantity}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

            logger.info(order)

            return order

        except BinanceAPIException as e:

            logger.error(e.message)

            raise

        except BinanceRequestException as e:

            logger.error(str(e))

            raise

        except Exception as e:

            logger.exception(str(e))

            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price,
    ):
        """
        Place a LIMIT order.
        """

        try:

            logger.info(
                f"LIMIT ORDER | {symbol} | {side} | Qty={quantity} | Price={price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

            logger.info(order)

            return order

        except BinanceAPIException as e:

            logger.error(e.message)

            raise

        except BinanceRequestException as e:

            logger.error(str(e))

            raise

        except Exception as e:

            logger.exception(str(e))

            raise