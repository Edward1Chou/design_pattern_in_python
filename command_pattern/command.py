#! /bin/env python
# -*- coding: utf-8 -*-
"""
module name: command.py
module description: implement of command pattern 
Authors: zhouchengyu(edwardchou903@icloud.com)
Date:    2017/06/09 17:04
"""
import os

verbose = True


class RenameFile(object):
    """
    rename filename
    """
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile(object):
    """
    create file
    """
    def __init__(self, path, txt='hello world!\n'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile(object):
    """
    read file
    """
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    """
    delet file, no undo
    :param path: 
    :return: 
    """
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)

if __name__ == '__main__':
    orig_name, new_name = 'file1', 'file2'

    command = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        command.append(cmd)
    [c.execute() for c in command]
    answer = input('reverse the executed command? [y/n]')

    if answer not in 'yY':
        print("no undo ,execute successfully!")
        exit()

    for c in reversed(command):
        try:
            c.undo()
        except AttributeError as e:
            pass
