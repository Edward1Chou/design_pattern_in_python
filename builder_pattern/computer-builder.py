#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: computer-builder.py
module description: builder pattern for build computer
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/05/22 20:01
"""


class Computer(object):
    """
    abstract class for computer
    """
    def __init__(self, serial_num):
        self.serial = serial_num
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = {'Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu)}
        return '\n'.join(info)


class ComputerBuilder(object):
    """
    implement for builder pattern
    """
    def __init__(self):
        self.computer = Computer('ABC123456')

    def configure_memory(self, memory_amount):
        """
        :param memory_amount: 
        :return: 
        """
        self.computer.memory = memory_amount

    def configure_hdd(self, hdd_amount):
        """
        :param hdd_amount: 
        :return: 
        """
        self.computer.hdd = hdd_amount

    def configure_gpu(self, gpu_module):
        """
        :param gpu_module: 
        :return: 
        """
        self.computer.gpu = gpu_module


class HardwareEngineer(object):
    """
    director
    """
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        """
        :param memory: 
        :param hdd: 
        :param gpu: 
        :return: 
        """
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=8, hdd=1000, gpu='Titax')
    computer = engineer.computer
    print(computer)
