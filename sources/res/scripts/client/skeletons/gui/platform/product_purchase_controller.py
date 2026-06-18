from __future__ import absolute_import
from collections import namedtuple
WotShopPrice = namedtuple('WotShopPrice', ('currency', 'value'))

class IWotShopPurchaseController(object):

    def purchaseProduct(self, storefront, productCode, productPrice):
        raise NotImplementedError