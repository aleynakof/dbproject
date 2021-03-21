import psycopg2
from psycopg2 import Error
import datetime

try:
    connection = psycopg2.connect(user='postgres',
                                  password='postgres',
                                  host='localhost',
                                  port=5432,
                                  database='postgres'
                                  )
    cursor = connection.cursor()

    # mobile tablosunu düşürüyoruz. Rollback'i yok
    # table_drop_sorgu = 'drop table mobile'
    #
    # print('Mobile tablosu drop edildi')
    #
    # # SQL sorgusu yazalım.
    # create_table_query = '''CREATE TABLE mobile
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       MODEL           TEXT    NOT NULL,
    #       PRICE         REAL); '''
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Table created successfully in PostgreSQL ")
    #
    # # SQL sorgusu çalıştıralım.
    # cursor.execute('select version()')
    # kayit = cursor.fetchone()
    # print(kayit)

    # insert
    # insert_sorgu1 = "insert into mobile values(1,'Iphone', 5000)"
    # insert_sorgu2 = "insert into mobile values(2,'Samsung', 15000)"
    # insert_sorgu3 = "insert into mobile values(3,'Vestel', 7000)"
    # insert_sorgu4 = "insert into mobile values(4,'Aselsan', 9000)"
    #
    # cursor.execute(insert_sorgu1)
    # cursor.execute(insert_sorgu2)
    # cursor.execute(insert_sorgu3)
    # cursor.execute(insert_sorgu4)
    # connection.commit()
    # print("başarılı")

    # update sorgu
    # update, olmayan satırı update ederken hata vermez.
    # row_count ile kontrol edilmeli
    # update_sorgu = '''update mobile
    #                  set price=51000
    #                  where id=13'''
    #
    # cursor.execute(update_sorgu)
    # sonuc = cursor.rowcount
    # connection.commit()
    #
    # if sonuc > 0:
    #     print('Update başarılı')
    # else:
    #     print('Update basarısız')

    # delete sorgu
    # delete_sorgu = 'delete from mobile where id=4'
    # cursor.execute(delete_sorgu)
    # sonuc = cursor.rowcount
    # connection.commit()

    # if sonuc > 0:
    #     print('Silme başarılı')
    # else:
    #     print('Silme basarısız')

    # # select sorgu
    # select_sorgu = 'select * from mobile'
    # cursor.execute(select_sorgu)
    # data = cursor.fetchall()
    # # liste geliyor
    # print('Data:', data)
    # print(data[0])

    # item tablosu oluşturuyoruz
    item_create_sorgu = '''
        CREATE TABLE item ( 
        item_id serial NOT NULL PRIMARY KEY, 
        item_name VARCHAR (100) NOT NULL, 
        purchase_time timestamp NOT NULL,
        price INTEGER NOT NULL, 
        )
    '''
    cursor.execute(item_create_sorgu)
    print('item tablosu oluşturuldu')

    # item tablosuna insert sorgusu oluşturalım
    item_insert_sorgu = 'insert into item values(%s, %s, %s,%s,%s)'
    simdi = datetime.datetime.now()
    item_tuple = (12, 'Keyboard', simdi, 150)
    cursor.execute(item_insert_sorgu, item_tuple)
    connection.commit()
    print('item basariyla eklendi.')

    cursor.execute(item_create_sorgu)

    print('Item tablosu oluşturuldu.')

    # item tablosu düşür.

    item_drop_sorgu = 'drop table item'
    cursor.execute(item_drop_sorgu)
    connection.commit()

    print('Item tablosu düşürüldü')
except (Exception, Error) as e:
    print("Hata oluştu", e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Bağlantı kapatıldı")
