import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

TESTNET = True


def validate_config():
    """
    Validate required environment variables.
    """

    missing = []

    if not API_KEY:
        missing.append("BINANCE_API_KEY")

    if not API_SECRET:
        missing.append("BINANCE_API_SECRET")

    if missing:
        raise ValueError(
            f"Missing environment variables: {', '.join(missing)}"
        )