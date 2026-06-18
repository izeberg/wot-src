from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(129950)
        bg_reward_screen = DynAccessor(129951)
        grade_change_particles = DynAccessor(129952)
        particles = DynAccessor(129953)
        up_particles = DynAccessor(129954)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(129955)
            crewCommander = DynAccessor(129956)
            crewDriver = DynAccessor(129957)
            crewGunner = DynAccessor(129958)
            crewLoader = DynAccessor(129959)
            crewRadioOperator = DynAccessor(129960)
            mentoringLicense = DynAccessor(129961)
            skillAdrenalineRush = DynAccessor(129962)
            skillAmbushMaster = DynAccessor(129963)
            skillArmorPatching = DynAccessor(129964)
            skillBattleTempered = DynAccessor(129965)
            skillBrothersInArms = DynAccessor(129966)
            skillBulletproof = DynAccessor(129967)
            skillClutchBraking = DynAccessor(129968)
            skillCommanderBonus = DynAccessor(129969)
            skillCommanderCoordination = DynAccessor(129970)
            skillCommanderEmergency = DynAccessor(129971)
            skillCommanderEnemyShotPredictor = DynAccessor(129972)
            skillCommanderPractical = DynAccessor(129973)
            skillCommanderTutor = DynAccessor(129974)
            skillConcealment = DynAccessor(129975)
            skillDesignatedTarget = DynAccessor(129976)
            skillDriverMotorExpert = DynAccessor(129977)
            skillDriverRammingMaster = DynAccessor(129978)
            skillDriverReliablePlacement = DynAccessor(129979)
            skillEagleEye = DynAccessor(129980)
            skillEfficiency = DynAccessor(129981)
            skillFirefighting = DynAccessor(129982)
            skillGunnerArmorer = DynAccessor(129983)
            skillGunnerFocus = DynAccessor(129984)
            skillGunnerLoneWolf = DynAccessor(129985)
            skillGunnerQuickAiming = DynAccessor(129986)
            skillHoldLine = DynAccessor(129987)
            skillIntuition = DynAccessor(129988)
            skillJackOfAllTrades = DynAccessor(129989)
            skillLoaderAmmunitionImprove = DynAccessor(129990)
            skillLoaderMelee = DynAccessor(129991)
            skillLoaderPerfectCharge = DynAccessor(129992)
            skillMagMastery = DynAccessor(129993)
            skillOffRoadDriving = DynAccessor(129994)
            skillPointBlast = DynAccessor(129995)
            skillPreventativeMaintenance = DynAccessor(129996)
            skillRadiomanExpert = DynAccessor(129997)
            skillRadiomanInterference = DynAccessor(129998)
            skillRadiomanSideBySide = DynAccessor(129999)
            skillRadiomanSignalInterception = DynAccessor(130000)
            skillRepairs = DynAccessor(130001)
            skillSafeStowage = DynAccessor(130002)
            skillSecondChance = DynAccessor(130003)
            skillSituationalAwareness = DynAccessor(130004)
            skillSixthSense = DynAccessor(130005)
            skillSmoothRide = DynAccessor(130006)
            skillSnapShot = DynAccessor(130007)
            skillSniper = DynAccessor(130008)
            skillStaySharp = DynAccessor(130009)
            skillSuspensionRepair = DynAccessor(130010)
            skillThreatSearch = DynAccessor(130011)
            skillUntrainedPenalty = DynAccessor(130012)
            statConcealment = DynAccessor(130013)
            statFirepower = DynAccessor(130014)
            statMobility = DynAccessor(130015)
            statSpotting = DynAccessor(130016)
            statSurvivability = DynAccessor(130017)

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
                                bg_big = DynAccessor(130018)
                                bg_medium = DynAccessor(130019)
                                bg_small = DynAccessor(130020)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(130021)
                            bg_medium = DynAccessor(130022)
                            bg_small = DynAccessor(130023)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(130024)
        bomber = DynAccessor(130025)
        inspire = DynAccessor(130026)
        minefield = DynAccessor(130027)
        patrol = DynAccessor(130028)
        recon = DynAccessor(130029)
        resuply = DynAccessor(130030)
        sabotageSquad = DynAccessor(130031)
        smokeCloud = DynAccessor(130032)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(130033)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130034)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130035)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130036)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130037)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130038)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130039)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130040)

            c_193 = _c_193()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(130041)
        style_ch1_lvl3 = DynAccessor(130042)
        style_ch1_lvl4 = DynAccessor(130043)
        style_ch2_lvl2 = DynAccessor(130044)
        style_ch2_lvl3 = DynAccessor(130045)
        style_ch2_lvl4 = DynAccessor(130046)
        style_ch3_lvl2 = DynAccessor(130047)
        style_ch3_lvl3 = DynAccessor(130048)
        style_ch3_lvl4 = DynAccessor(130049)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130050)
                    bg_small = DynAccessor(130051)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130052)
                    bg_small = DynAccessor(130053)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130054)
                    bg_small = DynAccessor(130055)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(130056)
        clouds_1366 = DynAccessor(130057)
        clouds_1600 = DynAccessor(130058)
        clouds_1920 = DynAccessor(130059)
        clouds_2560 = DynAccessor(130060)
        spark_white = DynAccessor(130061)
        spark_yellow = DynAccessor(130062)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(130063)
        godRaysNew_130x130 = DynAccessor(130064)
        godRaysNew_1600x1600 = DynAccessor(130065)
        no_epic_defeat_draw_ribbon = DynAccessor(130066)
        no_epic_victory_ribbon = DynAccessor(130067)
        rankAnimation_first = DynAccessor(130068)
        rankAnimation_second = DynAccessor(130069)
        rankAnimation_third = DynAccessor(130070)
        speech = DynAccessor(130071)
        yearly_style_fifth = DynAccessor(130072)
        yearly_style_fifth_loop = DynAccessor(130073)
        yearly_style_fourth = DynAccessor(130074)
        yearly_style_fourth_loop = DynAccessor(130075)
        yearly_style_sixth = DynAccessor(130076)
        yearly_style_sixth_loop = DynAccessor(130077)
        yearly_style_third = DynAccessor(130078)
        yearly_style_third_loop = DynAccessor(130079)
        yearly_styles = DynAccessor(130080)

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()
        no_epic_defeat_draw_ribbon = DynAccessor(130081)
        no_epic_victory_ribbon = DynAccessor(130082)

    comp7_light = _comp7_light()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(130083)
            veteran_frame_big = DynAccessor(130084)
            veteran_frame_small = DynAccessor(130085)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(130086)
        example_2 = DynAccessor(130087)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(130088)
        vehicle_sparks_2 = DynAccessor(130089)
        vehicle_sparks_3 = DynAccessor(130090)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(130091)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(130092)
        sparks_orange = DynAccessor(130093)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130094)
                    bg_medium = DynAccessor(130095)
                    bg_small = DynAccessor(130096)

                adaptive = _adaptive()
                bg_big = DynAccessor(130097)
                bg_medium = DynAccessor(130098)
                bg_small = DynAccessor(130099)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130100)
                    bg_medium = DynAccessor(130101)
                    bg_small = DynAccessor(130102)

                adaptive = _adaptive()
                bg_big = DynAccessor(130103)
                bg_medium = DynAccessor(130104)
                bg_small = DynAccessor(130105)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130106)
                    bg_medium = DynAccessor(130107)
                    bg_small = DynAccessor(130108)

                adaptive = _adaptive()
                bg_big = DynAccessor(130109)
                bg_medium = DynAccessor(130110)
                bg_small = DynAccessor(130111)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130112)
                    bg_medium = DynAccessor(130113)
                    bg_small = DynAccessor(130114)

                adaptive = _adaptive()
                bg_big = DynAccessor(130115)
                bg_medium = DynAccessor(130116)
                bg_small = DynAccessor(130117)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(130118)
            foreground_small = DynAccessor(130119)
            rays = DynAccessor(130120)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()
        rays = DynAccessor(130121)
        slide_overlay = DynAccessor(130122)

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
                        bronze_common = DynAccessor(130123)
                        bronze_rare = DynAccessor(130124)
                        gold_common = DynAccessor(130125)
                        gold_rare = DynAccessor(130126)
                        silver_common = DynAccessor(130127)
                        silver_rare = DynAccessor(130128)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(130129)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130130)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(130131)
                            gold = DynAccessor(130132)
                            silver = DynAccessor(130133)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130134)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(130135)
                        rare = DynAccessor(130136)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130137)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130138)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130139)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130140)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(130141)
                    compensationParticles = DynAccessor(130142)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(130143)
                        rare = DynAccessor(130144)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(130145)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(130146)
                        epic_small = DynAccessor(130147)
                        rare = DynAccessor(130148)
                        rare_small = DynAccessor(130149)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _common(DynAccessor):
                    __slots__ = ()

                    class _shield(DynAccessor):
                        __slots__ = ()
                        glowM = DynAccessor(130150)
                        glowS = DynAccessor(130151)

                    shield = _shield()

                common = _common()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(130152)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130153)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130154)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130155)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130156)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130157)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(130158)
                    vehicles_29969 = DynAccessor(130159)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(130160)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(130161)
            glow = DynAccessor(130162)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(130163)
            operation_10_stage_10 = DynAccessor(130164)
            operation_10_stage_5 = DynAccessor(130165)
            operation_10_stage_7 = DynAccessor(130166)
            operation_8_stage_1 = DynAccessor(130167)
            operation_8_stage_10 = DynAccessor(130168)
            operation_8_stage_5 = DynAccessor(130169)
            operation_8_stage_8 = DynAccessor(130170)
            operation_9_stage_1 = DynAccessor(130171)
            operation_9_stage_12 = DynAccessor(130172)
            operation_9_stage_5 = DynAccessor(130173)
            operation_9_stage_8 = DynAccessor(130174)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(130175)
            new_campaign_glow = DynAccessor(130176)
            new_campaign_sparks = DynAccessor(130177)
            smoke = DynAccessor(130178)
            sparks = DynAccessor(130179)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(130180)
            intro_op_10 = DynAccessor(130181)
            intro_op_8 = DynAccessor(130182)
            intro_op_9 = DynAccessor(130183)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(130184)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(130185)
            operation_8 = DynAccessor(130186)
            operation_9 = DynAccessor(130187)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(130188)
        pet_rays = DynAccessor(130189)
        synergy_blick = DynAccessor(130190)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(130191)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(130192)
        epic_victory_ribbon = DynAccessor(130193)
        no_epic_defeat_draw_ribbon = DynAccessor(130194)
        no_epic_victory_ribbon = DynAccessor(130195)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(130196)
        cycle_legendary = DynAccessor(130197)
        intro_epic = DynAccessor(130198)
        intro_legendary = DynAccessor(130199)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130200)
                single = DynAccessor(130201)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(130202)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130203)
                single = DynAccessor(130204)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130205)
                single = DynAccessor(130206)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(130207)
            icon_bg_effect = DynAccessor(130208)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(130209)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(130210)
        icon_bg_effect = DynAccessor(130211)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(130212)
        bg_hw_m = DynAccessor(130213)
        bg_hw_s = DynAccessor(130214)
        unlock_72x72 = DynAccessor(130215)

    user_missions = _user_missions()