from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(102159)
    _bootcampLesson2 = DynAccessor(102160)
    _bootcampLesson3_1 = DynAccessor(102161)
    _bootcampLesson3_2 = DynAccessor(102162)
    _bootcampLesson4 = DynAccessor(102163)
    _bootcampOutro = DynAccessor(102164)
    _tutorialInitial = DynAccessor(102165)
    _tutorialInitialLoop = DynAccessor(102166)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(102167)
        up_particles = DynAccessor(102168)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(102169)
            crewCommander = DynAccessor(102170)
            crewDriver = DynAccessor(102171)
            crewGunner = DynAccessor(102172)
            crewLoader = DynAccessor(102173)
            crewRadioOperator = DynAccessor(102174)
            skillAdrenalineRush = DynAccessor(102175)
            skillArmorer = DynAccessor(102176)
            skillArtLamp = DynAccessor(102177)
            skillBrothersInArms = DynAccessor(102178)
            skillCallForVengeance = DynAccessor(102179)
            skillClutchBraking = DynAccessor(102180)
            skillCommanderBonus = DynAccessor(102181)
            skillConcealment = DynAccessor(102182)
            skillControlledImpact = DynAccessor(102183)
            skillDeadEye = DynAccessor(102184)
            skillDesignatedTarget = DynAccessor(102185)
            skillEagleEye = DynAccessor(102186)
            skillExpert = DynAccessor(102187)
            skillFirefighting = DynAccessor(102188)
            skillIntuition = DynAccessor(102189)
            skillJackOfAllTrades = DynAccessor(102190)
            skillMentor = DynAccessor(102191)
            skillOffRoadDriving = DynAccessor(102192)
            skillPreventativeMaintenance = DynAccessor(102193)
            skillRelaying = DynAccessor(102194)
            skillRepairs = DynAccessor(102195)
            skillSafeStowage = DynAccessor(102196)
            skillSignalBoosting = DynAccessor(102197)
            skillSituationalAwareness = DynAccessor(102198)
            skillSixthSense = DynAccessor(102199)
            skillSmoothRide = DynAccessor(102200)
            skillSnapShot = DynAccessor(102201)
            skillSniper = DynAccessor(102202)
            skillSoundIntelligence = DynAccessor(102203)
            statConcealment = DynAccessor(102204)
            statFirepower = DynAccessor(102205)
            statMobility = DynAccessor(102206)
            statSpotting = DynAccessor(102207)
            statSurvivability = DynAccessor(102208)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(102209)
        ay_gun = DynAccessor(102210)
        ay_tracks = DynAccessor(102211)
        ay_turret = DynAccessor(102212)
        video_reward = DynAccessor(102213)
        video_reward_min = DynAccessor(102214)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(102215)
        c_201292_3 = DynAccessor(102216)
        c_201292_4 = DynAccessor(102217)
        c_201548_2 = DynAccessor(102218)
        c_201548_3 = DynAccessor(102219)
        c_201548_4 = DynAccessor(102220)
        c_202316_2 = DynAccessor(102221)
        c_202316_3 = DynAccessor(102222)
        c_202316_4 = DynAccessor(102223)
        v_151_0 = DynAccessor(102224)
        v_152_0 = DynAccessor(102225)
        v_153_0 = DynAccessor(102226)
        v_161_0 = DynAccessor(102227)
        v_162_0 = DynAccessor(102228)
        v_163_0 = DynAccessor(102229)
        v_165_0 = DynAccessor(102230)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(102231)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(102232)
            overcharge = DynAccessor(102233)
            power_shot = DynAccessor(102234)
            rapid_shelling = DynAccessor(102235)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(102236)
            Loop_1 = DynAccessor(102237)
            Loop_10 = DynAccessor(102238)
            Loop_2 = DynAccessor(102239)
            Loop_3 = DynAccessor(102240)
            Loop_4 = DynAccessor(102241)
            Loop_5 = DynAccessor(102242)
            Loop_6 = DynAccessor(102243)
            Loop_7 = DynAccessor(102244)
            Loop_8 = DynAccessor(102245)
            Loop_9 = DynAccessor(102246)

        progression = _progression()

        class _reward_vehicle(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(102247)
            G171_E77 = DynAccessor(102248)
            G171_E77_02 = DynAccessor(102249)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(102250)

        reward_vehicle = _reward_vehicle()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(102251)
        example_2 = DynAccessor(102252)
        example_3 = DynAccessor(102253)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(102254)
            gold = DynAccessor(102255)
            silver = DynAccessor(102256)
            standart = DynAccessor(102257)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(102258)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(102259)
            standart = DynAccessor(102260)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(102261)
            silver = DynAccessor(102262)
            standart = DynAccessor(102263)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(102264)
            standart = DynAccessor(102265)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(102266)
            mt_drops = DynAccessor(102267)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(102268)
            medium = DynAccessor(102269)
            small = DynAccessor(102270)
            tanks_6 = DynAccessor(102271)
            tanks_7 = DynAccessor(102272)
            tanks_8 = DynAccessor(102273)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _historicalBattles(DynAccessor):
        __slots__ = ()
        godrays = DynAccessor(102274)
        v_mainTake_loop = DynAccessor(102275)
        v_mainTake_start = DynAccessor(102276)

        class _progression_videos(DynAccessor):
            __slots__ = ()
            progression_defence_1 = DynAccessor(102277)
            progression_defence_2 = DynAccessor(102278)
            progression_defence_3 = DynAccessor(102279)
            progression_offence_1 = DynAccessor(102280)
            progression_offence_2 = DynAccessor(102281)
            progression_offence_3 = DynAccessor(102282)

        progression_videos = _progression_videos()

    historicalBattles = _historicalBattles()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(102283)
        operation_10 = DynAccessor(102284)
        operation_8 = DynAccessor(102285)
        operation_9 = DynAccessor(102286)
        video_operations_person = DynAccessor(102287)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(102288)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(102289)

    vehicle = _vehicle()