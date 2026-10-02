import logging
from gui.impl import backport
from gui.impl.gen import R
_logger = logging.getLogger(__name__)

def getVehicleParameterText(paramName, isTTC=False, isLong=False, isPositive=False):
    res = default = R.strings.tank_setup.kpi.bonus
    if isTTC:
        res = res.ttc
    else:
        if isLong:
            res = res.longDescr
        if isPositive:
            res = res.positive
            default = default.positive
        else:
            res = res.negative
            default = default.negative
        result = res.dyn(paramName) or default.dyn(paramName)
        if not result:
            _logger.debug('Text for vehicle parameter is not found: name=%s, isTTC=%s, isLong=%s, isPositive=%s', paramName, isTTC, isLong, isPositive)
            return R.invalid()
    return result()


def _getSignAndParamName(param):
    try:
        from gui.shared.gui_items import KPI
        if isinstance(param, KPI):
            isPositiveVal = int(param.value) >= 0
            isPositiveSpecVal = int(param.specValue) >= 0 if param.specValue is not None else False
            return (
             param.name, isPositiveVal, isPositiveSpecVal)
        suffix = 'AbilityKpi'
        name = param.name[:-len(suffix)] if param.name.endswith(suffix) else param.name
        isSequence = isinstance(param.value, (tuple, list)) and len(param.value) >= 2
        isPositiveVal = int(param.value[0]) if isSequence else int(param.value) >= 0
        isPositiveSpecVal = int(param.value[1]) >= 0 if isSequence else False
        return (
         name, isPositiveVal, isPositiveSpecVal)
    except (TypeError, IndexError, ValueError):
        paramName = getattr(param, 'name', 'Unknown')
        _logger.warning('_getSignAndParamName ended with error. Incorrect value or specValue, param name = [%s]', paramName)
        return

    return


def getKpiCombinedParameter(param):
    data = _getSignAndParamName(param)
    if data is None:
        return ''
    else:
        name, isPositiveVal, isPositiveSpecVal = data
        kpiValRes = R.strings.tank_setup.kpi.value
        kpiSpecValRes = R.strings.tank_setup.kpi.specValue
        value = (kpiValRes.positive if isPositiveVal else kpiValRes.negative).dyn(name)
        specValue = (kpiSpecValRes.positive if isPositiveSpecVal else kpiSpecValRes.negative).dyn(name)
        if not value or not specValue:
            _logger.warning('getKpiCombinedParameter some resources missing')
            return ''
        return backport.text(R.strings.tank_setup.kpi.bonus.combined.withoutSign(), value=backport.text(value()), specValue=backport.text(specValue()))


def getParamTitle(param):
    data = _getSignAndParamName(param)
    if data is None:
        return ''
    else:
        name, isPositiveVal, _ = data
        kpiRes = R.strings.tank_setup.kpi
        kpiValTitle = kpiRes.value.title
        valueSignKey = kpiRes.positive.capital if isPositiveVal else kpiRes.negative.capital
        value = kpiValTitle.dyn(name)
        if not (value and valueSignKey):
            _logger.warning('getParamTitle some resources missing')
            return ''
        return backport.text(R.strings.tank_setup.kpi.bonus(), valueSign=backport.text(valueSignKey()), value=backport.text(value()))


def getCombinedParamTitle(param):
    data = _getSignAndParamName(param)
    if data is None:
        return ''
    else:
        name, isPositiveVal, isPositiveSpecVal = data
        kpiRes = R.strings.tank_setup.kpi
        kpiValTitle = kpiRes.value.title
        kpiSpecValTitle = kpiRes.specValue.title
        valueSignKey = kpiRes.positive.capital if isPositiveVal else kpiRes.negative.capital
        specValueSignKey = kpiRes.positive if isPositiveSpecVal else kpiRes.negative
        value = kpiValTitle.dyn(name)
        specValue = kpiSpecValTitle.dyn(name)
        if not (value and specValue and valueSignKey and specValueSignKey):
            _logger.warning('getParamTitle some resources missing')
            return ''
        return backport.text(R.strings.tank_setup.kpi.bonus.combined(), valueSign=backport.text(valueSignKey()), value=backport.text(value()), specValueSign=backport.text(specValueSignKey()), specValue=backport.text(specValue()))