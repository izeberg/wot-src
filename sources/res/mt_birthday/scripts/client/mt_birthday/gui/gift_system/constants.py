from gifts import gifts_common
from constants_utils import ConstInjector

class GiftEventID(gifts_common.GiftEventID, ConstInjector):
    BIRTHDAY_2025 = 4
    gifts_common.GiftEventID.ALL += (BIRTHDAY_2025,)