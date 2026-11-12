import typing
from gui.shared.formatters import text_styles
from new_year.gui.bonuses.bonuses_packers import packBonuses
from gui.impl import backport
from gui.impl.gen import R
ITEMS_FORMATTER = "<font color='#F2F2F7'>{} x{}</font>"
ITEMS_WO_COUNT_FORMATTER = "<font color='#F2F2F7'>{}</font>"
CURRENCIES_FORMATTER = "<font color='#F2F2F7'>{}: {}</font>"

def formatPurchaseItems(items, packer=None, skipCount=False):
    formattedItems = []
    for bonus in packBonuses(items, packer):
        count = bonus.getValue() or 1
        label = bonus.getLabel()
        backportText = R.strings.ny.notifications.reward.product()
        if bonus.getName() in ('dossier_badge', 'vehicles'):
            formattedItems.append(backport.text(backportText, product=ITEMS_WO_COUNT_FORMATTER.format(label)))
        elif bonus.getName() == 'premium_plus':
            days = backport.text(R.strings.menu.Time.timeLeftShort.days(), day=count)
            formattedItems.append(backport.text(backportText, product=CURRENCIES_FORMATTER.format(label, days)))
        elif bonus.getName() in ('credits', 'gold', 'crystal', 'freeXP'):
            formattedItems.append(backport.text(backportText, product=CURRENCIES_FORMATTER.format(label, count)))
        else:
            formattedItems.append(backport.text(backportText, product=ITEMS_FORMATTER.format(label, count)))

    return (', ').join(formattedItems)


ITEM_VALUE_FORMAT = text_styles.tutorial('x{}')

def formatPurchasedItems(items):
    formattedItems = []
    for name, count in items.iteritems():
        backportText = R.strings.ny.notification.racoon.purchased.item.dyn(name)()
        formattedItems.append(backport.text(backportText, text=ITEM_VALUE_FORMAT.format(count)))

    return ('<br/><br/>').join(formattedItems)


def formatActivatedItem(name, count, progressPoints, leaderPoint):
    formattedItems = []
    subHeaderText = R.strings.ny.notification.racoon.activated.subHeader.dyn(name)()
    formattedItems.append(backport.text(subHeaderText, count=ITEM_VALUE_FORMAT.format(int(count))))
    progressText = R.strings.ny.notification.racoon.activated.progressPoints()
    formattedItems.append(backport.text(progressText, count=text_styles.vehicleName(str(int(progressPoints)))))
    if leaderPoint:
        leaderText = R.strings.ny.notification.racoon.activated.leaderPoints()
        formattedItems.append(backport.text(leaderText, count=text_styles.vehicleName(str(int(leaderPoint)))))
    return ('<br/><br/>').join(formattedItems)