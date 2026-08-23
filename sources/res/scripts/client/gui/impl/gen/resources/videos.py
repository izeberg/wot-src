from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(131019)
        bg_reward_screen = DynAccessor(131020)
        grade_change_particles = DynAccessor(131021)
        particles = DynAccessor(131022)
        up_particles = DynAccessor(131023)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(131024)
            crewCommander = DynAccessor(131025)
            crewDriver = DynAccessor(131026)
            crewGunner = DynAccessor(131027)
            crewLoader = DynAccessor(131028)
            crewRadioOperator = DynAccessor(131029)
            mentoringLicense = DynAccessor(131030)
            skillAdrenalineRush = DynAccessor(131031)
            skillAmbushMaster = DynAccessor(131032)
            skillArmorPatching = DynAccessor(131033)
            skillBattleTempered = DynAccessor(131034)
            skillBrothersInArms = DynAccessor(131035)
            skillBulletproof = DynAccessor(131036)
            skillClutchBraking = DynAccessor(131037)
            skillCommanderBonus = DynAccessor(131038)
            skillCommanderCoordination = DynAccessor(131039)
            skillCommanderEmergency = DynAccessor(131040)
            skillCommanderEnemyShotPredictor = DynAccessor(131041)
            skillCommanderPractical = DynAccessor(131042)
            skillCommanderTutor = DynAccessor(131043)
            skillConcealment = DynAccessor(131044)
            skillDesignatedTarget = DynAccessor(131045)
            skillDriverMotorExpert = DynAccessor(131046)
            skillDriverRammingMaster = DynAccessor(131047)
            skillDriverReliablePlacement = DynAccessor(131048)
            skillEagleEye = DynAccessor(131049)
            skillEfficiency = DynAccessor(131050)
            skillFirefighting = DynAccessor(131051)
            skillGunnerArmorer = DynAccessor(131052)
            skillGunnerFocus = DynAccessor(131053)
            skillGunnerLoneWolf = DynAccessor(131054)
            skillGunnerQuickAiming = DynAccessor(131055)
            skillHoldLine = DynAccessor(131056)
            skillIntuition = DynAccessor(131057)
            skillJackOfAllTrades = DynAccessor(131058)
            skillLoaderAmmunitionImprove = DynAccessor(131059)
            skillLoaderMelee = DynAccessor(131060)
            skillLoaderPerfectCharge = DynAccessor(131061)
            skillMagMastery = DynAccessor(131062)
            skillOffRoadDriving = DynAccessor(131063)
            skillPointBlast = DynAccessor(131064)
            skillPreventativeMaintenance = DynAccessor(131065)
            skillRadiomanExpert = DynAccessor(131066)
            skillRadiomanInterference = DynAccessor(131067)
            skillRadiomanSideBySide = DynAccessor(131068)
            skillRadiomanSignalInterception = DynAccessor(131069)
            skillRepairs = DynAccessor(131070)
            skillSafeStowage = DynAccessor(131071)
            skillSecondChance = DynAccessor(131072)
            skillSituationalAwareness = DynAccessor(131073)
            skillSixthSense = DynAccessor(131074)
            skillSmoothRide = DynAccessor(131075)
            skillSnapShot = DynAccessor(131076)
            skillSniper = DynAccessor(131077)
            skillStaySharp = DynAccessor(131078)
            skillSuspensionRepair = DynAccessor(131079)
            skillThreatSearch = DynAccessor(131080)
            skillUntrainedPenalty = DynAccessor(131081)
            statConcealment = DynAccessor(131082)
            statFirepower = DynAccessor(131083)
            statMobility = DynAccessor(131084)
            statSpotting = DynAccessor(131085)
            statSurvivability = DynAccessor(131086)

        advancedHints = _advancedHints()

    animations = _animations()

    class _asset_packs(DynAccessor):
        __slots__ = ()

        class _modes(DynAccessor):
            __slots__ = ()

            class _fall_tanks(DynAccessor):
                __slots__ = ()

                class _hangarEventBanners(DynAccessor):
                    __slots__ = ()

                    class _event(DynAccessor):
                        __slots__ = ()

                        class _FunRandomEntryPoint(DynAccessor):
                            __slots__ = ()

                            class _adaptive(DynAccessor):
                                __slots__ = ()
                                bg_big = DynAccessor(131087)
                                bg_medium = DynAccessor(131088)
                                bg_small = DynAccessor(131089)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(131090)
                            bg_medium = DynAccessor(131091)
                            bg_small = DynAccessor(131092)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(131093)
        bomber = DynAccessor(131094)
        inspire = DynAccessor(131095)
        minefield = DynAccessor(131096)
        patrol = DynAccessor(131097)
        recon = DynAccessor(131098)
        resuply = DynAccessor(131099)
        sabotageSquad = DynAccessor(131100)
        smokeCloud = DynAccessor(131101)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(131102)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131103)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131104)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131105)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131106)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131107)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131108)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131109)

            c_193 = _c_193()

            class _c_205(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(131110)

            c_205 = _c_205()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(131111)
        style_ch1_lvl3 = DynAccessor(131112)
        style_ch1_lvl4 = DynAccessor(131113)
        style_ch2_lvl2 = DynAccessor(131114)
        style_ch2_lvl3 = DynAccessor(131115)
        style_ch2_lvl4 = DynAccessor(131116)
        style_ch3_lvl2 = DynAccessor(131117)
        style_ch3_lvl3 = DynAccessor(131118)
        style_ch3_lvl4 = DynAccessor(131119)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(131120)
                    bg_small = DynAccessor(131121)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(131122)
                    bg_small = DynAccessor(131123)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(131124)
                    bg_small = DynAccessor(131125)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(131126)
        clouds_1366 = DynAccessor(131127)
        clouds_1600 = DynAccessor(131128)
        clouds_1920 = DynAccessor(131129)
        clouds_2560 = DynAccessor(131130)
        spark_white = DynAccessor(131131)
        spark_yellow = DynAccessor(131132)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(131133)
        godRaysNew_130x130 = DynAccessor(131134)
        godRaysNew_1600x1600 = DynAccessor(131135)
        no_epic_defeat_draw_ribbon = DynAccessor(131136)
        no_epic_victory_ribbon = DynAccessor(131137)
        rankAnimation_first = DynAccessor(131138)
        rankAnimation_second = DynAccessor(131139)
        rankAnimation_third = DynAccessor(131140)
        speech = DynAccessor(131141)
        yearly_style_fifth = DynAccessor(131142)
        yearly_style_fifth_loop = DynAccessor(131143)
        yearly_style_fourth = DynAccessor(131144)
        yearly_style_fourth_loop = DynAccessor(131145)
        yearly_style_sixth = DynAccessor(131146)
        yearly_style_sixth_loop = DynAccessor(131147)
        yearly_style_third = DynAccessor(131148)
        yearly_style_third_loop = DynAccessor(131149)
        yearly_styles = DynAccessor(131150)

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()
        no_epic_defeat_draw_ribbon = DynAccessor(131151)
        no_epic_victory_ribbon = DynAccessor(131152)

    comp7_light = _comp7_light()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(131153)
            veteran_frame_big = DynAccessor(131154)
            veteran_frame_small = DynAccessor(131155)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(131156)
        example_2 = DynAccessor(131157)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(131158)
        vehicle_sparks_2 = DynAccessor(131159)
        vehicle_sparks_3 = DynAccessor(131160)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(131161)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(131162)
        sparks_orange = DynAccessor(131163)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(131164)
                    bg_medium = DynAccessor(131165)
                    bg_small = DynAccessor(131166)

                adaptive = _adaptive()
                bg_big = DynAccessor(131167)
                bg_medium = DynAccessor(131168)
                bg_small = DynAccessor(131169)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(131170)
                    bg_medium = DynAccessor(131171)
                    bg_small = DynAccessor(131172)

                adaptive = _adaptive()
                bg_big = DynAccessor(131173)
                bg_medium = DynAccessor(131174)
                bg_small = DynAccessor(131175)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _JmEventBanner(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(131176)
                    bg_medium = DynAccessor(131177)
                    bg_small = DynAccessor(131178)

                adaptive = _adaptive()
                bg_big = DynAccessor(131179)
                bg_medium = DynAccessor(131180)
                bg_small = DynAccessor(131181)

            JmEventBanner = _JmEventBanner()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(131182)
                    bg_medium = DynAccessor(131183)
                    bg_small = DynAccessor(131184)

                adaptive = _adaptive()
                bg_big = DynAccessor(131185)
                bg_medium = DynAccessor(131186)
                bg_small = DynAccessor(131187)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(131188)
                    bg_medium = DynAccessor(131189)
                    bg_small = DynAccessor(131190)

                adaptive = _adaptive()
                bg_big = DynAccessor(131191)
                bg_medium = DynAccessor(131192)
                bg_small = DynAccessor(131193)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(131194)
            foreground_small = DynAccessor(131195)
            rays = DynAccessor(131196)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _journey_marathon(DynAccessor):
        __slots__ = ()
        confetti = DynAccessor(131197)
        flashlight = DynAccessor(131198)
        lore_Medium_02 = DynAccessor(131199)
        lore_Medium_05 = DynAccessor(131200)
        lore_Medium_16 = DynAccessor(131201)
        lore_Medium_21 = DynAccessor(131202)
        tea = DynAccessor(131203)

    journey_marathon = _journey_marathon()

    class _last_stand(DynAccessor):
        __slots__ = ()
        rays = DynAccessor(131204)
        slide_overlay = DynAccessor(131205)

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
                        bronze_common = DynAccessor(131206)
                        bronze_rare = DynAccessor(131207)
                        gold_common = DynAccessor(131208)
                        gold_rare = DynAccessor(131209)
                        silver_common = DynAccessor(131210)
                        silver_rare = DynAccessor(131211)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(131212)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131213)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(131214)
                            gold = DynAccessor(131215)
                            silver = DynAccessor(131216)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(131217)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(131218)
                        rare = DynAccessor(131219)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131220)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131221)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131222)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(131223)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(131224)
                    compensationParticles = DynAccessor(131225)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(131226)
                        rare = DynAccessor(131227)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(131228)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(131229)
                        epic_small = DynAccessor(131230)
                        rare = DynAccessor(131231)
                        rare_small = DynAccessor(131232)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _common(DynAccessor):
                    __slots__ = ()

                    class _shield(DynAccessor):
                        __slots__ = ()
                        glowM = DynAccessor(131233)
                        glowS = DynAccessor(131234)

                    shield = _shield()

                common = _common()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(131235)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131236)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131237)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131238)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131239)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(131240)

                noBoxesView = _noBoxesView()

            default = _default()

            class _fractal_cn(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        fractal_cn_common_common = DynAccessor(131241)
                        fractal_cn_common_rare = DynAccessor(131242)
                        fractal_cn_epic_common = DynAccessor(131243)
                        fractal_cn_epic_rare = DynAccessor(131244)
                        fractal_cn_rare_common = DynAccessor(131245)
                        fractal_cn_rare_rare = DynAccessor(131246)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(131247)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(131248)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            fractal_cn_common = DynAccessor(131249)
                            fractal_cn_epic = DynAccessor(131250)
                            fractal_cn_rare = DynAccessor(131251)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            fractal_cn_common = DynAccessor(131252)
                            fractal_cn_epic = DynAccessor(131253)
                            fractal_cn_rare = DynAccessor(131254)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            fractal_cn_common = DynAccessor(131255)
                            fractal_cn_epic = DynAccessor(131256)
                            fractal_cn_rare = DynAccessor(131257)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(131258)

                noBoxesView = _noBoxesView()

            fractal_cn = _fractal_cn()

            class _retro(DynAccessor):
                __slots__ = ()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(131259)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            retro = DynAccessor(131260)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            retro = DynAccessor(131261)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

            retro = _retro()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_2608204 = DynAccessor(131262)
                    vehicles_25681 = DynAccessor(131263)
                    vehicles_54161 = DynAccessor(131264)
                    vehicles_69441 = DynAccessor(131265)
                    vehicles_69921 = DynAccessor(131266)
                    vehicles_70145 = DynAccessor(131267)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(131268)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

            class _fractal_cn(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_2608201 = DynAccessor(131269)
                    vehicles_25681 = DynAccessor(131270)
                    vehicles_54161 = DynAccessor(131271)
                    vehicles_57937 = DynAccessor(131272)
                    vehicles_68401 = DynAccessor(131273)
                    vehicles_69441 = DynAccessor(131274)
                    vehicles_69921 = DynAccessor(131275)
                    vehicles_70145 = DynAccessor(131276)

                rarityOverlay = _rarityOverlay()

            fractal_cn = _fractal_cn()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(131277)
            glow = DynAccessor(131278)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(131279)
            operation_10_stage_10 = DynAccessor(131280)
            operation_10_stage_5 = DynAccessor(131281)
            operation_10_stage_7 = DynAccessor(131282)
            operation_8_stage_1 = DynAccessor(131283)
            operation_8_stage_10 = DynAccessor(131284)
            operation_8_stage_5 = DynAccessor(131285)
            operation_8_stage_8 = DynAccessor(131286)
            operation_9_stage_1 = DynAccessor(131287)
            operation_9_stage_12 = DynAccessor(131288)
            operation_9_stage_5 = DynAccessor(131289)
            operation_9_stage_8 = DynAccessor(131290)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(131291)
            new_campaign_glow = DynAccessor(131292)
            new_campaign_sparks = DynAccessor(131293)
            smoke = DynAccessor(131294)
            sparks = DynAccessor(131295)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(131296)
            intro_op_10 = DynAccessor(131297)
            intro_op_8 = DynAccessor(131298)
            intro_op_9 = DynAccessor(131299)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(131300)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(131301)
            operation_8 = DynAccessor(131302)
            operation_9 = DynAccessor(131303)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(131304)
        pet_rays = DynAccessor(131305)
        synergy_blick = DynAccessor(131306)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(131307)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(131308)
        epic_victory_ribbon = DynAccessor(131309)
        no_epic_defeat_draw_ribbon = DynAccessor(131310)
        no_epic_victory_ribbon = DynAccessor(131311)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(131312)
        cycle_legendary = DynAccessor(131313)
        intro_epic = DynAccessor(131314)
        intro_legendary = DynAccessor(131315)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(131316)
                single = DynAccessor(131317)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(131318)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(131319)
                single = DynAccessor(131320)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(131321)
                single = DynAccessor(131322)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(131323)
            icon_bg_effect = DynAccessor(131324)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(131325)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(131326)
        icon_bg_effect = DynAccessor(131327)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(131328)
        bg_hw_m = DynAccessor(131329)
        bg_hw_s = DynAccessor(131330)
        unlock_72x72 = DynAccessor(131331)

    user_missions = _user_missions()