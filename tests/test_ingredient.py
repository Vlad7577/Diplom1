from ingredient import Ingredient
import ingredient_types


class TestIngredient:

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        assert ingredient.get_name() == "hot sauce"

    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        assert ingredient.get_price() == 50

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE