from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(119259)
        grade_change_particles = DynAccessor(119260)
        particles = DynAccessor(119261)
        up_particles = DynAccessor(119262)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(119263)
            crewCommander = DynAccessor(119264)
            crewDriver = DynAccessor(119265)
            crewGunner = DynAccessor(119266)
            crewLoader = DynAccessor(119267)
            crewRadioOperator = DynAccessor(119268)
            mentoringLicense = DynAccessor(119269)
            skillAdrenalineRush = DynAccessor(119270)
            skillAmbushMaster = DynAccessor(119271)
            skillBrothersInArms = DynAccessor(119272)
            skillClutchBraking = DynAccessor(119273)
            skillCommanderBonus = DynAccessor(119274)
            skillCommanderCoordination = DynAccessor(119275)
            skillCommanderEmergency = DynAccessor(119276)
            skillCommanderEnemyShotPredictor = DynAccessor(119277)
            skillCommanderPractical = DynAccessor(119278)
            skillCommanderTutor = DynAccessor(119279)
            skillConcealment = DynAccessor(119280)
            skillDesignatedTarget = DynAccessor(119281)
            skillDriverMotorExpert = DynAccessor(119282)
            skillDriverRammingMaster = DynAccessor(119283)
            skillDriverReliablePlacement = DynAccessor(119284)
            skillEagleEye = DynAccessor(119285)
            skillEfficiency = DynAccessor(119286)
            skillFirefighting = DynAccessor(119287)
            skillGunnerArmorer = DynAccessor(119288)
            skillGunnerFocus = DynAccessor(119289)
            skillGunnerQuickAiming = DynAccessor(119290)
            skillIntuition = DynAccessor(119291)
            skillJackOfAllTrades = DynAccessor(119292)
            skillLoaderAmmunitionImprove = DynAccessor(119293)
            skillLoaderMelee = DynAccessor(119294)
            skillLoaderPerfectCharge = DynAccessor(119295)
            skillOffRoadDriving = DynAccessor(119296)
            skillPreventativeMaintenance = DynAccessor(119297)
            skillRadiomanExpert = DynAccessor(119298)
            skillRadiomanInterference = DynAccessor(119299)
            skillRadiomanSideBySide = DynAccessor(119300)
            skillRadiomanSignalInterception = DynAccessor(119301)
            skillRepairs = DynAccessor(119302)
            skillSafeStowage = DynAccessor(119303)
            skillSituationalAwareness = DynAccessor(119304)
            skillSixthSense = DynAccessor(119305)
            skillSmoothRide = DynAccessor(119306)
            skillSnapShot = DynAccessor(119307)
            skillSniper = DynAccessor(119308)
            skillUntrainedPenalty = DynAccessor(119309)
            statConcealment = DynAccessor(119310)
            statFirepower = DynAccessor(119311)
            statMobility = DynAccessor(119312)
            statSpotting = DynAccessor(119313)
            statSurvivability = DynAccessor(119314)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(119315)
        bomber = DynAccessor(119316)
        inspire = DynAccessor(119317)
        minefield = DynAccessor(119318)
        patrol = DynAccessor(119319)
        recon = DynAccessor(119320)
        resuply = DynAccessor(119321)
        sabotageSquad = DynAccessor(119322)
        smokeCloud = DynAccessor(119323)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(119324)
        style_ch1_lvl3 = DynAccessor(119325)
        style_ch1_lvl4 = DynAccessor(119326)
        style_ch2_lvl2 = DynAccessor(119327)
        style_ch2_lvl3 = DynAccessor(119328)
        style_ch2_lvl4 = DynAccessor(119329)
        style_ch3_lvl2 = DynAccessor(119330)
        style_ch3_lvl3 = DynAccessor(119331)
        style_ch3_lvl4 = DynAccessor(119332)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(119333)
                    bg_small = DynAccessor(119334)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(119335)
        clouds_1366 = DynAccessor(119336)
        clouds_1600 = DynAccessor(119337)
        clouds_1920 = DynAccessor(119338)
        clouds_2560 = DynAccessor(119339)
        spark_white = DynAccessor(119340)
        spark_yellow = DynAccessor(119341)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(119342)
        godRaysNew_130x130 = DynAccessor(119343)
        godRaysNew_1600x1600 = DynAccessor(119344)
        particles_280x170 = DynAccessor(119345)
        rankAnimation_first = DynAccessor(119346)
        rankAnimation_second = DynAccessor(119347)
        rankAnimation_third = DynAccessor(119348)
        yearly_style_fifth = DynAccessor(119349)
        yearly_style_fifth_loop = DynAccessor(119350)
        yearly_style_fourth = DynAccessor(119351)
        yearly_style_fourth_loop = DynAccessor(119352)
        yearly_style_sixth = DynAccessor(119353)
        yearly_style_sixth_loop = DynAccessor(119354)
        yearly_style_third = DynAccessor(119355)
        yearly_style_third_loop = DynAccessor(119356)
        yearly_styles = DynAccessor(119357)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(119358)
            veteran_frame_big = DynAccessor(119359)
            veteran_frame_small = DynAccessor(119360)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(119361)
        example_2 = DynAccessor(119362)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(119363)
        vehicle_sparks_2 = DynAccessor(119364)
        vehicle_sparks_3 = DynAccessor(119365)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(119366)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(119367)
        sparks_orange = DynAccessor(119368)

    flProgressionScreen = _flProgressionScreen()

    class _halloween(DynAccessor):
        __slots__ = ()

        class _artefacts(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(119369)
            bg_10 = DynAccessor(119370)
            bg_11 = DynAccessor(119371)
            bg_12 = DynAccessor(119372)
            bg_13 = DynAccessor(119373)
            bg_14 = DynAccessor(119374)
            bg_15 = DynAccessor(119375)
            bg_16 = DynAccessor(119376)
            bg_17 = DynAccessor(119377)
            bg_2 = DynAccessor(119378)
            bg_3 = DynAccessor(119379)
            bg_4 = DynAccessor(119380)
            bg_5 = DynAccessor(119381)
            bg_6 = DynAccessor(119382)
            bg_7 = DynAccessor(119383)
            bg_8 = DynAccessor(119384)
            bg_9 = DynAccessor(119385)
            bg_final = DynAccessor(119386)

        artefacts = _artefacts()
        king_reward = DynAccessor(119387)
        promo_loop = DynAccessor(119388)

    halloween = _halloween()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119389)
                    bg_medium = DynAccessor(119390)
                    bg_small = DynAccessor(119391)

                adaptive = _adaptive()
                bg_big = DynAccessor(119392)
                bg_medium = DynAccessor(119393)
                bg_small = DynAccessor(119394)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119395)
                    bg_medium = DynAccessor(119396)
                    bg_small = DynAccessor(119397)

                adaptive = _adaptive()
                bg_big = DynAccessor(119398)
                bg_medium = DynAccessor(119399)
                bg_small = DynAccessor(119400)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _HalloweenEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119401)
                    bg_medium = DynAccessor(119402)
                    bg_small = DynAccessor(119403)

                adaptive = _adaptive()
                bg_big = DynAccessor(119404)
                bg_medium = DynAccessor(119405)
                bg_small = DynAccessor(119406)

            HalloweenEntryPoint = _HalloweenEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(119407)
            foreground_small = DynAccessor(119408)
            rays = DynAccessor(119409)

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
                        bronze_common = DynAccessor(119410)
                        bronze_rare = DynAccessor(119411)
                        gold_common = DynAccessor(119412)
                        gold_rare = DynAccessor(119413)
                        silver_common = DynAccessor(119414)
                        silver_rare = DynAccessor(119415)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119416)
                        epic_small = DynAccessor(119417)
                        rare = DynAccessor(119418)
                        rare_small = DynAccessor(119419)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119420)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(119421)
                            gold = DynAccessor(119422)
                            silver = DynAccessor(119423)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119424)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119425)
                        rare = DynAccessor(119426)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119427)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119428)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119429)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119430)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(119431)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119432)
                        rare = DynAccessor(119433)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(119434)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119435)
                        epic_small = DynAccessor(119436)
                        rare = DynAccessor(119437)
                        rare_small = DynAccessor(119438)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119439)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119440)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119441)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119442)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119443)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119444)
                    vehicles_29969 = DynAccessor(119445)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119446)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(119447)
            operation_10_stage_10 = DynAccessor(119448)
            operation_10_stage_5 = DynAccessor(119449)
            operation_10_stage_7 = DynAccessor(119450)
            operation_8_stage_1 = DynAccessor(119451)
            operation_8_stage_10 = DynAccessor(119452)
            operation_8_stage_5 = DynAccessor(119453)
            operation_8_stage_8 = DynAccessor(119454)
            operation_9_stage_1 = DynAccessor(119455)
            operation_9_stage_12 = DynAccessor(119456)
            operation_9_stage_5 = DynAccessor(119457)
            operation_9_stage_8 = DynAccessor(119458)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(119459)
            new_campaign_glow = DynAccessor(119460)
            new_campaign_sparks = DynAccessor(119461)
            smoke = DynAccessor(119462)
            sparks = DynAccessor(119463)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(119464)
            intro_op_10 = DynAccessor(119465)
            intro_op_8 = DynAccessor(119466)
            intro_op_9 = DynAccessor(119467)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(119468)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(119469)
            operation_8 = DynAccessor(119470)
            operation_9 = DynAccessor(119471)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(119472)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(119473)
        epic_victory_ribbon = DynAccessor(119474)
        no_epic_defeat_draw_ribbon = DynAccessor(119475)
        no_epic_victory_ribbon = DynAccessor(119476)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(119477)
        cycle_legendary = DynAccessor(119478)
        intro_epic = DynAccessor(119479)
        intro_legendary = DynAccessor(119480)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119481)
                single = DynAccessor(119482)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(119483)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119484)
                single = DynAccessor(119485)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119486)
                single = DynAccessor(119487)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(119488)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(119489)
        bg_hw_m = DynAccessor(119490)
        bg_hw_s = DynAccessor(119491)
        unlock_72x72 = DynAccessor(119492)

    user_missions = _user_missions()