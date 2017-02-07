from haystack import indexes
from catalog.models import Product


class ProductIndexes(indexes.SearchIndex, indexes.Indexable):
    """
    Fulltext Index of the product model
    """
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    price = indexes.DecimalField(model_attr='price')
    old_price = indexes.DecimalField(model_attr='old_price')
    provider = indexes.CharField()
    brand = indexes.CharField()
    categories = indexes.MultiValueField(null=True)

    def get_model(self):
        return Product

    def prepare_provider(self, obj):
        return obj.provider.name

    def prepare_brand(self, obj):
        return obj.brand.name

    def prepare_categories(self, obj):
        return [category.name for category in obj.categories.all()]
