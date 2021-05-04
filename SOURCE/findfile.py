#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 This module find file on his name and path to him.
 If file exist return absolute path to this file.
"""

import os
#import sys


class FindFile():
    def ffile(name, directory):
        head_path = os.path.split(os.path.abspath('..\\'))
        #print ('1:', os.path.abspath('..\\'))
        #print('2: Диск с БД createdb.py: ', head_path[0])
        #path_db_dir = os.path.join(head_path[0], 'DATA\\')
        path_file = str(head_path[0]) + '\\' + 'VSEM\\' + directory + '\\' + '\\' + name
        #print('4: Путь к базе данных: ', path_file)		# временно, чтобы видеть сообщения консоли
        #input(' В середине класса FindFile press Enter')
        return path_file


#filename = 'vsem.db'
#dirname = 'DATA'
#print('filename:', name, 'dirname:', directory)
#input('1 Press ENTER')

if __name__ == "__main__":
    path_file = FindFile.ffile(filename, dirname)
    #print('path_file', path_file)
    #input('2 Press ENTER')

#input('В самом конце Press ENTER')