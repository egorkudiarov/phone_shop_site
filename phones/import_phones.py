import csv
from django.utils.text import slugify
from models import Phone

def handle(self, file_name='phones.csv', model=Phone):
    with open(file_name, newline='') as csvfile:
        filereader = csv.DictReader(csvfile, delimiter=';', dialect='UTF-8')
        for row in filereader:
            temp_model = model(
                id = row.get('id'),
                name = row.get('name'),
                price = row.get('price'),
                image = row.get('image'),
                lte_exists = row.get('lte_exists'),
                slug = slugify(row.get('name'))
                )
            print('xd')
            temp_model.save()

handle(file_name='phones.csv', model=Phone)
