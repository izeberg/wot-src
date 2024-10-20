from frameworks.wulf import ViewModel

class TooltipConstants(ViewModel):
    __slots__ = ()
    SKILL = 'crewPerkGf'
    SKILL_ALT = 'crewPerkAltGf'
    COMMANDER_BONUS = 'commanderBonus'
    ACHIEVEMENT = 'achievement'
    SKIN = 'crewSkin'
    DIRECTIVE = 'directive'
    TANKMAN = 'tankman'
    TANKMAN_NOT_RECRUITED = 'tankmanNotRecruited'
    SKILLS_EFFICIENCY = 'skillsEfficiency'
    CREW_SKILL_UNTRAINED = 'crewSkillUntrained'
    VEHICLE_PREVIEW_CREW_MEMBER = 'vehiclePreviewCrewMember'
    VEHICLE_CREW_MEMBER_IN_HANGAR = 'vehicleCrewMemberInHangar'
    UNIQUE_VOICEOVER_WITCHES = 'witches'

    def __init__(self, properties=0, commands=0):
        super(TooltipConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TooltipConstants, self)._initialize()