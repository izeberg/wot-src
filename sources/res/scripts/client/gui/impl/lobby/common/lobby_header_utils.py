from __future__ import absolute_import
HEADER_BUTTONS_COUNTERS_CHANGED_EVENT = 'lobbyHeaderButtonsCountersChanged'
_EXT_FIGHT_BUTTON_TOOLTIP_GETTERS = []

def registerFightButtonTooltipGetter(getter):
    _EXT_FIGHT_BUTTON_TOOLTIP_GETTERS.append(getter)


def findExtensionTooltip(pValidation):
    for getter in _EXT_FIGHT_BUTTON_TOOLTIP_GETTERS:
        tooltip = getter(pValidation)
        if tooltip is not None:
            return tooltip

    return