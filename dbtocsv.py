import psycopg2
from psycopg2 import Error
import datetime
import csv

dosya_adi = 'mobil_' + datetime.date.today().strftime("%d-%m-%Y") + '.csv'

csv_file = open(dosya_adi, "w", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Id', 'Model', 'Price'])

try:
    connection = psycopg2.connect(user='postgres',
                                  password='postgres',
                                  host='127.0.0.1',
                                  port=5432,
                                  database='postgres'
                                  )

    cursor = connection.cursor()
    # boş liste oluştur
    # model_satir = []

    select_sorgu = 'select * from mobile order by id'

    cursor.execute(select_sorgu)

    data = cursor.fetchall()
    print(type(data))
    print(data)

    print('***********************')
    for satir in data:
        # tuple ve liste alır
        csv_writer.writerow(satir)
        # print(satir)

except (Exception, Error) as e:
    print('Hata oluştu', e)

finally:
    csv_file.close()

    if connection:
        cursor.close()
        connection.close()
        print('Bağlantı kapatıldı')
