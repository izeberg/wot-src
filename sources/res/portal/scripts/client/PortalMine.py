from BasicMine import BasicMine

class PortalMine(BasicMine):

    def onLeaveWorld(self):
        if self.gameObject is not None:
            self.gameObject.detonate()
        super(PortalMine, self).onLeaveWorld()
        return