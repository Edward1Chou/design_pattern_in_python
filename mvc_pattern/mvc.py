#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: mvc.py
module description: implement for model-view-controller pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/07 10:52
"""

quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel(object):
    """
    model
    """
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not find!'
        return value


class QuoteTerminalView(object):
    """
    view
    """
    def show(self, quote):
        print('And the quote is: {}'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see?')


class QuoteTerminalController(object):
    """
    controller
    """
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
        quote = self.model.get_quote(n)
        self.view.show(quote)


if __name__ == "__main__":
    control = QuoteTerminalController()
    while True:
        control.run()