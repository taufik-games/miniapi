from haystack import indexes
from crawl.models import Page


class PageIndexes(indexes.SearchIndex, indexes.Indexable):
    """
    Config indexes of page.
    This is needed to check product category.
    Only the type of product_listing is needed.
    """
    text = indexes.CharField(document=True, use_template=True)
    page_id = indexes.IntegerField(model_attr='id')
    type = indexes.CharField(model_attr='type')
    provider = indexes.CharField()
    number = indexes.IntegerField()
    category = indexes.CharField()
    body = indexes.CharField()

    def get_model(self):
        return Page

    def prepare_provider(self, obj):
        return obj.file.provider

    def prepare_number(self, obj):
        return obj.number if obj.number else 0

    def prepare_category(self, obj):
        category = '-'
        if obj.type == 'product_listing':
            category = obj.category
        return category

    def prepare_body(self, obj):
        # Other then product_listing is not important
        body = '-'
        if obj.type == 'product_listing':
            body = obj.body
        return body
