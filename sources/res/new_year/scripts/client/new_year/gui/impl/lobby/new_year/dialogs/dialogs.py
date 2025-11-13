from th_async import th_async, th_await
from BWUtil import AsyncReturn
from gui.impl.dialogs import dialogs

@th_async
def showBuyDialog(window):
    result = yield th_await(dialogs.show(window))
    raise AsyncReturn(result)