import importlib
_WULF_TOOLTIP_CONTENT_FACTORY_PATHS = ('gui.impl.lobby.tooltips.preferred_map_slot_reward_tooltip', )

def registerWulfTooltipContentFactories():
    for path in _WULF_TOOLTIP_CONTENT_FACTORY_PATHS:
        importlib.import_module(path)