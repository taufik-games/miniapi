import base.parse


class HTMLDoc(base.parse.HTMLDoc):
    """
    Standard Fields of HTML parse
    """
    _name = ''
    _brand = ''
    _price = 0
    _old_price = 0

    @property
    def name(self):
        return self._name

    @property
    def brand(self):
        return self._brand

    @property
    def price(self):
        return self._price, self._old_price

    @staticmethod
    def provider(name, html_doc):
        # Choose provider
        if name == 'omoda.nl':
            return Omoda(html_doc=html_doc)
        elif name == 'zalando.nl':
            return Zalando(html_doc=html_doc)


class Omoda(HTMLDoc):
    """
    HTML parse of omoda.nl
    """

    def detail(self):
        return self.html_doc.main.find('section', {'class': 'section-detail'})

    @property
    def name(self):
        if self.detail():
            element = self.detail().find('h1')
            if element:
                self._name = element.string

        return self._name

    @property
    def brand(self):
        if self.detail():
            element = self.detail().find('h2')
            if element:
                self._brand = element.string

        return self._brand

    def price_find(self):
        price = 0
        old_price = 0
        element = self.html_doc.find('div', {'id': 'artikel-prijs'})
        if element:
            price = element.ins.string.split('\u00a0')[1]

            old_price = None
            if element.find('del'):
                old_price = element.find('del').string.split('\u00a0')[1]

            if not old_price:
                old_price = price

        return price, old_price

    @property
    def price(self):
        self._price, self._old_price = self.price_find()
        return self._price, self._old_price


class Zalando(HTMLDoc):
    """
    HTML parse of zalanda.nl
    """

    def product(self):
        return self.html_doc.find('div', {'id': 'productSidebar'})

    @property
    def name(self):
        self._name = self.product().h1.find('span', {'itemprop': 'name'}).string
        return self._name

    @property
    def brand(self):
        self._brand = self.product().h1.find('span', {'itemprop': 'brand'}).string
        return self._brand

    def price_find(self):
        # Standard
        element = self.html_doc.find('div', {'id': 'productDetailsMain'}).\
            find('span', {'itemprop': 'price'})
        if element:
            return element.string.split(' ')[1], element.string.split(' ')[1]

        # Discount
        element = self.html_doc.find('div', {'id': 'productDetailsMain'}). \
            find('span', {'id': 'articlePrice'})
        if element:
            old_price = self.html_doc.find('div', {'id': 'productDetailsMain'}). \
                find('span', {'id': 'articleOldPrice'})
            return element.string.split(' ')[1], old_price.string.split(' ')[1]

    @property
    def price(self):
        self._price, self._old_price = self.price_find()
        return self._price, self._old_price

