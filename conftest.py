from .data_test import BUN_NAME, BUN_PRICE, INGREDIENT_PRICE, INGREDIENT_NAME, INGREDIENT_PRICE_2, INGREDIENT_NAME_2
from .burger import Burger
from unittest.mock import Mock
import pytest


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME
    mock_bun.get_price.return_value = BUN_PRICE
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = INGREDIENT_PRICE
    mock_ingredient.name = INGREDIENT_NAME
    return mock_ingredient


@pytest.fixture
def mock_ingredient_2():
    mock_ingredient2 = Mock()
    mock_ingredient2.get_price.return_value = INGREDIENT_PRICE_2
    mock_ingredient2.name = INGREDIENT_NAME_2
    return mock_ingredient2
