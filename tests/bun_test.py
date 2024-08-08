from ..bun import Bun
from ..data_test import BUN_NAME, BUN_PRICE
import pytest


class TestBun:
    @pytest.mark.parametrize('method, expected_result', [(Bun(BUN_NAME, BUN_PRICE).get_name(),
                                                          BUN_NAME),
                                                         (Bun(BUN_NAME, BUN_PRICE).get_price(),
                                                          BUN_PRICE)])
    def test_get_name_and_price(self, method, expected_result):
        assert method == expected_result
