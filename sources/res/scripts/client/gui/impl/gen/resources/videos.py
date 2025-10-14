from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(119514)
        grade_change_particles = DynAccessor(119515)
        particles = DynAccessor(119516)
        up_particles = DynAccessor(119517)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(119518)
            crewCommander = DynAccessor(119519)
            crewDriver = DynAccessor(119520)
            crewGunner = DynAccessor(119521)
            crewLoader = DynAccessor(119522)
            crewRadioOperator = DynAccessor(119523)
            mentoringLicense = DynAccessor(119524)
            skillAdrenalineRush = DynAccessor(119525)
            skillAmbushMaster = DynAccessor(119526)
            skillBrothersInArms = DynAccessor(119527)
            skillClutchBraking = DynAccessor(119528)
            skillCommanderBonus = DynAccessor(119529)
            skillCommanderCoordination = DynAccessor(119530)
            skillCommanderEmergency = DynAccessor(119531)
            skillCommanderEnemyShotPredictor = DynAccessor(119532)
            skillCommanderPractical = DynAccessor(119533)
            skillCommanderTutor = DynAccessor(119534)
            skillConcealment = DynAccessor(119535)
            skillDesignatedTarget = DynAccessor(119536)
            skillDriverMotorExpert = DynAccessor(119537)
            skillDriverRammingMaster = DynAccessor(119538)
            skillDriverReliablePlacement = DynAccessor(119539)
            skillEagleEye = DynAccessor(119540)
            skillEfficiency = DynAccessor(119541)
            skillFirefighting = DynAccessor(119542)
            skillGunnerArmorer = DynAccessor(119543)
            skillGunnerFocus = DynAccessor(119544)
            skillGunnerQuickAiming = DynAccessor(119545)
            skillIntuition = DynAccessor(119546)
            skillJackOfAllTrades = DynAccessor(119547)
            skillLoaderAmmunitionImprove = DynAccessor(119548)
            skillLoaderMelee = DynAccessor(119549)
            skillLoaderPerfectCharge = DynAccessor(119550)
            skillOffRoadDriving = DynAccessor(119551)
            skillPreventativeMaintenance = DynAccessor(119552)
            skillRadiomanExpert = DynAccessor(119553)
            skillRadiomanInterference = DynAccessor(119554)
            skillRadiomanSideBySide = DynAccessor(119555)
            skillRadiomanSignalInterception = DynAccessor(119556)
            skillRepairs = DynAccessor(119557)
            skillSafeStowage = DynAccessor(119558)
            skillSituationalAwareness = DynAccessor(119559)
            skillSixthSense = DynAccessor(119560)
            skillSmoothRide = DynAccessor(119561)
            skillSnapShot = DynAccessor(119562)
            skillSniper = DynAccessor(119563)
            skillUntrainedPenalty = DynAccessor(119564)
            statConcealment = DynAccessor(119565)
            statFirepower = DynAccessor(119566)
            statMobility = DynAccessor(119567)
            statSpotting = DynAccessor(119568)
            statSurvivability = DynAccessor(119569)

        advancedHints = _advancedHints()

    animations = _animations()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(119570)
        bomber = DynAccessor(119571)
        inspire = DynAccessor(119572)
        minefield = DynAccessor(119573)
        patrol = DynAccessor(119574)
        recon = DynAccessor(119575)
        resuply = DynAccessor(119576)
        sabotageSquad = DynAccessor(119577)
        smokeCloud = DynAccessor(119578)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        style_ch1_lvl2 = DynAccessor(119579)
        style_ch1_lvl3 = DynAccessor(119580)
        style_ch1_lvl4 = DynAccessor(119581)
        style_ch2_lvl2 = DynAccessor(119582)
        style_ch2_lvl3 = DynAccessor(119583)
        style_ch2_lvl4 = DynAccessor(119584)
        style_ch3_lvl2 = DynAccessor(119585)
        style_ch3_lvl3 = DynAccessor(119586)
        style_ch3_lvl4 = DynAccessor(119587)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(119588)
                    bg_small = DynAccessor(119589)

                season_18 = _season_18()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(119590)
        clouds_1366 = DynAccessor(119591)
        clouds_1600 = DynAccessor(119592)
        clouds_1920 = DynAccessor(119593)
        clouds_2560 = DynAccessor(119594)
        spark_white = DynAccessor(119595)
        spark_yellow = DynAccessor(119596)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(119597)
        godRaysNew_130x130 = DynAccessor(119598)
        godRaysNew_1600x1600 = DynAccessor(119599)
        particles_280x170 = DynAccessor(119600)
        rankAnimation_first = DynAccessor(119601)
        rankAnimation_second = DynAccessor(119602)
        rankAnimation_third = DynAccessor(119603)
        yearly_style_fifth = DynAccessor(119604)
        yearly_style_fifth_loop = DynAccessor(119605)
        yearly_style_fourth = DynAccessor(119606)
        yearly_style_fourth_loop = DynAccessor(119607)
        yearly_style_sixth = DynAccessor(119608)
        yearly_style_sixth_loop = DynAccessor(119609)
        yearly_style_third = DynAccessor(119610)
        yearly_style_third_loop = DynAccessor(119611)
        yearly_styles = DynAccessor(119612)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(119613)
            veteran_frame_big = DynAccessor(119614)
            veteran_frame_small = DynAccessor(119615)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(119616)
        example_2 = DynAccessor(119617)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(119618)
        vehicle_sparks_2 = DynAccessor(119619)
        vehicle_sparks_3 = DynAccessor(119620)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(119621)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(119622)
        sparks_orange = DynAccessor(119623)

    flProgressionScreen = _flProgressionScreen()

    class _halloween(DynAccessor):
        __slots__ = ()

        class _artefacts(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(119624)
            bg_10 = DynAccessor(119625)
            bg_11 = DynAccessor(119626)
            bg_12 = DynAccessor(119627)
            bg_13 = DynAccessor(119628)
            bg_14 = DynAccessor(119629)
            bg_15 = DynAccessor(119630)
            bg_16 = DynAccessor(119631)
            bg_17 = DynAccessor(119632)
            bg_2 = DynAccessor(119633)
            bg_3 = DynAccessor(119634)
            bg_4 = DynAccessor(119635)
            bg_5 = DynAccessor(119636)
            bg_6 = DynAccessor(119637)
            bg_7 = DynAccessor(119638)
            bg_8 = DynAccessor(119639)
            bg_9 = DynAccessor(119640)
            bg_final = DynAccessor(119641)

        artefacts = _artefacts()
        king_reward = DynAccessor(119642)
        promo_loop = DynAccessor(119643)

    halloween = _halloween()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119644)
                    bg_medium = DynAccessor(119645)
                    bg_small = DynAccessor(119646)

                adaptive = _adaptive()
                bg_big = DynAccessor(119647)
                bg_medium = DynAccessor(119648)
                bg_small = DynAccessor(119649)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119650)
                    bg_medium = DynAccessor(119651)
                    bg_small = DynAccessor(119652)

                adaptive = _adaptive()
                bg_big = DynAccessor(119653)
                bg_medium = DynAccessor(119654)
                bg_small = DynAccessor(119655)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _HalloweenEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(119656)
                    bg_medium = DynAccessor(119657)
                    bg_small = DynAccessor(119658)

                adaptive = _adaptive()
                bg_big = DynAccessor(119659)
                bg_medium = DynAccessor(119660)
                bg_small = DynAccessor(119661)

            HalloweenEntryPoint = _HalloweenEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(119662)
            foreground_small = DynAccessor(119663)
            rays = DynAccessor(119664)

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
                        bronze_common = DynAccessor(119665)
                        bronze_rare = DynAccessor(119666)
                        gold_common = DynAccessor(119667)
                        gold_rare = DynAccessor(119668)
                        silver_common = DynAccessor(119669)
                        silver_rare = DynAccessor(119670)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119671)
                        epic_small = DynAccessor(119672)
                        rare = DynAccessor(119673)
                        rare_small = DynAccessor(119674)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119675)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(119676)
                            gold = DynAccessor(119677)
                            silver = DynAccessor(119678)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119679)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119680)
                        rare = DynAccessor(119681)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119682)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119683)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119684)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119685)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(119686)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(119687)
                        rare = DynAccessor(119688)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(119689)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(119690)
                        epic_small = DynAccessor(119691)
                        rare = DynAccessor(119692)
                        rare_small = DynAccessor(119693)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119694)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119695)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119696)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(119697)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(119698)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119699)
                    vehicles_29969 = DynAccessor(119700)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(119701)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(119702)
            operation_10_stage_10 = DynAccessor(119703)
            operation_10_stage_5 = DynAccessor(119704)
            operation_10_stage_7 = DynAccessor(119705)
            operation_8_stage_1 = DynAccessor(119706)
            operation_8_stage_10 = DynAccessor(119707)
            operation_8_stage_5 = DynAccessor(119708)
            operation_8_stage_8 = DynAccessor(119709)
            operation_9_stage_1 = DynAccessor(119710)
            operation_9_stage_12 = DynAccessor(119711)
            operation_9_stage_5 = DynAccessor(119712)
            operation_9_stage_8 = DynAccessor(119713)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(119714)
            new_campaign_glow = DynAccessor(119715)
            new_campaign_sparks = DynAccessor(119716)
            smoke = DynAccessor(119717)
            sparks = DynAccessor(119718)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(119719)
            intro_op_10 = DynAccessor(119720)
            intro_op_8 = DynAccessor(119721)
            intro_op_9 = DynAccessor(119722)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(119723)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(119724)
            operation_8 = DynAccessor(119725)
            operation_9 = DynAccessor(119726)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(119727)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(119728)
        epic_victory_ribbon = DynAccessor(119729)
        no_epic_defeat_draw_ribbon = DynAccessor(119730)
        no_epic_victory_ribbon = DynAccessor(119731)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(119732)
        cycle_legendary = DynAccessor(119733)
        intro_epic = DynAccessor(119734)
        intro_legendary = DynAccessor(119735)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119736)
                single = DynAccessor(119737)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(119738)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119739)
                single = DynAccessor(119740)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(119741)
                single = DynAccessor(119742)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(119743)

    story_mode = _story_mode()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(119744)
        bg_hw_m = DynAccessor(119745)
        bg_hw_s = DynAccessor(119746)
        unlock_72x72 = DynAccessor(119747)

    user_missions = _user_missions()