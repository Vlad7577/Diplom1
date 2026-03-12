from burger import Burger
from bun import Bun
from ingredient import Ingredient
import ingredient_types


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("black bun", 100)

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 250

    def test_remove_ingredient(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_move_ingredient(self):
        burger = Burger()
        bun = Bun("black bun", 100)

        ing1 = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        ing2 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "cutlet", 100)

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[1] == ing1

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        price = bun.price * 2 + ingredient.price

        expected_receipt = f"(==== {bun.name} ====)\n= {ingredient.name} =\n(==== {bun.name} ====)\n\nPrice: {price}"

        assert receipt == expected_receipt