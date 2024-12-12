from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(99035)
        grade_change_particles = DynAccessor(99036)
        particles = DynAccessor(99037)
        up_particles = DynAccessor(99038)

    achievements = _achievements()

    class _advent_calendar(DynAccessor):
        __slots__ = ()
        shine = DynAccessor(99039)

    advent_calendar = _advent_calendar()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(99040)
            crewCommander = DynAccessor(99041)
            crewDriver = DynAccessor(99042)
            crewGunner = DynAccessor(99043)
            crewLoader = DynAccessor(99044)
            crewRadioOperator = DynAccessor(99045)
            skillAdrenalineRush = DynAccessor(99046)
            skillAmbushMaster = DynAccessor(99047)
            skillBrothersInArms = DynAccessor(99048)
            skillCallForVengeance = DynAccessor(99049)
            skillClutchBraking = DynAccessor(99050)
            skillCommanderBonus = DynAccessor(99051)
            skillCommanderCoordination = DynAccessor(99052)
            skillCommanderEmergency = DynAccessor(99053)
            skillCommanderEnemyShotPredictor = DynAccessor(99054)
            skillCommanderPractical = DynAccessor(99055)
            skillCommanderTutor = DynAccessor(99056)
            skillConcealment = DynAccessor(99057)
            skillDesignatedTarget = DynAccessor(99058)
            skillDriverMotorExpert = DynAccessor(99059)
            skillDriverRammingMaster = DynAccessor(99060)
            skillDriverReliablePlacement = DynAccessor(99061)
            skillEagleEye = DynAccessor(99062)
            skillEfficiency = DynAccessor(99063)
            skillFirefighting = DynAccessor(99064)
            skillGunnerArmorer = DynAccessor(99065)
            skillGunnerFocus = DynAccessor(99066)
            skillGunnerQuickAiming = DynAccessor(99067)
            skillIntuition = DynAccessor(99068)
            skillJackOfAllTrades = DynAccessor(99069)
            skillLoaderAmmunitionImprove = DynAccessor(99070)
            skillLoaderMelee = DynAccessor(99071)
            skillLoaderPerfectCharge = DynAccessor(99072)
            skillOffRoadDriving = DynAccessor(99073)
            skillPreventativeMaintenance = DynAccessor(99074)
            skillRadiomanExpert = DynAccessor(99075)
            skillRadiomanInterference = DynAccessor(99076)
            skillRadiomanSideBySide = DynAccessor(99077)
            skillRadiomanSignalInterception = DynAccessor(99078)
            skillRepairs = DynAccessor(99079)
            skillSafeStowage = DynAccessor(99080)
            skillSituationalAwareness = DynAccessor(99081)
            skillSixthSense = DynAccessor(99082)
            skillSmoothRide = DynAccessor(99083)
            skillSnapShot = DynAccessor(99084)
            skillSniper = DynAccessor(99085)
            skillUntrainedPenalty = DynAccessor(99086)
            statConcealment = DynAccessor(99087)
            statFirepower = DynAccessor(99088)
            statMobility = DynAccessor(99089)
            statSpotting = DynAccessor(99090)
            statSurvivability = DynAccessor(99091)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(99092)
        style_ch1_lvl3 = DynAccessor(99093)
        style_ch1_lvl4 = DynAccessor(99094)
        style_ch2_lvl2 = DynAccessor(99095)
        style_ch2_lvl3 = DynAccessor(99096)
        style_ch2_lvl4 = DynAccessor(99097)
        style_ch3_lvl2 = DynAccessor(99098)
        style_ch3_lvl3 = DynAccessor(99099)
        style_ch3_lvl4 = DynAccessor(99100)

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(99101)
        clouds_1366 = DynAccessor(99102)
        clouds_1600 = DynAccessor(99103)
        clouds_1920 = DynAccessor(99104)
        clouds_2560 = DynAccessor(99105)
        spark_white = DynAccessor(99106)
        spark_yellow = DynAccessor(99107)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(99108)
        godRaysNew_130x130 = DynAccessor(99109)
        godRaysNew_1600x1600 = DynAccessor(99110)
        rankAnimation_first = DynAccessor(99111)
        rankAnimation_second = DynAccessor(99112)
        rankAnimation_third = DynAccessor(99113)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(99114)
            veteran_frame_big = DynAccessor(99115)
            veteran_frame_small = DynAccessor(99116)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(99117)
        example_2 = DynAccessor(99118)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(99119)
        vehicle_sparks_2 = DynAccessor(99120)
        vehicle_sparks_3 = DynAccessor(99121)

    dogtags = _dogtags()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        lootbox_prem = DynAccessor(99122)

    event_loot_boxes = _event_loot_boxes()

    class _grinch_progression(DynAccessor):
        __slots__ = ()
        GMPIntro = DynAccessor(99123)

    grinch_progression = _grinch_progression()

    class _lootbox(DynAccessor):
        __slots__ = ()

        class _customizable(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        bronze_common = DynAccessor(99124)
                        bronze_rare = DynAccessor(99125)
                        gold_common = DynAccessor(99126)
                        gold_rare = DynAccessor(99127)
                        silver_common = DynAccessor(99128)
                        silver_rare = DynAccessor(99129)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(99130)
                        epic_small = DynAccessor(99131)
                        rare = DynAccessor(99132)
                        rare_small = DynAccessor(99133)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(99134)

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(99135)
                            gold = DynAccessor(99136)
                            silver = DynAccessor(99137)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(99138)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(99139)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(99140)
                        rare = DynAccessor(99141)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(99142)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(99143)
                        epic_small = DynAccessor(99144)
                        rare = DynAccessor(99145)
                        rare_small = DynAccessor(99146)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(99147)
                    box = DynAccessor(99148)
                    hover = DynAccessor(99149)
                    idle = DynAccessor(99150)

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(99151)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(99152)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(99153)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(99154)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(99155)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(99156)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

        events = _events()

    lootbox = _lootbox()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _GuestRewardCongrats(DynAccessor):
            __slots__ = ()
            guestC = DynAccessor(99157)

        GuestRewardCongrats = _GuestRewardCongrats()

        class _StyleLootBoxCongrats(DynAccessor):
            __slots__ = ()
            A125_AEP_1 = DynAccessor(99158)
            A88_M53_55 = DynAccessor(99159)
            Cz02_TVP_T50 = DynAccessor(99160)
            Cz17_Vz_55 = DynAccessor(99161)
            F108_Panhard_EBR_105 = DynAccessor(99162)
            G121_Grille_15_L63 = DynAccessor(99163)
            G55_E_75 = DynAccessor(99164)
            G61_G_E = DynAccessor(99165)
            GB32_Tortoise = DynAccessor(99166)
            GB86_Centurion_Action_X = DynAccessor(99167)

        StyleLootBoxCongrats = _StyleLootBoxCongrats()

        class _VehicleLootBoxCongrats(DynAccessor):
            __slots__ = ()
            A168_XM_57 = DynAccessor(99168)
            Ch61_DZT_159 = DynAccessor(99169)
            Cz33_Vz_68_Squall = DynAccessor(99170)
            GB139_FV226_Contradictious = DynAccessor(99171)
            It34_Toro = DynAccessor(99172)

        VehicleLootBoxCongrats = _VehicleLootBoxCongrats()

        class _gift_machine(DynAccessor):
            __slots__ = ()
            error = DynAccessor(99173)
            idle = DynAccessor(99174)
            idle_has_coins = DynAccessor(99175)
            particles = DynAccessor(99176)
            reward = DynAccessor(99177)
            second_particles = DynAccessor(99178)
            special_reward = DynAccessor(99179)

        gift_machine = _gift_machine()

        class _level(DynAccessor):
            __slots__ = ()
            rhombs = DynAccessor(99180)

        level = _level()

        class _sacks(DynAccessor):
            __slots__ = ()
            background_glow = DynAccessor(99181)

            class _idle(DynAccessor):
                __slots__ = ()
                particles_small = DynAccessor(99182)
                shine = DynAccessor(99183)

            idle = _idle()
            particle_blast = DynAccessor(99184)
            particles_open_blast_slash = DynAccessor(99185)
            upgraded_slashes = DynAccessor(99186)

        sacks = _sacks()

        class _snowfall(DynAccessor):
            __slots__ = ()
            snowfall = DynAccessor(99187)

        snowfall = _snowfall()

        class _usm(DynAccessor):
            __slots__ = ()

            class _lootboxes(DynAccessor):
                __slots__ = ()

                class _idles(DynAccessor):
                    __slots__ = ()
                    Christmas = DynAccessor(99188)
                    Fairytale = DynAccessor(99189)
                    NewYear = DynAccessor(99190)
                    Oriental = DynAccessor(99191)
                    premium_empty = DynAccessor(99192)

                idles = _idles()
                lootbox_delivery = DynAccessor(99193)
                lootbox_entry = DynAccessor(99194)

                class _opening(DynAccessor):
                    __slots__ = ()
                    Christmas = DynAccessor(99195)
                    Fairytale = DynAccessor(99196)
                    NewYear = DynAccessor(99197)
                    Oriental = DynAccessor(99198)

                    class _idles(DynAccessor):
                        __slots__ = ()
                        Christmas = DynAccessor(99199)
                        Fairytale = DynAccessor(99200)
                        NewYear = DynAccessor(99201)
                        Oriental = DynAccessor(99202)

                        class _guestC(DynAccessor):
                            __slots__ = ()
                            Christmas = DynAccessor(99203)
                            Fairytale = DynAccessor(99204)
                            NewYear = DynAccessor(99205)
                            Oriental = DynAccessor(99206)

                        guestC = _guestC()

                    idles = _idles()

                opening = _opening()

            lootboxes = _lootboxes()

        usm = _usm()

    new_year = _new_year()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(99207)

    platoon = _platoon()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(99208)
        cycle_legendary = DynAccessor(99209)
        intro_epic = DynAccessor(99210)
        intro_legendary = DynAccessor(99211)

    rarity = _rarity()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(99212)

    story_mode = _story_mode()