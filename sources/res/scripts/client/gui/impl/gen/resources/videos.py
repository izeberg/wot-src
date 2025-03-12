from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(98216)
    _bootcampLesson2 = DynAccessor(98217)
    _bootcampLesson3_1 = DynAccessor(98218)
    _bootcampLesson3_2 = DynAccessor(98219)
    _bootcampLesson4 = DynAccessor(98220)
    _bootcampOutro = DynAccessor(98221)
    _tutorialInitial = DynAccessor(98222)
    _tutorialInitialLoop = DynAccessor(98223)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(98224)
        up_particles = DynAccessor(98225)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(98226)
            crewCommander = DynAccessor(98227)
            crewDriver = DynAccessor(98228)
            crewGunner = DynAccessor(98229)
            crewLoader = DynAccessor(98230)
            crewRadioOperator = DynAccessor(98231)
            skillAdrenalineRush = DynAccessor(98232)
            skillArmorer = DynAccessor(98233)
            skillArtLamp = DynAccessor(98234)
            skillBrothersInArms = DynAccessor(98235)
            skillCallForVengeance = DynAccessor(98236)
            skillClutchBraking = DynAccessor(98237)
            skillCommanderBonus = DynAccessor(98238)
            skillConcealment = DynAccessor(98239)
            skillControlledImpact = DynAccessor(98240)
            skillDeadEye = DynAccessor(98241)
            skillDesignatedTarget = DynAccessor(98242)
            skillEagleEye = DynAccessor(98243)
            skillExpert = DynAccessor(98244)
            skillFirefighting = DynAccessor(98245)
            skillIntuition = DynAccessor(98246)
            skillJackOfAllTrades = DynAccessor(98247)
            skillMentor = DynAccessor(98248)
            skillOffRoadDriving = DynAccessor(98249)
            skillPreventativeMaintenance = DynAccessor(98250)
            skillRelaying = DynAccessor(98251)
            skillRepairs = DynAccessor(98252)
            skillSafeStowage = DynAccessor(98253)
            skillSignalBoosting = DynAccessor(98254)
            skillSituationalAwareness = DynAccessor(98255)
            skillSixthSense = DynAccessor(98256)
            skillSmoothRide = DynAccessor(98257)
            skillSnapShot = DynAccessor(98258)
            skillSniper = DynAccessor(98259)
            skillSoundIntelligence = DynAccessor(98260)
            statConcealment = DynAccessor(98261)
            statFirepower = DynAccessor(98262)
            statMobility = DynAccessor(98263)
            statSpotting = DynAccessor(98264)
            statSurvivability = DynAccessor(98265)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(98266)
        ay_gun = DynAccessor(98267)
        ay_tracks = DynAccessor(98268)
        ay_turret = DynAccessor(98269)
        video_reward = DynAccessor(98270)
        video_reward_min = DynAccessor(98271)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(98272)
        c_201292_3 = DynAccessor(98273)
        c_201292_4 = DynAccessor(98274)
        c_201548_2 = DynAccessor(98275)
        c_201548_3 = DynAccessor(98276)
        c_201548_4 = DynAccessor(98277)
        c_202316_2 = DynAccessor(98278)
        c_202316_3 = DynAccessor(98279)
        c_202316_4 = DynAccessor(98280)
        v_151_0 = DynAccessor(98281)
        v_152_0 = DynAccessor(98282)
        v_153_0 = DynAccessor(98283)
        v_161_0 = DynAccessor(98284)
        v_162_0 = DynAccessor(98285)
        v_163_0 = DynAccessor(98286)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(98287)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(98288)
            overcharge = DynAccessor(98289)
            power_shot = DynAccessor(98290)
            rapid_shelling = DynAccessor(98291)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(98292)
            Loop_1 = DynAccessor(98293)
            Loop_10 = DynAccessor(98294)
            Loop_2 = DynAccessor(98295)
            Loop_3 = DynAccessor(98296)
            Loop_4 = DynAccessor(98297)
            Loop_5 = DynAccessor(98298)
            Loop_6 = DynAccessor(98299)
            Loop_7 = DynAccessor(98300)
            Loop_8 = DynAccessor(98301)
            Loop_9 = DynAccessor(98302)

        progression = _progression()

        class _reward_vehicle(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(98303)
            G171_E77 = DynAccessor(98304)
            G171_E77_02 = DynAccessor(98305)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(98306)

        reward_vehicle = _reward_vehicle()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(98307)
        example_2 = DynAccessor(98308)
        example_3 = DynAccessor(98309)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(98310)
            gold = DynAccessor(98311)
            silver = DynAccessor(98312)
            standart = DynAccessor(98313)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(98314)

        bd2024 = _bd2024()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(98315)
            standart = DynAccessor(98316)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(98317)
            silver = DynAccessor(98318)
            standart = DynAccessor(98319)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(98320)
            standart = DynAccessor(98321)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(98322)
            mt_drops = DynAccessor(98323)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(98324)
            medium = DynAccessor(98325)
            small = DynAccessor(98326)
            tanks_6 = DynAccessor(98327)
            tanks_7 = DynAccessor(98328)
            tanks_8 = DynAccessor(98329)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(98330)
        operation_10 = DynAccessor(98331)
        operation_8 = DynAccessor(98332)
        operation_9 = DynAccessor(98333)
        video_operations_person = DynAccessor(98334)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(98335)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(98336)

    vehicle = _vehicle()