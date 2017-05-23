#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: builder.py
module description: builder pattern for pizza ordering
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/23  10:07
"""
from enum import Enum
import time


PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick') # 生面团
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche') # 调味汁
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon '
                                    'ham mushrooms red_onion oregano') #糕点上装饰
STEP_DELAY = 3 # 单位秒


class Pizza(object):
    """
    abstract class: Pizza
    """
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        """
        :param dough: 
        :return: 
        """
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder(object):
    """
    one builder: build margarita pizza
    """
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        print("Progress: {}".format(self.progress.value))
        self.baking_time = 5

    def prepare_dough(self):
        """
        prepare dough: thin thick
        :return: 
        """
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        """
        add sauce: tomato creme_fraiche
        :return: 
        """
        print('add the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        """
        add topping: mozzarella double_mozzarella bacon 
                     ham mushrooms red_onion oregano
        :return: 
        """
        print('add the topping (double_mozzarella oregano) to your margarita')
        for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano):
            self.pizza.topping.append(i)
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarella, oregano)')

    def bake(self):
        """
        bake: pizzaProgress-->baking
        :return: 
        """
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder(object):
    """
    one builder: build creamy_bacon pizza
    """
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        """
        prepare dough: thin thick
        :return: 
        """
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        """
        add sauce: tomato creme_fraiche
        :return: 
        """
        print('add the creme_fraiche sauce to your creamy bacon...')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print("done with the creme_fraiche sauce")

    def add_topping(self):
        """
        add topping: mozzarella double_mozzarella bacon 
                     ham mushrooms red_onion oregano
        :return: 
        """
        print('add the topping (mozzarella bacon ham mushroom red onion'
              ' oregano) to your creamy bacon')
        for i in (PizzaTopping.mozzarella, PizzaTopping.bacon,
                  PizzaTopping.ham, PizzaTopping.mushrooms,
                  PizzaTopping.red_onion, PizzaTopping.oregano):
            self.pizza.topping.append(i)
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella bacon ham mushroom'
              ' red_onion oregano)')

    def bake(self):
        """
        bake: pizzaProgress-->baking
        :return: 
        """
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter(object):
    """
    director: waiter
    """
    def __init__(self):
        self.builder = None

    def construct_builder(self, builder):
        """
        implement of builder
        :param builder: 
        :return: 
        """
        self.builder = builder
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()
        self.builder.bake()

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    """
    validate input
    :param builders: 
    :return: 
    """
    try:
        pizza_style = input('What pizza would you like, '
                            '[m]argarita or [c]reamy bacon?')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy '
              'bacon (key c) are available')
        return (False, None)
    return (valid_input, builder)

if __name__ == "__main__":
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    builder = None
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_builder(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza))