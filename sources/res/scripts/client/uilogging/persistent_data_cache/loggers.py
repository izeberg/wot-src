import typing
from uilogging.base.logger import MetricsLogger, ifUILoggingEnabled, createPartnerID
from wotdecorators import noexcept
FEATURE = 'persistent_data_cache'
PDC_ERROR_ACTION = 'pdc_error'

class PDCFaultToleranceLogger(MetricsLogger):
    __slots__ = ()
    _ERROR_LEN_LIMIT = 499

    def __init__(self):
        super(PDCFaultToleranceLogger, self).__init__(FEATURE)

    @noexcept
    @ifUILoggingEnabled()
    def logErrors(self, errors):
        partnerID = createPartnerID() if len(errors) > 1 else None
        for errorType, (currentCount, error) in errors.iteritems():
            self.log(action=PDC_ERROR_ACTION, item=errorType, itemState=str(currentCount), info=error[:self._ERROR_LEN_LIMIT] or None, partnerID=partnerID)

        return