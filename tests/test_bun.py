from bun import Bun
from data.bun_test_data import bun_test_data
import pytest


class TestBun:

    # Тест метода __init__. Проверка корректности названия и цены в созданном экземпляре.
    @pytest.mark.parametrize("name, price", bun_test_data)
    def test_created_object_name_price_correct(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    # Тест метода get_name. Проверяет, что метод выводит текущее название созданного экземпляра.
    @pytest.mark.parametrize("name, price", bun_test_data)
    def test_get_name_of_created_object_returns_current_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Тест метода get_price. Проверяет, что метод выводит текущую цену созданного экземпляра.
    @pytest.mark.parametrize("name, price", bun_test_data)
    def test_get_price_of_created_object_returns_current_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
