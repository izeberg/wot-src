import sys, os
from functools import partial, wraps
from types import GeneratorType
import platform, ResMgr, BigWorld
from bwdebug import TRACE_MSG

class _BuiltinsAccessor(object):

    def __init__(self, field_name):
        self._field_name = field_name
        self._original = None
        return

    @property
    def original(self):
        return self._original or self._get()

    def set(self, value):
        self._original = self._get()
        self._set(value)

    def get(self):
        return self._get()

    def _set(self, value):
        raise NotImplementedError

    def _get(self):
        raise NotImplementedError

    def revert(self):
        if self._original:
            self.set(self._original)
            self._original = None
        return


class _ItemAccessor(_BuiltinsAccessor):

    def _set(self, value):
        __builtins__[self._field_name] = value

    def _get(self):
        return __builtins__[self._field_name]


class _AttrAccessor(_BuiltinsAccessor):

    def _set(self, value):
        setattr(__builtins__, self._field_name, value)

    def _get(self):
        return getattr(__builtins__, self._field_name)


try:
    _ = __builtins__['open']
    _open_accessor = _ItemAccessor('open')
except TypeError:
    _open_accessor = _AttrAccessor('open')

class _BwFile(object):

    def __init__(self, path):
        self._content = ResMgr.openSection(path).asBinary.split('\n')

    def __enter__(self):
        return self._content

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return iter(self._content)


def bwResReplaceOpen(name, *args):
    return _BwFile(name)


@partial
def bwResRelativeOpen(name, *args):
    try:
        absname = ResMgr.resolveToAbsolutePath(name)
    except Exception as e:
        raise IOError(2, ('Error = {}; name = {}').format(str(e), name))

    absname = unicode(absname)
    return _open_accessor.original(absname, *args)


def monkeyPatchOpen(full_replace=False):
    TRACE_MSG('BWUtil.monkeyPatchOpen: Patching open()', full_replace)
    if full_replace:
        new_open = bwResReplaceOpen
    else:
        new_open = bwResRelativeOpen
    _open_accessor.set(new_open)


def revertPatchedOpen():
    TRACE_MSG('BWUtil.revertPatchedOpen: Reverting open()')
    _open_accessor.revert()


def extendPath(path, name):
    from pkgutil import extend_path
    path = extend_path(path, name)
    if not isinstance(path, list):
        return path
    pname = os.path.join(*name.split('.'))
    init_py = '__init__' + os.extsep + 'py'
    path = path[:]
    for dir in sys.path:
        if not isinstance(dir, basestring) or not ResMgr.isDir(dir):
            continue
        subdir = os.path.join(dir, pname)
        initfile = os.path.join(subdir, init_py)
        if subdir not in path and ResMgr.isFile(initfile):
            path.append(subdir)

    return path


def longDistroNameToShort(longDistroName):
    if longDistroName.startswith('Red Hat'):
        return 'rhel'
    if longDistroName.startswith('CentOS'):
        return 'CentOS'
    return longDistroName


SHORT_NAME_ENTERPRISE_LINUX = 'el'
ENTERPRISE_LINUX_DISTROS = [
 'centos', 'rhel']
ALLOWED_DISTROS = ENTERPRISE_LINUX_DISTROS + ['fedora']

def finaliseShortNameFromReleaseInfo(longDistroName, versionStr, releaseName):
    majorVerStr = versionStr
    if '.' in versionStr:
        majorVerStr = versionStr[0:versionStr.index('.')]
    versionNum = int(majorVerStr)
    shortDistroName = longDistroNameToShort(longDistroName).lower()
    if shortDistroName not in ALLOWED_DISTROS:
        sys.stderr.write("Distribution '%s' is not supported\n" % shortDistroName)
        return None
    else:
        if shortDistroName in ENTERPRISE_LINUX_DISTROS:
            shortDistroName = SHORT_NAME_ENTERPRISE_LINUX
        return '%s%d' % (shortDistroName, versionNum)


def findPlatformName():
    if platform.system() == 'Windows':
        return 'win64'
    else:
        try:
            platformData = platform.linux_distribution()
        except AttributeError:
            sys.stderr.write('Unable to detect linux distribution. An old version of Python may be present. BigWorld requires Python 2.7.\n')
            return

        return finaliseShortNameFromReleaseInfo(*platformData)
        return


def getPlatformArchitecutre():
    try:
        return platform.processor()
    except:
        sys.stderr.write('Unable to detect platform architecture')
        return

    return


def getPlatformSuffix():
    platformName = findPlatformName()
    if not platformName:
        return None
    else:
        platformArchitecture = getPlatformArchitecutre()
        if not platformArchitecture:
            return None
        platformSuffix = platformName
        if platformName == 'el9':
            platformSuffix += '/' + platformArchitecture
        return platformSuffix


class AsyncReturn(StopIteration):
    __slots__ = ('value', )

    def __init__(self, value):
        self.value = value


def async(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        promise = BigWorld.Promise()

        def stepGen(result):
            result.then(handleResult)

        def handle(func, *args):
            try:
                stepGen(func(*args))
            except AsyncReturn as r:
                promise.set_value(r.value)
            except StopIteration:
                promise.set_value(None)
            except BaseException:
                promise.set_exception(*sys.exc_info())

            return

        def handleResult(result):
            try:
                result = result.get()
            except BaseException:
                handle(gen.throw, *sys.exc_info())
            else:
                handle(gen.send, result)

        handle(gen.send, None)
        return promise.get_future()

    return wrapper


def if_only_component(*components):

    def _real_decorator(func):

        def _wrapper(*args, **kwargs):
            if BigWorld.component in components:
                func(*args, **kwargs)

        return _wrapper

    return _real_decorator


def if_only_not_component(*components):

    def _real_decorator(func):

        def _wrapper(*args, **kwargs):
            if BigWorld.component not in components:
                func(*args, **kwargs)

        return _wrapper

    return _real_decorator