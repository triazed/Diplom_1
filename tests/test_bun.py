from bun import Bun
import pytest


class TestBun:

    test_data = [
        ["", 0.0],
        ["Булка ржаная бездрожжевая", 0.1],
        ["Булка пшеничная", 102.9]
    ]

    # Тест метода __init__. Проверка корректности названия и цены в созданном экземпляре.
    @pytest.mark.parametrize("name, price", test_data)
    def test_created_object_name_price_correct(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    # Тест метода get_name. Проверяет, что метод выводит текущее название созданного экземпляра.
    @pytest.mark.parametrize("name, price", test_data)
    def test_get_name_of_created_object_returns_current_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Тест метода get_price. Проверяет, что метод выводит текущую цену созданного экземпляра.
    @pytest.mark.parametrize("name, price", test_data)
    def test_get_price_of_created_object_returns_current_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
