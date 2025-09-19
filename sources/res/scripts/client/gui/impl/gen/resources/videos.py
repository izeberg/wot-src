from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(120030)
        grade_change_particles = DynAccessor(120031)
        particles = DynAccessor(120032)
        up_particles = DynAccessor(120033)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(120034)
            crewCommander = DynAccessor(120035)
            crewDriver = DynAccessor(120036)
            crewGunner = DynAccessor(120037)
            crewLoader = DynAccessor(120038)
            crewRadioOperator = DynAccessor(120039)
            mentoringLicense = DynAccessor(120040)
            skillAdrenalineRush = DynAccessor(120041)
            skillAmbushMaster = DynAccessor(120042)
            skillBrothersInArms = DynAccessor(120043)
            skillClutchBraking = DynAccessor(120044)
            skillCommanderBonus = DynAccessor(120045)
            skillCommanderCoordination = DynAccessor(120046)
            skillCommanderEmergency = DynAccessor(120047)
            skillCommanderEnemyShotPredictor = DynAccessor(120048)
            skillCommanderPractical = DynAccessor(120049)
            skillCommanderTutor = DynAccessor(120050)
            skillConcealment = DynAccessor(120051)
            skillDesignatedTarget = DynAccessor(120052)
            skillDriverMotorExpert = DynAccessor(120053)
            skillDriverRammingMaster = DynAccessor(120054)
            skillDriverReliablePlacement = DynAccessor(120055)
            skillEagleEye = DynAccessor(120056)
            skillEfficiency = DynAccessor(120057)
            skillFirefighting = DynAccessor(120058)
            skillGunnerArmorer = DynAccessor(120059)
            skillGunnerFocus = DynAccessor(120060)
            skillGunnerQuickAiming = DynAccessor(120061)
            skillIntuition = DynAccessor(120062)
            skillJackOfAllTrades = DynAccessor(120063)
            skillLoaderAmmunitionImprove = DynAccessor(120064)
            skillLoaderMelee = DynAccessor(120065)
            skillLoaderPerfectCharge = DynAccessor(120066)
            skillOffRoadDriving = DynAccessor(120067)
            skillPreventativeMaintenance = DynAccessor(120068)
            skillRadiomanExpert = DynAccessor(120069)
            skillRadiomanInterference = DynAccessor(120070)
            skillRadiomanSideBySide = DynAccessor(120071)
            skillRadiomanSignalInterception = DynAccessor(120072)
            skillRepairs = DynAccessor(120073)
            skillSafeStowage = DynAccessor(120074)
            skillSituationalAwareness = DynAccessor(120075)
            skillSixthSense = DynAccessor(120076)
            skillSmoothRide = DynAccessor(120077)
            skillSnapShot = DynAccessor(120078)
            skillSniper = DynAccessor(120079)
            skillUntrainedPenalty = DynAccessor(120080)
            statConcealment = DynAccessor(120081)
            statFirepower = DynAccessor(120082)
            statMobility = DynAccessor(120083)
            statSpotting = DynAccessor(120084)
            statSurvivability = DynAccessor(120085)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(120086)
        style_ch1_lvl3 = DynAccessor(120087)
        style_ch1_lvl4 = DynAccessor(120088)
        style_ch2_lvl2 = DynAccessor(120089)
        style_ch2_lvl3 = DynAccessor(120090)
        style_ch2_lvl4 = DynAccessor(120091)
        style_ch3_lvl2 = DynAccessor(120092)
        style_ch3_lvl3 = DynAccessor(120093)
        style_ch3_lvl4 = DynAccessor(120094)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(120095)
                    bg_small = DynAccessor(120096)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(120097)
        clouds_1366 = DynAccessor(120098)
        clouds_1600 = DynAccessor(120099)
        clouds_1920 = DynAccessor(120100)
        clouds_2560 = DynAccessor(120101)
        spark_white = DynAccessor(120102)
        spark_yellow = DynAccessor(120103)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(120104)
        godRaysNew_130x130 = DynAccessor(120105)
        godRaysNew_1600x1600 = DynAccessor(120106)
        particles_280x170 = DynAccessor(120107)
        rankAnimation_first = DynAccessor(120108)
        rankAnimation_second = DynAccessor(120109)
        rankAnimation_third = DynAccessor(120110)
        yearly_style_fifth = DynAccessor(120111)
        yearly_style_fifth_loop = DynAccessor(120112)
        yearly_style_fourth = DynAccessor(120113)
        yearly_style_fourth_loop = DynAccessor(120114)
        yearly_style_sixth = DynAccessor(120115)
        yearly_style_sixth_loop = DynAccessor(120116)
        yearly_style_third = DynAccessor(120117)
        yearly_style_third_loop = DynAccessor(120118)
        yearly_styles = DynAccessor(120119)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(120120)
            veteran_frame_big = DynAccessor(120121)
            veteran_frame_small = DynAccessor(120122)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(120123)
        example_2 = DynAccessor(120124)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(120125)
        vehicle_sparks_2 = DynAccessor(120126)
        vehicle_sparks_3 = DynAccessor(120127)

    dogtags = _dogtags()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120128)
                    bg_medium = DynAccessor(120129)
                    bg_small = DynAccessor(120130)

                adaptive = _adaptive()
                bg_big = DynAccessor(120131)
                bg_medium = DynAccessor(120132)
                bg_small = DynAccessor(120133)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120134)
                    bg_medium = DynAccessor(120135)
                    bg_small = DynAccessor(120136)

                adaptive = _adaptive()
                bg_big = DynAccessor(120137)
                bg_medium = DynAccessor(120138)
                bg_small = DynAccessor(120139)

            LSEntryPoint = _LSEntryPoint()

            class _WhiteTigerEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120140)
                    bg_medium = DynAccessor(120141)
                    bg_small = DynAccessor(120142)

                adaptive = _adaptive()
                bg_big = DynAccessor(120143)
                bg_medium = DynAccessor(120144)
                bg_small = DynAccessor(120145)

            WhiteTigerEntryPoint = _WhiteTigerEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(120146)
            foreground_small = DynAccessor(120147)
            rays = DynAccessor(120148)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()
        diff_icon_new = DynAccessor(120149)
        diff_icon_selected = DynAccessor(120150)
        king_reward = DynAccessor(120151)
        promo_loop = DynAccessor(120152)

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(120153)
            bg_2 = DynAccessor(120154)
            bg_3 = DynAccessor(120155)
            bg_4 = DynAccessor(120156)

        quants = _quants()
        reward_pass = DynAccessor(120157)
        slide_overlay = DynAccessor(120158)

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
                        bronze_common = DynAccessor(120159)
                        bronze_rare = DynAccessor(120160)
                        gold_common = DynAccessor(120161)
                        gold_rare = DynAccessor(120162)
                        silver_common = DynAccessor(120163)
                        silver_rare = DynAccessor(120164)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120165)
                        epic_small = DynAccessor(120166)
                        rare = DynAccessor(120167)
                        rare_small = DynAccessor(120168)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120169)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(120170)
                            gold = DynAccessor(120171)
                            silver = DynAccessor(120172)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120173)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(120174)
                        rare = DynAccessor(120175)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120176)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120177)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120178)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120179)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(120180)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(120181)
                        rare = DynAccessor(120182)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(120183)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120184)
                        epic_small = DynAccessor(120185)
                        rare = DynAccessor(120186)
                        rare_small = DynAccessor(120187)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120188)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120189)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120190)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120191)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120192)

                noBoxesView = _noBoxesView()

            default = _default()

            class _wt(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        wt_common = DynAccessor(120193)
                        wt_rare = DynAccessor(120194)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120195)
                        epic_small = DynAccessor(120196)
                        rare = DynAccessor(120197)
                        rare_small = DynAccessor(120198)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120199)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120200)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120201)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(120202)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120203)

                noBoxesView = _noBoxesView()

            wt = _wt()

            class _wt_cn(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        wt_common_common = DynAccessor(120204)
                        wt_common_rare = DynAccessor(120205)
                        wt_epic_common = DynAccessor(120206)
                        wt_epic_rare = DynAccessor(120207)
                        wt_rare_common = DynAccessor(120208)
                        wt_rare_rare = DynAccessor(120209)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120210)
                        epic_small = DynAccessor(120211)
                        rare = DynAccessor(120212)
                        rare_small = DynAccessor(120213)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120214)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            wt_common = DynAccessor(120215)
                            wt_epic = DynAccessor(120216)
                            wt_rare = DynAccessor(120217)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            wt_common = DynAccessor(120218)
                            wt_epic = DynAccessor(120219)
                            wt_rare = DynAccessor(120220)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            wt_common = DynAccessor(120221)
                            wt_epic = DynAccessor(120222)
                            wt_rare = DynAccessor(120223)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120224)

                noBoxesView = _noBoxesView()

            wt_cn = _wt_cn()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(120225)
                    vehicles_29969 = DynAccessor(120226)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(120227)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

            class _wt(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    vehicles_5233 = DynAccessor(120228)
                    vehicles_66113 = DynAccessor(120229)
                    vehicles_7537 = DynAccessor(120230)

                rarityOverlay = _rarityOverlay()

            wt = _wt()

            class _wt_cn(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_25091902 = DynAccessor(120231)
                    vehicles_31249 = DynAccessor(120232)
                    vehicles_5233 = DynAccessor(120233)
                    vehicles_66113 = DynAccessor(120234)
                    vehicles_7537 = DynAccessor(120235)

                rarityOverlay = _rarityOverlay()

            wt_cn = _wt_cn()

        events = _events()

    lootbox = _lootbox()

    class _one_time_gift(DynAccessor):
        __slots__ = ()
        background = DynAccessor(120236)

    one_time_gift = _one_time_gift()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(120237)
            operation_10_stage_10 = DynAccessor(120238)
            operation_10_stage_5 = DynAccessor(120239)
            operation_10_stage_7 = DynAccessor(120240)
            operation_8_stage_1 = DynAccessor(120241)
            operation_8_stage_10 = DynAccessor(120242)
            operation_8_stage_5 = DynAccessor(120243)
            operation_8_stage_8 = DynAccessor(120244)
            operation_9_stage_1 = DynAccessor(120245)
            operation_9_stage_12 = DynAccessor(120246)
            operation_9_stage_5 = DynAccessor(120247)
            operation_9_stage_8 = DynAccessor(120248)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(120249)
            new_campaign_glow = DynAccessor(120250)
            new_campaign_sparks = DynAccessor(120251)
            smoke = DynAccessor(120252)
            sparks = DynAccessor(120253)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(120254)
            intro_op_10 = DynAccessor(120255)
            intro_op_8 = DynAccessor(120256)
            intro_op_9 = DynAccessor(120257)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(120258)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(120259)
            operation_8 = DynAccessor(120260)
            operation_9 = DynAccessor(120261)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(120262)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(120263)
        epic_victory_ribbon = DynAccessor(120264)
        no_epic_defeat_draw_ribbon = DynAccessor(120265)
        no_epic_victory_ribbon = DynAccessor(120266)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(120267)
        cycle_legendary = DynAccessor(120268)
        intro_epic = DynAccessor(120269)
        intro_legendary = DynAccessor(120270)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120271)
                single = DynAccessor(120272)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(120273)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120274)
                single = DynAccessor(120275)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120276)
                single = DynAccessor(120277)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(120278)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(120279)
        bg_hw_m = DynAccessor(120280)
        bg_hw_s = DynAccessor(120281)
        unlock_72x72 = DynAccessor(120282)

    user_missions = _user_missions()