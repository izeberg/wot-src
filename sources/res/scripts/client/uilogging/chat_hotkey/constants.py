from enum import Enum
FEATURE = 'chat_hotkey'

class ChatHotkeyLogActions(Enum):
    HOTKEY_CLICKED = 'hotkey_clicked'
    COMMAND_SELECTED = 'command_selected'