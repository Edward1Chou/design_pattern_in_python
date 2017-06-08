#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: proxy.py
module description: implement of proxy design pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/08 17:08
"""


class SensitiveInfo(object):
    """
    store information
    """
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


class Info(object):
    """
    protected proxy for SensitiveInfo
    """
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = 'i am password!'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret?')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


if __name__ == '__main__':
    info = Info()

    while True:
        print('1. read list | 2. add user | 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('input name: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))
