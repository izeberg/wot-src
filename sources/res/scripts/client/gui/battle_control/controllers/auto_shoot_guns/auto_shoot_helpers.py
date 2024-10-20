from enum import Enum
AUTO_SHOOT_DEV_KEYS = False
AUTO_SHOOT_DEV_BURST_CLAMP = 1.0

class AutoShootDevCommand(Enum):
    RATE_UP = 0
    RATE_DOWN = 1
    RATE_SPEED_UP = 2
    RATE_SPEED_DOWN = 3
    CLAMP_BURST = 4
    RESET = 5