from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class ChatModel(BaseClientModel):
    __slots__ = ('hide', )

    def __init__(self, hide):
        super(ChatModel, self).__init__()
        self.hide = hide

    def __repr__(self):
        return '<ChatModel>: hide=%s' % self.hide