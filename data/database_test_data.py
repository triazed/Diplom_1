from ingredient import Ingredient
from bun import Bun


class DatabaseTestData:

    expected_buns = [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300)
        ]

    expected_sauces = [
        Ingredient("SAUCE", "hot sauce", 100),
        Ingredient("SAUCE", "sour cream", 200),
        Ingredient("SAUCE", "chili sauce", 300)
        ]

    expected_fillings = [
        Ingredient("FILLING", "cutlet", 100),
        Ingredient("FILLING", "dinosaur", 200),
        Ingredient("FILLING", "sausage", 300)
        ]

    expected_ingredients = expected_sauces + expected_fillings