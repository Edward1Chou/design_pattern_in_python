#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: lazy.py
module description: virtual proxy to initial lazily
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/08 14:27
"""


class LazyProperty(object):
    """
    decorator/ descriptor to override __get__
    """
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        # print('function overriden:{}'.format(self.fget))
        # print("function's name: {}".format(self.fuc_name))

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        # print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Sample(object):
    """
    for test
    """
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5)) # 假设这一行计算成本比较大
        return self._resource


if __name__ == '__main__':
    t = Sample()
    print(t.x)
    print(t.y)
    # do more things
    print(t.resource)
    print(t.resource)
