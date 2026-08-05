from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(130178)
        bg_reward_screen = DynAccessor(130179)
        grade_change_particles = DynAccessor(130180)
        particles = DynAccessor(130181)
        up_particles = DynAccessor(130182)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(130183)
            crewCommander = DynAccessor(130184)
            crewDriver = DynAccessor(130185)
            crewGunner = DynAccessor(130186)
            crewLoader = DynAccessor(130187)
            crewRadioOperator = DynAccessor(130188)
            mentoringLicense = DynAccessor(130189)
            skillAdrenalineRush = DynAccessor(130190)
            skillAmbushMaster = DynAccessor(130191)
            skillArmorPatching = DynAccessor(130192)
            skillBattleTempered = DynAccessor(130193)
            skillBrothersInArms = DynAccessor(130194)
            skillBulletproof = DynAccessor(130195)
            skillClutchBraking = DynAccessor(130196)
            skillCommanderBonus = DynAccessor(130197)
            skillCommanderCoordination = DynAccessor(130198)
            skillCommanderEmergency = DynAccessor(130199)
            skillCommanderEnemyShotPredictor = DynAccessor(130200)
            skillCommanderPractical = DynAccessor(130201)
            skillCommanderTutor = DynAccessor(130202)
            skillConcealment = DynAccessor(130203)
            skillDesignatedTarget = DynAccessor(130204)
            skillDriverMotorExpert = DynAccessor(130205)
            skillDriverRammingMaster = DynAccessor(130206)
            skillDriverReliablePlacement = DynAccessor(130207)
            skillEagleEye = DynAccessor(130208)
            skillEfficiency = DynAccessor(130209)
            skillFirefighting = DynAccessor(130210)
            skillGunnerArmorer = DynAccessor(130211)
            skillGunnerFocus = DynAccessor(130212)
            skillGunnerLoneWolf = DynAccessor(130213)
            skillGunnerQuickAiming = DynAccessor(130214)
            skillHoldLine = DynAccessor(130215)
            skillIntuition = DynAccessor(130216)
            skillJackOfAllTrades = DynAccessor(130217)
            skillLoaderAmmunitionImprove = DynAccessor(130218)
            skillLoaderMelee = DynAccessor(130219)
            skillLoaderPerfectCharge = DynAccessor(130220)
            skillMagMastery = DynAccessor(130221)
            skillOffRoadDriving = DynAccessor(130222)
            skillPointBlast = DynAccessor(130223)
            skillPreventativeMaintenance = DynAccessor(130224)
            skillRadiomanExpert = DynAccessor(130225)
            skillRadiomanInterference = DynAccessor(130226)
            skillRadiomanSideBySide = DynAccessor(130227)
            skillRadiomanSignalInterception = DynAccessor(130228)
            skillRepairs = DynAccessor(130229)
            skillSafeStowage = DynAccessor(130230)
            skillSecondChance = DynAccessor(130231)
            skillSituationalAwareness = DynAccessor(130232)
            skillSixthSense = DynAccessor(130233)
            skillSmoothRide = DynAccessor(130234)
            skillSnapShot = DynAccessor(130235)
            skillSniper = DynAccessor(130236)
            skillStaySharp = DynAccessor(130237)
            skillSuspensionRepair = DynAccessor(130238)
            skillThreatSearch = DynAccessor(130239)
            skillUntrainedPenalty = DynAccessor(130240)
            statConcealment = DynAccessor(130241)
            statFirepower = DynAccessor(130242)
            statMobility = DynAccessor(130243)
            statSpotting = DynAccessor(130244)
            statSurvivability = DynAccessor(130245)

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
                                bg_big = DynAccessor(130246)
                                bg_medium = DynAccessor(130247)
                                bg_small = DynAccessor(130248)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(130249)
                            bg_medium = DynAccessor(130250)
                            bg_small = DynAccessor(130251)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(130252)
        bomber = DynAccessor(130253)
        inspire = DynAccessor(130254)
        minefield = DynAccessor(130255)
        patrol = DynAccessor(130256)
        recon = DynAccessor(130257)
        resuply = DynAccessor(130258)
        sabotageSquad = DynAccessor(130259)
        smokeCloud = DynAccessor(130260)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(130261)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130262)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130263)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130264)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130265)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130266)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130267)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130268)

            c_193 = _c_193()

            class _c_205(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(130269)

            c_205 = _c_205()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(130270)
        style_ch1_lvl3 = DynAccessor(130271)
        style_ch1_lvl4 = DynAccessor(130272)
        style_ch2_lvl2 = DynAccessor(130273)
        style_ch2_lvl3 = DynAccessor(130274)
        style_ch2_lvl4 = DynAccessor(130275)
        style_ch3_lvl2 = DynAccessor(130276)
        style_ch3_lvl3 = DynAccessor(130277)
        style_ch3_lvl4 = DynAccessor(130278)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130279)
                    bg_small = DynAccessor(130280)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130281)
                    bg_small = DynAccessor(130282)

                season_19 = _season_19()

                class _season_20(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(130283)
                    bg_small = DynAccessor(130284)

                season_20 = _season_20()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(130285)
        clouds_1366 = DynAccessor(130286)
        clouds_1600 = DynAccessor(130287)
        clouds_1920 = DynAccessor(130288)
        clouds_2560 = DynAccessor(130289)
        spark_white = DynAccessor(130290)
        spark_yellow = DynAccessor(130291)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(130292)
        godRaysNew_130x130 = DynAccessor(130293)
        godRaysNew_1600x1600 = DynAccessor(130294)
        no_epic_defeat_draw_ribbon = DynAccessor(130295)
        no_epic_victory_ribbon = DynAccessor(130296)
        rankAnimation_first = DynAccessor(130297)
        rankAnimation_second = DynAccessor(130298)
        rankAnimation_third = DynAccessor(130299)
        speech = DynAccessor(130300)
        yearly_style_fifth = DynAccessor(130301)
        yearly_style_fifth_loop = DynAccessor(130302)
        yearly_style_fourth = DynAccessor(130303)
        yearly_style_fourth_loop = DynAccessor(130304)
        yearly_style_sixth = DynAccessor(130305)
        yearly_style_sixth_loop = DynAccessor(130306)
        yearly_style_third = DynAccessor(130307)
        yearly_style_third_loop = DynAccessor(130308)
        yearly_styles = DynAccessor(130309)

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()
        no_epic_defeat_draw_ribbon = DynAccessor(130310)
        no_epic_victory_ribbon = DynAccessor(130311)

    comp7_light = _comp7_light()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(130312)
            veteran_frame_big = DynAccessor(130313)
            veteran_frame_small = DynAccessor(130314)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(130315)
        example_2 = DynAccessor(130316)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(130317)
        vehicle_sparks_2 = DynAccessor(130318)
        vehicle_sparks_3 = DynAccessor(130319)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(130320)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(130321)
        sparks_orange = DynAccessor(130322)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130323)
                    bg_medium = DynAccessor(130324)
                    bg_small = DynAccessor(130325)

                adaptive = _adaptive()
                bg_big = DynAccessor(130326)
                bg_medium = DynAccessor(130327)
                bg_small = DynAccessor(130328)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130329)
                    bg_medium = DynAccessor(130330)
                    bg_small = DynAccessor(130331)

                adaptive = _adaptive()
                bg_big = DynAccessor(130332)
                bg_medium = DynAccessor(130333)
                bg_small = DynAccessor(130334)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130335)
                    bg_medium = DynAccessor(130336)
                    bg_small = DynAccessor(130337)

                adaptive = _adaptive()
                bg_big = DynAccessor(130338)
                bg_medium = DynAccessor(130339)
                bg_small = DynAccessor(130340)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(130341)
                    bg_medium = DynAccessor(130342)
                    bg_small = DynAccessor(130343)

                adaptive = _adaptive()
                bg_big = DynAccessor(130344)
                bg_medium = DynAccessor(130345)
                bg_small = DynAccessor(130346)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(130347)
            foreground_small = DynAccessor(130348)
            rays = DynAccessor(130349)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()
        rays = DynAccessor(130350)
        slide_overlay = DynAccessor(130351)

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
                        bronze_common = DynAccessor(130352)
                        bronze_rare = DynAccessor(130353)
                        gold_common = DynAccessor(130354)
                        gold_rare = DynAccessor(130355)
                        silver_common = DynAccessor(130356)
                        silver_rare = DynAccessor(130357)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(130358)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130359)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(130360)
                            gold = DynAccessor(130361)
                            silver = DynAccessor(130362)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130363)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(130364)
                        rare = DynAccessor(130365)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130366)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130367)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130368)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130369)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(130370)
                    compensationParticles = DynAccessor(130371)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(130372)
                        rare = DynAccessor(130373)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(130374)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(130375)
                        epic_small = DynAccessor(130376)
                        rare = DynAccessor(130377)
                        rare_small = DynAccessor(130378)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _common(DynAccessor):
                    __slots__ = ()

                    class _shield(DynAccessor):
                        __slots__ = ()
                        glowM = DynAccessor(130379)
                        glowS = DynAccessor(130380)

                    shield = _shield()

                common = _common()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(130381)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130382)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130383)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130384)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(130385)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(130386)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(130387)
                    vehicles_29969 = DynAccessor(130388)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(130389)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(130390)
            glow = DynAccessor(130391)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(130392)
            operation_10_stage_10 = DynAccessor(130393)
            operation_10_stage_5 = DynAccessor(130394)
            operation_10_stage_7 = DynAccessor(130395)
            operation_8_stage_1 = DynAccessor(130396)
            operation_8_stage_10 = DynAccessor(130397)
            operation_8_stage_5 = DynAccessor(130398)
            operation_8_stage_8 = DynAccessor(130399)
            operation_9_stage_1 = DynAccessor(130400)
            operation_9_stage_12 = DynAccessor(130401)
            operation_9_stage_5 = DynAccessor(130402)
            operation_9_stage_8 = DynAccessor(130403)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(130404)
            new_campaign_glow = DynAccessor(130405)
            new_campaign_sparks = DynAccessor(130406)
            smoke = DynAccessor(130407)
            sparks = DynAccessor(130408)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(130409)
            intro_op_10 = DynAccessor(130410)
            intro_op_8 = DynAccessor(130411)
            intro_op_9 = DynAccessor(130412)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(130413)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(130414)
            operation_8 = DynAccessor(130415)
            operation_9 = DynAccessor(130416)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(130417)
        pet_rays = DynAccessor(130418)
        synergy_blick = DynAccessor(130419)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(130420)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(130421)
        epic_victory_ribbon = DynAccessor(130422)
        no_epic_defeat_draw_ribbon = DynAccessor(130423)
        no_epic_victory_ribbon = DynAccessor(130424)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(130425)
        cycle_legendary = DynAccessor(130426)
        intro_epic = DynAccessor(130427)
        intro_legendary = DynAccessor(130428)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130429)
                single = DynAccessor(130430)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(130431)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130432)
                single = DynAccessor(130433)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(130434)
                single = DynAccessor(130435)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(130436)
            icon_bg_effect = DynAccessor(130437)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(130438)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(130439)
        icon_bg_effect = DynAccessor(130440)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(130441)
        bg_hw_m = DynAccessor(130442)
        bg_hw_s = DynAccessor(130443)
        unlock_72x72 = DynAccessor(130444)

    user_missions = _user_missions()