from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(94997)
        grade_change_particles = DynAccessor(94998)
        particles = DynAccessor(94999)
        up_particles = DynAccessor(95000)

    achievements = _achievements()

    class _advent_calendar(DynAccessor):
        __slots__ = ()
        shine = DynAccessor(95001)

    advent_calendar = _advent_calendar()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(95002)
            crewCommander = DynAccessor(95003)
            crewDriver = DynAccessor(95004)
            crewGunner = DynAccessor(95005)
            crewLoader = DynAccessor(95006)
            crewRadioOperator = DynAccessor(95007)
            mentoringLicense = DynAccessor(95008)
            skillAdrenalineRush = DynAccessor(95009)
            skillAmbushMaster = DynAccessor(95010)
            skillBrothersInArms = DynAccessor(95011)
            skillClutchBraking = DynAccessor(95012)
            skillCommanderBonus = DynAccessor(95013)
            skillCommanderCoordination = DynAccessor(95014)
            skillCommanderEmergency = DynAccessor(95015)
            skillCommanderEnemyShotPredictor = DynAccessor(95016)
            skillCommanderPractical = DynAccessor(95017)
            skillCommanderTutor = DynAccessor(95018)
            skillConcealment = DynAccessor(95019)
            skillDesignatedTarget = DynAccessor(95020)
            skillDriverMotorExpert = DynAccessor(95021)
            skillDriverRammingMaster = DynAccessor(95022)
            skillDriverReliablePlacement = DynAccessor(95023)
            skillEagleEye = DynAccessor(95024)
            skillEfficiency = DynAccessor(95025)
            skillFirefighting = DynAccessor(95026)
            skillGunnerArmorer = DynAccessor(95027)
            skillGunnerFocus = DynAccessor(95028)
            skillGunnerQuickAiming = DynAccessor(95029)
            skillIntuition = DynAccessor(95030)
            skillJackOfAllTrades = DynAccessor(95031)
            skillLoaderAmmunitionImprove = DynAccessor(95032)
            skillLoaderMelee = DynAccessor(95033)
            skillLoaderPerfectCharge = DynAccessor(95034)
            skillOffRoadDriving = DynAccessor(95035)
            skillPreventativeMaintenance = DynAccessor(95036)
            skillRadiomanExpert = DynAccessor(95037)
            skillRadiomanInterference = DynAccessor(95038)
            skillRadiomanSideBySide = DynAccessor(95039)
            skillRadiomanSignalInterception = DynAccessor(95040)
            skillRepairs = DynAccessor(95041)
            skillSafeStowage = DynAccessor(95042)
            skillSituationalAwareness = DynAccessor(95043)
            skillSixthSense = DynAccessor(95044)
            skillSmoothRide = DynAccessor(95045)
            skillSnapShot = DynAccessor(95046)
            skillSniper = DynAccessor(95047)
            skillUntrainedPenalty = DynAccessor(95048)
            statConcealment = DynAccessor(95049)
            statFirepower = DynAccessor(95050)
            statMobility = DynAccessor(95051)
            statSpotting = DynAccessor(95052)
            statSurvivability = DynAccessor(95053)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(95054)
        style_ch1_lvl3 = DynAccessor(95055)
        style_ch1_lvl4 = DynAccessor(95056)
        style_ch2_lvl2 = DynAccessor(95057)
        style_ch2_lvl3 = DynAccessor(95058)
        style_ch2_lvl4 = DynAccessor(95059)
        style_ch3_lvl2 = DynAccessor(95060)
        style_ch3_lvl3 = DynAccessor(95061)
        style_ch3_lvl4 = DynAccessor(95062)

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(95063)
        clouds_1366 = DynAccessor(95064)
        clouds_1600 = DynAccessor(95065)
        clouds_1920 = DynAccessor(95066)
        clouds_2560 = DynAccessor(95067)
        spark_white = DynAccessor(95068)
        spark_yellow = DynAccessor(95069)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(95070)
        godRaysNew_130x130 = DynAccessor(95071)
        godRaysNew_1600x1600 = DynAccessor(95072)
        particles_280x170 = DynAccessor(95073)
        rankAnimation_first = DynAccessor(95074)
        rankAnimation_second = DynAccessor(95075)
        rankAnimation_third = DynAccessor(95076)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(95077)
            veteran_frame_big = DynAccessor(95078)
            veteran_frame_small = DynAccessor(95079)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(95080)
        example_2 = DynAccessor(95081)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(95082)
        vehicle_sparks_2 = DynAccessor(95083)
        vehicle_sparks_3 = DynAccessor(95084)

    dogtags = _dogtags()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        lootbox_prem = DynAccessor(95085)

    event_loot_boxes = _event_loot_boxes()

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
                        bronze_common = DynAccessor(95086)
                        bronze_rare = DynAccessor(95087)
                        gold_common = DynAccessor(95088)
                        gold_rare = DynAccessor(95089)
                        silver_common = DynAccessor(95090)
                        silver_rare = DynAccessor(95091)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(95092)
                        epic_small = DynAccessor(95093)
                        rare = DynAccessor(95094)
                        rare_small = DynAccessor(95095)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95096)

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(95097)
                            gold = DynAccessor(95098)
                            silver = DynAccessor(95099)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95100)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(95101)
                        rare = DynAccessor(95102)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95103)
                    box = DynAccessor(95104)
                    hover = DynAccessor(95105)

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95106)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(95107)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(95108)
                        rare = DynAccessor(95109)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(95110)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(95111)
                        epic_small = DynAccessor(95112)
                        rare = DynAccessor(95113)
                        rare_small = DynAccessor(95114)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95115)
                    box = DynAccessor(95116)
                    hover = DynAccessor(95117)
                    idle = DynAccessor(95118)

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(95119)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(95120)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(95121)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(95122)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95123)

                noBoxesView = _noBoxesView()

            default = _default()

            class _stPatrick(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(95124)
                        rare = DynAccessor(95125)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(95126)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(95127)
                        epic_small = DynAccessor(95128)
                        rare = DynAccessor(95129)
                        rare_small = DynAccessor(95130)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95131)
                    box = DynAccessor(95132)
                    hover = DynAccessor(95133)
                    idle = DynAccessor(95134)

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(95135)

                noBoxesView = _noBoxesView()

            stPatrick = _stPatrick()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(95136)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(95137)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(95138)

    platoon = _platoon()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(95139)
        cycle_legendary = DynAccessor(95140)
        intro_epic = DynAccessor(95141)
        intro_legendary = DynAccessor(95142)

    rarity = _rarity()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(95143)

    story_mode = _story_mode()