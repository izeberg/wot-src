from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(101521)
    _bootcampLesson2 = DynAccessor(101522)
    _bootcampLesson3_1 = DynAccessor(101523)
    _bootcampLesson3_2 = DynAccessor(101524)
    _bootcampLesson4 = DynAccessor(101525)
    _bootcampOutro = DynAccessor(101526)
    _tutorialInitial = DynAccessor(101527)
    _tutorialInitialLoop = DynAccessor(101528)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(101529)
        up_particles = DynAccessor(101530)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(101531)
            crewCommander = DynAccessor(101532)
            crewDriver = DynAccessor(101533)
            crewGunner = DynAccessor(101534)
            crewLoader = DynAccessor(101535)
            crewRadioOperator = DynAccessor(101536)
            skillAdrenalineRush = DynAccessor(101537)
            skillArmorer = DynAccessor(101538)
            skillArtLamp = DynAccessor(101539)
            skillBrothersInArms = DynAccessor(101540)
            skillCallForVengeance = DynAccessor(101541)
            skillClutchBraking = DynAccessor(101542)
            skillCommanderBonus = DynAccessor(101543)
            skillConcealment = DynAccessor(101544)
            skillControlledImpact = DynAccessor(101545)
            skillDeadEye = DynAccessor(101546)
            skillDesignatedTarget = DynAccessor(101547)
            skillEagleEye = DynAccessor(101548)
            skillExpert = DynAccessor(101549)
            skillFirefighting = DynAccessor(101550)
            skillIntuition = DynAccessor(101551)
            skillJackOfAllTrades = DynAccessor(101552)
            skillMentor = DynAccessor(101553)
            skillOffRoadDriving = DynAccessor(101554)
            skillPreventativeMaintenance = DynAccessor(101555)
            skillRelaying = DynAccessor(101556)
            skillRepairs = DynAccessor(101557)
            skillSafeStowage = DynAccessor(101558)
            skillSignalBoosting = DynAccessor(101559)
            skillSituationalAwareness = DynAccessor(101560)
            skillSixthSense = DynAccessor(101561)
            skillSmoothRide = DynAccessor(101562)
            skillSnapShot = DynAccessor(101563)
            skillSniper = DynAccessor(101564)
            skillSoundIntelligence = DynAccessor(101565)
            statConcealment = DynAccessor(101566)
            statFirepower = DynAccessor(101567)
            statMobility = DynAccessor(101568)
            statSpotting = DynAccessor(101569)
            statSurvivability = DynAccessor(101570)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(101571)
        ay_gun = DynAccessor(101572)
        ay_tracks = DynAccessor(101573)
        ay_turret = DynAccessor(101574)
        video_reward = DynAccessor(101575)
        video_reward_min = DynAccessor(101576)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(101577)
        c_201292_3 = DynAccessor(101578)
        c_201292_4 = DynAccessor(101579)
        c_201548_2 = DynAccessor(101580)
        c_201548_3 = DynAccessor(101581)
        c_201548_4 = DynAccessor(101582)
        c_202316_2 = DynAccessor(101583)
        c_202316_3 = DynAccessor(101584)
        c_202316_4 = DynAccessor(101585)
        v_151_0 = DynAccessor(101586)
        v_152_0 = DynAccessor(101587)
        v_153_0 = DynAccessor(101588)
        v_171_0 = DynAccessor(101589)
        v_172_0 = DynAccessor(101590)
        v_173_0 = DynAccessor(101591)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(101592)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(101593)
            overcharge = DynAccessor(101594)
            power_shot = DynAccessor(101595)
            rapid_shelling = DynAccessor(101596)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(101597)
            Loop_1 = DynAccessor(101598)
            Loop_10 = DynAccessor(101599)
            Loop_2 = DynAccessor(101600)
            Loop_3 = DynAccessor(101601)
            Loop_4 = DynAccessor(101602)
            Loop_5 = DynAccessor(101603)
            Loop_6 = DynAccessor(101604)
            Loop_7 = DynAccessor(101605)
            Loop_8 = DynAccessor(101606)
            Loop_9 = DynAccessor(101607)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(101608)
        example_2 = DynAccessor(101609)
        example_3 = DynAccessor(101610)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(101611)
            gold = DynAccessor(101612)
            silver = DynAccessor(101613)
            standart = DynAccessor(101614)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(101615)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(101616)
            small = DynAccessor(101617)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(101618)
            standart = DynAccessor(101619)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(101620)
            standart = DynAccessor(101621)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(101622)
            standart = DynAccessor(101623)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(101624)
            mtl_1_35 = DynAccessor(101625)
            mt_drops = DynAccessor(101626)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(101627)
            medium = DynAccessor(101628)
            small = DynAccessor(101629)
            tanks_6 = DynAccessor(101630)
            tanks_7 = DynAccessor(101631)
            tanks_8 = DynAccessor(101632)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(101633)
            G171_E77 = DynAccessor(101634)
            G171_E77_02 = DynAccessor(101635)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(101636)
            intro = DynAccessor(101637)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(101638)
            Pl35_CS_57_Sokol = DynAccessor(101639)

        mtl_universal = _mtl_universal()

        class _tanks_birthday_2025(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(101640)
            A124_T54E2 = DynAccessor(101641)
            A149_AMBT = DynAccessor(101642)
            Ch43_WZ_122_2 = DynAccessor(101643)
            F130_AMX_Tracteur_D = DynAccessor(101644)
            G168_KJpz_T_III = DynAccessor(101645)
            GB110_FV4201_Chieftain_Prototype = DynAccessor(101646)
            GB112_Caliban = DynAccessor(101647)
            intro = DynAccessor(101648)
            It18_Progetto_C45_mod_71 = DynAccessor(101649)
            Pl19_CS_52_LIS = DynAccessor(101650)
            R188_Object_259A = DynAccessor(101651)
            R227_Object_407_MZ = DynAccessor(101652)

        tanks_birthday_2025 = _tanks_birthday_2025()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(101653)
        operation_10 = DynAccessor(101654)
        operation_8 = DynAccessor(101655)
        operation_9 = DynAccessor(101656)
        video_operations_person = DynAccessor(101657)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(101658)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(101659)

    vehicle = _vehicle()