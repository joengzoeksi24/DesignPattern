# -*- coding:utf-8 -*-
# @time   : 2019-12-13 16:10
# @author : xulei
# @project: DesignPattern

from BuilderPattern.Meal import Meal
from BuilderPattern.VegBurger import VegBurger
from BuilderPattern.ChickenBurger import ChickenBurger
from BuilderPattern.Coke import Coke
from BuilderPattern.Pepsi import Pepsi


# 实际的Builder类负责创建Meal对象
class MealBuilder:
    def prepareVegMeal(self):
        meal = Meal()
        meal.addItem(VegBurger())
        meal.addItem(Coke())
        return meal

    def prepareNonVegMeal(self):
        meal = Meal()
        meal.addItem(ChickenBurger())
        meal.addItem(Pepsi())
        return meal

