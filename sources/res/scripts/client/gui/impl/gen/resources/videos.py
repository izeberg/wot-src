from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(125444)
        bg_reward_screen = DynAccessor(125445)
        grade_change_particles = DynAccessor(125446)
        particles = DynAccessor(125447)
        up_particles = DynAccessor(125448)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(125449)
            crewCommander = DynAccessor(125450)
            crewDriver = DynAccessor(125451)
            crewGunner = DynAccessor(125452)
            crewLoader = DynAccessor(125453)
            crewRadioOperator = DynAccessor(125454)
            mentoringLicense = DynAccessor(125455)
            skillAdrenalineRush = DynAccessor(125456)
            skillAmbushMaster = DynAccessor(125457)
            skillArmorPatching = DynAccessor(125458)
            skillBattleTempered = DynAccessor(125459)
            skillBrothersInArms = DynAccessor(125460)
            skillBulletproof = DynAccessor(125461)
            skillClutchBraking = DynAccessor(125462)
            skillCommanderBonus = DynAccessor(125463)
            skillCommanderCoordination = DynAccessor(125464)
            skillCommanderEmergency = DynAccessor(125465)
            skillCommanderEnemyShotPredictor = DynAccessor(125466)
            skillCommanderPractical = DynAccessor(125467)
            skillCommanderTutor = DynAccessor(125468)
            skillConcealment = DynAccessor(125469)
            skillDesignatedTarget = DynAccessor(125470)
            skillDriverMotorExpert = DynAccessor(125471)
            skillDriverRammingMaster = DynAccessor(125472)
            skillDriverReliablePlacement = DynAccessor(125473)
            skillEagleEye = DynAccessor(125474)
            skillEfficiency = DynAccessor(125475)
            skillFirefighting = DynAccessor(125476)
            skillGunnerArmorer = DynAccessor(125477)
            skillGunnerFocus = DynAccessor(125478)
            skillGunnerLoneWolf = DynAccessor(125479)
            skillGunnerQuickAiming = DynAccessor(125480)
            skillHoldLine = DynAccessor(125481)
            skillIntuition = DynAccessor(125482)
            skillJackOfAllTrades = DynAccessor(125483)
            skillLoaderAmmunitionImprove = DynAccessor(125484)
            skillLoaderMelee = DynAccessor(125485)
            skillLoaderPerfectCharge = DynAccessor(125486)
            skillMagMastery = DynAccessor(125487)
            skillOffRoadDriving = DynAccessor(125488)
            skillPointBlast = DynAccessor(125489)
            skillPreventativeMaintenance = DynAccessor(125490)
            skillRadiomanExpert = DynAccessor(125491)
            skillRadiomanInterference = DynAccessor(125492)
            skillRadiomanSideBySide = DynAccessor(125493)
            skillRadiomanSignalInterception = DynAccessor(125494)
            skillRepairs = DynAccessor(125495)
            skillSafeStowage = DynAccessor(125496)
            skillSecondChance = DynAccessor(125497)
            skillSituationalAwareness = DynAccessor(125498)
            skillSixthSense = DynAccessor(125499)
            skillSmoothRide = DynAccessor(125500)
            skillSnapShot = DynAccessor(125501)
            skillSniper = DynAccessor(125502)
            skillStaySharp = DynAccessor(125503)
            skillSuspensionRepair = DynAccessor(125504)
            skillThreatSearch = DynAccessor(125505)
            skillUntrainedPenalty = DynAccessor(125506)
            statConcealment = DynAccessor(125507)
            statFirepower = DynAccessor(125508)
            statMobility = DynAccessor(125509)
            statSpotting = DynAccessor(125510)
            statSurvivability = DynAccessor(125511)

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
                                bg_big = DynAccessor(125512)
                                bg_medium = DynAccessor(125513)
                                bg_small = DynAccessor(125514)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(125515)
                            bg_medium = DynAccessor(125516)
                            bg_small = DynAccessor(125517)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(125518)
        bomber = DynAccessor(125519)
        inspire = DynAccessor(125520)
        minefield = DynAccessor(125521)
        patrol = DynAccessor(125522)
        recon = DynAccessor(125523)
        resuply = DynAccessor(125524)
        sabotageSquad = DynAccessor(125525)
        smokeCloud = DynAccessor(125526)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(125527)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125528)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125529)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125530)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125531)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125532)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125533)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125534)

            c_193 = _c_193()

            class _c_194(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125535)

            c_194 = _c_194()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125536)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125537)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125538)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125539)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(125540)
        style_ch1_lvl3 = DynAccessor(125541)
        style_ch1_lvl4 = DynAccessor(125542)
        style_ch2_lvl2 = DynAccessor(125543)
        style_ch2_lvl3 = DynAccessor(125544)
        style_ch2_lvl4 = DynAccessor(125545)
        style_ch3_lvl2 = DynAccessor(125546)
        style_ch3_lvl3 = DynAccessor(125547)
        style_ch3_lvl4 = DynAccessor(125548)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125549)
                    bg_small = DynAccessor(125550)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125551)
                    bg_small = DynAccessor(125552)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(125553)
        clouds_1366 = DynAccessor(125554)
        clouds_1600 = DynAccessor(125555)
        clouds_1920 = DynAccessor(125556)
        clouds_2560 = DynAccessor(125557)
        spark_white = DynAccessor(125558)
        spark_yellow = DynAccessor(125559)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(125560)
        godRaysNew_130x130 = DynAccessor(125561)
        godRaysNew_1600x1600 = DynAccessor(125562)
        rankAnimation_first = DynAccessor(125563)
        rankAnimation_second = DynAccessor(125564)
        rankAnimation_third = DynAccessor(125565)
        yearly_style_fifth = DynAccessor(125566)
        yearly_style_fifth_loop = DynAccessor(125567)
        yearly_style_fourth = DynAccessor(125568)
        yearly_style_fourth_loop = DynAccessor(125569)
        yearly_style_sixth = DynAccessor(125570)
        yearly_style_sixth_loop = DynAccessor(125571)
        yearly_style_third = DynAccessor(125572)
        yearly_style_third_loop = DynAccessor(125573)
        yearly_styles = DynAccessor(125574)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(125575)
            veteran_frame_big = DynAccessor(125576)
            veteran_frame_small = DynAccessor(125577)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(125578)
        example_2 = DynAccessor(125579)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(125580)
        vehicle_sparks_2 = DynAccessor(125581)
        vehicle_sparks_3 = DynAccessor(125582)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(125583)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(125584)
        sparks_orange = DynAccessor(125585)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125586)
                    bg_medium = DynAccessor(125587)
                    bg_small = DynAccessor(125588)

                adaptive = _adaptive()
                bg_big = DynAccessor(125589)
                bg_medium = DynAccessor(125590)
                bg_small = DynAccessor(125591)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125592)
                    bg_medium = DynAccessor(125593)
                    bg_small = DynAccessor(125594)

                adaptive = _adaptive()
                bg_big = DynAccessor(125595)
                bg_medium = DynAccessor(125596)
                bg_small = DynAccessor(125597)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125598)
                    bg_medium = DynAccessor(125599)
                    bg_small = DynAccessor(125600)

                adaptive = _adaptive()
                bg_big = DynAccessor(125601)
                bg_medium = DynAccessor(125602)
                bg_small = DynAccessor(125603)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(125604)
            foreground_small = DynAccessor(125605)
            rays = DynAccessor(125606)

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
                        bronze_common = DynAccessor(125607)
                        bronze_rare = DynAccessor(125608)
                        gold_common = DynAccessor(125609)
                        gold_rare = DynAccessor(125610)
                        silver_common = DynAccessor(125611)
                        silver_rare = DynAccessor(125612)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125613)
                        epic_small = DynAccessor(125614)
                        rare = DynAccessor(125615)
                        rare_small = DynAccessor(125616)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125617)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(125618)
                            gold = DynAccessor(125619)
                            silver = DynAccessor(125620)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125621)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125622)
                        rare = DynAccessor(125623)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125624)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125625)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125626)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125627)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(125628)
                    compensationParticles = DynAccessor(125629)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125630)
                        rare = DynAccessor(125631)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125632)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125633)
                        epic_small = DynAccessor(125634)
                        rare = DynAccessor(125635)
                        rare_small = DynAccessor(125636)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125637)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125638)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125639)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125640)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125641)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125642)

                noBoxesView = _noBoxesView()

            default = _default()

            class _stPatrick(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125643)
                        rare = DynAccessor(125644)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125645)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125646)
                        epic_small = DynAccessor(125647)
                        rare = DynAccessor(125648)
                        rare_small = DynAccessor(125649)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125650)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125651)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125652)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125653)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125654)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125655)

                noBoxesView = _noBoxesView()

            stPatrick = _stPatrick()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125656)
                    vehicles_29969 = DynAccessor(125657)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125658)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(125659)
            operation_10_stage_10 = DynAccessor(125660)
            operation_10_stage_5 = DynAccessor(125661)
            operation_10_stage_7 = DynAccessor(125662)
            operation_8_stage_1 = DynAccessor(125663)
            operation_8_stage_10 = DynAccessor(125664)
            operation_8_stage_5 = DynAccessor(125665)
            operation_8_stage_8 = DynAccessor(125666)
            operation_9_stage_1 = DynAccessor(125667)
            operation_9_stage_12 = DynAccessor(125668)
            operation_9_stage_5 = DynAccessor(125669)
            operation_9_stage_8 = DynAccessor(125670)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(125671)
            new_campaign_glow = DynAccessor(125672)
            new_campaign_sparks = DynAccessor(125673)
            smoke = DynAccessor(125674)
            sparks = DynAccessor(125675)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(125676)
            intro_op_10 = DynAccessor(125677)
            intro_op_8 = DynAccessor(125678)
            intro_op_9 = DynAccessor(125679)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(125680)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(125681)
            operation_8 = DynAccessor(125682)
            operation_9 = DynAccessor(125683)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(125684)
        pet_rays = DynAccessor(125685)
        synergy_blick = DynAccessor(125686)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(125687)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(125688)
        epic_victory_ribbon = DynAccessor(125689)
        no_epic_defeat_draw_ribbon = DynAccessor(125690)
        no_epic_victory_ribbon = DynAccessor(125691)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(125692)
        cycle_legendary = DynAccessor(125693)
        intro_epic = DynAccessor(125694)
        intro_legendary = DynAccessor(125695)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125696)
                single = DynAccessor(125697)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(125698)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125699)
                single = DynAccessor(125700)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125701)
                single = DynAccessor(125702)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(125703)
            icon_bg_effect = DynAccessor(125704)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(125705)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(125706)
        icon_bg_effect = DynAccessor(125707)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(125708)
        bg_hw_m = DynAccessor(125709)
        bg_hw_s = DynAccessor(125710)
        unlock_72x72 = DynAccessor(125711)

    user_missions = _user_missions()