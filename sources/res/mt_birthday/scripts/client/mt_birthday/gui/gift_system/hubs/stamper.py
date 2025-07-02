from gui.gift_system.hubs.base.stamper import GiftEventBaseStamper
from mt_birthday.birthday_constants import BIRTHDAY_2025_STAMP_CODE, BIRTHDAY_2025_STAMP_CODE_SPECIAL

class GiftEventBirthdayStamper(GiftEventBaseStamper):
    __slots__ = ()
    _STAMPS = {
     BIRTHDAY_2025_STAMP_CODE, BIRTHDAY_2025_STAMP_CODE_SPECIAL}