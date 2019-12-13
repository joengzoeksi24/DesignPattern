# -*- coding:utf-8 -*-
# @time   : 2019-12-13 16:16
# @author : xulei
# @project: DesignPattern

from BuilderPattern.MealBuilder import MealBuilder

if __name__ == '__main__':
    mealBuilder = MealBuilder()

    vegMeal = mealBuilder.prepareVegMeal()
    print("Veg Meal")
    vegMeal.showItems()
    print("Total Cost: " + str(vegMeal.getCost()))

    nonVegMeal = mealBuilder.prepareNonVegMeal()
    print("\nNon-Veg Meal")
    nonVegMeal.showItems()
    print("Total Cost:" + str(nonVegMeal.getCost()))

"""
Meal.py
    def __init__(self):
        self.items = []
Veg Meal
Item: Veg Burger, Packing: Wrapper, Price: 25.0
Item: Coke, Packing: Bottle, Price: 30.0
Total Cost: 55.0

Non-Veg Meal
Item: Chicken Burger, Packing: Wrapper, Price: 50.5
Item: Pepsi, Packing: Bottle, Price: 35.0
Total Cost:85.5
"""
'''
Meal.py
items = []  # 类中全局变量
Veg Meal
Item: Veg Burger, Packing: Wrapper, Price: 25.0
Item: Coke, Packing: Bottle, Price: 30.0
Total Cost: 55.0

Non-Veg Meal
Item: Veg Burger, Packing: Wrapper, Price: 25.0
Item: Coke, Packing: Bottle, Price: 30.0
Item: Chicken Burger, Packing: Wrapper, Price: 50.5
Item: Pepsi, Packing: Bottle, Price: 35.0
Total Cost:140.5
'''