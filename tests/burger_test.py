from ..data_test import INGREDIENT_NAME, BUN_NAME, BURGER_PRICE, INGREDIENT_NAME_2


class TestBurger:
    def test_set_buns(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun.name == BUN_NAME

    def test_add_ingredient(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].name == INGREDIENT_NAME

    def test_get_price(self, mock_bun, mock_ingredient, burger):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == BURGER_PRICE

    def test_remove_ingredient(self, mock_ingredient, mock_ingredient_2, burger):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0].name == INGREDIENT_NAME_2
