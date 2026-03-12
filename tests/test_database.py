from database import Database
import ingredient_types


class TestDatabase:

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    def test_ingredient_type(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[0].get_type() in [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]