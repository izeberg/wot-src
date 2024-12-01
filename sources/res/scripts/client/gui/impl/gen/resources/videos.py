from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(93749)
    _bootcampLesson2 = DynAccessor(93750)
    _bootcampLesson3_1 = DynAccessor(93751)
    _bootcampLesson3_2 = DynAccessor(93752)
    _bootcampLesson4 = DynAccessor(93753)
    _bootcampOutro = DynAccessor(93754)
    _tutorialInitial = DynAccessor(93755)
    _tutorialInitialLoop = DynAccessor(93756)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(93757)
        up_particles = DynAccessor(93758)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(93759)
            crewCommander = DynAccessor(93760)
            crewDriver = DynAccessor(93761)
            crewGunner = DynAccessor(93762)
            crewLoader = DynAccessor(93763)
            crewRadioOperator = DynAccessor(93764)
            skillAdrenalineRush = DynAccessor(93765)
            skillArmorer = DynAccessor(93766)
            skillArtLamp = DynAccessor(93767)
            skillBrothersInArms = DynAccessor(93768)
            skillCallForVengeance = DynAccessor(93769)
            skillClutchBraking = DynAccessor(93770)
            skillCommanderBonus = DynAccessor(93771)
            skillConcealment = DynAccessor(93772)
            skillControlledImpact = DynAccessor(93773)
            skillDeadEye = DynAccessor(93774)
            skillDesignatedTarget = DynAccessor(93775)
            skillEagleEye = DynAccessor(93776)
            skillExpert = DynAccessor(93777)
            skillFirefighting = DynAccessor(93778)
            skillIntuition = DynAccessor(93779)
            skillJackOfAllTrades = DynAccessor(93780)
            skillMentor = DynAccessor(93781)
            skillOffRoadDriving = DynAccessor(93782)
            skillPreventativeMaintenance = DynAccessor(93783)
            skillRelaying = DynAccessor(93784)
            skillRepairs = DynAccessor(93785)
            skillSafeStowage = DynAccessor(93786)
            skillSignalBoosting = DynAccessor(93787)
            skillSituationalAwareness = DynAccessor(93788)
            skillSixthSense = DynAccessor(93789)
            skillSmoothRide = DynAccessor(93790)
            skillSnapShot = DynAccessor(93791)
            skillSniper = DynAccessor(93792)
            skillSoundIntelligence = DynAccessor(93793)
            statConcealment = DynAccessor(93794)
            statFirepower = DynAccessor(93795)
            statMobility = DynAccessor(93796)
            statSpotting = DynAccessor(93797)
            statSurvivability = DynAccessor(93798)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(93799)
        ay_gun = DynAccessor(93800)
        ay_tracks = DynAccessor(93801)
        ay_turret = DynAccessor(93802)
        video_reward = DynAccessor(93803)
        video_reward_min = DynAccessor(93804)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(93805)
        c_201292_3 = DynAccessor(93806)
        c_201292_4 = DynAccessor(93807)
        c_201548_2 = DynAccessor(93808)
        c_201548_3 = DynAccessor(93809)
        c_201548_4 = DynAccessor(93810)
        c_202316_2 = DynAccessor(93811)
        c_202316_3 = DynAccessor(93812)
        c_202316_4 = DynAccessor(93813)
        v_151_0 = DynAccessor(93814)
        v_152_0 = DynAccessor(93815)
        v_153_0 = DynAccessor(93816)

    battle_pass = _battle_pass()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(93817)
        example_2 = DynAccessor(93818)
        example_3 = DynAccessor(93819)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(93820)
            gold = DynAccessor(93821)
            silver = DynAccessor(93822)
            standart = DynAccessor(93823)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(93824)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(93825)
            standart = DynAccessor(93826)

        cosmic2024 = _cosmic2024()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(93827)
            standart = DynAccessor(93828)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(93829)
            mt_drops = DynAccessor(93830)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(93831)
            magic = DynAccessor(93832)
            standart = DynAccessor(93833)
            ussr = DynAccessor(93834)
            xmas = DynAccessor(93835)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(93836)
            ny_2025_small = DynAccessor(93837)
            ny_2025_tanks = DynAccessor(93838)

        ny2025 = _ny2025()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(93839)
            medium = DynAccessor(93840)
            small = DynAccessor(93841)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _new_year(DynAccessor):
        __slots__ = ()
        ng_greetings = DynAccessor(93842)
        ng_startup = DynAccessor(93843)
        onboarding_complete = DynAccessor(93844)

        class _quests(DynAccessor):
            __slots__ = ()
            quest_giver_daily_1 = DynAccessor(93845)
            quest_giver_daily_2 = DynAccessor(93846)
            quest_giver_daily_3 = DynAccessor(93847)
            quest_giver_daily_4 = DynAccessor(93848)
            quest_giver_daily_5 = DynAccessor(93849)
            quest_giver_daily_6 = DynAccessor(93850)
            quest_giver_first_entry = DynAccessor(93851)
            quest_giver_idle = DynAccessor(93852)
            quest_giver_weekly_1 = DynAccessor(93853)
            quest_giver_weekly_2 = DynAccessor(93854)
            quest_giver_weekly_3 = DynAccessor(93855)
            quest_giver_weekly_4 = DynAccessor(93856)
            quest_giver_weekly_5 = DynAccessor(93857)
            quest_giver_weekly_6 = DynAccessor(93858)

        quests = _quests()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(93859)
            tv_screen_idle = DynAccessor(93860)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(93861)

    platoon = _platoon()

    class _VehicleLootBoxCongrats(DynAccessor):
        __slots__ = ()
        A127_TL_1_LPC = DynAccessor(93862)
        customizations_113740 = DynAccessor(93863)
        customizations_22348 = DynAccessor(93864)
        customizations_31308 = DynAccessor(93865)
        customizations_75084 = DynAccessor(93866)
        customizations_93772 = DynAccessor(93867)
        F126_Char_Lourd_AP58 = DynAccessor(93868)
        F69_AMX13_57_100 = DynAccessor(93869)
        G162_Project_Kpz_07P_E = DynAccessor(93870)
        G36_PzII_J = DynAccessor(93871)
        G44_JagdTigerH = DynAccessor(93872)
        G48_E_25 = DynAccessor(93873)
        intro = DynAccessor(93874)
        It21_Lion = DynAccessor(93875)
        J36_Type_63_HT = DynAccessor(93876)
        ny_2025_tanks = DynAccessor(93877)
        R115_IS_3_auto_S = DynAccessor(93878)
        R173_K_91_2_122 = DynAccessor(93879)
        R178_Object_780 = DynAccessor(93880)
        R200_KV_4_Turchaninov = DynAccessor(93881)
        R219_Waffentrager_E100_Gold = DynAccessor(93882)
        R50_SU76I = DynAccessor(93883)

    VehicleLootBoxCongrats = _VehicleLootBoxCongrats()