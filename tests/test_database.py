from database import Database
from data.database_test_data import DatabaseTestData


class TestDatabase:

    # Тест метода __init__. Проверяет, что в созданном экземпляре устанавливаются дефолтные наименования и цены булок.
    def test_buns_default_values_set_correctly(self):
        database = Database()
        actual_buns = database.buns
        for i in range(len(DatabaseTestData.expected_buns)):
            assert DatabaseTestData.expected_buns[i].name == actual_buns[i].name
            assert DatabaseTestData.expected_buns[i].price == actual_buns[i].price

    # Тест метода __init__. Проверяет, что в созданном экземпляре устанавливаются дефолтные наименования и цены соусов.
    def test_sauces_default_values_set_correctly(self):
        database = Database()
        actual_sauces = [i for i in database.ingredients if i.type == "SAUCE"]
        for i in range(len(DatabaseTestData.expected_sauces)):
            assert DatabaseTestData.expected_sauces[i].name == actual_sauces[i].name
            assert DatabaseTestData.expected_sauces[i].price == actual_sauces[i].price

    # Тест метода __init__. Проверяет, что в созданном экземпляре устанавливаются дефолтные наименования и цены начинок.
    def test_fillings_default_values_set_correctly(self):
        database = Database()
        actual_fillings = [i for i in database.ingredients if i.type == "FILLING"]
        for i in range(len(DatabaseTestData.expected_fillings)):
            assert DatabaseTestData.expected_fillings[i].name == actual_fillings[i].name
            assert DatabaseTestData.expected_fillings[i].price == actual_fillings[i].price

    # Тест метода available_buns. Проверяет, что метод возвращает корректный список доступных булок.
    def test_available_buns_returns_correct_list(self):
        database = Database()
        actual_buns = database.available_buns()
        for i in range(len(DatabaseTestData.expected_buns)):
            assert DatabaseTestData.expected_buns[i].name == actual_buns[i].name
            assert DatabaseTestData.expected_buns[i].price == actual_buns[i].price

    # Тест метода available_ingredients. Проверяет, что метод возвращает корректный список доступных ингредиентов.
    def test_available_ingredients_returns_correct_list(self):
        database = Database()
        actual_ingredients = database.available_ingredients()
        for i in range(len(DatabaseTestData.expected_ingredients)):
            assert DatabaseTestData.expected_ingredients[i].type == actual_ingredients[i].type
            assert DatabaseTestData.expected_ingredients[i].name == actual_ingredients[i].name
            assert DatabaseTestData.expected_ingredients[i].price == actual_ingredients[i].price
