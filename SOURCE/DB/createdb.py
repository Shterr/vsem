# -*- coding: utf-8 -*-

# This module creates database if it not exist.

# import checkdb
import sqlite3
import os

name_db = 'vsem.db'
head_path=os.path.split(os.path.abspath('..\\'))
print('Путь к файлу createdb.py: ', head_path[0])

path_db_dir = os.path.join(head_path[0], 'DATA\\')
print('Текущиий каталог: ', path_db_dir)	# временно, чтобы видеть сообщения консоли
path_db = os.path.join(path_db_dir, name_db)
print('Путь к базе данных: ', path_db)		# временно, чтобы видеть сообщения консоли

# проверка на существование базы данных
if not os.path.exists(path_db):
    try:
        conn = sqlite3.connect(path_db)     # создание базы данных
        cursor = conn.cursor()              # создание курсора выполнения запросов к БД
        conn.commit()                       # фиксирую выполенные операции
        conn.close()                        # Закрываю соединение
    except sqlite3.Error as message:            
        print('Ошибка БД: ' + str(message))

# Создание таблиц в БД
#conn = sqlite3.connect(path_db)
#cursor = conn.cursor()

input('Press Enter ')   # временно, чтобы видеть сообщения консоли