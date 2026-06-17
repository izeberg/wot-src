from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(129441)
        bg_reward_screen = DynAccessor(129442)
        grade_change_particles = DynAccessor(129443)
        particles = DynAccessor(129444)
        up_particles = DynAccessor(129445)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(129446)
            crewCommander = DynAccessor(129447)
            crewDriver = DynAccessor(129448)
            crewGunner = DynAccessor(129449)
            crewLoader = DynAccessor(129450)
            crewRadioOperator = DynAccessor(129451)
            mentoringLicense = DynAccessor(129452)
            skillAdrenalineRush = DynAccessor(129453)
            skillAmbushMaster = DynAccessor(129454)
            skillArmorPatching = DynAccessor(129455)
            skillBattleTempered = DynAccessor(129456)
            skillBrothersInArms = DynAccessor(129457)
            skillBulletproof = DynAccessor(129458)
            skillClutchBraking = DynAccessor(129459)
            skillCommanderBonus = DynAccessor(129460)
            skillCommanderCoordination = DynAccessor(129461)
            skillCommanderEmergency = DynAccessor(129462)
            skillCommanderEnemyShotPredictor = DynAccessor(129463)
            skillCommanderPractical = DynAccessor(129464)
            skillCommanderTutor = DynAccessor(129465)
            skillConcealment = DynAccessor(129466)
            skillDesignatedTarget = DynAccessor(129467)
            skillDriverMotorExpert = DynAccessor(129468)
            skillDriverRammingMaster = DynAccessor(129469)
            skillDriverReliablePlacement = DynAccessor(129470)
            skillEagleEye = DynAccessor(129471)
            skillEfficiency = DynAccessor(129472)
            skillFirefighting = DynAccessor(129473)
            skillGunnerArmorer = DynAccessor(129474)
            skillGunnerFocus = DynAccessor(129475)
            skillGunnerLoneWolf = DynAccessor(129476)
            skillGunnerQuickAiming = DynAccessor(129477)
            skillHoldLine = DynAccessor(129478)
            skillIntuition = DynAccessor(129479)
            skillJackOfAllTrades = DynAccessor(129480)
            skillLoaderAmmunitionImprove = DynAccessor(129481)
            skillLoaderMelee = DynAccessor(129482)
            skillLoaderPerfectCharge = DynAccessor(129483)
            skillMagMastery = DynAccessor(129484)
            skillOffRoadDriving = DynAccessor(129485)
            skillPointBlast = DynAccessor(129486)
            skillPreventativeMaintenance = DynAccessor(129487)
            skillRadiomanExpert = DynAccessor(129488)
            skillRadiomanInterference = DynAccessor(129489)
            skillRadiomanSideBySide = DynAccessor(129490)
            skillRadiomanSignalInterception = DynAccessor(129491)
            skillRepairs = DynAccessor(129492)
            skillSafeStowage = DynAccessor(129493)
            skillSecondChance = DynAccessor(129494)
            skillSituationalAwareness = DynAccessor(129495)
            skillSixthSense = DynAccessor(129496)
            skillSmoothRide = DynAccessor(129497)
            skillSnapShot = DynAccessor(129498)
            skillSniper = DynAccessor(129499)
            skillStaySharp = DynAccessor(129500)
            skillSuspensionRepair = DynAccessor(129501)
            skillThreatSearch = DynAccessor(129502)
            skillUntrainedPenalty = DynAccessor(129503)
            statConcealment = DynAccessor(129504)
            statFirepower = DynAccessor(129505)
            statMobility = DynAccessor(129506)
            statSpotting = DynAccessor(129507)
            statSurvivability = DynAccessor(129508)

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
                                bg_big = DynAccessor(129509)
                                bg_medium = DynAccessor(129510)
                                bg_small = DynAccessor(129511)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(129512)
                            bg_medium = DynAccessor(129513)
                            bg_small = DynAccessor(129514)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(129515)
        bomber = DynAccessor(129516)
        inspire = DynAccessor(129517)
        minefield = DynAccessor(129518)
        patrol = DynAccessor(129519)
        recon = DynAccessor(129520)
        resuply = DynAccessor(129521)
        sabotageSquad = DynAccessor(129522)
        smokeCloud = DynAccessor(129523)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(129524)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129525)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129526)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129527)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129528)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129529)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129530)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(129531)

            c_193 = _c_193()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(129532)
        style_ch1_lvl3 = DynAccessor(129533)
        style_ch1_lvl4 = DynAccessor(129534)
        style_ch2_lvl2 = DynAccessor(129535)
        style_ch2_lvl3 = DynAccessor(129536)
        style_ch2_lvl4 = DynAccessor(129537)
        style_ch3_lvl2 = DynAccessor(129538)
        style_ch3_lvl3 = DynAccessor(129539)
        style_ch3_lvl4 = DynAccessor(129540)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(129541)
                    bg_small = DynAccessor(129542)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(129543)
                    bg_small = DynAccessor(129544)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(129545)
                    bg_small = DynAccessor(129546)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(129547)
        clouds_1366 = DynAccessor(129548)
        clouds_1600 = DynAccessor(129549)
        clouds_1920 = DynAccessor(129550)
        clouds_2560 = DynAccessor(129551)
        spark_white = DynAccessor(129552)
        spark_yellow = DynAccessor(129553)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(129554)
        godRaysNew_130x130 = DynAccessor(129555)
        godRaysNew_1600x1600 = DynAccessor(129556)
        no_epic_defeat_draw_ribbon = DynAccessor(129557)
        no_epic_victory_ribbon = DynAccessor(129558)
        rankAnimation_first = DynAccessor(129559)
        rankAnimation_second = DynAccessor(129560)
        rankAnimation_third = DynAccessor(129561)
        speech = DynAccessor(129562)
        yearly_style_fifth = DynAccessor(129563)
        yearly_style_fifth_loop = DynAccessor(129564)
        yearly_style_fourth = DynAccessor(129565)
        yearly_style_fourth_loop = DynAccessor(129566)
        yearly_style_sixth = DynAccessor(129567)
        yearly_style_sixth_loop = DynAccessor(129568)
        yearly_style_third = DynAccessor(129569)
        yearly_style_third_loop = DynAccessor(129570)
        yearly_styles = DynAccessor(129571)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(129572)
            veteran_frame_big = DynAccessor(129573)
            veteran_frame_small = DynAccessor(129574)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(129575)
        example_2 = DynAccessor(129576)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(129577)
        vehicle_sparks_2 = DynAccessor(129578)
        vehicle_sparks_3 = DynAccessor(129579)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(129580)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(129581)
        sparks_orange = DynAccessor(129582)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129583)
                    bg_medium = DynAccessor(129584)
                    bg_small = DynAccessor(129585)

                adaptive = _adaptive()
                bg_big = DynAccessor(129586)
                bg_medium = DynAccessor(129587)
                bg_small = DynAccessor(129588)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129589)
                    bg_medium = DynAccessor(129590)
                    bg_small = DynAccessor(129591)

                adaptive = _adaptive()
                bg_big = DynAccessor(129592)
                bg_medium = DynAccessor(129593)
                bg_small = DynAccessor(129594)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129595)
                    bg_medium = DynAccessor(129596)
                    bg_small = DynAccessor(129597)

                adaptive = _adaptive()
                bg_big = DynAccessor(129598)
                bg_medium = DynAccessor(129599)
                bg_small = DynAccessor(129600)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(129601)
                    bg_medium = DynAccessor(129602)
                    bg_small = DynAccessor(129603)

                adaptive = _adaptive()
                bg_big = DynAccessor(129604)
                bg_medium = DynAccessor(129605)
                bg_small = DynAccessor(129606)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(129607)
            foreground_small = DynAccessor(129608)
            rays = DynAccessor(129609)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(129610)
            bg_2 = DynAccessor(129611)
            bg_3 = DynAccessor(129612)
            bg_4 = DynAccessor(129613)

        quants = _quants()
        rays = DynAccessor(129614)
        slide_overlay = DynAccessor(129615)

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
                        bronze_common = DynAccessor(129616)
                        bronze_rare = DynAccessor(129617)
                        gold_common = DynAccessor(129618)
                        gold_rare = DynAccessor(129619)
                        silver_common = DynAccessor(129620)
                        silver_rare = DynAccessor(129621)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(129622)
                        epic_small = DynAccessor(129623)
                        rare = DynAccessor(129624)
                        rare_small = DynAccessor(129625)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129626)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(129627)
                            gold = DynAccessor(129628)
                            silver = DynAccessor(129629)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(129630)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(129631)
                        rare = DynAccessor(129632)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129633)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129634)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129635)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(129636)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(129637)
                    compensationParticles = DynAccessor(129638)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(129639)
                        rare = DynAccessor(129640)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(129641)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(129642)
                        epic_small = DynAccessor(129643)
                        rare = DynAccessor(129644)
                        rare_small = DynAccessor(129645)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(129646)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129647)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129648)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129649)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(129650)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(129651)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(129652)
                    vehicles_29969 = DynAccessor(129653)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(129654)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(129655)
            glow = DynAccessor(129656)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(129657)
            operation_10_stage_10 = DynAccessor(129658)
            operation_10_stage_5 = DynAccessor(129659)
            operation_10_stage_7 = DynAccessor(129660)
            operation_8_stage_1 = DynAccessor(129661)
            operation_8_stage_10 = DynAccessor(129662)
            operation_8_stage_5 = DynAccessor(129663)
            operation_8_stage_8 = DynAccessor(129664)
            operation_9_stage_1 = DynAccessor(129665)
            operation_9_stage_12 = DynAccessor(129666)
            operation_9_stage_5 = DynAccessor(129667)
            operation_9_stage_8 = DynAccessor(129668)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(129669)
            new_campaign_glow = DynAccessor(129670)
            new_campaign_sparks = DynAccessor(129671)
            smoke = DynAccessor(129672)
            sparks = DynAccessor(129673)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(129674)
            intro_op_10 = DynAccessor(129675)
            intro_op_8 = DynAccessor(129676)
            intro_op_9 = DynAccessor(129677)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(129678)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(129679)
            operation_8 = DynAccessor(129680)
            operation_9 = DynAccessor(129681)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(129682)
        pet_rays = DynAccessor(129683)
        synergy_blick = DynAccessor(129684)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(129685)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(129686)
        epic_victory_ribbon = DynAccessor(129687)
        no_epic_defeat_draw_ribbon = DynAccessor(129688)
        no_epic_victory_ribbon = DynAccessor(129689)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(129690)
        cycle_legendary = DynAccessor(129691)
        intro_epic = DynAccessor(129692)
        intro_legendary = DynAccessor(129693)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129694)
                single = DynAccessor(129695)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(129696)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129697)
                single = DynAccessor(129698)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129699)
                single = DynAccessor(129700)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(129701)
            icon_bg_effect = DynAccessor(129702)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(129703)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(129704)
        icon_bg_effect = DynAccessor(129705)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(129706)
        bg_hw_m = DynAccessor(129707)
        bg_hw_s = DynAccessor(129708)
        unlock_72x72 = DynAccessor(129709)

    user_missions = _user_missions()