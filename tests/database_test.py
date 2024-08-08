from ..database import Database
from ..data_test import LEN_BUNS, LEN_INGREDIENTS
import pytest


class TestDatabase:
    @pytest.mark.parametrize('method, expected_result', [(Database().available_buns(),
                                                          LEN_BUNS),
                                                         (Database().available_ingredients(),
                                                          LEN_INGREDIENTS)])
    def test_available_buns_and_ingredients(self, method, expected_result):
        assert len(method) == expected_result