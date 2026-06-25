from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(129996)
        bg_reward_screen = DynAccessor(129997)
        grade_change_particles = DynAccessor(129998)
        particles = DynAccessor(129999)
        up_particles = DynAccessor(130000)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(130001)
            crewCommander = DynAccessor(130002)
            crewDriver = DynAccessor(130003)
            crewGunner = DynAccessor(130004)
            crewLoader = DynAccessor(130005)
            crewRadioOperator = DynAccessor(130006)
            mentoringLicense = DynAccessor(130007)
            skillAdrenalineRush = DynAccessor(130008)
            skillAmbushMaster = DynAccessor(130009)
            skillArmorPatching = DynAccessor(130010)
            skillBattleTempered = DynAccessor(130011)
            skillBrothersInArms = DynAccessor(130012)
            skillBulletproof = DynAccessor(130013)
            skillClutchBraking = DynAccessor(130014)
            skillCommanderBonus = DynAccessor(130015)
            skillCommanderCoordination = DynAccessor(130016)
            skillCommanderEmergency = DynAccessor(130017)
            skillCommanderEnemyShotPredictor = DynAccessor(130018)
            skillCommanderPractical = DynAccessor(130019)
            skillCommanderTutor = DynAccessor(130020)
            skillConcealment = DynAccessor(130021)
            skillDesignatedTarget = DynAccessor(130022)
            skillDriverMotorExpert = DynAccessor(130023)
            skillDriverRammingMaster = DynAccessor(130024)
            skillDriverReliablePlacement = DynAccessor(130025)
            skillEagleEye = DynAccessor(130026)
            skillEfficiency = DynAccessor(130027)
            skillFirefighting = DynAccessor(130028)
            skillGunnerArmorer = DynAccessor(130029)
            skillGunnerFocus = DynAccessor(130030)
            skillGunnerLoneWolf = DynAccessor(130031)
            skillGunnerQuickAiming = DynAccessor(130032)
            skillHoldLine = DynAccessor(130033)
            skillIntuition = DynAccessor(130034)
            skillJackOfAllTrades = DynAccessor(130035)
            skillLoaderAmmunitionImprove = DynAccessor(130036)
            skillLoaderMelee = DynAccessor(130037)
            skillLoaderPerfectCharge = DynAccessor(130038)
            skillMagMastery = DynAccessor(130039)
            skillOffRoadDriving = DynAccessor(130040)
            skillPointBlast = DynAccessor(130041)
            skillPreventativeMaintenance = DynAccessor(130042)
            skillRadiomanExpert = DynAccessor(130043)
            skillRadiomanInterference = DynAccessor(130044)
            skillRadiomanSideBySide = DynAccessor(130045)
            skillRadiomanSignalInterception = DynAccessor(130046)
            skillRepairs = DynAccessor(130047)
            skillSafeStowage = DynAccessor(130048)
            skillSecondChance = DynAccessor(130049)
            skillSituationalAwareness = DynAccessor(130050)
            skillSixthSense = DynAccessor(130051)
            skillSmoothRide = DynAccessor(130052)
            skillSnapShot = DynAccessor(130053)
            skillSniper = DynAccessor(130054)
            skillStaySharp = DynAccessor(130055)
            skillSuspensionRepair = DynAccessor(130056)
            skillThreatSearch = DynAccessor(130057)
            skillUntrainedPenalty = DynAccessor(130058)
            statConcealment = DynAccessor(130059)
            statFirepower = DynAccessor(130060)
            statMobility = DynAccessor(130061)
            statSpotting = DynAccessor(130062)
            statSurvivability = DynAccessor(130063)

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
                                bg_big = DynAccessor(130064)
                                bg_medium = DynAccessor(130065)
                                bg_small = DynAccessor(130066)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(130067)
                            bg_medium = DynAccessor(130068)
                            bg_small = DynAccessor(130069)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(130070)
        bomber = DynAccessor(130071)
        inspire = DynAccessor(130072)
        minefield = DynAccessor(130073)
        patrol = DynAccessor(130074)
        recon = DynAccessor(130075)
        resuply = DynAccessor(130076)
        sabotageSquad = DynAccessor(130077)
        smokeCloud = DynAccessor(130078)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(130079)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130080)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130081)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130082)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130083)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130084)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130085)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130086)

            c_193 = _c_193()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(130087)
        style_ch1_lvl3 = DynAccessor(130088)
        style_ch1_lvl4 = DynAccessor(130089)
        style_ch2_lvl2 = DynAccessor(130090)
        style_ch2_lvl3 = DynAccessor(130091)
        style_ch2_lvl4 = DynAccessor(130092)
        style_ch3_lvl2 = DynAccessor(130093)
        style_ch3_lvl3 = DynAccessor(130094)
        style_ch3_lvl4 = DynAccessor(130095)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130096)
                    bg_small = DynAccessor(130097)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130098)
                    bg_small = DynAccessor(130099)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130100)
                    bg_small = DynAccessor(130101)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(130102)
        clouds_1366 = DynAccessor(130103)
        clouds_1600 = DynAccessor(130104)
        clouds_1920 = DynAccessor(130105)
        clouds_2560 = DynAccessor(130106)
        spark_white = DynAccessor(130107)
        spark_yellow = DynAccessor(130108)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(130109)
        godRaysNew_130x130 = DynAccessor(130110)
        godRaysNew_1600x1600 = DynAccessor(130111)
        no_epic_defeat_draw_ribbon = DynAccessor(130112)
        no_epic_victory_ribbon = DynAccessor(130113)
        rankAnimation_first = DynAccessor(130114)
        rankAnimation_second = DynAccessor(130115)
        rankAnimation_third = DynAccessor(130116)
        speech = DynAccessor(130117)
        yearly_style_fifth = DynAccessor(130118)
        yearly_style_fifth_loop = DynAccessor(130119)
        yearly_style_fourth = DynAccessor(130120)
        yearly_style_fourth_loop = DynAccessor(130121)
        yearly_style_sixth = DynAccessor(130122)
        yearly_style_sixth_loop = DynAccessor(130123)
        yearly_style_third = DynAccessor(130124)
        yearly_style_third_loop = DynAccessor(130125)
        yearly_styles = DynAccessor(130126)

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()
        no_epic_defeat_draw_ribbon = DynAccessor(130127)
        no_epic_victory_ribbon = DynAccessor(130128)

    comp7_light = _comp7_light()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(130129)
            veteran_frame_big = DynAccessor(130130)
            veteran_frame_small = DynAccessor(130131)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(130132)
        example_2 = DynAccessor(130133)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(130134)
        vehicle_sparks_2 = DynAccessor(130135)
        vehicle_sparks_3 = DynAccessor(130136)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(130137)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(130138)
        sparks_orange = DynAccessor(130139)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130140)
                    bg_medium = DynAccessor(130141)
                    bg_small = DynAccessor(130142)

                adaptive = _adaptive()
                bg_big = DynAccessor(130143)
                bg_medium = DynAccessor(130144)
                bg_small = DynAccessor(130145)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130146)
                    bg_medium = DynAccessor(130147)
                    bg_small = DynAccessor(130148)

                adaptive = _adaptive()
                bg_big = DynAccessor(130149)
                bg_medium = DynAccessor(130150)
                bg_small = DynAccessor(130151)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130152)
                    bg_medium = DynAccessor(130153)
                    bg_small = DynAccessor(130154)

                adaptive = _adaptive()
                bg_big = DynAccessor(130155)
                bg_medium = DynAccessor(130156)
                bg_small = DynAccessor(130157)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130158)
                    bg_medium = DynAccessor(130159)
                    bg_small = DynAccessor(130160)

                adaptive = _adaptive()
                bg_big = DynAccessor(130161)
                bg_medium = DynAccessor(130162)
                bg_small = DynAccessor(130163)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(130164)
            foreground_small = DynAccessor(130165)
            rays = DynAccessor(130166)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()
        rays = DynAccessor(130167)
        slide_overlay = DynAccessor(130168)

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
                        bronze_common = DynAccessor(130169)
                        bronze_rare = DynAccessor(130170)
                        gold_common = DynAccessor(130171)
                        gold_rare = DynAccessor(130172)
                        silver_common = DynAccessor(130173)
                        silver_rare = DynAccessor(130174)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(130175)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130176)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(130177)
                            gold = DynAccessor(130178)
                            silver = DynAccessor(130179)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130180)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(130181)
                        rare = DynAccessor(130182)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130183)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130184)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130185)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130186)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(130187)
                    compensationParticles = DynAccessor(130188)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(130189)
                        rare = DynAccessor(130190)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(130191)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(130192)
                        epic_small = DynAccessor(130193)
                        rare = DynAccessor(130194)
                        rare_small = DynAccessor(130195)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _common(DynAccessor):
                    __slots__ = ()

                    class _shield(DynAccessor):
                        __slots__ = ()
                        glowM = DynAccessor(130196)
                        glowS = DynAccessor(130197)

                    shield = _shield()

                common = _common()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(130198)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130199)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130200)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130201)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130202)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130203)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(130204)
                    vehicles_29969 = DynAccessor(130205)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(130206)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(130207)
            glow = DynAccessor(130208)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(130209)
            operation_10_stage_10 = DynAccessor(130210)
            operation_10_stage_5 = DynAccessor(130211)
            operation_10_stage_7 = DynAccessor(130212)
            operation_8_stage_1 = DynAccessor(130213)
            operation_8_stage_10 = DynAccessor(130214)
            operation_8_stage_5 = DynAccessor(130215)
            operation_8_stage_8 = DynAccessor(130216)
            operation_9_stage_1 = DynAccessor(130217)
            operation_9_stage_12 = DynAccessor(130218)
            operation_9_stage_5 = DynAccessor(130219)
            operation_9_stage_8 = DynAccessor(130220)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(130221)
            new_campaign_glow = DynAccessor(130222)
            new_campaign_sparks = DynAccessor(130223)
            smoke = DynAccessor(130224)
            sparks = DynAccessor(130225)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(130226)
            intro_op_10 = DynAccessor(130227)
            intro_op_8 = DynAccessor(130228)
            intro_op_9 = DynAccessor(130229)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(130230)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(130231)
            operation_8 = DynAccessor(130232)
            operation_9 = DynAccessor(130233)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(130234)
        pet_rays = DynAccessor(130235)
        synergy_blick = DynAccessor(130236)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(130237)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(130238)
        epic_victory_ribbon = DynAccessor(130239)
        no_epic_defeat_draw_ribbon = DynAccessor(130240)
        no_epic_victory_ribbon = DynAccessor(130241)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(130242)
        cycle_legendary = DynAccessor(130243)
        intro_epic = DynAccessor(130244)
        intro_legendary = DynAccessor(130245)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130246)
                single = DynAccessor(130247)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(130248)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130249)
                single = DynAccessor(130250)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130251)
                single = DynAccessor(130252)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(130253)
            icon_bg_effect = DynAccessor(130254)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(130255)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(130256)
        icon_bg_effect = DynAccessor(130257)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(130258)
        bg_hw_m = DynAccessor(130259)
        bg_hw_s = DynAccessor(130260)
        unlock_72x72 = DynAccessor(130261)

    user_missions = _user_missions()