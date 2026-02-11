from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(124863)
        bg_reward_screen = DynAccessor(124864)
        grade_change_particles = DynAccessor(124865)
        particles = DynAccessor(124866)
        up_particles = DynAccessor(124867)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(124868)
            crewCommander = DynAccessor(124869)
            crewDriver = DynAccessor(124870)
            crewGunner = DynAccessor(124871)
            crewLoader = DynAccessor(124872)
            crewRadioOperator = DynAccessor(124873)
            mentoringLicense = DynAccessor(124874)
            skillAdrenalineRush = DynAccessor(124875)
            skillAmbushMaster = DynAccessor(124876)
            skillBrothersInArms = DynAccessor(124877)
            skillClutchBraking = DynAccessor(124878)
            skillCommanderBonus = DynAccessor(124879)
            skillCommanderCoordination = DynAccessor(124880)
            skillCommanderEmergency = DynAccessor(124881)
            skillCommanderEnemyShotPredictor = DynAccessor(124882)
            skillCommanderPractical = DynAccessor(124883)
            skillCommanderTutor = DynAccessor(124884)
            skillConcealment = DynAccessor(124885)
            skillDesignatedTarget = DynAccessor(124886)
            skillDriverMotorExpert = DynAccessor(124887)
            skillDriverRammingMaster = DynAccessor(124888)
            skillDriverReliablePlacement = DynAccessor(124889)
            skillEagleEye = DynAccessor(124890)
            skillEfficiency = DynAccessor(124891)
            skillFirefighting = DynAccessor(124892)
            skillGunnerArmorer = DynAccessor(124893)
            skillGunnerFocus = DynAccessor(124894)
            skillGunnerQuickAiming = DynAccessor(124895)
            skillIntuition = DynAccessor(124896)
            skillJackOfAllTrades = DynAccessor(124897)
            skillLoaderAmmunitionImprove = DynAccessor(124898)
            skillLoaderMelee = DynAccessor(124899)
            skillLoaderPerfectCharge = DynAccessor(124900)
            skillOffRoadDriving = DynAccessor(124901)
            skillPreventativeMaintenance = DynAccessor(124902)
            skillRadiomanExpert = DynAccessor(124903)
            skillRadiomanInterference = DynAccessor(124904)
            skillRadiomanSideBySide = DynAccessor(124905)
            skillRadiomanSignalInterception = DynAccessor(124906)
            skillRepairs = DynAccessor(124907)
            skillSafeStowage = DynAccessor(124908)
            skillSituationalAwareness = DynAccessor(124909)
            skillSixthSense = DynAccessor(124910)
            skillSmoothRide = DynAccessor(124911)
            skillSnapShot = DynAccessor(124912)
            skillSniper = DynAccessor(124913)
            skillUntrainedPenalty = DynAccessor(124914)
            statConcealment = DynAccessor(124915)
            statFirepower = DynAccessor(124916)
            statMobility = DynAccessor(124917)
            statSpotting = DynAccessor(124918)
            statSurvivability = DynAccessor(124919)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(124920)
        bomber = DynAccessor(124921)
        inspire = DynAccessor(124922)
        minefield = DynAccessor(124923)
        patrol = DynAccessor(124924)
        recon = DynAccessor(124925)
        resuply = DynAccessor(124926)
        sabotageSquad = DynAccessor(124927)
        smokeCloud = DynAccessor(124928)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(124929)
        style_ch1_lvl3 = DynAccessor(124930)
        style_ch1_lvl4 = DynAccessor(124931)
        style_ch2_lvl2 = DynAccessor(124932)
        style_ch2_lvl3 = DynAccessor(124933)
        style_ch2_lvl4 = DynAccessor(124934)
        style_ch3_lvl2 = DynAccessor(124935)
        style_ch3_lvl3 = DynAccessor(124936)
        style_ch3_lvl4 = DynAccessor(124937)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(124938)
                    bg_small = DynAccessor(124939)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(124940)
        clouds_1366 = DynAccessor(124941)
        clouds_1600 = DynAccessor(124942)
        clouds_1920 = DynAccessor(124943)
        clouds_2560 = DynAccessor(124944)
        spark_white = DynAccessor(124945)
        spark_yellow = DynAccessor(124946)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(124947)
        godRaysNew_130x130 = DynAccessor(124948)
        godRaysNew_1600x1600 = DynAccessor(124949)
        rankAnimation_first = DynAccessor(124950)
        rankAnimation_second = DynAccessor(124951)
        rankAnimation_third = DynAccessor(124952)
        yearly_style_fifth = DynAccessor(124953)
        yearly_style_fifth_loop = DynAccessor(124954)
        yearly_style_fourth = DynAccessor(124955)
        yearly_style_fourth_loop = DynAccessor(124956)
        yearly_style_sixth = DynAccessor(124957)
        yearly_style_sixth_loop = DynAccessor(124958)
        yearly_style_third = DynAccessor(124959)
        yearly_style_third_loop = DynAccessor(124960)
        yearly_styles = DynAccessor(124961)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(124962)
            veteran_frame_big = DynAccessor(124963)
            veteran_frame_small = DynAccessor(124964)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(124965)
        example_2 = DynAccessor(124966)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(124967)
        vehicle_sparks_2 = DynAccessor(124968)
        vehicle_sparks_3 = DynAccessor(124969)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(124970)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(124971)
        sparks_orange = DynAccessor(124972)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(124973)
                    bg_medium = DynAccessor(124974)
                    bg_small = DynAccessor(124975)

                adaptive = _adaptive()
                bg_big = DynAccessor(124976)
                bg_medium = DynAccessor(124977)
                bg_small = DynAccessor(124978)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(124979)
                    bg_medium = DynAccessor(124980)
                    bg_small = DynAccessor(124981)

                adaptive = _adaptive()
                bg_big = DynAccessor(124982)
                bg_medium = DynAccessor(124983)
                bg_small = DynAccessor(124984)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _FunRandomEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(124985)
                    bg_medium = DynAccessor(124986)
                    bg_small = DynAccessor(124987)

                adaptive = _adaptive()
                bg_big = DynAccessor(124988)
                bg_medium = DynAccessor(124989)
                bg_small = DynAccessor(124990)

            FunRandomEntryPoint = _FunRandomEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(124991)
            foreground_small = DynAccessor(124992)
            rays = DynAccessor(124993)

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
                        bronze_common = DynAccessor(124994)
                        bronze_rare = DynAccessor(124995)
                        gold_common = DynAccessor(124996)
                        gold_rare = DynAccessor(124997)
                        silver_common = DynAccessor(124998)
                        silver_rare = DynAccessor(124999)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125000)
                        epic_small = DynAccessor(125001)
                        rare = DynAccessor(125002)
                        rare_small = DynAccessor(125003)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125004)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(125005)
                            gold = DynAccessor(125006)
                            silver = DynAccessor(125007)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125008)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125009)
                        rare = DynAccessor(125010)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125011)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125012)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125013)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125014)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(125015)
                    compensationParticles = DynAccessor(125016)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125017)
                        rare = DynAccessor(125018)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125019)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125020)
                        epic_small = DynAccessor(125021)
                        rare = DynAccessor(125022)
                        rare_small = DynAccessor(125023)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125024)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125025)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125026)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125027)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125028)

                noBoxesView = _noBoxesView()

            default = _default()

            class _lunar(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125029)
                        rare = DynAccessor(125030)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125031)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125032)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125033)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125034)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125035)

                noBoxesView = _noBoxesView()

            lunar = _lunar()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125036)
                    vehicles_29969 = DynAccessor(125037)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125038)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(125039)
            operation_10_stage_10 = DynAccessor(125040)
            operation_10_stage_5 = DynAccessor(125041)
            operation_10_stage_7 = DynAccessor(125042)
            operation_8_stage_1 = DynAccessor(125043)
            operation_8_stage_10 = DynAccessor(125044)
            operation_8_stage_5 = DynAccessor(125045)
            operation_8_stage_8 = DynAccessor(125046)
            operation_9_stage_1 = DynAccessor(125047)
            operation_9_stage_12 = DynAccessor(125048)
            operation_9_stage_5 = DynAccessor(125049)
            operation_9_stage_8 = DynAccessor(125050)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(125051)
            new_campaign_glow = DynAccessor(125052)
            new_campaign_sparks = DynAccessor(125053)
            smoke = DynAccessor(125054)
            sparks = DynAccessor(125055)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(125056)
            intro_op_10 = DynAccessor(125057)
            intro_op_8 = DynAccessor(125058)
            intro_op_9 = DynAccessor(125059)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(125060)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(125061)
            operation_8 = DynAccessor(125062)
            operation_9 = DynAccessor(125063)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(125064)
        pet_rays = DynAccessor(125065)
        synergy_blick = DynAccessor(125066)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(125067)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(125068)
        epic_victory_ribbon = DynAccessor(125069)
        no_epic_defeat_draw_ribbon = DynAccessor(125070)
        no_epic_victory_ribbon = DynAccessor(125071)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(125072)
        cycle_legendary = DynAccessor(125073)
        intro_epic = DynAccessor(125074)
        intro_legendary = DynAccessor(125075)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125076)
                single = DynAccessor(125077)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(125078)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125079)
                single = DynAccessor(125080)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125081)
                single = DynAccessor(125082)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(125083)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(125084)
        bg_hw_m = DynAccessor(125085)
        bg_hw_s = DynAccessor(125086)
        unlock_72x72 = DynAccessor(125087)

    user_missions = _user_missions()