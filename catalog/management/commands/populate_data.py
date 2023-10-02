import  json

from django.core.management import BaseCommand

from catalog.models import Product, Catrgory, Contact
from skystore.settings import  BASE_DIR
class Command(BaseCommand):
    help = 'Заполнение базы данных фикстурами'

    def handle(self, *args, **options):
        Product.object.all().delete()
        Category.object.all().delete()
        Contact.object.all().delete()

        with open(BASE_DIR/'catalog/fixtures/category.json', encoding='utf-8') as fp:
            category_data = json.load(fp)
            for item in category_data:
                Catrgory.objects.create(
                    pk= item['pk'],
                    name = item["fields"]["name"],
                    description = item["fields"]["description"]
                )
        with open(BASE_DIR/'catalog/fixtures/product.json', encoding='utf-8') as fp:
            product_data = json.load(fp)
            for item in product_data:
                category_pk = item["fields"]["category"]
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(
                    pk= item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"],
                    preview_description=item["fields"]["preview_description"],
                    image=item["fields"]["image"]
                    category=category,
                    price=item["fields"]["price"],
                    created_at=item["fields"]["created_at"],
                    last_modified=item["fields"]["last_modified"],
                )

        with open(BASE_DIR/'catalog/fixtures/contact.json', encoding='utf-8') as fp:
            contact_data = json.load(fp)
            for item in contact_data:
                Contact.objects.create(
                    pk= item['pk'],
                    country=item["fields"]["country"],
                    inn=item["fields"]["inn"],
                    address=item["fields"]["address"] )