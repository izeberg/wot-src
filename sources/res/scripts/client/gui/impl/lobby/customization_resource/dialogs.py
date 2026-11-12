from BWUtil import AsyncReturn
from gui.impl.dialogs import dialogs
from gui.impl.dialogs.gf_builders import ConfirmCancelDialogBuilder
from gui.impl.gen import R
from gui.impl.pub.dialog_window import DialogButtons
from th_async import th_async, th_await
_DIMMER_ALPHA = 0.8

@th_async
def showCustomizationResourceExitConfirmDialog():
    texts = R.strings.event.customizationResource.exitConfirmation
    layoutID = R.views.lobby.customization.CustomizationCloseConfirmationDialog()
    builder = ConfirmCancelDialogBuilder(layoutID=layoutID)
    builder.setTitle(texts.title())
    builder.setDescription(texts.description())
    builder.setConfirmButtonLabel(texts.confirm())
    builder.setCancelButtonLabel(texts.cancel())
    builder.setFocusedButtonID(DialogButtons.CANCEL)
    builder.setDimmerAlpha(_DIMMER_ALPHA)
    result = yield th_await(dialogs.show(builder.build()))
    raise AsyncReturn(result.result in DialogButtons.ACCEPT_BUTTONS)