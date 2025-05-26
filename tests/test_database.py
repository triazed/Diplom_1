from database import Database
from bun import Bun
from ingredient import Ingredient


class TestDatabase:

    def setup_method(self):

        self.expected_buns = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300),
        ]
        self.expected_sauces = [
            Ingredient("SAUCE", "hot sauce", 100),
            Ingredient("SAUCE", "sour cream", 200),
            Ingredient("SAUCE", "chili sauce", 300)
        ]
        self.expected_fillings = [
            Ingredient("FILLING", "cutlet", 100),
            Ingredient("FILLING", "dinosaur", 200),
            Ingredient("FILLING", "sausage", 300)
        ]
        self.expected_ingredients = self.expected_sauces + self.expected_fillings


    # Тест метода __init__. Проверяет, что в созданном экземпляре устанавливаются дефолтные наименования и цены булок.
    def test_buns_default_values_set_correctly(self):
        database = Database()
        actual_buns = database.buns
        for i in range(len(self.expected_buns)):
            assert self.expected_buns[i].name == actual_buns[i].name
            assert self.expected_buns[i].price == actual_buns[i].price

    # Тест метода __init__. Проверяет, что в созданном экземпляре устанавливаются дефолтные наименования и цены соусов.
    def test_sauces_default_values_set_correctly(self):
        database = Database()
        actual_sauces = [i for i in database.ingredients if i.type == "SAUCE"]
        for i in range(len(self.expected_sauces)):
            assert self.expected_sauces[i].name == actual_sauces[i].name
            assert self.expected_sauces[i].price == actual_sauces[i].price

    # Тест метода __init__. Проверяет, что в созданном экземпляре устанавливаются дефолтные наименования и цены начинок.
    def test_fillings_default_values_set_correctly(self):
        database = Database()
        actual_fillings = [i for i in database.ingredients if i.type == "FILLING"]
        for i in range(len(self.expected_fillings)):
            assert self.expected_fillings[i].name == actual_fillings[i].name
            assert self.expected_fillings[i].price == actual_fillings[i].price

    # Тест метода available_buns. Проверяет, что метод возвращает корректный список доступных булок.
    def test_available_buns_returns_correct_list(self):
        database = Database()
        actual_buns = database.available_buns()
        for i in range(len(self.expected_buns)):
            assert self.expected_buns[i].name == actual_buns[i].name
            assert self.expected_buns[i].price == actual_buns[i].price

    # Тест метода available_ingredients. Проверяет, что метод возвращает корректный список доступных ингредиентов.
    def test_available_ingredients_returns_correct_list(self):
        database = Database()
        actual_ingredients = database.available_ingredients()
        for i in range(len(self.expected_ingredients)):
            assert self.expected_ingredients[i].type == actual_ingredients[i].type
            assert self.expected_ingredients[i].name == actual_ingredients[i].name
            assert self.expected_ingredients[i].price == actual_ingredients[i].price
