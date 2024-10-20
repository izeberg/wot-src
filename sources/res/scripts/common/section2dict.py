import typing
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
    TReaders = typing.Dict[(str, typing.Callable[([DataSection], dict)])]

def _parseDataSection(dataSection, readers=None):
    if not len(dataSection.values()):
        return _normalizeValue(dataSection.asString)
    result = {}
    for section in dataSection.values():
        if section.isAttribute:
            continue
        key = section.name
        if readers and key in readers:
            value = readers[key](section)
        else:
            value = _parseDataSection(section, readers)
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [
                 result[key], value]
        else:
            result[key] = value

    return result


def _normalizeValue(value):
    if value.isdigit():
        value = int(value)
    else:
        try:
            value = float(value)
        except ValueError:
            pass

    return value


def parse(data, readers=None):
    if not len(data.values()):
        return {}
    return _parseDataSection(data, readers)