from gui.shared.system_factory import registerQuestBuilder
from tank_academy.gui.server_events.event_items import TankAcademyGroupQuestBuilder, TankAcademyTokenQuestBuilder, TankAcademyQuestBuilder

def registerTankAcademyQuests():
    registerQuestBuilder(TankAcademyQuestBuilder, index=0)
    registerQuestBuilder(TankAcademyTokenQuestBuilder, index=0)
    registerQuestBuilder(TankAcademyGroupQuestBuilder, index=0)