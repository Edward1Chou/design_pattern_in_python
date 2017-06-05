#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: facade.py
module description: implement for facade pattern
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/05 11:55
"""
from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class User(object):
    pass


class Process(object):
    pass


class File(object):
    pass


class Server(metaclass=ABCMeta):
    """
    abstract class for server
    """
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    """
    file server: inherit Server class
    """
    def __init__(self):
        """
        初始化文件服务进程要求的操作
        """
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        """
        启动文件服务进程要求的操作
        :return: 
        """
        print('booting the {}'.format(self))
        self.state = State.running

    def kill(self, restart=True):
        """
        终止文件服务进程要求的操作
        :param restart: 
        :return: 
        """
        print('Killing {}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        """
        检查访问权限的有效性和用户权限等
        :param user: 
        :param name: 
        :param permission: 
        :return: 
        """
        print("trying to create the file '{}' for user '{}' with"
              "permissions {}".format(name, user, permissions))


class ProcessServer(Server):
    """
    process server: inherit Server class
    """
    def __init__(self):
        """
        初始化进程服务进程要求的操作
        """
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        """
        启动进程服务进程要求的操作
        :return: 
        """
        print('booting the {}'.format(self))
        self.state = State.running

    def kill(self, restart=True):
        """
        终止进程服务进程要求的操作
        :param restart: 
        :return: 
        """
        print('Killing {}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        """
        检查用户权限和生成PID等
        :param user: 
        :param name: 
        :return: 
        """
        print("trying to create the process '{}' for user '{}'".format(name, user))


class WindowsServer(object):
    pass


class NetworkServer(object):
    pass


class OperatingSystem(object):
    """
    外观
    """
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


if __name__ == '__main__':
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')

