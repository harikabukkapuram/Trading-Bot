# Validators placeholder
from bot.exceptions import ValidationError


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str) -> str:
    """
    Validate trading symbol.
    """

    if not symbol:
        raise ValidationError("Symbol cannot be empty.")

    symbol = symbol.strip().upper()

    if len(symbol) < 6:
        raise ValidationError("Invalid trading symbol.")

    return symbol


def validate_side(side: str) -> str:
    """
    Validate BUY / SELL.
    """

    if not side:
        raise ValidationError("Side is required.")

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValidationError(
            "Side must be BUY or SELL."
        )

    return side


def validate_order_type(order_type: str) -> str:
    """
    Validate MARKET / LIMIT.
    """

    if not order_type:
        raise ValidationError("Order type is required.")

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity) -> float:
    """
    Validate quantity.
    """

    try:
        quantity = float(quantity)
    except ValueError:
        raise ValidationError(
            "Quantity must be numeric."
        )

    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(price, order_type):
    """
    Validate price.
    """

    if order_type.upper() == "MARKET":
        return None

    if price is None:
        raise ValidationError(
            "Price is required for LIMIT orders."
        )

    try:
        price = float(price)
    except ValueError:
        raise ValidationError(
            "Price must be numeric."
        )

    if price <= 0:
        raise ValidationError(
            "Price must be greater than zero."
        )

    return price


def validate_inputs(
    symbol,
    side,
    order_type,
    quantity,
    price=None,
):
    """
    Validate every CLI input.
    """

    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    price = validate_price(price, order_type)

    return {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "price": price,
    }