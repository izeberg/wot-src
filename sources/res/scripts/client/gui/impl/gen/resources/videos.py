from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _bootcampLesson1 = DynAccessor(101518)
    _bootcampLesson2 = DynAccessor(101519)
    _bootcampLesson3_1 = DynAccessor(101520)
    _bootcampLesson3_2 = DynAccessor(101521)
    _bootcampLesson4 = DynAccessor(101522)
    _bootcampOutro = DynAccessor(101523)
    _tutorialInitial = DynAccessor(101524)
    _tutorialInitialLoop = DynAccessor(101525)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(101526)
        up_particles = DynAccessor(101527)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(101528)
            crewCommander = DynAccessor(101529)
            crewDriver = DynAccessor(101530)
            crewGunner = DynAccessor(101531)
            crewLoader = DynAccessor(101532)
            crewRadioOperator = DynAccessor(101533)
            skillAdrenalineRush = DynAccessor(101534)
            skillArmorer = DynAccessor(101535)
            skillArtLamp = DynAccessor(101536)
            skillBrothersInArms = DynAccessor(101537)
            skillCallForVengeance = DynAccessor(101538)
            skillClutchBraking = DynAccessor(101539)
            skillCommanderBonus = DynAccessor(101540)
            skillConcealment = DynAccessor(101541)
            skillControlledImpact = DynAccessor(101542)
            skillDeadEye = DynAccessor(101543)
            skillDesignatedTarget = DynAccessor(101544)
            skillEagleEye = DynAccessor(101545)
            skillExpert = DynAccessor(101546)
            skillFirefighting = DynAccessor(101547)
            skillIntuition = DynAccessor(101548)
            skillJackOfAllTrades = DynAccessor(101549)
            skillMentor = DynAccessor(101550)
            skillOffRoadDriving = DynAccessor(101551)
            skillPreventativeMaintenance = DynAccessor(101552)
            skillRelaying = DynAccessor(101553)
            skillRepairs = DynAccessor(101554)
            skillSafeStowage = DynAccessor(101555)
            skillSignalBoosting = DynAccessor(101556)
            skillSituationalAwareness = DynAccessor(101557)
            skillSixthSense = DynAccessor(101558)
            skillSmoothRide = DynAccessor(101559)
            skillSnapShot = DynAccessor(101560)
            skillSniper = DynAccessor(101561)
            skillSoundIntelligence = DynAccessor(101562)
            statConcealment = DynAccessor(101563)
            statFirepower = DynAccessor(101564)
            statMobility = DynAccessor(101565)
            statSpotting = DynAccessor(101566)
            statSurvivability = DynAccessor(101567)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(101568)
        ay_gun = DynAccessor(101569)
        ay_tracks = DynAccessor(101570)
        ay_turret = DynAccessor(101571)
        video_reward = DynAccessor(101572)
        video_reward_min = DynAccessor(101573)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        c_201292_2 = DynAccessor(101574)
        c_201292_3 = DynAccessor(101575)
        c_201292_4 = DynAccessor(101576)
        c_201548_2 = DynAccessor(101577)
        c_201548_3 = DynAccessor(101578)
        c_201548_4 = DynAccessor(101579)
        c_202316_2 = DynAccessor(101580)
        c_202316_3 = DynAccessor(101581)
        c_202316_4 = DynAccessor(101582)
        v_151_0 = DynAccessor(101583)
        v_152_0 = DynAccessor(101584)
        v_153_0 = DynAccessor(101585)
        v_171_0 = DynAccessor(101586)
        v_172_0 = DynAccessor(101587)
        v_173_0 = DynAccessor(101588)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(101589)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(101590)
            overcharge = DynAccessor(101591)
            power_shot = DynAccessor(101592)
            rapid_shelling = DynAccessor(101593)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(101594)
            Loop_1 = DynAccessor(101595)
            Loop_10 = DynAccessor(101596)
            Loop_2 = DynAccessor(101597)
            Loop_3 = DynAccessor(101598)
            Loop_4 = DynAccessor(101599)
            Loop_5 = DynAccessor(101600)
            Loop_6 = DynAccessor(101601)
            Loop_7 = DynAccessor(101602)
            Loop_8 = DynAccessor(101603)
            Loop_9 = DynAccessor(101604)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(101605)
        example_2 = DynAccessor(101606)
        example_3 = DynAccessor(101607)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(101608)
            gold = DynAccessor(101609)
            silver = DynAccessor(101610)
            standart = DynAccessor(101611)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(101612)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(101613)
            small = DynAccessor(101614)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(101615)
            standart = DynAccessor(101616)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(101617)
            standart = DynAccessor(101618)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(101619)
            standart = DynAccessor(101620)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(101621)
            mtl_1_35 = DynAccessor(101622)
            mt_drops = DynAccessor(101623)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(101624)
            medium = DynAccessor(101625)
            small = DynAccessor(101626)
            tanks_6 = DynAccessor(101627)
            tanks_7 = DynAccessor(101628)
            tanks_8 = DynAccessor(101629)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(101630)
            G171_E77 = DynAccessor(101631)
            G171_E77_02 = DynAccessor(101632)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(101633)
            intro = DynAccessor(101634)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(101635)
            Pl35_CS_57_Sokol = DynAccessor(101636)

        mtl_universal = _mtl_universal()

        class _tanks_birthday_2025(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(101637)
            A124_T54E2 = DynAccessor(101638)
            A149_AMBT = DynAccessor(101639)
            Ch43_WZ_122_2 = DynAccessor(101640)
            F130_AMX_Tracteur_D = DynAccessor(101641)
            G168_KJpz_T_III = DynAccessor(101642)
            GB110_FV4201_Chieftain_Prototype = DynAccessor(101643)
            GB112_Caliban = DynAccessor(101644)
            intro = DynAccessor(101645)
            It18_Progetto_C45_mod_71 = DynAccessor(101646)
            Pl19_CS_52_LIS = DynAccessor(101647)
            R188_Object_259A = DynAccessor(101648)
            R227_Object_407_MZ = DynAccessor(101649)

        tanks_birthday_2025 = _tanks_birthday_2025()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(101650)
        operation_10 = DynAccessor(101651)
        operation_8 = DynAccessor(101652)
        operation_9 = DynAccessor(101653)
        video_operations_person = DynAccessor(101654)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(101655)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(101656)

    vehicle = _vehicle()