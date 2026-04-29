import CGF
_historicalBattlesManagers = {}

def registerHistoricalBattlesManager(domain):

    def registrator(cls):
        CGF.registerManager(cls, False, domain)
        _historicalBattlesManagers[cls.__name__] = (cls, domain)
        return cls

    return registrator


def historicalBattlesManagers():
    return _historicalBattlesManagers