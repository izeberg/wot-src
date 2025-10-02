from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(119326)
        grade_change_particles = DynAccessor(119327)
        particles = DynAccessor(119328)
        up_particles = DynAccessor(119329)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(119330)
            crewCommander = DynAccessor(119331)
            crewDriver = DynAccessor(119332)
            crewGunner = DynAccessor(119333)
            crewLoader = DynAccessor(119334)
            crewRadioOperator = DynAccessor(119335)
            mentoringLicense = DynAccessor(119336)
            skillAdrenalineRush = DynAccessor(119337)
            skillAmbushMaster = DynAccessor(119338)
            skillBrothersInArms = DynAccessor(119339)
            skillClutchBraking = DynAccessor(119340)
            skillCommanderBonus = DynAccessor(119341)
            skillCommanderCoordination = DynAccessor(119342)
            skillCommanderEmergency = DynAccessor(119343)
            skillCommanderEnemyShotPredictor = DynAccessor(119344)
            skillCommanderPractical = DynAccessor(119345)
            skillCommanderTutor = DynAccessor(119346)
            skillConcealment = DynAccessor(119347)
            skillDesignatedTarget = DynAccessor(119348)
            skillDriverMotorExpert = DynAccessor(119349)
            skillDriverRammingMaster = DynAccessor(119350)
            skillDriverReliablePlacement = DynAccessor(119351)
            skillEagleEye = DynAccessor(119352)
            skillEfficiency = DynAccessor(119353)
            skillFirefighting = DynAccessor(119354)
            skillGunnerArmorer = DynAccessor(119355)
            skillGunnerFocus = DynAccessor(119356)
            skillGunnerQuickAiming = DynAccessor(119357)
            skillIntuition = DynAccessor(119358)
            skillJackOfAllTrades = DynAccessor(119359)
            skillLoaderAmmunitionImprove = DynAccessor(119360)
            skillLoaderMelee = DynAccessor(119361)
            skillLoaderPerfectCharge = DynAccessor(119362)
            skillOffRoadDriving = DynAccessor(119363)
            skillPreventativeMaintenance = DynAccessor(119364)
            skillRadiomanExpert = DynAccessor(119365)
            skillRadiomanInterference = DynAccessor(119366)
            skillRadiomanSideBySide = DynAccessor(119367)
            skillRadiomanSignalInterception = DynAccessor(119368)
            skillRepairs = DynAccessor(119369)
            skillSafeStowage = DynAccessor(119370)
            skillSituationalAwareness = DynAccessor(119371)
            skillSixthSense = DynAccessor(119372)
            skillSmoothRide = DynAccessor(119373)
            skillSnapShot = DynAccessor(119374)
            skillSniper = DynAccessor(119375)
            skillUntrainedPenalty = DynAccessor(119376)
            statConcealment = DynAccessor(119377)
            statFirepower = DynAccessor(119378)
            statMobility = DynAccessor(119379)
            statSpotting = DynAccessor(119380)
            statSurvivability = DynAccessor(119381)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(119382)
        bomber = DynAccessor(119383)
        inspire = DynAccessor(119384)
        minefield = DynAccessor(119385)
        patrol = DynAccessor(119386)
        recon = DynAccessor(119387)
        resuply = DynAccessor(119388)
        sabotageSquad = DynAccessor(119389)
        smokeCloud = DynAccessor(119390)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(119391)
        style_ch1_lvl3 = DynAccessor(119392)
        style_ch1_lvl4 = DynAccessor(119393)
        style_ch2_lvl2 = DynAccessor(119394)
        style_ch2_lvl3 = DynAccessor(119395)
        style_ch2_lvl4 = DynAccessor(119396)
        style_ch3_lvl2 = DynAccessor(119397)
        style_ch3_lvl3 = DynAccessor(119398)
        style_ch3_lvl4 = DynAccessor(119399)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(119400)
                    bg_small = DynAccessor(119401)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(119402)
        clouds_1366 = DynAccessor(119403)
        clouds_1600 = DynAccessor(119404)
        clouds_1920 = DynAccessor(119405)
        clouds_2560 = DynAccessor(119406)
        spark_white = DynAccessor(119407)
        spark_yellow = DynAccessor(119408)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(119409)
        godRaysNew_130x130 = DynAccessor(119410)
        godRaysNew_1600x1600 = DynAccessor(119411)
        particles_280x170 = DynAccessor(119412)
        rankAnimation_first = DynAccessor(119413)
        rankAnimation_second = DynAccessor(119414)
        rankAnimation_third = DynAccessor(119415)
        yearly_style_fifth = DynAccessor(119416)
        yearly_style_fifth_loop = DynAccessor(119417)
        yearly_style_fourth = DynAccessor(119418)
        yearly_style_fourth_loop = DynAccessor(119419)
        yearly_style_sixth = DynAccessor(119420)
        yearly_style_sixth_loop = DynAccessor(119421)
        yearly_style_third = DynAccessor(119422)
        yearly_style_third_loop = DynAccessor(119423)
        yearly_styles = DynAccessor(119424)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(119425)
            veteran_frame_big = DynAccessor(119426)
            veteran_frame_small = DynAccessor(119427)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(119428)
        example_2 = DynAccessor(119429)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(119430)
        vehicle_sparks_2 = DynAccessor(119431)
        vehicle_sparks_3 = DynAccessor(119432)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(119433)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(119434)
        sparks_orange = DynAccessor(119435)

    flProgressionScreen = _flProgressionScreen()

    class _halloween(DynAccessor):
        __slots__ = ()

        class _artefacts(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(119436)
            bg_10 = DynAccessor(119437)
            bg_11 = DynAccessor(119438)
            bg_12 = DynAccessor(119439)
            bg_13 = DynAccessor(119440)
            bg_14 = DynAccessor(119441)
            bg_15 = DynAccessor(119442)
            bg_16 = DynAccessor(119443)
            bg_17 = DynAccessor(119444)
            bg_2 = DynAccessor(119445)
            bg_3 = DynAccessor(119446)
            bg_4 = DynAccessor(119447)
            bg_5 = DynAccessor(119448)
            bg_6 = DynAccessor(119449)
            bg_7 = DynAccessor(119450)
            bg_8 = DynAccessor(119451)
            bg_9 = DynAccessor(119452)
            bg_final = DynAccessor(119453)

        artefacts = _artefacts()
        king_reward = DynAccessor(119454)
        promo_loop = DynAccessor(119455)

    halloween = _halloween()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119456)
                    bg_medium = DynAccessor(119457)
                    bg_small = DynAccessor(119458)

                adaptive = _adaptive()
                bg_big = DynAccessor(119459)
                bg_medium = DynAccessor(119460)
                bg_small = DynAccessor(119461)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119462)
                    bg_medium = DynAccessor(119463)
                    bg_small = DynAccessor(119464)

                adaptive = _adaptive()
                bg_big = DynAccessor(119465)
                bg_medium = DynAccessor(119466)
                bg_small = DynAccessor(119467)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _HalloweenEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119468)
                    bg_medium = DynAccessor(119469)
                    bg_small = DynAccessor(119470)

                adaptive = _adaptive()
                bg_big = DynAccessor(119471)
                bg_medium = DynAccessor(119472)
                bg_small = DynAccessor(119473)

            HalloweenEntryPoint = _HalloweenEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(119474)
            foreground_small = DynAccessor(119475)
            rays = DynAccessor(119476)

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
                        bronze_common = DynAccessor(119477)
                        bronze_rare = DynAccessor(119478)
                        gold_common = DynAccessor(119479)
                        gold_rare = DynAccessor(119480)
                        silver_common = DynAccessor(119481)
                        silver_rare = DynAccessor(119482)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119483)
                        epic_small = DynAccessor(119484)
                        rare = DynAccessor(119485)
                        rare_small = DynAccessor(119486)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119487)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(119488)
                            gold = DynAccessor(119489)
                            silver = DynAccessor(119490)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119491)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119492)
                        rare = DynAccessor(119493)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119494)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119495)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119496)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119497)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(119498)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119499)
                        rare = DynAccessor(119500)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(119501)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119502)
                        epic_small = DynAccessor(119503)
                        rare = DynAccessor(119504)
                        rare_small = DynAccessor(119505)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119506)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119507)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119508)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119509)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119510)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119511)
                    vehicles_29969 = DynAccessor(119512)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119513)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(119514)
            operation_10_stage_10 = DynAccessor(119515)
            operation_10_stage_5 = DynAccessor(119516)
            operation_10_stage_7 = DynAccessor(119517)
            operation_8_stage_1 = DynAccessor(119518)
            operation_8_stage_10 = DynAccessor(119519)
            operation_8_stage_5 = DynAccessor(119520)
            operation_8_stage_8 = DynAccessor(119521)
            operation_9_stage_1 = DynAccessor(119522)
            operation_9_stage_12 = DynAccessor(119523)
            operation_9_stage_5 = DynAccessor(119524)
            operation_9_stage_8 = DynAccessor(119525)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(119526)
            new_campaign_glow = DynAccessor(119527)
            new_campaign_sparks = DynAccessor(119528)
            smoke = DynAccessor(119529)
            sparks = DynAccessor(119530)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(119531)
            intro_op_10 = DynAccessor(119532)
            intro_op_8 = DynAccessor(119533)
            intro_op_9 = DynAccessor(119534)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(119535)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(119536)
            operation_8 = DynAccessor(119537)
            operation_9 = DynAccessor(119538)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(119539)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(119540)
        epic_victory_ribbon = DynAccessor(119541)
        no_epic_defeat_draw_ribbon = DynAccessor(119542)
        no_epic_victory_ribbon = DynAccessor(119543)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(119544)
        cycle_legendary = DynAccessor(119545)
        intro_epic = DynAccessor(119546)
        intro_legendary = DynAccessor(119547)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119548)
                single = DynAccessor(119549)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(119550)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119551)
                single = DynAccessor(119552)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119553)
                single = DynAccessor(119554)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(119555)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(119556)
        bg_hw_m = DynAccessor(119557)
        bg_hw_s = DynAccessor(119558)
        unlock_72x72 = DynAccessor(119559)

    user_missions = _user_missions()