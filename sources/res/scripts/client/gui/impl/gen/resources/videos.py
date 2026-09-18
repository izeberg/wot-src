from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(135038)
        bg_reward_screen = DynAccessor(135039)
        grade_change_particles = DynAccessor(135040)
        particles = DynAccessor(135041)
        up_particles = DynAccessor(135042)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(135043)
            crewCommander = DynAccessor(135044)
            crewDriver = DynAccessor(135045)
            crewGunner = DynAccessor(135046)
            crewLoader = DynAccessor(135047)
            crewRadioOperator = DynAccessor(135048)
            mentoringLicense = DynAccessor(135049)
            skillAdrenalineRush = DynAccessor(135050)
            skillAmbushMaster = DynAccessor(135051)
            skillArmorPatching = DynAccessor(135052)
            skillBattleTempered = DynAccessor(135053)
            skillBrothersInArms = DynAccessor(135054)
            skillBulletproof = DynAccessor(135055)
            skillClutchBraking = DynAccessor(135056)
            skillCommanderBonus = DynAccessor(135057)
            skillCommanderCoordination = DynAccessor(135058)
            skillCommanderEmergency = DynAccessor(135059)
            skillCommanderEnemyShotPredictor = DynAccessor(135060)
            skillCommanderPractical = DynAccessor(135061)
            skillCommanderTutor = DynAccessor(135062)
            skillConcealment = DynAccessor(135063)
            skillDesignatedTarget = DynAccessor(135064)
            skillDriverMotorExpert = DynAccessor(135065)
            skillDriverRammingMaster = DynAccessor(135066)
            skillDriverReliablePlacement = DynAccessor(135067)
            skillEagleEye = DynAccessor(135068)
            skillEfficiency = DynAccessor(135069)
            skillFirefighting = DynAccessor(135070)
            skillGunnerArmorer = DynAccessor(135071)
            skillGunnerFocus = DynAccessor(135072)
            skillGunnerLoneWolf = DynAccessor(135073)
            skillGunnerQuickAiming = DynAccessor(135074)
            skillHoldLine = DynAccessor(135075)
            skillIntuition = DynAccessor(135076)
            skillJackOfAllTrades = DynAccessor(135077)
            skillLoaderAmmunitionImprove = DynAccessor(135078)
            skillLoaderMelee = DynAccessor(135079)
            skillLoaderPerfectCharge = DynAccessor(135080)
            skillMagMastery = DynAccessor(135081)
            skillOffRoadDriving = DynAccessor(135082)
            skillPointBlast = DynAccessor(135083)
            skillPreventativeMaintenance = DynAccessor(135084)
            skillRadiomanExpert = DynAccessor(135085)
            skillRadiomanInterference = DynAccessor(135086)
            skillRadiomanSideBySide = DynAccessor(135087)
            skillRadiomanSignalInterception = DynAccessor(135088)
            skillRepairs = DynAccessor(135089)
            skillSafeStowage = DynAccessor(135090)
            skillSecondChance = DynAccessor(135091)
            skillSituationalAwareness = DynAccessor(135092)
            skillSixthSense = DynAccessor(135093)
            skillSmoothRide = DynAccessor(135094)
            skillSnapShot = DynAccessor(135095)
            skillSniper = DynAccessor(135096)
            skillStaySharp = DynAccessor(135097)
            skillSuspensionRepair = DynAccessor(135098)
            skillThreatSearch = DynAccessor(135099)
            skillUntrainedPenalty = DynAccessor(135100)
            statConcealment = DynAccessor(135101)
            statFirepower = DynAccessor(135102)
            statMobility = DynAccessor(135103)
            statSpotting = DynAccessor(135104)
            statSurvivability = DynAccessor(135105)

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
                                bg_big = DynAccessor(135106)
                                bg_medium = DynAccessor(135107)
                                bg_small = DynAccessor(135108)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(135109)
                            bg_medium = DynAccessor(135110)
                            bg_small = DynAccessor(135111)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(135112)
        bomber = DynAccessor(135113)
        inspire = DynAccessor(135114)
        minefield = DynAccessor(135115)
        patrol = DynAccessor(135116)
        recon = DynAccessor(135117)
        resuply = DynAccessor(135118)
        sabotageSquad = DynAccessor(135119)
        smokeCloud = DynAccessor(135120)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(135121)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135122)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135123)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135124)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135125)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135126)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135127)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(135128)

            c_193 = _c_193()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(135129)
        style_ch1_lvl3 = DynAccessor(135130)
        style_ch1_lvl4 = DynAccessor(135131)
        style_ch2_lvl2 = DynAccessor(135132)
        style_ch2_lvl3 = DynAccessor(135133)
        style_ch2_lvl4 = DynAccessor(135134)
        style_ch3_lvl2 = DynAccessor(135135)
        style_ch3_lvl3 = DynAccessor(135136)
        style_ch3_lvl4 = DynAccessor(135137)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(135138)
                    bg_small = DynAccessor(135139)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(135140)
                    bg_small = DynAccessor(135141)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(135142)
                    bg_small = DynAccessor(135143)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(135144)
        clouds_1366 = DynAccessor(135145)
        clouds_1600 = DynAccessor(135146)
        clouds_1920 = DynAccessor(135147)
        clouds_2560 = DynAccessor(135148)
        spark_white = DynAccessor(135149)
        spark_yellow = DynAccessor(135150)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(135151)
        godRaysNew_130x130 = DynAccessor(135152)
        godRaysNew_1600x1600 = DynAccessor(135153)
        no_epic_defeat_draw_ribbon = DynAccessor(135154)
        no_epic_victory_ribbon = DynAccessor(135155)
        rankAnimation_first = DynAccessor(135156)
        rankAnimation_second = DynAccessor(135157)
        rankAnimation_third = DynAccessor(135158)
        speech = DynAccessor(135159)
        yearly_style_fifth = DynAccessor(135160)
        yearly_style_fifth_loop = DynAccessor(135161)
        yearly_style_fourth = DynAccessor(135162)
        yearly_style_fourth_loop = DynAccessor(135163)
        yearly_style_sixth = DynAccessor(135164)
        yearly_style_sixth_loop = DynAccessor(135165)
        yearly_style_third = DynAccessor(135166)
        yearly_style_third_loop = DynAccessor(135167)
        yearly_styles = DynAccessor(135168)

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()
        no_epic_defeat_draw_ribbon = DynAccessor(135169)
        no_epic_victory_ribbon = DynAccessor(135170)

    comp7_light = _comp7_light()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(135171)
            veteran_frame_big = DynAccessor(135172)
            veteran_frame_small = DynAccessor(135173)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(135174)
        example_2 = DynAccessor(135175)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(135176)
        vehicle_sparks_2 = DynAccessor(135177)
        vehicle_sparks_3 = DynAccessor(135178)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(135179)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(135180)
        sparks_orange = DynAccessor(135181)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(135182)
                    bg_medium = DynAccessor(135183)
                    bg_small = DynAccessor(135184)

                adaptive = _adaptive()
                bg_big = DynAccessor(135185)
                bg_medium = DynAccessor(135186)
                bg_small = DynAccessor(135187)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(135188)
                    bg_medium = DynAccessor(135189)
                    bg_small = DynAccessor(135190)

                adaptive = _adaptive()
                bg_big = DynAccessor(135191)
                bg_medium = DynAccessor(135192)
                bg_small = DynAccessor(135193)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(135194)
                    bg_medium = DynAccessor(135195)
                    bg_small = DynAccessor(135196)

                adaptive = _adaptive()
                bg_big = DynAccessor(135197)
                bg_medium = DynAccessor(135198)
                bg_small = DynAccessor(135199)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(135200)
                    bg_medium = DynAccessor(135201)
                    bg_small = DynAccessor(135202)

                adaptive = _adaptive()
                bg_big = DynAccessor(135203)
                bg_medium = DynAccessor(135204)
                bg_small = DynAccessor(135205)

            StPatrickEntryPoint = _StPatrickEntryPoint()

            class _WhiteTigerEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(135206)
                    bg_medium = DynAccessor(135207)
                    bg_small = DynAccessor(135208)

                adaptive = _adaptive()
                bg_big = DynAccessor(135209)
                bg_medium = DynAccessor(135210)
                bg_small = DynAccessor(135211)

            WhiteTigerEntryPoint = _WhiteTigerEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(135212)
            foreground_small = DynAccessor(135213)
            rays = DynAccessor(135214)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()
        rays = DynAccessor(135215)
        slide_overlay = DynAccessor(135216)

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
                        bronze_common = DynAccessor(135217)
                        bronze_rare = DynAccessor(135218)
                        gold_common = DynAccessor(135219)
                        gold_rare = DynAccessor(135220)
                        silver_common = DynAccessor(135221)
                        silver_rare = DynAccessor(135222)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(135223)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135224)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(135225)
                            gold = DynAccessor(135226)
                            silver = DynAccessor(135227)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(135228)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(135229)
                        rare = DynAccessor(135230)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135231)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135232)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135233)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(135234)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(135235)
                    compensationParticles = DynAccessor(135236)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(135237)
                        rare = DynAccessor(135238)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(135239)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(135240)
                        epic_small = DynAccessor(135241)
                        rare = DynAccessor(135242)
                        rare_small = DynAccessor(135243)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _common(DynAccessor):
                    __slots__ = ()

                    class _shield(DynAccessor):
                        __slots__ = ()
                        glowM = DynAccessor(135244)
                        glowS = DynAccessor(135245)

                    shield = _shield()

                common = _common()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(135246)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135247)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135248)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135249)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(135250)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(135251)

                noBoxesView = _noBoxesView()

            default = _default()

            class _wt(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        wt_common = DynAccessor(135252)
                        wt_rare = DynAccessor(135253)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(135254)
                        epic_small = DynAccessor(135255)
                        rare = DynAccessor(135256)
                        rare_small = DynAccessor(135257)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(135258)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(135259)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(135260)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(135261)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            wt = DynAccessor(135262)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(135263)

                noBoxesView = _noBoxesView()

            wt = _wt()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(135264)
                    vehicles_29969 = DynAccessor(135265)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(135266)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(135267)
            glow = DynAccessor(135268)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(135269)
            operation_10_stage_10 = DynAccessor(135270)
            operation_10_stage_5 = DynAccessor(135271)
            operation_10_stage_7 = DynAccessor(135272)
            operation_11_stage_10 = DynAccessor(135273)
            operation_11_stage_13 = DynAccessor(135274)
            operation_11_stage_2 = DynAccessor(135275)
            operation_11_stage_6 = DynAccessor(135276)
            operation_8_stage_1 = DynAccessor(135277)
            operation_8_stage_10 = DynAccessor(135278)
            operation_8_stage_5 = DynAccessor(135279)
            operation_8_stage_8 = DynAccessor(135280)
            operation_9_stage_1 = DynAccessor(135281)
            operation_9_stage_12 = DynAccessor(135282)
            operation_9_stage_5 = DynAccessor(135283)
            operation_9_stage_8 = DynAccessor(135284)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(135285)
            new_campaign_glow = DynAccessor(135286)
            new_campaign_sparks = DynAccessor(135287)
            smoke = DynAccessor(135288)
            sparks = DynAccessor(135289)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(135290)
            intro_op_10 = DynAccessor(135291)
            intro_op_11 = DynAccessor(135292)
            intro_op_8 = DynAccessor(135293)
            intro_op_9 = DynAccessor(135294)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(135295)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(135296)
            operation_11 = DynAccessor(135297)
            operation_8 = DynAccessor(135298)
            operation_9 = DynAccessor(135299)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(135300)
        pet_rays = DynAccessor(135301)
        synergy_blick = DynAccessor(135302)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(135303)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(135304)
        epic_victory_ribbon = DynAccessor(135305)
        no_epic_defeat_draw_ribbon = DynAccessor(135306)
        no_epic_victory_ribbon = DynAccessor(135307)

    post_battle = _post_battle()

    class _prebattle_highlights(DynAccessor):
        __slots__ = ()

        class _marker(DynAccessor):
            __slots__ = ()

            class _big(DynAccessor):
                __slots__ = ()

                class _bronze(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135308)
                    loop_top = DynAccessor(135309)
                    start = DynAccessor(135310)
                    start_top = DynAccessor(135311)

                bronze = _bronze()

                class _gold(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135312)
                    loop_top = DynAccessor(135313)
                    start = DynAccessor(135314)
                    start_top = DynAccessor(135315)

                gold = _gold()

                class _iron(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135316)
                    loop_top = DynAccessor(135317)
                    start = DynAccessor(135318)
                    start_top = DynAccessor(135319)

                iron = _iron()

                class _prestige(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135320)
                    loop_top = DynAccessor(135321)
                    start = DynAccessor(135322)
                    start_top = DynAccessor(135323)

                prestige = _prestige()

                class _silver(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135324)
                    loop_top = DynAccessor(135325)
                    start = DynAccessor(135326)
                    start_top = DynAccessor(135327)

                silver = _silver()

            big = _big()

            class _medium(DynAccessor):
                __slots__ = ()

                class _bronze(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135328)
                    loop_top = DynAccessor(135329)
                    start = DynAccessor(135330)
                    start_top = DynAccessor(135331)

                bronze = _bronze()

                class _gold(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135332)
                    loop_top = DynAccessor(135333)
                    start = DynAccessor(135334)
                    start_top = DynAccessor(135335)

                gold = _gold()

                class _iron(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135336)
                    loop_top = DynAccessor(135337)
                    start = DynAccessor(135338)
                    start_top = DynAccessor(135339)

                iron = _iron()

                class _prestige(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135340)
                    loop_top = DynAccessor(135341)
                    start = DynAccessor(135342)
                    start_top = DynAccessor(135343)

                prestige = _prestige()

                class _silver(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135344)
                    loop_top = DynAccessor(135345)
                    start = DynAccessor(135346)
                    start_top = DynAccessor(135347)

                silver = _silver()

            medium = _medium()

            class _small(DynAccessor):
                __slots__ = ()

                class _bronze(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135348)
                    loop_top = DynAccessor(135349)
                    start = DynAccessor(135350)
                    start_top = DynAccessor(135351)

                bronze = _bronze()

                class _gold(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135352)
                    loop_top = DynAccessor(135353)
                    start = DynAccessor(135354)
                    start_top = DynAccessor(135355)

                gold = _gold()

                class _iron(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135356)
                    loop_top = DynAccessor(135357)
                    start = DynAccessor(135358)
                    start_top = DynAccessor(135359)

                iron = _iron()

                class _prestige(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135360)
                    loop_top = DynAccessor(135361)
                    start = DynAccessor(135362)
                    start_top = DynAccessor(135363)

                prestige = _prestige()

                class _silver(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135364)
                    loop_top = DynAccessor(135365)
                    start = DynAccessor(135366)
                    start_top = DynAccessor(135367)

                silver = _silver()

            small = _small()

            class _upscale(DynAccessor):
                __slots__ = ()

                class _bronze(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135368)
                    loop_top = DynAccessor(135369)
                    start = DynAccessor(135370)
                    start_top = DynAccessor(135371)

                bronze = _bronze()

                class _gold(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135372)
                    loop_top = DynAccessor(135373)
                    start = DynAccessor(135374)
                    start_top = DynAccessor(135375)

                gold = _gold()

                class _iron(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135376)
                    loop_top = DynAccessor(135377)
                    start = DynAccessor(135378)
                    start_top = DynAccessor(135379)

                iron = _iron()

                class _prestige(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135380)
                    loop_top = DynAccessor(135381)
                    start = DynAccessor(135382)
                    start_top = DynAccessor(135383)

                prestige = _prestige()

                class _silver(DynAccessor):
                    __slots__ = ()
                    loop = DynAccessor(135384)
                    loop_top = DynAccessor(135385)
                    start = DynAccessor(135386)
                    start_top = DynAccessor(135387)

                silver = _silver()

            upscale = _upscale()

        marker = _marker()

    prebattle_highlights = _prebattle_highlights()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(135388)
        cycle_legendary = DynAccessor(135389)
        intro_epic = DynAccessor(135390)
        intro_legendary = DynAccessor(135391)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(135392)
                single = DynAccessor(135393)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(135394)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(135395)
                single = DynAccessor(135396)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(135397)
                single = DynAccessor(135398)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(135399)
            icon_bg_effect = DynAccessor(135400)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(135401)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(135402)
        icon_bg_effect = DynAccessor(135403)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(135404)
        bg_hw_m = DynAccessor(135405)
        bg_hw_s = DynAccessor(135406)
        unlock_72x72 = DynAccessor(135407)

    user_missions = _user_missions()