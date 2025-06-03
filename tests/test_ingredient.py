from ingredient import Ingredient
from data.ingredient_test_data import ingredient_test_data
import pytest


class TestIngredient:

    # Тест метода __init__. Проверка корректности типа, названия и цены в созданном экземпляре.
    @pytest.mark.parametrize("ing_type, name, price", ingredient_test_data)
    def test_created_object_type_name_price_correct(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.type == ing_type
        assert ingredient.name == name
        assert ingredient.price == price

    # Тест метода get_price. Проверяет, что метод выводит текущую цену созданного экземпляра.
    @pytest.mark.parametrize("ing_type, name, price", ingredient_test_data)
    def test_get_price_returns_current_price(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_price() == price

    # Тест метода get_name. Проверяет, что метод выводит текущее название созданного экземпляра.
    @pytest.mark.parametrize("ing_type, name, price", ingredient_test_data)
    def test_get_name_returns_current_name(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_name() == name

    # Тест метода get_type. Проверяет, что метод выводит текущий тип созданного экземпляра.
    @pytest.mark.parametrize("ing_type, name, price", ingredient_test_data)
    def test_get_type_returns_current_type(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type
