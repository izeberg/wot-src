from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IEarlyAccessController

class EarlyAccessViewImpl(ViewImpl):
    __earlyAccessCtrl = dependency.descriptor(IEarlyAccessController)

    def _initialize(self):
        super(EarlyAccessViewImpl, self)._initialize()
        self.__earlyAccessCtrl.hangarFeatureState.enter(self.layoutID)

    def _finalize(self):
        self.__earlyAccessCtrl.hangarFeatureState.exit(self.layoutID)
        super(EarlyAccessViewImpl, self)._finalize()