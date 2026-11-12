import logging
from constants import LOOTBOX_KEY_PREFIX
from gui.shared.money import ZERO_MONEY, Currency, Money
from new_year_common.items.components.ny_constants import TOKEN_MANDARIN
_TOKEN_COMPENSATION_PREFIX = 'lb_comp:'
_CURRENCY_TOKENS = (TOKEN_MANDARIN,)
_logger = logging.getLogger(__name__)

def prepareRaidRewardResult(result):
    if result and result.success and result.auxData:
        bonus = result.auxData.get('bonus', [])
        dataUsedKeys = result.auxData.get('clientData', {}).get('usedKeys', {})
        dataFailedKeys = result.auxData.get('extData', {}).get('failedKeys', {})
        for rewards in bonus:
            preformatCompensationValue(rewards)
            preformatStyle(rewards)
            preformatKey(rewards, dataUsedKeys, dataFailedKeys)
            preformatVehicleItems(rewards)
            preformatMeta(rewards, result)


def preformatCompensationValue(rewards):
    compValue = ZERO_MONEY
    for vehiclesDict in _getVehiclesList(rewards):
        for vehicleData in vehiclesDict.itervalues():
            for compensation in ('rentCompensation', 'customCompensation'):
                if compensation in vehicleData:
                    compValue += Money.makeFromMoneyTuple(vehicleData[compensation])

    tokens = rewards.get('tokens', {})
    popTokens = set()
    for tokenName, info in tokens.iteritems():
        if tokenName.startswith(_TOKEN_COMPENSATION_PREFIX):
            currency, amount = _parseCompensationToken(tokenName)
            compValue += Money.makeFrom(currency, amount)
            if currency in _CURRENCY_TOKENS:
                tokens[currency]['count'] -= amount * info['count']
                if tokens[currency]['count'] == 0:
                    popTokens.add(currency)

    for tokenName in popTokens:
        tokens.pop(tokenName)

    for currency in Currency.ALL:
        if compValue.get(currency, 0) > 0:
            currencyValue = rewards.pop(currency, 0)
            newCurrencyValue = currencyValue - compValue.get(currency, 0)
            if newCurrencyValue:
                rewards[currency] = max(newCurrencyValue, 0)


def preformatStyle(rewards):
    customizations = rewards.get('customizations', [])
    if customizations:
        rewards['customizations'] = [ cData for cData in customizations if not cData.get('boundToCurrentVehicle', False) ]
        if not rewards['customizations']:
            rewards.pop('customizations')


def preformatKey(rewards, dataUsedKeys, dataFailedKeys):
    for token in rewards.get('tokens', {}).iterkeys():
        if token.startswith(LOOTBOX_KEY_PREFIX):
            _, keyID = token.split(':')
            if int(keyID) in dataUsedKeys or int(keyID) in dataFailedKeys:
                rewards['tokens'][token]['count'] += 1


def preformatVehicleItems(rewards):
    items = rewards.get('items')
    if not items:
        return
    else:
        for vehiclesDict in _getVehiclesList(rewards):
            for vehicleData in vehiclesDict.itervalues():
                for unlockModule in vehicleData.get('unlockModules', []):
                    items.pop(unlockModule, None)

        return


def preformatMeta(rewards, result):
    meta = rewards.get('meta', {})
    if not meta:
        return
    else:
        clientData = result.auxData.setdefault('clientData', {})
        clientData['uniqueOpening'] = clientData.get('uniqueOpening', False) | (meta.pop('glow', None) is not None)
        if not meta:
            del rewards['meta']
        return


def _getVehiclesList(rewards):
    vehiclesList = rewards.get('vehicles', [])
    if isinstance(vehiclesList, dict):
        return [vehiclesList]
    return vehiclesList


def _parseCompensationToken(tokenID):
    try:
        _, currency, value, _, _ = tokenID.split(':')
        return (currency, int(value))
    except ValueError as error:
        _logger.error(error)
        return (None, None)

    return