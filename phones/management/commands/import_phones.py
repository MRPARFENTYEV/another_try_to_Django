import csv
import sys

import psycopg2
from django.core.management.base import BaseCommand
# sys.path.insert(0, '..')
from phones.models import Phone





class Command(BaseCommand):
    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_model =Phone(id =phone['id'], name=phone['name'], price=phone['price'], image=phone['image'],
                               release_date=phone['release_date'],lte_exists=phone['lte_exists'],
                                  slug=str(phone['name']).lower().replace(' ', '-'))
            phone_model.save()
            # for p_val in phone.values():
            #     print(phone.values())
            #     indif = [el for el in p_val]
            #
            #     def create_slug(phone_name):
            #
            #         return phone_name.lower().replace(' ', '-')
            #     phone_model.save()
            #     print(indif)
            #     print('Look here')
            #     phone_mod = Phone(name=indif[1], price=indif[2], image=indif[3], release_date=indif[4],lte_exists=indif[5],
            #                       slug=create_slug(indif[1]))
            #
            #     phone_mod.save()

# import  csv
# key = {'default': {
#     'database': 'netology_import_phones',
#     'host': '127.0.0.1',
#     'port': '5432',
#     'user': 'postgres',
#     'password': 'Sqlzaebal',
# }}
# conn = psycopg2.connect(**key['default'])
# def insert_phone(indif):
#     with conn.cursor() as cursor:
#         print(indif)
#         cursor.execute('INSERT INTO phones_phone(name,image,price,release_date,lte_exists,slug) VALUES(%s,%s,%s,%s,%s,%s)', (indif[1],indif[2],indif[3],indif[4],indif[5],create_slug(indif[1])))
#
#
#         conn.commit()
#         print("Данные добавлены")
# def create_slug(phone_name):
#     return phone_name.lower().replace(' ','-')
#
# with open(r'C:\Users\mrpar\DJANGO_DB\2.1-databases\work_with_database\phones.csv', 'r') as file:
#     phones = list(csv.DictReader(file, delimiter=';'))
#     # print(phones)
#     for phone in phones:
#         p_val = phone.values()
#         indif = [el for el in p_val]
#         insert_phone(indif)



