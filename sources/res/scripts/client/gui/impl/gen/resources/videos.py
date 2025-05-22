from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(100117)
    _bootcampLesson2 = DynAccessor(100118)
    _bootcampLesson3_1 = DynAccessor(100119)
    _bootcampLesson3_2 = DynAccessor(100120)
    _bootcampLesson4 = DynAccessor(100121)
    _bootcampOutro = DynAccessor(100122)
    _tutorialInitial = DynAccessor(100123)
    _tutorialInitialLoop = DynAccessor(100124)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(100125)
        up_particles = DynAccessor(100126)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(100127)
            crewCommander = DynAccessor(100128)
            crewDriver = DynAccessor(100129)
            crewGunner = DynAccessor(100130)
            crewLoader = DynAccessor(100131)
            crewRadioOperator = DynAccessor(100132)
            skillAdrenalineRush = DynAccessor(100133)
            skillArmorer = DynAccessor(100134)
            skillArtLamp = DynAccessor(100135)
            skillBrothersInArms = DynAccessor(100136)
            skillCallForVengeance = DynAccessor(100137)
            skillClutchBraking = DynAccessor(100138)
            skillCommanderBonus = DynAccessor(100139)
            skillConcealment = DynAccessor(100140)
            skillControlledImpact = DynAccessor(100141)
            skillDeadEye = DynAccessor(100142)
            skillDesignatedTarget = DynAccessor(100143)
            skillEagleEye = DynAccessor(100144)
            skillExpert = DynAccessor(100145)
            skillFirefighting = DynAccessor(100146)
            skillIntuition = DynAccessor(100147)
            skillJackOfAllTrades = DynAccessor(100148)
            skillMentor = DynAccessor(100149)
            skillOffRoadDriving = DynAccessor(100150)
            skillPreventativeMaintenance = DynAccessor(100151)
            skillRelaying = DynAccessor(100152)
            skillRepairs = DynAccessor(100153)
            skillSafeStowage = DynAccessor(100154)
            skillSignalBoosting = DynAccessor(100155)
            skillSituationalAwareness = DynAccessor(100156)
            skillSixthSense = DynAccessor(100157)
            skillSmoothRide = DynAccessor(100158)
            skillSnapShot = DynAccessor(100159)
            skillSniper = DynAccessor(100160)
            skillSoundIntelligence = DynAccessor(100161)
            statConcealment = DynAccessor(100162)
            statFirepower = DynAccessor(100163)
            statMobility = DynAccessor(100164)
            statSpotting = DynAccessor(100165)
            statSurvivability = DynAccessor(100166)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(100167)
        ay_gun = DynAccessor(100168)
        ay_tracks = DynAccessor(100169)
        ay_turret = DynAccessor(100170)
        video_reward = DynAccessor(100171)
        video_reward_min = DynAccessor(100172)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(100173)
        c_201292_3 = DynAccessor(100174)
        c_201292_4 = DynAccessor(100175)
        c_201548_2 = DynAccessor(100176)
        c_201548_3 = DynAccessor(100177)
        c_201548_4 = DynAccessor(100178)
        c_202316_2 = DynAccessor(100179)
        c_202316_3 = DynAccessor(100180)
        c_202316_4 = DynAccessor(100181)
        v_151_0 = DynAccessor(100182)
        v_152_0 = DynAccessor(100183)
        v_153_0 = DynAccessor(100184)
        v_171_0 = DynAccessor(100185)
        v_172_0 = DynAccessor(100186)
        v_173_0 = DynAccessor(100187)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(100188)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(100189)
            overcharge = DynAccessor(100190)
            power_shot = DynAccessor(100191)
            rapid_shelling = DynAccessor(100192)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(100193)
            Loop_1 = DynAccessor(100194)
            Loop_10 = DynAccessor(100195)
            Loop_2 = DynAccessor(100196)
            Loop_3 = DynAccessor(100197)
            Loop_4 = DynAccessor(100198)
            Loop_5 = DynAccessor(100199)
            Loop_6 = DynAccessor(100200)
            Loop_7 = DynAccessor(100201)
            Loop_8 = DynAccessor(100202)
            Loop_9 = DynAccessor(100203)

        progression = _progression()

        class _reward_vehicle(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(100204)
            G171_E77 = DynAccessor(100205)
            G171_E77_02 = DynAccessor(100206)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(100207)

        reward_vehicle = _reward_vehicle()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(100208)
        example_2 = DynAccessor(100209)
        example_3 = DynAccessor(100210)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(100211)
            gold = DynAccessor(100212)
            silver = DynAccessor(100213)
            standart = DynAccessor(100214)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(100215)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(100216)
            standart = DynAccessor(100217)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(100218)
            silver = DynAccessor(100219)
            standart = DynAccessor(100220)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(100221)
            standart = DynAccessor(100222)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(100223)
            mtl_1_35 = DynAccessor(100224)
            mt_drops = DynAccessor(100225)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(100226)
            medium = DynAccessor(100227)
            small = DynAccessor(100228)
            tanks_6 = DynAccessor(100229)
            tanks_7 = DynAccessor(100230)
            tanks_8 = DynAccessor(100231)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(100232)
        operation_10 = DynAccessor(100233)
        operation_8 = DynAccessor(100234)
        operation_9 = DynAccessor(100235)
        video_operations_person = DynAccessor(100236)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(100237)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(100238)

    vehicle = _vehicle()

    class _VehicleLootBoxCongrats(DynAccessor):
        __slots__ = ()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(100239)
            G164_Kpz_Pr_68_P = DynAccessor(100240)
            Pl35_CS_57_Sokol = DynAccessor(100241)

        mtl_universal = _mtl_universal()

    VehicleLootBoxCongrats = _VehicleLootBoxCongrats()