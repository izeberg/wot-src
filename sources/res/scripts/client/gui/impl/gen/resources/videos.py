from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(119741)
        grade_change_particles = DynAccessor(119742)
        particles = DynAccessor(119743)
        up_particles = DynAccessor(119744)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(119745)
            crewCommander = DynAccessor(119746)
            crewDriver = DynAccessor(119747)
            crewGunner = DynAccessor(119748)
            crewLoader = DynAccessor(119749)
            crewRadioOperator = DynAccessor(119750)
            mentoringLicense = DynAccessor(119751)
            skillAdrenalineRush = DynAccessor(119752)
            skillAmbushMaster = DynAccessor(119753)
            skillBrothersInArms = DynAccessor(119754)
            skillClutchBraking = DynAccessor(119755)
            skillCommanderBonus = DynAccessor(119756)
            skillCommanderCoordination = DynAccessor(119757)
            skillCommanderEmergency = DynAccessor(119758)
            skillCommanderEnemyShotPredictor = DynAccessor(119759)
            skillCommanderPractical = DynAccessor(119760)
            skillCommanderTutor = DynAccessor(119761)
            skillConcealment = DynAccessor(119762)
            skillDesignatedTarget = DynAccessor(119763)
            skillDriverMotorExpert = DynAccessor(119764)
            skillDriverRammingMaster = DynAccessor(119765)
            skillDriverReliablePlacement = DynAccessor(119766)
            skillEagleEye = DynAccessor(119767)
            skillEfficiency = DynAccessor(119768)
            skillFirefighting = DynAccessor(119769)
            skillGunnerArmorer = DynAccessor(119770)
            skillGunnerFocus = DynAccessor(119771)
            skillGunnerQuickAiming = DynAccessor(119772)
            skillIntuition = DynAccessor(119773)
            skillJackOfAllTrades = DynAccessor(119774)
            skillLoaderAmmunitionImprove = DynAccessor(119775)
            skillLoaderMelee = DynAccessor(119776)
            skillLoaderPerfectCharge = DynAccessor(119777)
            skillOffRoadDriving = DynAccessor(119778)
            skillPreventativeMaintenance = DynAccessor(119779)
            skillRadiomanExpert = DynAccessor(119780)
            skillRadiomanInterference = DynAccessor(119781)
            skillRadiomanSideBySide = DynAccessor(119782)
            skillRadiomanSignalInterception = DynAccessor(119783)
            skillRepairs = DynAccessor(119784)
            skillSafeStowage = DynAccessor(119785)
            skillSituationalAwareness = DynAccessor(119786)
            skillSixthSense = DynAccessor(119787)
            skillSmoothRide = DynAccessor(119788)
            skillSnapShot = DynAccessor(119789)
            skillSniper = DynAccessor(119790)
            skillUntrainedPenalty = DynAccessor(119791)
            statConcealment = DynAccessor(119792)
            statFirepower = DynAccessor(119793)
            statMobility = DynAccessor(119794)
            statSpotting = DynAccessor(119795)
            statSurvivability = DynAccessor(119796)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(119797)
        bomber = DynAccessor(119798)
        inspire = DynAccessor(119799)
        minefield = DynAccessor(119800)
        patrol = DynAccessor(119801)
        recon = DynAccessor(119802)
        resuply = DynAccessor(119803)
        sabotageSquad = DynAccessor(119804)
        smokeCloud = DynAccessor(119805)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(119806)
        style_ch1_lvl3 = DynAccessor(119807)
        style_ch1_lvl4 = DynAccessor(119808)
        style_ch2_lvl2 = DynAccessor(119809)
        style_ch2_lvl3 = DynAccessor(119810)
        style_ch2_lvl4 = DynAccessor(119811)
        style_ch3_lvl2 = DynAccessor(119812)
        style_ch3_lvl3 = DynAccessor(119813)
        style_ch3_lvl4 = DynAccessor(119814)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(119815)
                    bg_extra = DynAccessor(119816)
                    bg_extra_small = DynAccessor(119817)
                    bg_small = DynAccessor(119818)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(119819)
        clouds_1366 = DynAccessor(119820)
        clouds_1600 = DynAccessor(119821)
        clouds_1920 = DynAccessor(119822)
        clouds_2560 = DynAccessor(119823)
        spark_white = DynAccessor(119824)
        spark_yellow = DynAccessor(119825)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(119826)
        godRaysNew_130x130 = DynAccessor(119827)
        godRaysNew_1600x1600 = DynAccessor(119828)
        particles_280x170 = DynAccessor(119829)
        rankAnimation_first = DynAccessor(119830)
        rankAnimation_second = DynAccessor(119831)
        rankAnimation_third = DynAccessor(119832)
        yearly_style_fifth = DynAccessor(119833)
        yearly_style_fifth_loop = DynAccessor(119834)
        yearly_style_fourth = DynAccessor(119835)
        yearly_style_fourth_loop = DynAccessor(119836)
        yearly_style_sixth = DynAccessor(119837)
        yearly_style_sixth_loop = DynAccessor(119838)
        yearly_style_third = DynAccessor(119839)
        yearly_style_third_loop = DynAccessor(119840)
        yearly_styles = DynAccessor(119841)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(119842)
            veteran_frame_big = DynAccessor(119843)
            veteran_frame_small = DynAccessor(119844)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(119845)
        example_2 = DynAccessor(119846)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(119847)
        vehicle_sparks_2 = DynAccessor(119848)
        vehicle_sparks_3 = DynAccessor(119849)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(119850)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(119851)
        sparks_orange = DynAccessor(119852)

    flProgressionScreen = _flProgressionScreen()

    class _halloween(DynAccessor):
        __slots__ = ()

        class _artefacts(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(119853)
            bg_10 = DynAccessor(119854)
            bg_11 = DynAccessor(119855)
            bg_12 = DynAccessor(119856)
            bg_13 = DynAccessor(119857)
            bg_14 = DynAccessor(119858)
            bg_15 = DynAccessor(119859)
            bg_16 = DynAccessor(119860)
            bg_17 = DynAccessor(119861)
            bg_2 = DynAccessor(119862)
            bg_3 = DynAccessor(119863)
            bg_4 = DynAccessor(119864)
            bg_5 = DynAccessor(119865)
            bg_6 = DynAccessor(119866)
            bg_7 = DynAccessor(119867)
            bg_8 = DynAccessor(119868)
            bg_9 = DynAccessor(119869)
            bg_final = DynAccessor(119870)

        artefacts = _artefacts()
        king_reward = DynAccessor(119871)
        promo_loop = DynAccessor(119872)

    halloween = _halloween()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119873)
                    bg_medium = DynAccessor(119874)
                    bg_small = DynAccessor(119875)

                adaptive = _adaptive()
                bg_big = DynAccessor(119876)
                bg_medium = DynAccessor(119877)
                bg_small = DynAccessor(119878)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119879)
                    bg_medium = DynAccessor(119880)
                    bg_small = DynAccessor(119881)

                adaptive = _adaptive()
                bg_big = DynAccessor(119882)
                bg_medium = DynAccessor(119883)
                bg_small = DynAccessor(119884)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _HalloweenEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119885)
                    bg_medium = DynAccessor(119886)
                    bg_small = DynAccessor(119887)

                adaptive = _adaptive()
                bg_big = DynAccessor(119888)
                bg_medium = DynAccessor(119889)
                bg_small = DynAccessor(119890)

            HalloweenEntryPoint = _HalloweenEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(119891)
            foreground_small = DynAccessor(119892)
            rays = DynAccessor(119893)

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
                        bronze_common = DynAccessor(119894)
                        bronze_rare = DynAccessor(119895)
                        gold_common = DynAccessor(119896)
                        gold_rare = DynAccessor(119897)
                        silver_common = DynAccessor(119898)
                        silver_rare = DynAccessor(119899)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119900)
                        epic_small = DynAccessor(119901)
                        rare = DynAccessor(119902)
                        rare_small = DynAccessor(119903)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119904)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(119905)
                            gold = DynAccessor(119906)
                            silver = DynAccessor(119907)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119908)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119909)
                        rare = DynAccessor(119910)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119911)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119912)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119913)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119914)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(119915)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119916)
                        rare = DynAccessor(119917)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(119918)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119919)
                        epic_small = DynAccessor(119920)
                        rare = DynAccessor(119921)
                        rare_small = DynAccessor(119922)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119923)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119924)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119925)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119926)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119927)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119928)
                    vehicles_29969 = DynAccessor(119929)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119930)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(119931)
            operation_10_stage_10 = DynAccessor(119932)
            operation_10_stage_5 = DynAccessor(119933)
            operation_10_stage_7 = DynAccessor(119934)
            operation_8_stage_1 = DynAccessor(119935)
            operation_8_stage_10 = DynAccessor(119936)
            operation_8_stage_5 = DynAccessor(119937)
            operation_8_stage_8 = DynAccessor(119938)
            operation_9_stage_1 = DynAccessor(119939)
            operation_9_stage_12 = DynAccessor(119940)
            operation_9_stage_5 = DynAccessor(119941)
            operation_9_stage_8 = DynAccessor(119942)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(119943)
            new_campaign_glow = DynAccessor(119944)
            new_campaign_sparks = DynAccessor(119945)
            smoke = DynAccessor(119946)
            sparks = DynAccessor(119947)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(119948)
            intro_op_10 = DynAccessor(119949)
            intro_op_8 = DynAccessor(119950)
            intro_op_9 = DynAccessor(119951)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(119952)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(119953)
            operation_8 = DynAccessor(119954)
            operation_9 = DynAccessor(119955)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(119956)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(119957)
        epic_victory_ribbon = DynAccessor(119958)
        no_epic_defeat_draw_ribbon = DynAccessor(119959)
        no_epic_victory_ribbon = DynAccessor(119960)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(119961)
        cycle_legendary = DynAccessor(119962)
        intro_epic = DynAccessor(119963)
        intro_legendary = DynAccessor(119964)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119965)
                single = DynAccessor(119966)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(119967)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119968)
                single = DynAccessor(119969)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119970)
                single = DynAccessor(119971)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(119972)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(119973)
        bg_hw_m = DynAccessor(119974)
        bg_hw_s = DynAccessor(119975)
        unlock_72x72 = DynAccessor(119976)

    user_missions = _user_missions()