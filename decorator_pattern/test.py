#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: test.py
module description: test for decoration pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/04 15:13
"""
import logging


def use_logging(func):

    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper


def foo():
    print('i am foo')

test = use_logging(foo)  # 因为装饰器use_logging(foo)返回的时函数对象wrapper这条语句相当于test=wrapper
test()                   # 执行test()就相当于执行 wrapper()


@use_logging
def foo():
    print("i am foo")

print("-----------使用语法糖后----------------")
foo()
