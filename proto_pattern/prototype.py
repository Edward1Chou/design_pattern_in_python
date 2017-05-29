#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: proto design pattern
module description: proto pattern for books
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/29
"""

import copy
from collections import OrderedDict


class Book(object):
    """
    abstract class for the book
    """
    def __init__(self, name, authors, price, **rest):
        """
        :param name: 
        :param authors: 
        :param price: 
        :param rest: 包括 出版商、长度、标签、出版日期 
        """
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        introduce_list = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            introduce_list.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                introduce_list.append('$')
            introduce_list.append('\n')
        return ''.join(introduce_list)


class Prototype(object):
    """
    implement for proto pattern
    """
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        """
        to track object
        :param identifier: 
        :param obj: 
        :return: 
        """
        self.objects[identifier] = obj

    def unregister(self, identifier):
        """
        delete obj
        :param identifier: 
        :return: 
        """
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        """
        deep copy
        :param identifier: 
        :param attr: 
        :return: 
        """
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M. Ritchie'),
              price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structure'))
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
    print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))



