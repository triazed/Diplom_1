from burger import Burger
from unittest.mock import Mock


class TestBurger:

    # Тест метода __init__. Проверка, что в созданном экземпляре устанавливаются дефолтные значения булки и ингредиентов.
    def test_new_object_default_values_correct(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    # Тест метода set_buns. Проверяет, что метод устанавливает булку.
    def test_set_buns_bun_is_set(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    # Тест метода add_ingredient. Проверяет, что метод добавляет ингредиент.
    def test_add_ingredient_added_to_list(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    # Тест метода remove_ingredient. Проверяет, что метод удаляет ингредиент.
    def test_remove_ingredient_removed_from_list(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    # Тест метода move_ingredient. Проверяет, что метод изменяет позицию ингредиента в списке.
    def test_move_ingredient_index_changed(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_2

    # Тест метода get_price. Проверяет, что метод возвращает корректную цену для текущего экземпляра.
    def test_get_price_returns_current_price(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_price.return_value = 102.5
        mock_ingredient.get_price.return_value = 10.3
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == mock_bun.get_price.return_value*2 + mock_ingredient.get_price.return_value

    # Тест метода get_receipt. Проверяет, что метод возвращает чек с информацией текущего экземпляра.
    def test_get_receipt_returns_ingredients_and_price(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка пшеничная"
        mock_bun.get_price.return_value = 102.5
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "Соус"
        mock_ingredient.get_name.return_value = "Министерский"
        mock_ingredient.get_price.return_value = 50.9
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price.return_value*2 + mock_ingredient.get_price.return_value
        expected_results = ["Булка пшеничная", "соус Министерский", str(expected_price)]
        actual_receipt = burger.get_receipt()
        for i in expected_results:
            assert i in actual_receipt
