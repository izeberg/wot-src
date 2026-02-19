from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(106043)
    _tutorialInitialLoop = DynAccessor(106044)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(106045)
        up_particles = DynAccessor(106046)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(106047)
            crewCommander = DynAccessor(106048)
            crewDriver = DynAccessor(106049)
            crewGunner = DynAccessor(106050)
            crewLoader = DynAccessor(106051)
            crewRadioOperator = DynAccessor(106052)
            skillAdrenalineRush = DynAccessor(106053)
            skillArmorer = DynAccessor(106054)
            skillArtLamp = DynAccessor(106055)
            skillBrothersInArms = DynAccessor(106056)
            skillCallForVengeance = DynAccessor(106057)
            skillClutchBraking = DynAccessor(106058)
            skillCommanderBonus = DynAccessor(106059)
            skillConcealment = DynAccessor(106060)
            skillControlledImpact = DynAccessor(106061)
            skillDeadEye = DynAccessor(106062)
            skillDesignatedTarget = DynAccessor(106063)
            skillEagleEye = DynAccessor(106064)
            skillExpert = DynAccessor(106065)
            skillFirefighting = DynAccessor(106066)
            skillIntuition = DynAccessor(106067)
            skillJackOfAllTrades = DynAccessor(106068)
            skillMentor = DynAccessor(106069)
            skillOffRoadDriving = DynAccessor(106070)
            skillPreventativeMaintenance = DynAccessor(106071)
            skillRelaying = DynAccessor(106072)
            skillRepairs = DynAccessor(106073)
            skillSafeStowage = DynAccessor(106074)
            skillSignalBoosting = DynAccessor(106075)
            skillSituationalAwareness = DynAccessor(106076)
            skillSixthSense = DynAccessor(106077)
            skillSmoothRide = DynAccessor(106078)
            skillSnapShot = DynAccessor(106079)
            skillSniper = DynAccessor(106080)
            skillSoundIntelligence = DynAccessor(106081)
            statConcealment = DynAccessor(106082)
            statFirepower = DynAccessor(106083)
            statMobility = DynAccessor(106084)
            statSpotting = DynAccessor(106085)
            statSurvivability = DynAccessor(106086)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(106087)
        ay_gun = DynAccessor(106088)
        ay_tracks = DynAccessor(106089)
        ay_turret = DynAccessor(106090)
        video_reward = DynAccessor(106091)
        video_reward_min = DynAccessor(106092)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmunitionCrit = DynAccessor(106093)
        FueltankCrit = DynAccessor(106094)
        InSafetyWhileNotObserved = DynAccessor(106095)
        KilledWhileObserved = DynAccessor(106096)
        ModuleDamage = DynAccessor(106097)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_185_0 = DynAccessor(106098)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(106099)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(106100)
            overcharge = DynAccessor(106101)
            power_shot = DynAccessor(106102)
            rapid_shelling = DynAccessor(106103)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(106104)
            Loop_1 = DynAccessor(106105)
            Loop_10 = DynAccessor(106106)
            Loop_2 = DynAccessor(106107)
            Loop_3 = DynAccessor(106108)
            Loop_4 = DynAccessor(106109)
            Loop_5 = DynAccessor(106110)
            Loop_6 = DynAccessor(106111)
            Loop_7 = DynAccessor(106112)
            Loop_8 = DynAccessor(106113)
            Loop_9 = DynAccessor(106114)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(106115)
        example_2 = DynAccessor(106116)
        example_3 = DynAccessor(106117)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(106118)
            gold = DynAccessor(106119)
            silver = DynAccessor(106120)
            standart = DynAccessor(106121)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(106122)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(106123)
            small = DynAccessor(106124)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(106125)
            standart = DynAccessor(106126)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(106127)
            standart = DynAccessor(106128)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(106129)
            standart = DynAccessor(106130)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(106131)
            mtl_1_35 = DynAccessor(106132)
            mt_drops = DynAccessor(106133)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(106134)
            medium = DynAccessor(106135)
            small = DynAccessor(106136)
            tanks_6 = DynAccessor(106137)
            tanks_7 = DynAccessor(106138)
            tanks_8 = DynAccessor(106139)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(106140)
            G171_E77 = DynAccessor(106141)
            G171_E77_02 = DynAccessor(106142)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(106143)
            intro = DynAccessor(106144)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(106145)
            Pl35_CS_57_Sokol = DynAccessor(106146)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(106147)
        operation_10 = DynAccessor(106148)
        operation_8 = DynAccessor(106149)
        operation_9 = DynAccessor(106150)
        operation_99 = DynAccessor(106151)
        video_operations_person = DynAccessor(106152)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(106153)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(106154)

    vehicle = _vehicle()