from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(96483)
    _bootcampLesson2 = DynAccessor(96484)
    _bootcampLesson3_1 = DynAccessor(96485)
    _bootcampLesson3_2 = DynAccessor(96486)
    _bootcampLesson4 = DynAccessor(96487)
    _bootcampOutro = DynAccessor(96488)
    _tutorialInitial = DynAccessor(96489)
    _tutorialInitialLoop = DynAccessor(96490)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(96491)
        up_particles = DynAccessor(96492)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(96493)
            crewCommander = DynAccessor(96494)
            crewDriver = DynAccessor(96495)
            crewGunner = DynAccessor(96496)
            crewLoader = DynAccessor(96497)
            crewRadioOperator = DynAccessor(96498)
            skillAdrenalineRush = DynAccessor(96499)
            skillArmorer = DynAccessor(96500)
            skillArtLamp = DynAccessor(96501)
            skillBrothersInArms = DynAccessor(96502)
            skillCallForVengeance = DynAccessor(96503)
            skillClutchBraking = DynAccessor(96504)
            skillCommanderBonus = DynAccessor(96505)
            skillConcealment = DynAccessor(96506)
            skillControlledImpact = DynAccessor(96507)
            skillDeadEye = DynAccessor(96508)
            skillDesignatedTarget = DynAccessor(96509)
            skillEagleEye = DynAccessor(96510)
            skillExpert = DynAccessor(96511)
            skillFirefighting = DynAccessor(96512)
            skillIntuition = DynAccessor(96513)
            skillJackOfAllTrades = DynAccessor(96514)
            skillMentor = DynAccessor(96515)
            skillOffRoadDriving = DynAccessor(96516)
            skillPreventativeMaintenance = DynAccessor(96517)
            skillRelaying = DynAccessor(96518)
            skillRepairs = DynAccessor(96519)
            skillSafeStowage = DynAccessor(96520)
            skillSignalBoosting = DynAccessor(96521)
            skillSituationalAwareness = DynAccessor(96522)
            skillSixthSense = DynAccessor(96523)
            skillSmoothRide = DynAccessor(96524)
            skillSnapShot = DynAccessor(96525)
            skillSniper = DynAccessor(96526)
            skillSoundIntelligence = DynAccessor(96527)
            statConcealment = DynAccessor(96528)
            statFirepower = DynAccessor(96529)
            statMobility = DynAccessor(96530)
            statSpotting = DynAccessor(96531)
            statSurvivability = DynAccessor(96532)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(96533)
        ay_gun = DynAccessor(96534)
        ay_tracks = DynAccessor(96535)
        ay_turret = DynAccessor(96536)
        video_reward = DynAccessor(96537)
        video_reward_min = DynAccessor(96538)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(96539)
        c_201292_3 = DynAccessor(96540)
        c_201292_4 = DynAccessor(96541)
        c_201548_2 = DynAccessor(96542)
        c_201548_3 = DynAccessor(96543)
        c_201548_4 = DynAccessor(96544)
        c_202316_2 = DynAccessor(96545)
        c_202316_3 = DynAccessor(96546)
        c_202316_4 = DynAccessor(96547)
        v_151_0 = DynAccessor(96548)
        v_152_0 = DynAccessor(96549)
        v_153_0 = DynAccessor(96550)

    battle_pass = _battle_pass()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(96551)
        example_2 = DynAccessor(96552)
        example_3 = DynAccessor(96553)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(96554)
            gold = DynAccessor(96555)
            silver = DynAccessor(96556)
            standart = DynAccessor(96557)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(96558)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(96559)
            standart = DynAccessor(96560)

        cosmic2024 = _cosmic2024()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(96561)
            standart = DynAccessor(96562)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(96563)
            mt_drops = DynAccessor(96564)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(96565)
            medium = DynAccessor(96566)
            small = DynAccessor(96567)
            tanks_6 = DynAccessor(96568)
            tanks_7 = DynAccessor(96569)
            tanks_8 = DynAccessor(96570)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(96571)
        operation_10 = DynAccessor(96572)
        operation_8 = DynAccessor(96573)
        operation_9 = DynAccessor(96574)
        video_operations_person = DynAccessor(96575)
        video_reward = DynAccessor(96576)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(96577)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(96578)

    vehicle = _vehicle()