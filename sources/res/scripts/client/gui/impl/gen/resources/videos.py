from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(125358)
        bg_reward_screen = DynAccessor(125359)
        grade_change_particles = DynAccessor(125360)
        particles = DynAccessor(125361)
        up_particles = DynAccessor(125362)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(125363)
            crewCommander = DynAccessor(125364)
            crewDriver = DynAccessor(125365)
            crewGunner = DynAccessor(125366)
            crewLoader = DynAccessor(125367)
            crewRadioOperator = DynAccessor(125368)
            mentoringLicense = DynAccessor(125369)
            skillAdrenalineRush = DynAccessor(125370)
            skillAmbushMaster = DynAccessor(125371)
            skillArmorPatching = DynAccessor(125372)
            skillBattleTempered = DynAccessor(125373)
            skillBrothersInArms = DynAccessor(125374)
            skillBulletproof = DynAccessor(125375)
            skillClutchBraking = DynAccessor(125376)
            skillCommanderBonus = DynAccessor(125377)
            skillCommanderCoordination = DynAccessor(125378)
            skillCommanderEmergency = DynAccessor(125379)
            skillCommanderEnemyShotPredictor = DynAccessor(125380)
            skillCommanderPractical = DynAccessor(125381)
            skillCommanderTutor = DynAccessor(125382)
            skillConcealment = DynAccessor(125383)
            skillDesignatedTarget = DynAccessor(125384)
            skillDriverMotorExpert = DynAccessor(125385)
            skillDriverRammingMaster = DynAccessor(125386)
            skillDriverReliablePlacement = DynAccessor(125387)
            skillEagleEye = DynAccessor(125388)
            skillEfficiency = DynAccessor(125389)
            skillFirefighting = DynAccessor(125390)
            skillGunnerArmorer = DynAccessor(125391)
            skillGunnerFocus = DynAccessor(125392)
            skillGunnerLoneWolf = DynAccessor(125393)
            skillGunnerQuickAiming = DynAccessor(125394)
            skillHoldLine = DynAccessor(125395)
            skillIntuition = DynAccessor(125396)
            skillJackOfAllTrades = DynAccessor(125397)
            skillLoaderAmmunitionImprove = DynAccessor(125398)
            skillLoaderMelee = DynAccessor(125399)
            skillLoaderPerfectCharge = DynAccessor(125400)
            skillMagMastery = DynAccessor(125401)
            skillOffRoadDriving = DynAccessor(125402)
            skillPointBlast = DynAccessor(125403)
            skillPreventativeMaintenance = DynAccessor(125404)
            skillRadiomanExpert = DynAccessor(125405)
            skillRadiomanInterference = DynAccessor(125406)
            skillRadiomanSideBySide = DynAccessor(125407)
            skillRadiomanSignalInterception = DynAccessor(125408)
            skillRepairs = DynAccessor(125409)
            skillSafeStowage = DynAccessor(125410)
            skillSecondChance = DynAccessor(125411)
            skillSituationalAwareness = DynAccessor(125412)
            skillSixthSense = DynAccessor(125413)
            skillSmoothRide = DynAccessor(125414)
            skillSnapShot = DynAccessor(125415)
            skillSniper = DynAccessor(125416)
            skillStaySharp = DynAccessor(125417)
            skillSuspensionRepair = DynAccessor(125418)
            skillThreatSearch = DynAccessor(125419)
            skillUntrainedPenalty = DynAccessor(125420)
            statConcealment = DynAccessor(125421)
            statFirepower = DynAccessor(125422)
            statMobility = DynAccessor(125423)
            statSpotting = DynAccessor(125424)
            statSurvivability = DynAccessor(125425)

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
                                bg_big = DynAccessor(125426)
                                bg_medium = DynAccessor(125427)
                                bg_small = DynAccessor(125428)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(125429)
                            bg_medium = DynAccessor(125430)
                            bg_small = DynAccessor(125431)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(125432)
        bomber = DynAccessor(125433)
        inspire = DynAccessor(125434)
        minefield = DynAccessor(125435)
        patrol = DynAccessor(125436)
        recon = DynAccessor(125437)
        resuply = DynAccessor(125438)
        sabotageSquad = DynAccessor(125439)
        smokeCloud = DynAccessor(125440)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(125441)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125442)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125443)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125444)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125445)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125446)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125447)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125448)

            c_193 = _c_193()

            class _c_194(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125449)

            c_194 = _c_194()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125450)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125451)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125452)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(125453)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(125454)
        style_ch1_lvl3 = DynAccessor(125455)
        style_ch1_lvl4 = DynAccessor(125456)
        style_ch2_lvl2 = DynAccessor(125457)
        style_ch2_lvl3 = DynAccessor(125458)
        style_ch2_lvl4 = DynAccessor(125459)
        style_ch3_lvl2 = DynAccessor(125460)
        style_ch3_lvl3 = DynAccessor(125461)
        style_ch3_lvl4 = DynAccessor(125462)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125463)
                    bg_small = DynAccessor(125464)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(125465)
                    bg_small = DynAccessor(125466)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(125467)
        clouds_1366 = DynAccessor(125468)
        clouds_1600 = DynAccessor(125469)
        clouds_1920 = DynAccessor(125470)
        clouds_2560 = DynAccessor(125471)
        spark_white = DynAccessor(125472)
        spark_yellow = DynAccessor(125473)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(125474)
        godRaysNew_130x130 = DynAccessor(125475)
        godRaysNew_1600x1600 = DynAccessor(125476)
        rankAnimation_first = DynAccessor(125477)
        rankAnimation_second = DynAccessor(125478)
        rankAnimation_third = DynAccessor(125479)
        yearly_style_fifth = DynAccessor(125480)
        yearly_style_fifth_loop = DynAccessor(125481)
        yearly_style_fourth = DynAccessor(125482)
        yearly_style_fourth_loop = DynAccessor(125483)
        yearly_style_sixth = DynAccessor(125484)
        yearly_style_sixth_loop = DynAccessor(125485)
        yearly_style_third = DynAccessor(125486)
        yearly_style_third_loop = DynAccessor(125487)
        yearly_styles = DynAccessor(125488)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(125489)
            veteran_frame_big = DynAccessor(125490)
            veteran_frame_small = DynAccessor(125491)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(125492)
        example_2 = DynAccessor(125493)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(125494)
        vehicle_sparks_2 = DynAccessor(125495)
        vehicle_sparks_3 = DynAccessor(125496)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(125497)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(125498)
        sparks_orange = DynAccessor(125499)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125500)
                    bg_medium = DynAccessor(125501)
                    bg_small = DynAccessor(125502)

                adaptive = _adaptive()
                bg_big = DynAccessor(125503)
                bg_medium = DynAccessor(125504)
                bg_small = DynAccessor(125505)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(125506)
                    bg_medium = DynAccessor(125507)
                    bg_small = DynAccessor(125508)

                adaptive = _adaptive()
                bg_big = DynAccessor(125509)
                bg_medium = DynAccessor(125510)
                bg_small = DynAccessor(125511)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
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

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(125518)
            foreground_small = DynAccessor(125519)
            rays = DynAccessor(125520)

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
                        bronze_common = DynAccessor(125521)
                        bronze_rare = DynAccessor(125522)
                        gold_common = DynAccessor(125523)
                        gold_rare = DynAccessor(125524)
                        silver_common = DynAccessor(125525)
                        silver_rare = DynAccessor(125526)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125527)
                        epic_small = DynAccessor(125528)
                        rare = DynAccessor(125529)
                        rare_small = DynAccessor(125530)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125531)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(125532)
                            gold = DynAccessor(125533)
                            silver = DynAccessor(125534)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125535)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125536)
                        rare = DynAccessor(125537)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125538)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125539)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125540)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125541)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(125542)
                    compensationParticles = DynAccessor(125543)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125544)
                        rare = DynAccessor(125545)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125546)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125547)
                        epic_small = DynAccessor(125548)
                        rare = DynAccessor(125549)
                        rare_small = DynAccessor(125550)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125551)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125552)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125553)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125554)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125555)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125556)

                noBoxesView = _noBoxesView()

            default = _default()

            class _stPatrick(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(125557)
                        rare = DynAccessor(125558)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(125559)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(125560)
                        epic_small = DynAccessor(125561)
                        rare = DynAccessor(125562)
                        rare_small = DynAccessor(125563)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(125564)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125565)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125566)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125567)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(125568)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(125569)

                noBoxesView = _noBoxesView()

            stPatrick = _stPatrick()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125570)
                    vehicles_29969 = DynAccessor(125571)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(125572)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(125573)
            operation_10_stage_10 = DynAccessor(125574)
            operation_10_stage_5 = DynAccessor(125575)
            operation_10_stage_7 = DynAccessor(125576)
            operation_8_stage_1 = DynAccessor(125577)
            operation_8_stage_10 = DynAccessor(125578)
            operation_8_stage_5 = DynAccessor(125579)
            operation_8_stage_8 = DynAccessor(125580)
            operation_9_stage_1 = DynAccessor(125581)
            operation_9_stage_12 = DynAccessor(125582)
            operation_9_stage_5 = DynAccessor(125583)
            operation_9_stage_8 = DynAccessor(125584)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(125585)
            new_campaign_glow = DynAccessor(125586)
            new_campaign_sparks = DynAccessor(125587)
            smoke = DynAccessor(125588)
            sparks = DynAccessor(125589)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(125590)
            intro_op_10 = DynAccessor(125591)
            intro_op_8 = DynAccessor(125592)
            intro_op_9 = DynAccessor(125593)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(125594)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(125595)
            operation_8 = DynAccessor(125596)
            operation_9 = DynAccessor(125597)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(125598)
        pet_rays = DynAccessor(125599)
        synergy_blick = DynAccessor(125600)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(125601)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(125602)
        epic_victory_ribbon = DynAccessor(125603)
        no_epic_defeat_draw_ribbon = DynAccessor(125604)
        no_epic_victory_ribbon = DynAccessor(125605)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(125606)
        cycle_legendary = DynAccessor(125607)
        intro_epic = DynAccessor(125608)
        intro_legendary = DynAccessor(125609)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125610)
                single = DynAccessor(125611)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(125612)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125613)
                single = DynAccessor(125614)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(125615)
                single = DynAccessor(125616)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(125617)
            icon_bg_effect = DynAccessor(125618)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(125619)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(125620)
        icon_bg_effect = DynAccessor(125621)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(125622)
        bg_hw_m = DynAccessor(125623)
        bg_hw_s = DynAccessor(125624)
        unlock_72x72 = DynAccessor(125625)

    user_missions = _user_missions()