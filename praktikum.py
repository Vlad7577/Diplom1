from typing import List

from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient


def main():
    # Инициализируем базу данных
    database: Database = Database()

    # Создадим новый бургер
    burger: Burger = Burger()

    # Получаем список доступных булок
    buns: List[Bun] = database.available_buns()

    # Получаем список доступных ингредиентов
    ingredients: List[Ingredient] = database.available_ingredients()

    # Собираем бургер
    burger.set_buns(buns[0])

    burger.add_ingredient(ingredients[1])
    burger.add_ingredient(ingredients[4])
    burger.add_ingredient(ingredients[3])
    burger.add_ingredient(ingredients[5])

    # Перемещаем ингредиент
    burger.move_ingredient(2, 1)

    # Удаляем ингредиент
    burger.remove_ingredient(3)

    # Печатаем рецепт
    print(burger.get_receipt())


if _name_ == "_main_":
    main()