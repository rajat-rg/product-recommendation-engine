from django.core.management.base import BaseCommand
import pandas as pd
from products.models import products_model
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        data = pd.read_csv('5000_products.csv')
        for PID, TITLE, TAGS in zip(data.uniq_id, data.product_name, data.tags):
            model = products_model(PID = PID, name = TITLE, tags = TAGS)
            model.save()
        # now run the command in cmd: python manage.py updatemodels 