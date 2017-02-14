import base.api
from haystack.query import SearchQuerySet


class Search(base.api.Api):

    def get_check(self):
        response = None
        results = []

        if self.request.query_params.get('q'):
            response = SearchQuerySet().filter(content=self.request.query_params.get('q'))

        if self.request.query_params.get('name'):
            response = SearchQuerySet().filter(name__exact=self.request.query_params.get('name')) if not response \
                else response.filter(name__exact=self.request.query_params.get('name'))

        if self.request.query_params.get('brand'):
            response = SearchQuerySet().filter(brand__exact=self.request.query_params.get('brand')) if not response \
                else response.filter(brand__exact=self.request.query_params.get('brand'))

        if response:
            for result in response:
                results.append({'name': result.name, 'provider': result.provider, 'brand': result.brand,
                                'price': result.price, 'old_price': result.old_price})

        return results, self.http.HTTP_200_OK

