from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(125035)
        bg_reward_screen = DynAccessor(125036)
        grade_change_particles = DynAccessor(125037)
        particles = DynAccessor(125038)
        up_particles = DynAccessor(125039)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(125040)
            crewCommander = DynAccessor(125041)
            crewDriver = DynAccessor(125042)
            crewGunner = DynAccessor(125043)
            crewLoader = DynAccessor(125044)
            crewRadioOperator = DynAccessor(125045)
            mentoringLicense = DynAccessor(125046)
            skillAdrenalineRush = DynAccessor(125047)
            skillAmbushMaster = DynAccessor(125048)
            skillArmorPatching = DynAccessor(125049)
            skillBattleTempered = DynAccessor(125050)
            skillBrothersInArms = DynAccessor(125051)
            skillBulletproof = DynAccessor(125052)
            skillClutchBraking = DynAccessor(125053)
            skillCommanderBonus = DynAccessor(125054)
            skillCommanderCoordination = DynAccessor(125055)
            skillCommanderEmergency = DynAccessor(125056)
            skillCommanderEnemyShotPredictor = DynAccessor(125057)
            skillCommanderPractical = DynAccessor(125058)
            skillCommanderTutor = DynAccessor(125059)
            skillConcealment = DynAccessor(125060)
            skillDesignatedTarget = DynAccessor(125061)
            skillDriverMotorExpert = DynAccessor(125062)
            skillDriverRammingMaster = DynAccessor(125063)
            skillDriverReliablePlacement = DynAccessor(125064)
            skillEagleEye = DynAccessor(125065)
            skillEfficiency = DynAccessor(125066)
            skillFirefighting = DynAccessor(125067)
            skillGunnerArmorer = DynAccessor(125068)
            skillGunnerFocus = DynAccessor(125069)
            skillGunnerLoneWolf = DynAccessor(125070)
            skillGunnerQuickAiming = DynAccessor(125071)
            skillHoldLine = DynAccessor(125072)
            skillIntuition = DynAccessor(125073)
            skillJackOfAllTrades = DynAccessor(125074)
            skillLoaderAmmunitionImprove = DynAccessor(125075)
            skillLoaderMelee = DynAccessor(125076)
            skillLoaderPerfectCharge = DynAccessor(125077)
            skillMagMastery = DynAccessor(125078)
            skillOffRoadDriving = DynAccessor(125079)
            skillPointBlast = DynAccessor(125080)
            skillPreventativeMaintenance = DynAccessor(125081)
            skillRadiomanExpert = DynAccessor(125082)
            skillRadiomanInterference = DynAccessor(125083)
            skillRadiomanSideBySide = DynAccessor(125084)
            skillRadiomanSignalInterception = DynAccessor(125085)
            skillRepairs = DynAccessor(125086)
            skillSafeStowage = DynAccessor(125087)
            skillSecondChance = DynAccessor(125088)
            skillSituationalAwareness = DynAccessor(125089)
            skillSixthSense = DynAccessor(125090)
            skillSmoothRide = DynAccessor(125091)
            skillSnapShot = DynAccessor(125092)
            skillSniper = DynAccessor(125093)
            skillStaySharp = DynAccessor(125094)
            skillSuspensionRepair = DynAccessor(125095)
            skillThreatSearch = DynAccessor(125096)
            skillUntrainedPenalty = DynAccessor(125097)
            statConcealment = DynAccessor(125098)
            statFirepower = DynAccessor(125099)
            statMobility = DynAccessor(125100)
            statSpotting = DynAccessor(125101)
            statSurvivability = DynAccessor(125102)

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
                                bg_big = DynAccessor(125103)
                                bg_medium = DynAccessor(125104)
                                bg_small = DynAccessor(125105)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(125106)
                            bg_medium = DynAccessor(125107)
                            bg_small = DynAccessor(125108)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(125109)
        bomber = DynAccessor(125110)
        inspire = DynAccessor(125111)
        minefield = DynAccessor(125112)
        patrol = DynAccessor(125113)
        recon = DynAccessor(125114)
        resuply = DynAccessor(125115)
        sabotageSquad = DynAccessor(125116)
        smokeCloud = DynAccessor(125117)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(125118)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125119)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125120)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125121)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125122)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125123)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125124)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125125)

            c_193 = _c_193()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125126)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125127)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125128)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125129)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(125130)
        style_ch1_lvl3 = DynAccessor(125131)
        style_ch1_lvl4 = DynAccessor(125132)
        style_ch2_lvl2 = DynAccessor(125133)
        style_ch2_lvl3 = DynAccessor(125134)
        style_ch2_lvl4 = DynAccessor(125135)
        style_ch3_lvl2 = DynAccessor(125136)
        style_ch3_lvl3 = DynAccessor(125137)
        style_ch3_lvl4 = DynAccessor(125138)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125139)
                    bg_small = DynAccessor(125140)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125141)
                    bg_small = DynAccessor(125142)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(125143)
        clouds_1366 = DynAccessor(125144)
        clouds_1600 = DynAccessor(125145)
        clouds_1920 = DynAccessor(125146)
        clouds_2560 = DynAccessor(125147)
        spark_white = DynAccessor(125148)
        spark_yellow = DynAccessor(125149)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(125150)
        godRaysNew_130x130 = DynAccessor(125151)
        godRaysNew_1600x1600 = DynAccessor(125152)
        rankAnimation_first = DynAccessor(125153)
        rankAnimation_second = DynAccessor(125154)
        rankAnimation_third = DynAccessor(125155)
        yearly_style_fifth = DynAccessor(125156)
        yearly_style_fifth_loop = DynAccessor(125157)
        yearly_style_fourth = DynAccessor(125158)
        yearly_style_fourth_loop = DynAccessor(125159)
        yearly_style_sixth = DynAccessor(125160)
        yearly_style_sixth_loop = DynAccessor(125161)
        yearly_style_third = DynAccessor(125162)
        yearly_style_third_loop = DynAccessor(125163)
        yearly_styles = DynAccessor(125164)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(125165)
            veteran_frame_big = DynAccessor(125166)
            veteran_frame_small = DynAccessor(125167)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(125168)
        example_2 = DynAccessor(125169)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(125170)
        vehicle_sparks_2 = DynAccessor(125171)
        vehicle_sparks_3 = DynAccessor(125172)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(125173)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(125174)
        sparks_orange = DynAccessor(125175)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125176)
                    bg_medium = DynAccessor(125177)
                    bg_small = DynAccessor(125178)

                adaptive = _adaptive()
                bg_big = DynAccessor(125179)
                bg_medium = DynAccessor(125180)
                bg_small = DynAccessor(125181)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125182)
                    bg_medium = DynAccessor(125183)
                    bg_small = DynAccessor(125184)

                adaptive = _adaptive()
                bg_big = DynAccessor(125185)
                bg_medium = DynAccessor(125186)
                bg_small = DynAccessor(125187)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125188)
                    bg_medium = DynAccessor(125189)
                    bg_small = DynAccessor(125190)

                adaptive = _adaptive()
                bg_big = DynAccessor(125191)
                bg_medium = DynAccessor(125192)
                bg_small = DynAccessor(125193)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(125194)
            foreground_small = DynAccessor(125195)
            rays = DynAccessor(125196)

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
                        bronze_common = DynAccessor(125197)
                        bronze_rare = DynAccessor(125198)
                        gold_common = DynAccessor(125199)
                        gold_rare = DynAccessor(125200)
                        silver_common = DynAccessor(125201)
                        silver_rare = DynAccessor(125202)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125203)
                        epic_small = DynAccessor(125204)
                        rare = DynAccessor(125205)
                        rare_small = DynAccessor(125206)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125207)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(125208)
                            gold = DynAccessor(125209)
                            silver = DynAccessor(125210)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125211)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125212)
                        rare = DynAccessor(125213)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125214)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125215)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125216)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125217)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(125218)
                    compensationParticles = DynAccessor(125219)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125220)
                        rare = DynAccessor(125221)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125222)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125223)
                        epic_small = DynAccessor(125224)
                        rare = DynAccessor(125225)
                        rare_small = DynAccessor(125226)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125227)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125228)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125229)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125230)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125231)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125232)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125233)
                    vehicles_29969 = DynAccessor(125234)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125235)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(125236)
            operation_10_stage_10 = DynAccessor(125237)
            operation_10_stage_5 = DynAccessor(125238)
            operation_10_stage_7 = DynAccessor(125239)
            operation_8_stage_1 = DynAccessor(125240)
            operation_8_stage_10 = DynAccessor(125241)
            operation_8_stage_5 = DynAccessor(125242)
            operation_8_stage_8 = DynAccessor(125243)
            operation_9_stage_1 = DynAccessor(125244)
            operation_9_stage_12 = DynAccessor(125245)
            operation_9_stage_5 = DynAccessor(125246)
            operation_9_stage_8 = DynAccessor(125247)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(125248)
            new_campaign_glow = DynAccessor(125249)
            new_campaign_sparks = DynAccessor(125250)
            smoke = DynAccessor(125251)
            sparks = DynAccessor(125252)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(125253)
            intro_op_10 = DynAccessor(125254)
            intro_op_8 = DynAccessor(125255)
            intro_op_9 = DynAccessor(125256)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(125257)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(125258)
            operation_8 = DynAccessor(125259)
            operation_9 = DynAccessor(125260)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(125261)
        pet_rays = DynAccessor(125262)
        synergy_blick = DynAccessor(125263)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(125264)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(125265)
        epic_victory_ribbon = DynAccessor(125266)
        no_epic_defeat_draw_ribbon = DynAccessor(125267)
        no_epic_victory_ribbon = DynAccessor(125268)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(125269)
        cycle_legendary = DynAccessor(125270)
        intro_epic = DynAccessor(125271)
        intro_legendary = DynAccessor(125272)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125273)
                single = DynAccessor(125274)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(125275)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125276)
                single = DynAccessor(125277)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125278)
                single = DynAccessor(125279)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(125280)
            icon_bg_effect = DynAccessor(125281)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(125282)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(125283)
        icon_bg_effect = DynAccessor(125284)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(125285)
        bg_hw_m = DynAccessor(125286)
        bg_hw_s = DynAccessor(125287)
        unlock_72x72 = DynAccessor(125288)

    user_missions = _user_missions()