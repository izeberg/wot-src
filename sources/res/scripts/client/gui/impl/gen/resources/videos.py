from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(93779)
    _bootcampLesson2 = DynAccessor(93780)
    _bootcampLesson3_1 = DynAccessor(93781)
    _bootcampLesson3_2 = DynAccessor(93782)
    _bootcampLesson4 = DynAccessor(93783)
    _bootcampOutro = DynAccessor(93784)
    _tutorialInitial = DynAccessor(93785)
    _tutorialInitialLoop = DynAccessor(93786)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(93787)
        up_particles = DynAccessor(93788)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(93789)
            crewCommander = DynAccessor(93790)
            crewDriver = DynAccessor(93791)
            crewGunner = DynAccessor(93792)
            crewLoader = DynAccessor(93793)
            crewRadioOperator = DynAccessor(93794)
            skillAdrenalineRush = DynAccessor(93795)
            skillArmorer = DynAccessor(93796)
            skillArtLamp = DynAccessor(93797)
            skillBrothersInArms = DynAccessor(93798)
            skillCallForVengeance = DynAccessor(93799)
            skillClutchBraking = DynAccessor(93800)
            skillCommanderBonus = DynAccessor(93801)
            skillConcealment = DynAccessor(93802)
            skillControlledImpact = DynAccessor(93803)
            skillDeadEye = DynAccessor(93804)
            skillDesignatedTarget = DynAccessor(93805)
            skillEagleEye = DynAccessor(93806)
            skillExpert = DynAccessor(93807)
            skillFirefighting = DynAccessor(93808)
            skillIntuition = DynAccessor(93809)
            skillJackOfAllTrades = DynAccessor(93810)
            skillMentor = DynAccessor(93811)
            skillOffRoadDriving = DynAccessor(93812)
            skillPreventativeMaintenance = DynAccessor(93813)
            skillRelaying = DynAccessor(93814)
            skillRepairs = DynAccessor(93815)
            skillSafeStowage = DynAccessor(93816)
            skillSignalBoosting = DynAccessor(93817)
            skillSituationalAwareness = DynAccessor(93818)
            skillSixthSense = DynAccessor(93819)
            skillSmoothRide = DynAccessor(93820)
            skillSnapShot = DynAccessor(93821)
            skillSniper = DynAccessor(93822)
            skillSoundIntelligence = DynAccessor(93823)
            statConcealment = DynAccessor(93824)
            statFirepower = DynAccessor(93825)
            statMobility = DynAccessor(93826)
            statSpotting = DynAccessor(93827)
            statSurvivability = DynAccessor(93828)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(93829)
        ay_gun = DynAccessor(93830)
        ay_tracks = DynAccessor(93831)
        ay_turret = DynAccessor(93832)
        video_reward = DynAccessor(93833)
        video_reward_min = DynAccessor(93834)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(93835)
        c_201292_3 = DynAccessor(93836)
        c_201292_4 = DynAccessor(93837)
        c_201548_2 = DynAccessor(93838)
        c_201548_3 = DynAccessor(93839)
        c_201548_4 = DynAccessor(93840)
        c_202316_2 = DynAccessor(93841)
        c_202316_3 = DynAccessor(93842)
        c_202316_4 = DynAccessor(93843)
        v_151_0 = DynAccessor(93844)
        v_152_0 = DynAccessor(93845)
        v_153_0 = DynAccessor(93846)

    battle_pass = _battle_pass()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(93847)
        example_2 = DynAccessor(93848)
        example_3 = DynAccessor(93849)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(93850)
            gold = DynAccessor(93851)
            silver = DynAccessor(93852)
            standart = DynAccessor(93853)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(93854)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(93855)
            standart = DynAccessor(93856)

        cosmic2024 = _cosmic2024()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(93857)
            standart = DynAccessor(93858)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(93859)
            mt_drops = DynAccessor(93860)

        mt_lootbox = _mt_lootbox()

        class _ny2024(DynAccessor):
            __slots__ = ()
            china = DynAccessor(93861)
            magic = DynAccessor(93862)
            standart = DynAccessor(93863)
            ussr = DynAccessor(93864)
            xmas = DynAccessor(93865)

        ny2024 = _ny2024()

        class _ny2025(DynAccessor):
            __slots__ = ()
            ny_2025_big = DynAccessor(93866)
            ny_2025_small = DynAccessor(93867)
            ny_2025_tanks = DynAccessor(93868)

        ny2025 = _ny2025()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(93869)
            medium = DynAccessor(93870)
            small = DynAccessor(93871)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _new_year(DynAccessor):
        __slots__ = ()
        ng_greetings = DynAccessor(93872)
        ng_startup = DynAccessor(93873)
        onboarding_complete = DynAccessor(93874)

        class _quests(DynAccessor):
            __slots__ = ()
            quest_giver_daily_1 = DynAccessor(93875)
            quest_giver_daily_2 = DynAccessor(93876)
            quest_giver_daily_3 = DynAccessor(93877)
            quest_giver_daily_4 = DynAccessor(93878)
            quest_giver_daily_5 = DynAccessor(93879)
            quest_giver_daily_6 = DynAccessor(93880)
            quest_giver_first_entry = DynAccessor(93881)
            quest_giver_idle = DynAccessor(93882)
            quest_giver_weekly_1 = DynAccessor(93883)
            quest_giver_weekly_2 = DynAccessor(93884)
            quest_giver_weekly_3 = DynAccessor(93885)
            quest_giver_weekly_4 = DynAccessor(93886)
            quest_giver_weekly_5 = DynAccessor(93887)
            quest_giver_weekly_6 = DynAccessor(93888)

        quests = _quests()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(93889)
            tv_screen_idle = DynAccessor(93890)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(93891)

    platoon = _platoon()

    class _VehicleLootBoxCongrats(DynAccessor):
        __slots__ = ()
        A156_T54_2022 = DynAccessor(93892)
        A163_H_3 = DynAccessor(93893)
        A163_H_3_2 = DynAccessor(93894)
        Ch56_BZ_74_1 = DynAccessor(93895)
        customizations_7990860 = DynAccessor(93896)
        customizations_7999308 = DynAccessor(93897)
        customizations_7999564 = DynAccessor(93898)
        customizations_8001356 = DynAccessor(93899)
        customizations_8001612 = DynAccessor(93900)
        Cz14_Skoda_T_56 = DynAccessor(93901)
        Cz32_Vz_58_Koncept = DynAccessor(93902)
        F106_Panhard_EBR_75_Mle1954 = DynAccessor(93903)
        F116_Bat_Chatillon_Bourrasque = DynAccessor(93904)
        F129_Schneider_120_AC_Gendarme = DynAccessor(93905)
        F97_ELC_EVEN_90 = DynAccessor(93906)
        GB118_Taurus_CA = DynAccessor(93907)
        GB128_Nemesis = DynAccessor(93908)
        GB99_Turtle_Mk1 = DynAccessor(93909)
        intro = DynAccessor(93910)
        It13_Progetto_M35_mod_46 = DynAccessor(93911)
        It32_Prototipo_6 = DynAccessor(93912)
        ny_2025_tanks = DynAccessor(93913)
        R199_SU_122V = DynAccessor(93914)
        R203_Object_168N = DynAccessor(93915)
        S31_Strv_K = DynAccessor(93916)

    VehicleLootBoxCongrats = _VehicleLootBoxCongrats()