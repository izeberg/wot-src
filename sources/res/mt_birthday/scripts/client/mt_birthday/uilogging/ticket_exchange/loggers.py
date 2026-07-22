from uilogging.base.logger import MetricsLogger
from wotdecorators import noexcept

class TicketExchangeLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(TicketExchangeLogger, self).__init__('exchange_tickets')

    @noexcept
    def logEnter(self):
        self.log(action='EnterMainScreen', item='MainScreen')

    @noexcept
    def logExit(self):
        self.log(action='ExitMainScreen', item='MainScreen')