# Exceptions placeholder
class TradingBotError(Exception):
    """
    Base exception for the application.
    """
    pass


class ValidationError(TradingBotError):
    """
    Raised when user input validation fails.
    """
    pass


class ClientInitializationError(TradingBotError):
    """
    Raised when Binance client initialization fails.
    """
    pass


class OrderPlacementError(TradingBotError):
    """
    Raised when Binance rejects an order.
    """
    pass


class NetworkError(TradingBotError):
    """
    Raised when a network problem occurs.
    """
    pass