#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: apple-factory.py
module description: factory pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/22 19:15
"""
MIN14 = '1.4GHz Mac mini'


class AppleFactory(object):
    """
    factory pattern for buy apple    
    """
    class MacMini14(object):
        """
        apple model: mac_min_14
        """
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = {"Model: {}".format(MIN14),
                    "Memory: {}GB".format(self.memory),
                    "Hdd: {}GB".format(self.hdd),
                    "Graphics Card: {}".format(self.gpu)}
            return '\n'.join(info)

    def build_computer(self, model):
        """
        implement factory pattern
        :return: 
        """
        if (model == MIN14):
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))


if __name__ == "__main__":
    fac = AppleFactory()
    mac_mini = fac.build_computer(MIN14)
    print(mac_mini)
    unknown = fac.build_computer("Alias")
