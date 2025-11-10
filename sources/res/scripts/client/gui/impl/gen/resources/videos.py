from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(119867)
        grade_change_particles = DynAccessor(119868)
        particles = DynAccessor(119869)
        up_particles = DynAccessor(119870)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(119871)
            crewCommander = DynAccessor(119872)
            crewDriver = DynAccessor(119873)
            crewGunner = DynAccessor(119874)
            crewLoader = DynAccessor(119875)
            crewRadioOperator = DynAccessor(119876)
            mentoringLicense = DynAccessor(119877)
            skillAdrenalineRush = DynAccessor(119878)
            skillAmbushMaster = DynAccessor(119879)
            skillBrothersInArms = DynAccessor(119880)
            skillClutchBraking = DynAccessor(119881)
            skillCommanderBonus = DynAccessor(119882)
            skillCommanderCoordination = DynAccessor(119883)
            skillCommanderEmergency = DynAccessor(119884)
            skillCommanderEnemyShotPredictor = DynAccessor(119885)
            skillCommanderPractical = DynAccessor(119886)
            skillCommanderTutor = DynAccessor(119887)
            skillConcealment = DynAccessor(119888)
            skillDesignatedTarget = DynAccessor(119889)
            skillDriverMotorExpert = DynAccessor(119890)
            skillDriverRammingMaster = DynAccessor(119891)
            skillDriverReliablePlacement = DynAccessor(119892)
            skillEagleEye = DynAccessor(119893)
            skillEfficiency = DynAccessor(119894)
            skillFirefighting = DynAccessor(119895)
            skillGunnerArmorer = DynAccessor(119896)
            skillGunnerFocus = DynAccessor(119897)
            skillGunnerQuickAiming = DynAccessor(119898)
            skillIntuition = DynAccessor(119899)
            skillJackOfAllTrades = DynAccessor(119900)
            skillLoaderAmmunitionImprove = DynAccessor(119901)
            skillLoaderMelee = DynAccessor(119902)
            skillLoaderPerfectCharge = DynAccessor(119903)
            skillOffRoadDriving = DynAccessor(119904)
            skillPreventativeMaintenance = DynAccessor(119905)
            skillRadiomanExpert = DynAccessor(119906)
            skillRadiomanInterference = DynAccessor(119907)
            skillRadiomanSideBySide = DynAccessor(119908)
            skillRadiomanSignalInterception = DynAccessor(119909)
            skillRepairs = DynAccessor(119910)
            skillSafeStowage = DynAccessor(119911)
            skillSituationalAwareness = DynAccessor(119912)
            skillSixthSense = DynAccessor(119913)
            skillSmoothRide = DynAccessor(119914)
            skillSnapShot = DynAccessor(119915)
            skillSniper = DynAccessor(119916)
            skillUntrainedPenalty = DynAccessor(119917)
            statConcealment = DynAccessor(119918)
            statFirepower = DynAccessor(119919)
            statMobility = DynAccessor(119920)
            statSpotting = DynAccessor(119921)
            statSurvivability = DynAccessor(119922)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(119923)
        bomber = DynAccessor(119924)
        inspire = DynAccessor(119925)
        minefield = DynAccessor(119926)
        patrol = DynAccessor(119927)
        recon = DynAccessor(119928)
        resuply = DynAccessor(119929)
        sabotageSquad = DynAccessor(119930)
        smokeCloud = DynAccessor(119931)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(119932)
        style_ch1_lvl3 = DynAccessor(119933)
        style_ch1_lvl4 = DynAccessor(119934)
        style_ch2_lvl2 = DynAccessor(119935)
        style_ch2_lvl3 = DynAccessor(119936)
        style_ch2_lvl4 = DynAccessor(119937)
        style_ch3_lvl2 = DynAccessor(119938)
        style_ch3_lvl3 = DynAccessor(119939)
        style_ch3_lvl4 = DynAccessor(119940)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(119941)
                    bg_extra = DynAccessor(119942)
                    bg_extra_small = DynAccessor(119943)
                    bg_small = DynAccessor(119944)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(119945)
        clouds_1366 = DynAccessor(119946)
        clouds_1600 = DynAccessor(119947)
        clouds_1920 = DynAccessor(119948)
        clouds_2560 = DynAccessor(119949)
        spark_white = DynAccessor(119950)
        spark_yellow = DynAccessor(119951)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(119952)
        godRaysNew_130x130 = DynAccessor(119953)
        godRaysNew_1600x1600 = DynAccessor(119954)
        particles_280x170 = DynAccessor(119955)
        rankAnimation_first = DynAccessor(119956)
        rankAnimation_second = DynAccessor(119957)
        rankAnimation_third = DynAccessor(119958)
        yearly_style_fifth = DynAccessor(119959)
        yearly_style_fifth_loop = DynAccessor(119960)
        yearly_style_fourth = DynAccessor(119961)
        yearly_style_fourth_loop = DynAccessor(119962)
        yearly_style_sixth = DynAccessor(119963)
        yearly_style_sixth_loop = DynAccessor(119964)
        yearly_style_third = DynAccessor(119965)
        yearly_style_third_loop = DynAccessor(119966)
        yearly_styles = DynAccessor(119967)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(119968)
            veteran_frame_big = DynAccessor(119969)
            veteran_frame_small = DynAccessor(119970)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(119971)
        example_2 = DynAccessor(119972)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(119973)
        vehicle_sparks_2 = DynAccessor(119974)
        vehicle_sparks_3 = DynAccessor(119975)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(119976)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(119977)
        sparks_orange = DynAccessor(119978)

    flProgressionScreen = _flProgressionScreen()

    class _halloween(DynAccessor):
        __slots__ = ()

        class _artefacts(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(119979)
            bg_10 = DynAccessor(119980)
            bg_11 = DynAccessor(119981)
            bg_12 = DynAccessor(119982)
            bg_13 = DynAccessor(119983)
            bg_14 = DynAccessor(119984)
            bg_15 = DynAccessor(119985)
            bg_16 = DynAccessor(119986)
            bg_17 = DynAccessor(119987)
            bg_2 = DynAccessor(119988)
            bg_3 = DynAccessor(119989)
            bg_4 = DynAccessor(119990)
            bg_5 = DynAccessor(119991)
            bg_6 = DynAccessor(119992)
            bg_7 = DynAccessor(119993)
            bg_8 = DynAccessor(119994)
            bg_9 = DynAccessor(119995)
            bg_final = DynAccessor(119996)

        artefacts = _artefacts()
        king_reward = DynAccessor(119997)
        promo_loop = DynAccessor(119998)

    halloween = _halloween()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119999)
                    bg_medium = DynAccessor(120000)
                    bg_small = DynAccessor(120001)

                adaptive = _adaptive()
                bg_big = DynAccessor(120002)
                bg_medium = DynAccessor(120003)
                bg_small = DynAccessor(120004)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120005)
                    bg_medium = DynAccessor(120006)
                    bg_small = DynAccessor(120007)

                adaptive = _adaptive()
                bg_big = DynAccessor(120008)
                bg_medium = DynAccessor(120009)
                bg_small = DynAccessor(120010)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _HalloweenEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(120011)
                    bg_medium = DynAccessor(120012)
                    bg_small = DynAccessor(120013)

                adaptive = _adaptive()
                bg_big = DynAccessor(120014)
                bg_medium = DynAccessor(120015)
                bg_small = DynAccessor(120016)

            HalloweenEntryPoint = _HalloweenEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(120017)
            foreground_small = DynAccessor(120018)
            rays = DynAccessor(120019)

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
                        bronze_common = DynAccessor(120020)
                        bronze_rare = DynAccessor(120021)
                        gold_common = DynAccessor(120022)
                        gold_rare = DynAccessor(120023)
                        silver_common = DynAccessor(120024)
                        silver_rare = DynAccessor(120025)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120026)
                        epic_small = DynAccessor(120027)
                        rare = DynAccessor(120028)
                        rare_small = DynAccessor(120029)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120030)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(120031)
                            gold = DynAccessor(120032)
                            silver = DynAccessor(120033)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120034)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(120035)
                        rare = DynAccessor(120036)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120037)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120038)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120039)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120040)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(120041)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(120042)
                        rare = DynAccessor(120043)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(120044)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(120045)
                        epic_small = DynAccessor(120046)
                        rare = DynAccessor(120047)
                        rare_small = DynAccessor(120048)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120049)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120050)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120051)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(120052)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(120053)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(120054)
                    vehicles_29969 = DynAccessor(120055)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(120056)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            glow = DynAccessor(120057)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(120058)
            operation_10_stage_10 = DynAccessor(120059)
            operation_10_stage_5 = DynAccessor(120060)
            operation_10_stage_7 = DynAccessor(120061)
            operation_8_stage_1 = DynAccessor(120062)
            operation_8_stage_10 = DynAccessor(120063)
            operation_8_stage_5 = DynAccessor(120064)
            operation_8_stage_8 = DynAccessor(120065)
            operation_9_stage_1 = DynAccessor(120066)
            operation_9_stage_12 = DynAccessor(120067)
            operation_9_stage_5 = DynAccessor(120068)
            operation_9_stage_8 = DynAccessor(120069)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(120070)
            new_campaign_glow = DynAccessor(120071)
            new_campaign_sparks = DynAccessor(120072)
            smoke = DynAccessor(120073)
            sparks = DynAccessor(120074)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(120075)
            intro_op_10 = DynAccessor(120076)
            intro_op_8 = DynAccessor(120077)
            intro_op_9 = DynAccessor(120078)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(120079)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(120080)
            operation_8 = DynAccessor(120081)
            operation_9 = DynAccessor(120082)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(120083)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(120084)
        epic_victory_ribbon = DynAccessor(120085)
        no_epic_defeat_draw_ribbon = DynAccessor(120086)
        no_epic_victory_ribbon = DynAccessor(120087)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(120088)
        cycle_legendary = DynAccessor(120089)
        intro_epic = DynAccessor(120090)
        intro_legendary = DynAccessor(120091)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120092)
                single = DynAccessor(120093)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(120094)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120095)
                single = DynAccessor(120096)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(120097)
                single = DynAccessor(120098)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(120099)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(120100)
        bg_hw_m = DynAccessor(120101)
        bg_hw_s = DynAccessor(120102)
        unlock_72x72 = DynAccessor(120103)

    user_missions = _user_missions()