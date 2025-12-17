from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(124205)
        bg_reward_screen = DynAccessor(124206)
        grade_change_particles = DynAccessor(124207)
        particles = DynAccessor(124208)
        up_particles = DynAccessor(124209)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(124210)
            crewCommander = DynAccessor(124211)
            crewDriver = DynAccessor(124212)
            crewGunner = DynAccessor(124213)
            crewLoader = DynAccessor(124214)
            crewRadioOperator = DynAccessor(124215)
            mentoringLicense = DynAccessor(124216)
            skillAdrenalineRush = DynAccessor(124217)
            skillAmbushMaster = DynAccessor(124218)
            skillBrothersInArms = DynAccessor(124219)
            skillClutchBraking = DynAccessor(124220)
            skillCommanderBonus = DynAccessor(124221)
            skillCommanderCoordination = DynAccessor(124222)
            skillCommanderEmergency = DynAccessor(124223)
            skillCommanderEnemyShotPredictor = DynAccessor(124224)
            skillCommanderPractical = DynAccessor(124225)
            skillCommanderTutor = DynAccessor(124226)
            skillConcealment = DynAccessor(124227)
            skillDesignatedTarget = DynAccessor(124228)
            skillDriverMotorExpert = DynAccessor(124229)
            skillDriverRammingMaster = DynAccessor(124230)
            skillDriverReliablePlacement = DynAccessor(124231)
            skillEagleEye = DynAccessor(124232)
            skillEfficiency = DynAccessor(124233)
            skillFirefighting = DynAccessor(124234)
            skillGunnerArmorer = DynAccessor(124235)
            skillGunnerFocus = DynAccessor(124236)
            skillGunnerQuickAiming = DynAccessor(124237)
            skillIntuition = DynAccessor(124238)
            skillJackOfAllTrades = DynAccessor(124239)
            skillLoaderAmmunitionImprove = DynAccessor(124240)
            skillLoaderMelee = DynAccessor(124241)
            skillLoaderPerfectCharge = DynAccessor(124242)
            skillOffRoadDriving = DynAccessor(124243)
            skillPreventativeMaintenance = DynAccessor(124244)
            skillRadiomanExpert = DynAccessor(124245)
            skillRadiomanInterference = DynAccessor(124246)
            skillRadiomanSideBySide = DynAccessor(124247)
            skillRadiomanSignalInterception = DynAccessor(124248)
            skillRepairs = DynAccessor(124249)
            skillSafeStowage = DynAccessor(124250)
            skillSituationalAwareness = DynAccessor(124251)
            skillSixthSense = DynAccessor(124252)
            skillSmoothRide = DynAccessor(124253)
            skillSnapShot = DynAccessor(124254)
            skillSniper = DynAccessor(124255)
            skillUntrainedPenalty = DynAccessor(124256)
            statConcealment = DynAccessor(124257)
            statFirepower = DynAccessor(124258)
            statMobility = DynAccessor(124259)
            statSpotting = DynAccessor(124260)
            statSurvivability = DynAccessor(124261)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(124262)
        bomber = DynAccessor(124263)
        inspire = DynAccessor(124264)
        minefield = DynAccessor(124265)
        patrol = DynAccessor(124266)
        recon = DynAccessor(124267)
        resuply = DynAccessor(124268)
        sabotageSquad = DynAccessor(124269)
        smokeCloud = DynAccessor(124270)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(124271)
        style_ch1_lvl3 = DynAccessor(124272)
        style_ch1_lvl4 = DynAccessor(124273)
        style_ch2_lvl2 = DynAccessor(124274)
        style_ch2_lvl3 = DynAccessor(124275)
        style_ch2_lvl4 = DynAccessor(124276)
        style_ch3_lvl2 = DynAccessor(124277)
        style_ch3_lvl3 = DynAccessor(124278)
        style_ch3_lvl4 = DynAccessor(124279)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(124280)
                    bg_small = DynAccessor(124281)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(124282)
        clouds_1366 = DynAccessor(124283)
        clouds_1600 = DynAccessor(124284)
        clouds_1920 = DynAccessor(124285)
        clouds_2560 = DynAccessor(124286)
        spark_white = DynAccessor(124287)
        spark_yellow = DynAccessor(124288)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(124289)
        godRaysNew_130x130 = DynAccessor(124290)
        godRaysNew_1600x1600 = DynAccessor(124291)
        rankAnimation_first = DynAccessor(124292)
        rankAnimation_second = DynAccessor(124293)
        rankAnimation_third = DynAccessor(124294)
        yearly_style_fifth = DynAccessor(124295)
        yearly_style_fifth_loop = DynAccessor(124296)
        yearly_style_fourth = DynAccessor(124297)
        yearly_style_fourth_loop = DynAccessor(124298)
        yearly_style_sixth = DynAccessor(124299)
        yearly_style_sixth_loop = DynAccessor(124300)
        yearly_style_third = DynAccessor(124301)
        yearly_style_third_loop = DynAccessor(124302)
        yearly_styles = DynAccessor(124303)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(124304)
            veteran_frame_big = DynAccessor(124305)
            veteran_frame_small = DynAccessor(124306)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(124307)
        example_2 = DynAccessor(124308)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(124309)
        vehicle_sparks_2 = DynAccessor(124310)
        vehicle_sparks_3 = DynAccessor(124311)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(124312)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(124313)
        sparks_orange = DynAccessor(124314)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(124315)
                    bg_medium = DynAccessor(124316)
                    bg_small = DynAccessor(124317)

                adaptive = _adaptive()
                bg_big = DynAccessor(124318)
                bg_medium = DynAccessor(124319)
                bg_small = DynAccessor(124320)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(124321)
                    bg_medium = DynAccessor(124322)
                    bg_small = DynAccessor(124323)

                adaptive = _adaptive()
                bg_big = DynAccessor(124324)
                bg_medium = DynAccessor(124325)
                bg_small = DynAccessor(124326)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(124327)
            foreground_small = DynAccessor(124328)
            rays = DynAccessor(124329)

        battle_button = _battle_button()

    header_footer = _header_footer()

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
                        bronze_common = DynAccessor(124330)
                        bronze_rare = DynAccessor(124331)
                        gold_common = DynAccessor(124332)
                        gold_rare = DynAccessor(124333)
                        silver_common = DynAccessor(124334)
                        silver_rare = DynAccessor(124335)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(124336)
                        epic_small = DynAccessor(124337)
                        rare = DynAccessor(124338)
                        rare_small = DynAccessor(124339)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124340)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(124341)
                            gold = DynAccessor(124342)
                            silver = DynAccessor(124343)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(124344)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(124345)
                        rare = DynAccessor(124346)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124347)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124348)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124349)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(124350)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(124351)
                    compensationParticles = DynAccessor(124352)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(124353)
                        rare = DynAccessor(124354)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(124355)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(124356)
                        epic_small = DynAccessor(124357)
                        rare = DynAccessor(124358)
                        rare_small = DynAccessor(124359)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124360)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124361)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124362)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(124363)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(124364)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(124365)
                    vehicles_29969 = DynAccessor(124366)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(124367)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(124368)
            operation_10_stage_10 = DynAccessor(124369)
            operation_10_stage_5 = DynAccessor(124370)
            operation_10_stage_7 = DynAccessor(124371)
            operation_8_stage_1 = DynAccessor(124372)
            operation_8_stage_10 = DynAccessor(124373)
            operation_8_stage_5 = DynAccessor(124374)
            operation_8_stage_8 = DynAccessor(124375)
            operation_9_stage_1 = DynAccessor(124376)
            operation_9_stage_12 = DynAccessor(124377)
            operation_9_stage_5 = DynAccessor(124378)
            operation_9_stage_8 = DynAccessor(124379)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(124380)
            new_campaign_glow = DynAccessor(124381)
            new_campaign_sparks = DynAccessor(124382)
            smoke = DynAccessor(124383)
            sparks = DynAccessor(124384)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(124385)
            intro_op_10 = DynAccessor(124386)
            intro_op_8 = DynAccessor(124387)
            intro_op_9 = DynAccessor(124388)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(124389)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(124390)
            operation_8 = DynAccessor(124391)
            operation_9 = DynAccessor(124392)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(124393)
        pet_rays = DynAccessor(124394)
        synergy_blick = DynAccessor(124395)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(124396)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(124397)
        epic_victory_ribbon = DynAccessor(124398)
        no_epic_defeat_draw_ribbon = DynAccessor(124399)
        no_epic_victory_ribbon = DynAccessor(124400)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(124401)
        cycle_legendary = DynAccessor(124402)
        intro_epic = DynAccessor(124403)
        intro_legendary = DynAccessor(124404)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(124405)
                single = DynAccessor(124406)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(124407)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(124408)
                single = DynAccessor(124409)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(124410)
                single = DynAccessor(124411)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(124412)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(124413)
        bg_hw_m = DynAccessor(124414)
        bg_hw_s = DynAccessor(124415)
        unlock_72x72 = DynAccessor(124416)

    user_missions = _user_missions()