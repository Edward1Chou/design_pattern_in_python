#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: factory_method
module description: design pattern: factory method 
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/15 22:05
"""

import xml.etree.ElementTree as Etree
import json


class JSONConnector(object):
    """
    parse class for json
    """
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector(object):
    """
    parse class for xml
    """
    def __init__(self, filepath):
        self.tree = Etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """
    :param filepath: 
    :return: 
    """
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    """
    wrap for connection_factory()
    :param filepath: 
    :return: 
    """
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory

if __name__ == '__main__':
    # test raise error
    sqlite_factory = connect_to('person.sq3')
    print()
    # test xml
    xml_factory = connect_to('person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person',
                                                     'lastName', 'Liar'))
    print('Found: {} person(s)'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({}): '.format(p.find('type').text),
               p.find('number').text) for p in liar.find('phoneNumbers')]
    print()
    # test json
    json_factory = connect_to('donut.json')
    json_data = json_factory.parsed_data
    print('Found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t
         in donut['topping']]










