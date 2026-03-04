from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(125123)
        bg_reward_screen = DynAccessor(125124)
        grade_change_particles = DynAccessor(125125)
        particles = DynAccessor(125126)
        up_particles = DynAccessor(125127)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(125128)
            crewCommander = DynAccessor(125129)
            crewDriver = DynAccessor(125130)
            crewGunner = DynAccessor(125131)
            crewLoader = DynAccessor(125132)
            crewRadioOperator = DynAccessor(125133)
            mentoringLicense = DynAccessor(125134)
            skillAdrenalineRush = DynAccessor(125135)
            skillAmbushMaster = DynAccessor(125136)
            skillArmorPatching = DynAccessor(125137)
            skillBattleTempered = DynAccessor(125138)
            skillBrothersInArms = DynAccessor(125139)
            skillBulletproof = DynAccessor(125140)
            skillClutchBraking = DynAccessor(125141)
            skillCommanderBonus = DynAccessor(125142)
            skillCommanderCoordination = DynAccessor(125143)
            skillCommanderEmergency = DynAccessor(125144)
            skillCommanderEnemyShotPredictor = DynAccessor(125145)
            skillCommanderPractical = DynAccessor(125146)
            skillCommanderTutor = DynAccessor(125147)
            skillConcealment = DynAccessor(125148)
            skillDesignatedTarget = DynAccessor(125149)
            skillDriverMotorExpert = DynAccessor(125150)
            skillDriverRammingMaster = DynAccessor(125151)
            skillDriverReliablePlacement = DynAccessor(125152)
            skillEagleEye = DynAccessor(125153)
            skillEfficiency = DynAccessor(125154)
            skillFirefighting = DynAccessor(125155)
            skillGunnerArmorer = DynAccessor(125156)
            skillGunnerFocus = DynAccessor(125157)
            skillGunnerLoneWolf = DynAccessor(125158)
            skillGunnerQuickAiming = DynAccessor(125159)
            skillHoldLine = DynAccessor(125160)
            skillIntuition = DynAccessor(125161)
            skillJackOfAllTrades = DynAccessor(125162)
            skillLoaderAmmunitionImprove = DynAccessor(125163)
            skillLoaderMelee = DynAccessor(125164)
            skillLoaderPerfectCharge = DynAccessor(125165)
            skillMagMastery = DynAccessor(125166)
            skillOffRoadDriving = DynAccessor(125167)
            skillPointBlast = DynAccessor(125168)
            skillPreventativeMaintenance = DynAccessor(125169)
            skillRadiomanExpert = DynAccessor(125170)
            skillRadiomanInterference = DynAccessor(125171)
            skillRadiomanSideBySide = DynAccessor(125172)
            skillRadiomanSignalInterception = DynAccessor(125173)
            skillRepairs = DynAccessor(125174)
            skillSafeStowage = DynAccessor(125175)
            skillSecondChance = DynAccessor(125176)
            skillSituationalAwareness = DynAccessor(125177)
            skillSixthSense = DynAccessor(125178)
            skillSmoothRide = DynAccessor(125179)
            skillSnapShot = DynAccessor(125180)
            skillSniper = DynAccessor(125181)
            skillStaySharp = DynAccessor(125182)
            skillSuspensionRepair = DynAccessor(125183)
            skillThreatSearch = DynAccessor(125184)
            skillUntrainedPenalty = DynAccessor(125185)
            statConcealment = DynAccessor(125186)
            statFirepower = DynAccessor(125187)
            statMobility = DynAccessor(125188)
            statSpotting = DynAccessor(125189)
            statSurvivability = DynAccessor(125190)

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
                                bg_big = DynAccessor(125191)
                                bg_medium = DynAccessor(125192)
                                bg_small = DynAccessor(125193)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(125194)
                            bg_medium = DynAccessor(125195)
                            bg_small = DynAccessor(125196)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(125197)
        bomber = DynAccessor(125198)
        inspire = DynAccessor(125199)
        minefield = DynAccessor(125200)
        patrol = DynAccessor(125201)
        recon = DynAccessor(125202)
        resuply = DynAccessor(125203)
        sabotageSquad = DynAccessor(125204)
        smokeCloud = DynAccessor(125205)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(125206)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125207)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125208)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125209)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125210)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125211)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125212)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125213)

            c_193 = _c_193()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125214)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125215)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125216)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125217)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(125218)
        style_ch1_lvl3 = DynAccessor(125219)
        style_ch1_lvl4 = DynAccessor(125220)
        style_ch2_lvl2 = DynAccessor(125221)
        style_ch2_lvl3 = DynAccessor(125222)
        style_ch2_lvl4 = DynAccessor(125223)
        style_ch3_lvl2 = DynAccessor(125224)
        style_ch3_lvl3 = DynAccessor(125225)
        style_ch3_lvl4 = DynAccessor(125226)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125227)
                    bg_small = DynAccessor(125228)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125229)
                    bg_small = DynAccessor(125230)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(125231)
        clouds_1366 = DynAccessor(125232)
        clouds_1600 = DynAccessor(125233)
        clouds_1920 = DynAccessor(125234)
        clouds_2560 = DynAccessor(125235)
        spark_white = DynAccessor(125236)
        spark_yellow = DynAccessor(125237)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(125238)
        godRaysNew_130x130 = DynAccessor(125239)
        godRaysNew_1600x1600 = DynAccessor(125240)
        rankAnimation_first = DynAccessor(125241)
        rankAnimation_second = DynAccessor(125242)
        rankAnimation_third = DynAccessor(125243)
        yearly_style_fifth = DynAccessor(125244)
        yearly_style_fifth_loop = DynAccessor(125245)
        yearly_style_fourth = DynAccessor(125246)
        yearly_style_fourth_loop = DynAccessor(125247)
        yearly_style_sixth = DynAccessor(125248)
        yearly_style_sixth_loop = DynAccessor(125249)
        yearly_style_third = DynAccessor(125250)
        yearly_style_third_loop = DynAccessor(125251)
        yearly_styles = DynAccessor(125252)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(125253)
            veteran_frame_big = DynAccessor(125254)
            veteran_frame_small = DynAccessor(125255)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(125256)
        example_2 = DynAccessor(125257)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(125258)
        vehicle_sparks_2 = DynAccessor(125259)
        vehicle_sparks_3 = DynAccessor(125260)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(125261)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(125262)
        sparks_orange = DynAccessor(125263)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125264)
                    bg_medium = DynAccessor(125265)
                    bg_small = DynAccessor(125266)

                adaptive = _adaptive()
                bg_big = DynAccessor(125267)
                bg_medium = DynAccessor(125268)
                bg_small = DynAccessor(125269)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125270)
                    bg_medium = DynAccessor(125271)
                    bg_small = DynAccessor(125272)

                adaptive = _adaptive()
                bg_big = DynAccessor(125273)
                bg_medium = DynAccessor(125274)
                bg_small = DynAccessor(125275)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125276)
                    bg_medium = DynAccessor(125277)
                    bg_small = DynAccessor(125278)

                adaptive = _adaptive()
                bg_big = DynAccessor(125279)
                bg_medium = DynAccessor(125280)
                bg_small = DynAccessor(125281)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(125282)
            foreground_small = DynAccessor(125283)
            rays = DynAccessor(125284)

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
                        bronze_common = DynAccessor(125285)
                        bronze_rare = DynAccessor(125286)
                        gold_common = DynAccessor(125287)
                        gold_rare = DynAccessor(125288)
                        silver_common = DynAccessor(125289)
                        silver_rare = DynAccessor(125290)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125291)
                        epic_small = DynAccessor(125292)
                        rare = DynAccessor(125293)
                        rare_small = DynAccessor(125294)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125295)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(125296)
                            gold = DynAccessor(125297)
                            silver = DynAccessor(125298)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125299)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125300)
                        rare = DynAccessor(125301)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125302)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125303)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125304)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125305)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(125306)
                    compensationParticles = DynAccessor(125307)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125308)
                        rare = DynAccessor(125309)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125310)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125311)
                        epic_small = DynAccessor(125312)
                        rare = DynAccessor(125313)
                        rare_small = DynAccessor(125314)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125315)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125316)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125317)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125318)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125319)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125320)

                noBoxesView = _noBoxesView()

            default = _default()

            class _stPatrick(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125321)
                        rare = DynAccessor(125322)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125323)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125324)
                        epic_small = DynAccessor(125325)
                        rare = DynAccessor(125326)
                        rare_small = DynAccessor(125327)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125328)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125329)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125330)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125331)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125332)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125333)

                noBoxesView = _noBoxesView()

            stPatrick = _stPatrick()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125334)
                    vehicles_29969 = DynAccessor(125335)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125336)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(125337)
            operation_10_stage_10 = DynAccessor(125338)
            operation_10_stage_5 = DynAccessor(125339)
            operation_10_stage_7 = DynAccessor(125340)
            operation_8_stage_1 = DynAccessor(125341)
            operation_8_stage_10 = DynAccessor(125342)
            operation_8_stage_5 = DynAccessor(125343)
            operation_8_stage_8 = DynAccessor(125344)
            operation_9_stage_1 = DynAccessor(125345)
            operation_9_stage_12 = DynAccessor(125346)
            operation_9_stage_5 = DynAccessor(125347)
            operation_9_stage_8 = DynAccessor(125348)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(125349)
            new_campaign_glow = DynAccessor(125350)
            new_campaign_sparks = DynAccessor(125351)
            smoke = DynAccessor(125352)
            sparks = DynAccessor(125353)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(125354)
            intro_op_10 = DynAccessor(125355)
            intro_op_8 = DynAccessor(125356)
            intro_op_9 = DynAccessor(125357)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(125358)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(125359)
            operation_8 = DynAccessor(125360)
            operation_9 = DynAccessor(125361)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(125362)
        pet_rays = DynAccessor(125363)
        synergy_blick = DynAccessor(125364)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(125365)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(125366)
        epic_victory_ribbon = DynAccessor(125367)
        no_epic_defeat_draw_ribbon = DynAccessor(125368)
        no_epic_victory_ribbon = DynAccessor(125369)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(125370)
        cycle_legendary = DynAccessor(125371)
        intro_epic = DynAccessor(125372)
        intro_legendary = DynAccessor(125373)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125374)
                single = DynAccessor(125375)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(125376)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125377)
                single = DynAccessor(125378)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125379)
                single = DynAccessor(125380)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(125381)
            icon_bg_effect = DynAccessor(125382)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(125383)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(125384)
        icon_bg_effect = DynAccessor(125385)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(125386)
        bg_hw_m = DynAccessor(125387)
        bg_hw_s = DynAccessor(125388)
        unlock_72x72 = DynAccessor(125389)

    user_missions = _user_missions()