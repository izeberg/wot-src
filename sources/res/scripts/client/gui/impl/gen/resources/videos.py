from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(96514)
    _bootcampLesson2 = DynAccessor(96515)
    _bootcampLesson3_1 = DynAccessor(96516)
    _bootcampLesson3_2 = DynAccessor(96517)
    _bootcampLesson4 = DynAccessor(96518)
    _bootcampOutro = DynAccessor(96519)
    _tutorialInitial = DynAccessor(96520)
    _tutorialInitialLoop = DynAccessor(96521)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(96522)
        up_particles = DynAccessor(96523)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(96524)
            crewCommander = DynAccessor(96525)
            crewDriver = DynAccessor(96526)
            crewGunner = DynAccessor(96527)
            crewLoader = DynAccessor(96528)
            crewRadioOperator = DynAccessor(96529)
            skillAdrenalineRush = DynAccessor(96530)
            skillArmorer = DynAccessor(96531)
            skillArtLamp = DynAccessor(96532)
            skillBrothersInArms = DynAccessor(96533)
            skillCallForVengeance = DynAccessor(96534)
            skillClutchBraking = DynAccessor(96535)
            skillCommanderBonus = DynAccessor(96536)
            skillConcealment = DynAccessor(96537)
            skillControlledImpact = DynAccessor(96538)
            skillDeadEye = DynAccessor(96539)
            skillDesignatedTarget = DynAccessor(96540)
            skillEagleEye = DynAccessor(96541)
            skillExpert = DynAccessor(96542)
            skillFirefighting = DynAccessor(96543)
            skillIntuition = DynAccessor(96544)
            skillJackOfAllTrades = DynAccessor(96545)
            skillMentor = DynAccessor(96546)
            skillOffRoadDriving = DynAccessor(96547)
            skillPreventativeMaintenance = DynAccessor(96548)
            skillRelaying = DynAccessor(96549)
            skillRepairs = DynAccessor(96550)
            skillSafeStowage = DynAccessor(96551)
            skillSignalBoosting = DynAccessor(96552)
            skillSituationalAwareness = DynAccessor(96553)
            skillSixthSense = DynAccessor(96554)
            skillSmoothRide = DynAccessor(96555)
            skillSnapShot = DynAccessor(96556)
            skillSniper = DynAccessor(96557)
            skillSoundIntelligence = DynAccessor(96558)
            statConcealment = DynAccessor(96559)
            statFirepower = DynAccessor(96560)
            statMobility = DynAccessor(96561)
            statSpotting = DynAccessor(96562)
            statSurvivability = DynAccessor(96563)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(96564)
        ay_gun = DynAccessor(96565)
        ay_tracks = DynAccessor(96566)
        ay_turret = DynAccessor(96567)
        video_reward = DynAccessor(96568)
        video_reward_min = DynAccessor(96569)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(96570)
        c_201292_3 = DynAccessor(96571)
        c_201292_4 = DynAccessor(96572)
        c_201548_2 = DynAccessor(96573)
        c_201548_3 = DynAccessor(96574)
        c_201548_4 = DynAccessor(96575)
        c_202316_2 = DynAccessor(96576)
        c_202316_3 = DynAccessor(96577)
        c_202316_4 = DynAccessor(96578)
        v_151_0 = DynAccessor(96579)
        v_152_0 = DynAccessor(96580)
        v_153_0 = DynAccessor(96581)

    battle_pass = _battle_pass()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(96582)
        example_2 = DynAccessor(96583)
        example_3 = DynAccessor(96584)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(96585)
            gold = DynAccessor(96586)
            silver = DynAccessor(96587)
            standart = DynAccessor(96588)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(96589)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(96590)
            standart = DynAccessor(96591)

        cosmic2024 = _cosmic2024()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(96592)
            standart = DynAccessor(96593)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(96594)
            mt_drops = DynAccessor(96595)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(96596)
            medium = DynAccessor(96597)
            small = DynAccessor(96598)
            tanks_6 = DynAccessor(96599)
            tanks_7 = DynAccessor(96600)
            tanks_8 = DynAccessor(96601)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(96602)
        intro_video_min = DynAccessor(96603)
        operation_10 = DynAccessor(96604)
        operation_8 = DynAccessor(96605)
        operation_9 = DynAccessor(96606)
        video_operations_person = DynAccessor(96607)
        video_reward = DynAccessor(96608)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(96609)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(96610)

    vehicle = _vehicle()