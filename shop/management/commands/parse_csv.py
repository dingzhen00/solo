import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from itertools import islice
from shop.models import eletronics, eletronicsdetail

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/shop/data/empty_file2.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
                # for row in reader:
            i = 1
            for row in islice(reader, 5000):
                print(row)
                ele=eletronics.objects.filter(eid=i).first()
                eproducts = eletronicsdetail.objects.create(img=row[0], href=row[1],eletronics=ele)
                eproducts.save()
                i+=1
                print("data parsed successfully")

