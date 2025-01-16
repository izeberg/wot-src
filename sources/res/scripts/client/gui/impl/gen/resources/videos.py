from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(96491)
    _bootcampLesson2 = DynAccessor(96492)
    _bootcampLesson3_1 = DynAccessor(96493)
    _bootcampLesson3_2 = DynAccessor(96494)
    _bootcampLesson4 = DynAccessor(96495)
    _bootcampOutro = DynAccessor(96496)
    _tutorialInitial = DynAccessor(96497)
    _tutorialInitialLoop = DynAccessor(96498)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(96499)
        up_particles = DynAccessor(96500)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(96501)
            crewCommander = DynAccessor(96502)
            crewDriver = DynAccessor(96503)
            crewGunner = DynAccessor(96504)
            crewLoader = DynAccessor(96505)
            crewRadioOperator = DynAccessor(96506)
            skillAdrenalineRush = DynAccessor(96507)
            skillArmorer = DynAccessor(96508)
            skillArtLamp = DynAccessor(96509)
            skillBrothersInArms = DynAccessor(96510)
            skillCallForVengeance = DynAccessor(96511)
            skillClutchBraking = DynAccessor(96512)
            skillCommanderBonus = DynAccessor(96513)
            skillConcealment = DynAccessor(96514)
            skillControlledImpact = DynAccessor(96515)
            skillDeadEye = DynAccessor(96516)
            skillDesignatedTarget = DynAccessor(96517)
            skillEagleEye = DynAccessor(96518)
            skillExpert = DynAccessor(96519)
            skillFirefighting = DynAccessor(96520)
            skillIntuition = DynAccessor(96521)
            skillJackOfAllTrades = DynAccessor(96522)
            skillMentor = DynAccessor(96523)
            skillOffRoadDriving = DynAccessor(96524)
            skillPreventativeMaintenance = DynAccessor(96525)
            skillRelaying = DynAccessor(96526)
            skillRepairs = DynAccessor(96527)
            skillSafeStowage = DynAccessor(96528)
            skillSignalBoosting = DynAccessor(96529)
            skillSituationalAwareness = DynAccessor(96530)
            skillSixthSense = DynAccessor(96531)
            skillSmoothRide = DynAccessor(96532)
            skillSnapShot = DynAccessor(96533)
            skillSniper = DynAccessor(96534)
            skillSoundIntelligence = DynAccessor(96535)
            statConcealment = DynAccessor(96536)
            statFirepower = DynAccessor(96537)
            statMobility = DynAccessor(96538)
            statSpotting = DynAccessor(96539)
            statSurvivability = DynAccessor(96540)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(96541)
        ay_gun = DynAccessor(96542)
        ay_tracks = DynAccessor(96543)
        ay_turret = DynAccessor(96544)
        video_reward = DynAccessor(96545)
        video_reward_min = DynAccessor(96546)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(96547)
        c_201292_3 = DynAccessor(96548)
        c_201292_4 = DynAccessor(96549)
        c_201548_2 = DynAccessor(96550)
        c_201548_3 = DynAccessor(96551)
        c_201548_4 = DynAccessor(96552)
        c_202316_2 = DynAccessor(96553)
        c_202316_3 = DynAccessor(96554)
        c_202316_4 = DynAccessor(96555)
        v_151_0 = DynAccessor(96556)
        v_152_0 = DynAccessor(96557)
        v_153_0 = DynAccessor(96558)

    battle_pass = _battle_pass()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(96559)
        example_2 = DynAccessor(96560)
        example_3 = DynAccessor(96561)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(96562)
            gold = DynAccessor(96563)
            silver = DynAccessor(96564)
            standart = DynAccessor(96565)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(96566)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(96567)
            standart = DynAccessor(96568)

        cosmic2024 = _cosmic2024()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(96569)
            standart = DynAccessor(96570)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(96571)
            mt_drops = DynAccessor(96572)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(96573)
            medium = DynAccessor(96574)
            small = DynAccessor(96575)
            tanks_6 = DynAccessor(96576)
            tanks_7 = DynAccessor(96577)
            tanks_8 = DynAccessor(96578)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(96579)
        intro_video_min = DynAccessor(96580)
        operation_10 = DynAccessor(96581)
        operation_8 = DynAccessor(96582)
        operation_9 = DynAccessor(96583)
        video_operations_person = DynAccessor(96584)
        video_reward = DynAccessor(96585)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(96586)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(96587)

    vehicle = _vehicle()