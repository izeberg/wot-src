from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(120187)
        grade_change_particles = DynAccessor(120188)
        particles = DynAccessor(120189)
        up_particles = DynAccessor(120190)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(120191)
            crewCommander = DynAccessor(120192)
            crewDriver = DynAccessor(120193)
            crewGunner = DynAccessor(120194)
            crewLoader = DynAccessor(120195)
            crewRadioOperator = DynAccessor(120196)
            mentoringLicense = DynAccessor(120197)
            skillAdrenalineRush = DynAccessor(120198)
            skillAmbushMaster = DynAccessor(120199)
            skillBrothersInArms = DynAccessor(120200)
            skillClutchBraking = DynAccessor(120201)
            skillCommanderBonus = DynAccessor(120202)
            skillCommanderCoordination = DynAccessor(120203)
            skillCommanderEmergency = DynAccessor(120204)
            skillCommanderEnemyShotPredictor = DynAccessor(120205)
            skillCommanderPractical = DynAccessor(120206)
            skillCommanderTutor = DynAccessor(120207)
            skillConcealment = DynAccessor(120208)
            skillDesignatedTarget = DynAccessor(120209)
            skillDriverMotorExpert = DynAccessor(120210)
            skillDriverRammingMaster = DynAccessor(120211)
            skillDriverReliablePlacement = DynAccessor(120212)
            skillEagleEye = DynAccessor(120213)
            skillEfficiency = DynAccessor(120214)
            skillFirefighting = DynAccessor(120215)
            skillGunnerArmorer = DynAccessor(120216)
            skillGunnerFocus = DynAccessor(120217)
            skillGunnerQuickAiming = DynAccessor(120218)
            skillIntuition = DynAccessor(120219)
            skillJackOfAllTrades = DynAccessor(120220)
            skillLoaderAmmunitionImprove = DynAccessor(120221)
            skillLoaderMelee = DynAccessor(120222)
            skillLoaderPerfectCharge = DynAccessor(120223)
            skillOffRoadDriving = DynAccessor(120224)
            skillPreventativeMaintenance = DynAccessor(120225)
            skillRadiomanExpert = DynAccessor(120226)
            skillRadiomanInterference = DynAccessor(120227)
            skillRadiomanSideBySide = DynAccessor(120228)
            skillRadiomanSignalInterception = DynAccessor(120229)
            skillRepairs = DynAccessor(120230)
            skillSafeStowage = DynAccessor(120231)
            skillSituationalAwareness = DynAccessor(120232)
            skillSixthSense = DynAccessor(120233)
            skillSmoothRide = DynAccessor(120234)
            skillSnapShot = DynAccessor(120235)
            skillSniper = DynAccessor(120236)
            skillUntrainedPenalty = DynAccessor(120237)
            statConcealment = DynAccessor(120238)
            statFirepower = DynAccessor(120239)
            statMobility = DynAccessor(120240)
            statSpotting = DynAccessor(120241)
            statSurvivability = DynAccessor(120242)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(120243)
        style_ch1_lvl3 = DynAccessor(120244)
        style_ch1_lvl4 = DynAccessor(120245)
        style_ch2_lvl2 = DynAccessor(120246)
        style_ch2_lvl3 = DynAccessor(120247)
        style_ch2_lvl4 = DynAccessor(120248)
        style_ch3_lvl2 = DynAccessor(120249)
        style_ch3_lvl3 = DynAccessor(120250)
        style_ch3_lvl4 = DynAccessor(120251)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg_extra = DynAccessor(120252)
                    bg_extra_small = DynAccessor(120253)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(120254)
        clouds_1366 = DynAccessor(120255)
        clouds_1600 = DynAccessor(120256)
        clouds_1920 = DynAccessor(120257)
        clouds_2560 = DynAccessor(120258)
        spark_white = DynAccessor(120259)
        spark_yellow = DynAccessor(120260)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(120261)
        godRaysNew_130x130 = DynAccessor(120262)
        godRaysNew_1600x1600 = DynAccessor(120263)
        particles_280x170 = DynAccessor(120264)
        rankAnimation_first = DynAccessor(120265)
        rankAnimation_second = DynAccessor(120266)
        rankAnimation_third = DynAccessor(120267)
        yearly_style_fifth = DynAccessor(120268)
        yearly_style_fifth_loop = DynAccessor(120269)
        yearly_style_fourth = DynAccessor(120270)
        yearly_style_fourth_loop = DynAccessor(120271)
        yearly_style_sixth = DynAccessor(120272)
        yearly_style_sixth_loop = DynAccessor(120273)
        yearly_style_third = DynAccessor(120274)
        yearly_style_third_loop = DynAccessor(120275)
        yearly_styles = DynAccessor(120276)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(120277)
            veteran_frame_big = DynAccessor(120278)
            veteran_frame_small = DynAccessor(120279)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(120280)
        example_2 = DynAccessor(120281)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(120282)
        vehicle_sparks_2 = DynAccessor(120283)
        vehicle_sparks_3 = DynAccessor(120284)

    dogtags = _dogtags()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120285)
                    bg_medium = DynAccessor(120286)
                    bg_small = DynAccessor(120287)

                adaptive = _adaptive()
                bg_big = DynAccessor(120288)
                bg_medium = DynAccessor(120289)
                bg_small = DynAccessor(120290)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120291)
                    bg_medium = DynAccessor(120292)
                    bg_small = DynAccessor(120293)

                adaptive = _adaptive()
                bg_big = DynAccessor(120294)
                bg_medium = DynAccessor(120295)
                bg_small = DynAccessor(120296)

            LSEntryPoint = _LSEntryPoint()

            class _WhiteTigerEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120297)
                    bg_medium = DynAccessor(120298)
                    bg_small = DynAccessor(120299)

                adaptive = _adaptive()
                bg_big = DynAccessor(120300)
                bg_medium = DynAccessor(120301)
                bg_small = DynAccessor(120302)

            WhiteTigerEntryPoint = _WhiteTigerEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(120303)
            foreground_small = DynAccessor(120304)
            rays = DynAccessor(120305)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()
        diff_icon_new = DynAccessor(120306)
        diff_icon_selected = DynAccessor(120307)
        king_reward = DynAccessor(120308)
        promo_loop = DynAccessor(120309)

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(120310)
            bg_2 = DynAccessor(120311)
            bg_3 = DynAccessor(120312)
            bg_4 = DynAccessor(120313)

        quants = _quants()
        reward_pass = DynAccessor(120314)
        slide_overlay = DynAccessor(120315)

    last_stand = _last_stand()

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
                        bronze_common = DynAccessor(120316)
                        bronze_rare = DynAccessor(120317)
                        gold_common = DynAccessor(120318)
                        gold_rare = DynAccessor(120319)
                        silver_common = DynAccessor(120320)
                        silver_rare = DynAccessor(120321)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120322)
                        epic_small = DynAccessor(120323)
                        rare = DynAccessor(120324)
                        rare_small = DynAccessor(120325)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120326)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(120327)
                            gold = DynAccessor(120328)
                            silver = DynAccessor(120329)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120330)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(120331)
                        rare = DynAccessor(120332)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120333)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120334)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120335)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120336)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(120337)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(120338)
                        rare = DynAccessor(120339)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(120340)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120341)
                        epic_small = DynAccessor(120342)
                        rare = DynAccessor(120343)
                        rare_small = DynAccessor(120344)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120345)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120346)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120347)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120348)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120349)

                noBoxesView = _noBoxesView()

            default = _default()

            class _wt(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        wt_common = DynAccessor(120350)
                        wt_rare = DynAccessor(120351)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120352)
                        epic_small = DynAccessor(120353)
                        rare = DynAccessor(120354)
                        rare_small = DynAccessor(120355)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120356)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120357)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120358)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120359)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120360)

                noBoxesView = _noBoxesView()

            wt = _wt()

            class _wt_cn(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        wt_common_common = DynAccessor(120361)
                        wt_common_rare = DynAccessor(120362)
                        wt_epic_common = DynAccessor(120363)
                        wt_epic_rare = DynAccessor(120364)
                        wt_rare_common = DynAccessor(120365)
                        wt_rare_rare = DynAccessor(120366)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120367)
                        epic_small = DynAccessor(120368)
                        rare = DynAccessor(120369)
                        rare_small = DynAccessor(120370)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120371)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            wt_common = DynAccessor(120372)
                            wt_epic = DynAccessor(120373)
                            wt_rare = DynAccessor(120374)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            wt_common = DynAccessor(120375)
                            wt_epic = DynAccessor(120376)
                            wt_rare = DynAccessor(120377)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            wt_common = DynAccessor(120378)
                            wt_epic = DynAccessor(120379)
                            wt_rare = DynAccessor(120380)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120381)

                noBoxesView = _noBoxesView()

            wt_cn = _wt_cn()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(120382)
                    vehicles_29969 = DynAccessor(120383)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(120384)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

            class _wt(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    vehicles_5233 = DynAccessor(120385)
                    vehicles_66113 = DynAccessor(120386)
                    vehicles_7537 = DynAccessor(120387)

                rarityOverlay = _rarityOverlay()

            wt = _wt()

            class _wt_cn(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_25091902 = DynAccessor(120388)
                    vehicles_31249 = DynAccessor(120389)
                    vehicles_5233 = DynAccessor(120390)
                    vehicles_66113 = DynAccessor(120391)
                    vehicles_7537 = DynAccessor(120392)

                rarityOverlay = _rarityOverlay()

            wt_cn = _wt_cn()

        events = _events()

    lootbox = _lootbox()

    class _one_time_gift(DynAccessor):
        __slots__ = ()
        background = DynAccessor(120393)

    one_time_gift = _one_time_gift()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(120394)
            operation_10_stage_10 = DynAccessor(120395)
            operation_10_stage_5 = DynAccessor(120396)
            operation_10_stage_7 = DynAccessor(120397)
            operation_8_stage_1 = DynAccessor(120398)
            operation_8_stage_10 = DynAccessor(120399)
            operation_8_stage_5 = DynAccessor(120400)
            operation_8_stage_8 = DynAccessor(120401)
            operation_9_stage_1 = DynAccessor(120402)
            operation_9_stage_12 = DynAccessor(120403)
            operation_9_stage_5 = DynAccessor(120404)
            operation_9_stage_8 = DynAccessor(120405)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(120406)
            new_campaign_glow = DynAccessor(120407)
            new_campaign_sparks = DynAccessor(120408)
            smoke = DynAccessor(120409)
            sparks = DynAccessor(120410)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(120411)
            intro_op_10 = DynAccessor(120412)
            intro_op_8 = DynAccessor(120413)
            intro_op_9 = DynAccessor(120414)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(120415)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(120416)
            operation_8 = DynAccessor(120417)
            operation_9 = DynAccessor(120418)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(120419)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(120420)
        epic_victory_ribbon = DynAccessor(120421)
        no_epic_defeat_draw_ribbon = DynAccessor(120422)
        no_epic_victory_ribbon = DynAccessor(120423)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(120424)
        cycle_legendary = DynAccessor(120425)
        intro_epic = DynAccessor(120426)
        intro_legendary = DynAccessor(120427)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120428)
                single = DynAccessor(120429)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(120430)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120431)
                single = DynAccessor(120432)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120433)
                single = DynAccessor(120434)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(120435)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(120436)
        bg_hw_m = DynAccessor(120437)
        bg_hw_s = DynAccessor(120438)
        unlock_72x72 = DynAccessor(120439)

    user_missions = _user_missions()