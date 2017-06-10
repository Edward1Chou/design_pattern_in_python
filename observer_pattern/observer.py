#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: observer.py
module description: implement of observer_pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/10 14:28
"""


class Publisher(object):
    """
    发布者：Publisher
    """
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers] # 广播


class DefaultFormatter(Publisher):
    """
    继承Publisher: 默认的格式
    """
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name,
                                               self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify() # if try is right execute else


class HexFormatter(object):
    """
    与Publisher()整体、部分关系(关联)
    十六进制格式化程序
    """
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name,
                                                      hex(publisher.data)))


class BinaryFormatter(object):
    """
    与Publisher()整体、部分关系（关联）
    二进制格式化程序
    """
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name,
                                                      bin(publisher.data)))


if __name__ == '__main__':
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print() # 预防性编程
    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)

