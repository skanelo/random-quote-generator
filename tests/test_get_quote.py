"""This file contains the tests for the quote module."""

from random_quote_generator import get_quote
from random_quote_generator.quotes import quotes


def test_get_quote() -> None:
    """Test get_quote function.

    GIVEN (nothing)
    WHEN get_quote is called
    THEN random quote from quotes is returned
    """
    quote = get_quote()

    assert quote in quotes
    assert quote in quotes
    assert quote in quotes
