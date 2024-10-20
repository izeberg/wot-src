import typing
from wg_async import wg_async, wg_await
from helpers import dependency
from skeletons.gui.platform.wgnp_controllers import IWGNPDemoAccRequestController
if typing.TYPE_CHECKING:
    from typing import Callable
    from gui.platform.wgnp.demo_account.request import ValidateNicknameParams

class ValidationRequestWrapper(object):
    __slots__ = ('_isDisposed', )
    _wgnpDemoAccCtrl = dependency.descriptor(IWGNPDemoAccRequestController)
    _instances = list()

    def __init__(self):
        super(ValidationRequestWrapper, self).__init__()
        self._isDisposed = False

    @wg_async
    def process(self, name, callback):
        self._isDisposed = False
        response = yield wg_await(self._wgnpDemoAccCtrl.validateNickname(name))
        if not self._isDisposed:
            callback(response)
        ValidationRequestWrapper.utilize(self)

    def dispose(self):
        self._isDisposed = True

    @staticmethod
    def create():
        if ValidationRequestWrapper._instances:
            return ValidationRequestWrapper._instances.pop()
        return ValidationRequestWrapper()

    @staticmethod
    def utilize(wrapper):
        if wrapper not in ValidationRequestWrapper._instances:
            ValidationRequestWrapper._instances.append(wrapper)