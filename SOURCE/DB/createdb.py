# -*- coding: utf-8 -*-

# This module creates database if it not exist.

# import checkdb
import sqlite3
import os

name_db = 'vsem.db'
head_path=os.path.split(os.path.abspath('..\\'))
print('Диск с БД createdb.py: ', head_path[0])
path_db_dir = os.path.join(head_path[0], 'DATA\\')
print('Текущиий каталог: ', path_db_dir)	# временно, чтобы видеть сообщения консоли
path_db = os.path.join(path_db_dir, name_db)
print('Путь к базе данных: ', path_db)		# временно, чтобы видеть сообщения консоли

# проверка на существование базы данных
if not os.path.exists(path_db):
    try:
        conn = sqlite3.connect(path_db)     # создание базы данных
        cursor = conn.cursor()              # создание курсора выполнения запросов к БД
        # create tables
        cursor.executescript("""CREATE TABLE tirages
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        tirage TEXT);
        
        CREATE TABLE quantity_tirages
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        quantity_tirages INTEGER);  -- default volue 1
        
        CREATE TABLE periods
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        period INTEGER);   -- period: 1 - 1 tirage, 2 - per tirage, 3 - per month
        
        CREATE TABLE phones
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT);
        
        CREATE TABLE addresses
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT);
        
        CREATE TABLE announces
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_tirage INTEGER NOT NULL,
        id_quantity_tir INTEGER NOT NULL,
        id_period INTEGER,
        id_phone INTEGER,
        id_address INTEGER,
        announces TEXT,
        FOREIGN KEY (id_tirage) REFERENCES tirages (id)
        FOREIGN KEY (id_quantity_tir) REFERENCES quantity_tirages (id)
        FOREIGN KEY (id_period) REFERENCES periods (id)
        FOREIGN KEY (id_phone) REFERENCES phones (id)
        FOREIGN KEY (id_address) REFERENCES addresses (id)
        );
        """)
        conn.commit()                       # фиксирую выполенные операции
        conn.close()                        # Закрываю соединение
    except sqlite3.Error as message:            
        print('Ошибка БД: ' + str(message))


input('Press Enter ')   # временно, чтобы видеть сообщения консоли