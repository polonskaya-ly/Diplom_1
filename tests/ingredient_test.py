from ..ingredient import Ingredient
from ..data_test import INGREDIENT_NAME, INGREDIENT_PRICE
from ..ingredient_types import INGREDIENT_TYPE_SAUCE
import pytest


class TestIngredient:
    @pytest.mark.parametrize('method, expected_result', [(Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME,
                                                                     INGREDIENT_PRICE).get_name(),
                                                         INGREDIENT_NAME),
                                                         (Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME,
                                                                     INGREDIENT_PRICE).get_price(),
                                                         INGREDIENT_PRICE),
                                                         (Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME,
                                                                     INGREDIENT_PRICE).get_type(),
                                                          INGREDIENT_TYPE_SAUCE)])
    def test_get_name_price_and_type(self, method, expected_result):
        assert method == expected_result
