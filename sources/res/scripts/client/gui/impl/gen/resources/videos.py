from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(129431)
        bg_reward_screen = DynAccessor(129432)
        grade_change_particles = DynAccessor(129433)
        particles = DynAccessor(129434)
        up_particles = DynAccessor(129435)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(129436)
            crewCommander = DynAccessor(129437)
            crewDriver = DynAccessor(129438)
            crewGunner = DynAccessor(129439)
            crewLoader = DynAccessor(129440)
            crewRadioOperator = DynAccessor(129441)
            mentoringLicense = DynAccessor(129442)
            skillAdrenalineRush = DynAccessor(129443)
            skillAmbushMaster = DynAccessor(129444)
            skillArmorPatching = DynAccessor(129445)
            skillBattleTempered = DynAccessor(129446)
            skillBrothersInArms = DynAccessor(129447)
            skillBulletproof = DynAccessor(129448)
            skillClutchBraking = DynAccessor(129449)
            skillCommanderBonus = DynAccessor(129450)
            skillCommanderCoordination = DynAccessor(129451)
            skillCommanderEmergency = DynAccessor(129452)
            skillCommanderEnemyShotPredictor = DynAccessor(129453)
            skillCommanderPractical = DynAccessor(129454)
            skillCommanderTutor = DynAccessor(129455)
            skillConcealment = DynAccessor(129456)
            skillDesignatedTarget = DynAccessor(129457)
            skillDriverMotorExpert = DynAccessor(129458)
            skillDriverRammingMaster = DynAccessor(129459)
            skillDriverReliablePlacement = DynAccessor(129460)
            skillEagleEye = DynAccessor(129461)
            skillEfficiency = DynAccessor(129462)
            skillFirefighting = DynAccessor(129463)
            skillGunnerArmorer = DynAccessor(129464)
            skillGunnerFocus = DynAccessor(129465)
            skillGunnerLoneWolf = DynAccessor(129466)
            skillGunnerQuickAiming = DynAccessor(129467)
            skillHoldLine = DynAccessor(129468)
            skillIntuition = DynAccessor(129469)
            skillJackOfAllTrades = DynAccessor(129470)
            skillLoaderAmmunitionImprove = DynAccessor(129471)
            skillLoaderMelee = DynAccessor(129472)
            skillLoaderPerfectCharge = DynAccessor(129473)
            skillMagMastery = DynAccessor(129474)
            skillOffRoadDriving = DynAccessor(129475)
            skillPointBlast = DynAccessor(129476)
            skillPreventativeMaintenance = DynAccessor(129477)
            skillRadiomanExpert = DynAccessor(129478)
            skillRadiomanInterference = DynAccessor(129479)
            skillRadiomanSideBySide = DynAccessor(129480)
            skillRadiomanSignalInterception = DynAccessor(129481)
            skillRepairs = DynAccessor(129482)
            skillSafeStowage = DynAccessor(129483)
            skillSecondChance = DynAccessor(129484)
            skillSituationalAwareness = DynAccessor(129485)
            skillSixthSense = DynAccessor(129486)
            skillSmoothRide = DynAccessor(129487)
            skillSnapShot = DynAccessor(129488)
            skillSniper = DynAccessor(129489)
            skillStaySharp = DynAccessor(129490)
            skillSuspensionRepair = DynAccessor(129491)
            skillThreatSearch = DynAccessor(129492)
            skillUntrainedPenalty = DynAccessor(129493)
            statConcealment = DynAccessor(129494)
            statFirepower = DynAccessor(129495)
            statMobility = DynAccessor(129496)
            statSpotting = DynAccessor(129497)
            statSurvivability = DynAccessor(129498)

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
                                bg_big = DynAccessor(129499)
                                bg_medium = DynAccessor(129500)
                                bg_small = DynAccessor(129501)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(129502)
                            bg_medium = DynAccessor(129503)
                            bg_small = DynAccessor(129504)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(129505)
        bomber = DynAccessor(129506)
        inspire = DynAccessor(129507)
        minefield = DynAccessor(129508)
        patrol = DynAccessor(129509)
        recon = DynAccessor(129510)
        resuply = DynAccessor(129511)
        sabotageSquad = DynAccessor(129512)
        smokeCloud = DynAccessor(129513)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(129514)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129515)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129516)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129517)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129518)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129519)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129520)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129521)

            c_193 = _c_193()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(129522)
        style_ch1_lvl3 = DynAccessor(129523)
        style_ch1_lvl4 = DynAccessor(129524)
        style_ch2_lvl2 = DynAccessor(129525)
        style_ch2_lvl3 = DynAccessor(129526)
        style_ch2_lvl4 = DynAccessor(129527)
        style_ch3_lvl2 = DynAccessor(129528)
        style_ch3_lvl3 = DynAccessor(129529)
        style_ch3_lvl4 = DynAccessor(129530)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(129531)
                    bg_small = DynAccessor(129532)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(129533)
                    bg_small = DynAccessor(129534)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(129535)
                    bg_small = DynAccessor(129536)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(129537)
        clouds_1366 = DynAccessor(129538)
        clouds_1600 = DynAccessor(129539)
        clouds_1920 = DynAccessor(129540)
        clouds_2560 = DynAccessor(129541)
        spark_white = DynAccessor(129542)
        spark_yellow = DynAccessor(129543)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(129544)
        godRaysNew_130x130 = DynAccessor(129545)
        godRaysNew_1600x1600 = DynAccessor(129546)
        no_epic_defeat_draw_ribbon = DynAccessor(129547)
        no_epic_victory_ribbon = DynAccessor(129548)
        rankAnimation_first = DynAccessor(129549)
        rankAnimation_second = DynAccessor(129550)
        rankAnimation_third = DynAccessor(129551)
        speech = DynAccessor(129552)
        yearly_style_fifth = DynAccessor(129553)
        yearly_style_fifth_loop = DynAccessor(129554)
        yearly_style_fourth = DynAccessor(129555)
        yearly_style_fourth_loop = DynAccessor(129556)
        yearly_style_sixth = DynAccessor(129557)
        yearly_style_sixth_loop = DynAccessor(129558)
        yearly_style_third = DynAccessor(129559)
        yearly_style_third_loop = DynAccessor(129560)
        yearly_styles = DynAccessor(129561)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(129562)
            veteran_frame_big = DynAccessor(129563)
            veteran_frame_small = DynAccessor(129564)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(129565)
        example_2 = DynAccessor(129566)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(129567)
        vehicle_sparks_2 = DynAccessor(129568)
        vehicle_sparks_3 = DynAccessor(129569)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(129570)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(129571)
        sparks_orange = DynAccessor(129572)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129573)
                    bg_medium = DynAccessor(129574)
                    bg_small = DynAccessor(129575)

                adaptive = _adaptive()
                bg_big = DynAccessor(129576)
                bg_medium = DynAccessor(129577)
                bg_small = DynAccessor(129578)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129579)
                    bg_medium = DynAccessor(129580)
                    bg_small = DynAccessor(129581)

                adaptive = _adaptive()
                bg_big = DynAccessor(129582)
                bg_medium = DynAccessor(129583)
                bg_small = DynAccessor(129584)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129585)
                    bg_medium = DynAccessor(129586)
                    bg_small = DynAccessor(129587)

                adaptive = _adaptive()
                bg_big = DynAccessor(129588)
                bg_medium = DynAccessor(129589)
                bg_small = DynAccessor(129590)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129591)
                    bg_medium = DynAccessor(129592)
                    bg_small = DynAccessor(129593)

                adaptive = _adaptive()
                bg_big = DynAccessor(129594)
                bg_medium = DynAccessor(129595)
                bg_small = DynAccessor(129596)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(129597)
            foreground_small = DynAccessor(129598)
            rays = DynAccessor(129599)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(129600)
            bg_2 = DynAccessor(129601)
            bg_3 = DynAccessor(129602)
            bg_4 = DynAccessor(129603)

        quants = _quants()
        rays = DynAccessor(129604)
        slide_overlay = DynAccessor(129605)

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
                        bronze_common = DynAccessor(129606)
                        bronze_rare = DynAccessor(129607)
                        gold_common = DynAccessor(129608)
                        gold_rare = DynAccessor(129609)
                        silver_common = DynAccessor(129610)
                        silver_rare = DynAccessor(129611)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(129612)
                        epic_small = DynAccessor(129613)
                        rare = DynAccessor(129614)
                        rare_small = DynAccessor(129615)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129616)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(129617)
                            gold = DynAccessor(129618)
                            silver = DynAccessor(129619)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(129620)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(129621)
                        rare = DynAccessor(129622)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129623)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129624)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129625)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(129626)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(129627)
                    compensationParticles = DynAccessor(129628)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(129629)
                        rare = DynAccessor(129630)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(129631)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(129632)
                        epic_small = DynAccessor(129633)
                        rare = DynAccessor(129634)
                        rare_small = DynAccessor(129635)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(129636)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129637)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129638)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129639)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129640)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(129641)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(129642)
                    vehicles_29969 = DynAccessor(129643)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(129644)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(129645)
            glow = DynAccessor(129646)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(129647)
            operation_10_stage_10 = DynAccessor(129648)
            operation_10_stage_5 = DynAccessor(129649)
            operation_10_stage_7 = DynAccessor(129650)
            operation_8_stage_1 = DynAccessor(129651)
            operation_8_stage_10 = DynAccessor(129652)
            operation_8_stage_5 = DynAccessor(129653)
            operation_8_stage_8 = DynAccessor(129654)
            operation_9_stage_1 = DynAccessor(129655)
            operation_9_stage_12 = DynAccessor(129656)
            operation_9_stage_5 = DynAccessor(129657)
            operation_9_stage_8 = DynAccessor(129658)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(129659)
            new_campaign_glow = DynAccessor(129660)
            new_campaign_sparks = DynAccessor(129661)
            smoke = DynAccessor(129662)
            sparks = DynAccessor(129663)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(129664)
            intro_op_10 = DynAccessor(129665)
            intro_op_8 = DynAccessor(129666)
            intro_op_9 = DynAccessor(129667)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(129668)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(129669)
            operation_8 = DynAccessor(129670)
            operation_9 = DynAccessor(129671)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(129672)
        pet_rays = DynAccessor(129673)
        synergy_blick = DynAccessor(129674)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(129675)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(129676)
        epic_victory_ribbon = DynAccessor(129677)
        no_epic_defeat_draw_ribbon = DynAccessor(129678)
        no_epic_victory_ribbon = DynAccessor(129679)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(129680)
        cycle_legendary = DynAccessor(129681)
        intro_epic = DynAccessor(129682)
        intro_legendary = DynAccessor(129683)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129684)
                single = DynAccessor(129685)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(129686)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129687)
                single = DynAccessor(129688)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129689)
                single = DynAccessor(129690)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(129691)
            icon_bg_effect = DynAccessor(129692)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(129693)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(129694)
        icon_bg_effect = DynAccessor(129695)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(129696)
        bg_hw_m = DynAccessor(129697)
        bg_hw_s = DynAccessor(129698)
        unlock_72x72 = DynAccessor(129699)

    user_missions = _user_missions()