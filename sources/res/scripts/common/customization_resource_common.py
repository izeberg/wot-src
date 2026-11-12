CUSTOMIZATION_RESOURCE_CURRENCY_CODE = 'paintcoin'

def getCustomizationResourceExchangePrice(priceGroups, priceGroupTags):
    priceGroupTags = frozenset(priceGroupTags)
    tagMatches = [ group for group in priceGroups if frozenset(group['tags']) and frozenset(group['tags']).issubset(priceGroupTags)
                 ]
    if len(tagMatches) == 1:
        return tagMatches[0]['price']
    return 0