from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(100140)
    _bootcampLesson2 = DynAccessor(100141)
    _bootcampLesson3_1 = DynAccessor(100142)
    _bootcampLesson3_2 = DynAccessor(100143)
    _bootcampLesson4 = DynAccessor(100144)
    _bootcampOutro = DynAccessor(100145)
    _tutorialInitial = DynAccessor(100146)
    _tutorialInitialLoop = DynAccessor(100147)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(100148)
        up_particles = DynAccessor(100149)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(100150)
            crewCommander = DynAccessor(100151)
            crewDriver = DynAccessor(100152)
            crewGunner = DynAccessor(100153)
            crewLoader = DynAccessor(100154)
            crewRadioOperator = DynAccessor(100155)
            skillAdrenalineRush = DynAccessor(100156)
            skillArmorer = DynAccessor(100157)
            skillArtLamp = DynAccessor(100158)
            skillBrothersInArms = DynAccessor(100159)
            skillCallForVengeance = DynAccessor(100160)
            skillClutchBraking = DynAccessor(100161)
            skillCommanderBonus = DynAccessor(100162)
            skillConcealment = DynAccessor(100163)
            skillControlledImpact = DynAccessor(100164)
            skillDeadEye = DynAccessor(100165)
            skillDesignatedTarget = DynAccessor(100166)
            skillEagleEye = DynAccessor(100167)
            skillExpert = DynAccessor(100168)
            skillFirefighting = DynAccessor(100169)
            skillIntuition = DynAccessor(100170)
            skillJackOfAllTrades = DynAccessor(100171)
            skillMentor = DynAccessor(100172)
            skillOffRoadDriving = DynAccessor(100173)
            skillPreventativeMaintenance = DynAccessor(100174)
            skillRelaying = DynAccessor(100175)
            skillRepairs = DynAccessor(100176)
            skillSafeStowage = DynAccessor(100177)
            skillSignalBoosting = DynAccessor(100178)
            skillSituationalAwareness = DynAccessor(100179)
            skillSixthSense = DynAccessor(100180)
            skillSmoothRide = DynAccessor(100181)
            skillSnapShot = DynAccessor(100182)
            skillSniper = DynAccessor(100183)
            skillSoundIntelligence = DynAccessor(100184)
            statConcealment = DynAccessor(100185)
            statFirepower = DynAccessor(100186)
            statMobility = DynAccessor(100187)
            statSpotting = DynAccessor(100188)
            statSurvivability = DynAccessor(100189)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(100190)
        ay_gun = DynAccessor(100191)
        ay_tracks = DynAccessor(100192)
        ay_turret = DynAccessor(100193)
        video_reward = DynAccessor(100194)
        video_reward_min = DynAccessor(100195)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(100196)
        c_201292_3 = DynAccessor(100197)
        c_201292_4 = DynAccessor(100198)
        c_201548_2 = DynAccessor(100199)
        c_201548_3 = DynAccessor(100200)
        c_201548_4 = DynAccessor(100201)
        c_202316_2 = DynAccessor(100202)
        c_202316_3 = DynAccessor(100203)
        c_202316_4 = DynAccessor(100204)
        v_151_0 = DynAccessor(100205)
        v_152_0 = DynAccessor(100206)
        v_153_0 = DynAccessor(100207)
        v_171_0 = DynAccessor(100208)
        v_172_0 = DynAccessor(100209)
        v_173_0 = DynAccessor(100210)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(100211)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(100212)
            overcharge = DynAccessor(100213)
            power_shot = DynAccessor(100214)
            rapid_shelling = DynAccessor(100215)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(100216)
            Loop_1 = DynAccessor(100217)
            Loop_10 = DynAccessor(100218)
            Loop_2 = DynAccessor(100219)
            Loop_3 = DynAccessor(100220)
            Loop_4 = DynAccessor(100221)
            Loop_5 = DynAccessor(100222)
            Loop_6 = DynAccessor(100223)
            Loop_7 = DynAccessor(100224)
            Loop_8 = DynAccessor(100225)
            Loop_9 = DynAccessor(100226)

        progression = _progression()

        class _reward_vehicle(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(100227)
            G171_E77 = DynAccessor(100228)
            G171_E77_02 = DynAccessor(100229)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(100230)

        reward_vehicle = _reward_vehicle()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(100231)
        example_2 = DynAccessor(100232)
        example_3 = DynAccessor(100233)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(100234)
            gold = DynAccessor(100235)
            silver = DynAccessor(100236)
            standart = DynAccessor(100237)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(100238)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(100239)
            standart = DynAccessor(100240)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(100241)
            silver = DynAccessor(100242)
            standart = DynAccessor(100243)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(100244)
            standart = DynAccessor(100245)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(100246)
            mtl_1_35 = DynAccessor(100247)
            mt_drops = DynAccessor(100248)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(100249)
            medium = DynAccessor(100250)
            small = DynAccessor(100251)
            tanks_6 = DynAccessor(100252)
            tanks_7 = DynAccessor(100253)
            tanks_8 = DynAccessor(100254)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(100255)
        operation_10 = DynAccessor(100256)
        operation_8 = DynAccessor(100257)
        operation_9 = DynAccessor(100258)
        video_operations_person = DynAccessor(100259)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(100260)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(100261)

    vehicle = _vehicle()

    class _VehicleLootBoxCongrats(DynAccessor):
        __slots__ = ()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(100262)
            G164_Kpz_Pr_68_P = DynAccessor(100263)
            Pl35_CS_57_Sokol = DynAccessor(100264)

        mtl_universal = _mtl_universal()

    VehicleLootBoxCongrats = _VehicleLootBoxCongrats()