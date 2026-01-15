from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(106059)
    _tutorialInitialLoop = DynAccessor(106060)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(106061)
        up_particles = DynAccessor(106062)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(106063)
            crewCommander = DynAccessor(106064)
            crewDriver = DynAccessor(106065)
            crewGunner = DynAccessor(106066)
            crewLoader = DynAccessor(106067)
            crewRadioOperator = DynAccessor(106068)
            skillAdrenalineRush = DynAccessor(106069)
            skillArmorer = DynAccessor(106070)
            skillArtLamp = DynAccessor(106071)
            skillBrothersInArms = DynAccessor(106072)
            skillCallForVengeance = DynAccessor(106073)
            skillClutchBraking = DynAccessor(106074)
            skillCommanderBonus = DynAccessor(106075)
            skillConcealment = DynAccessor(106076)
            skillControlledImpact = DynAccessor(106077)
            skillDeadEye = DynAccessor(106078)
            skillDesignatedTarget = DynAccessor(106079)
            skillEagleEye = DynAccessor(106080)
            skillExpert = DynAccessor(106081)
            skillFirefighting = DynAccessor(106082)
            skillIntuition = DynAccessor(106083)
            skillJackOfAllTrades = DynAccessor(106084)
            skillMentor = DynAccessor(106085)
            skillOffRoadDriving = DynAccessor(106086)
            skillPreventativeMaintenance = DynAccessor(106087)
            skillRelaying = DynAccessor(106088)
            skillRepairs = DynAccessor(106089)
            skillSafeStowage = DynAccessor(106090)
            skillSignalBoosting = DynAccessor(106091)
            skillSituationalAwareness = DynAccessor(106092)
            skillSixthSense = DynAccessor(106093)
            skillSmoothRide = DynAccessor(106094)
            skillSnapShot = DynAccessor(106095)
            skillSniper = DynAccessor(106096)
            skillSoundIntelligence = DynAccessor(106097)
            statConcealment = DynAccessor(106098)
            statFirepower = DynAccessor(106099)
            statMobility = DynAccessor(106100)
            statSpotting = DynAccessor(106101)
            statSurvivability = DynAccessor(106102)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(106103)
        ay_gun = DynAccessor(106104)
        ay_tracks = DynAccessor(106105)
        ay_turret = DynAccessor(106106)
        video_reward = DynAccessor(106107)
        video_reward_min = DynAccessor(106108)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(106109)
        FueltankCrit = DynAccessor(106110)
        InSafetyWhileNotObserved = DynAccessor(106111)
        KilledWhileObserved = DynAccessor(106112)
        ModuleDamage = DynAccessor(106113)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_185_0 = DynAccessor(106114)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(106115)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(106116)
            overcharge = DynAccessor(106117)
            power_shot = DynAccessor(106118)
            rapid_shelling = DynAccessor(106119)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(106120)
            Loop_1 = DynAccessor(106121)
            Loop_10 = DynAccessor(106122)
            Loop_2 = DynAccessor(106123)
            Loop_3 = DynAccessor(106124)
            Loop_4 = DynAccessor(106125)
            Loop_5 = DynAccessor(106126)
            Loop_6 = DynAccessor(106127)
            Loop_7 = DynAccessor(106128)
            Loop_8 = DynAccessor(106129)
            Loop_9 = DynAccessor(106130)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(106131)
        example_2 = DynAccessor(106132)
        example_3 = DynAccessor(106133)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(106134)
            gold = DynAccessor(106135)
            silver = DynAccessor(106136)
            standart = DynAccessor(106137)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(106138)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(106139)
            small = DynAccessor(106140)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(106141)
            standart = DynAccessor(106142)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(106143)
            standart = DynAccessor(106144)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(106145)
            standart = DynAccessor(106146)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(106147)
            mtl_1_35 = DynAccessor(106148)
            mt_drops = DynAccessor(106149)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(106150)
            medium = DynAccessor(106151)
            small = DynAccessor(106152)
            tanks_6 = DynAccessor(106153)
            tanks_7 = DynAccessor(106154)
            tanks_8 = DynAccessor(106155)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(106156)
            G171_E77 = DynAccessor(106157)
            G171_E77_02 = DynAccessor(106158)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(106159)
            intro = DynAccessor(106160)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(106161)
            Pl35_CS_57_Sokol = DynAccessor(106162)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(106163)
        operation_10 = DynAccessor(106164)
        operation_8 = DynAccessor(106165)
        operation_9 = DynAccessor(106166)
        operation_99 = DynAccessor(106167)
        video_operations_person = DynAccessor(106168)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(106169)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(106170)

    vehicle = _vehicle()