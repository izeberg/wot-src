from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(128742)
        bg_reward_screen = DynAccessor(128743)
        grade_change_particles = DynAccessor(128744)
        particles = DynAccessor(128745)
        up_particles = DynAccessor(128746)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(128747)
            crewCommander = DynAccessor(128748)
            crewDriver = DynAccessor(128749)
            crewGunner = DynAccessor(128750)
            crewLoader = DynAccessor(128751)
            crewRadioOperator = DynAccessor(128752)
            mentoringLicense = DynAccessor(128753)
            skillAdrenalineRush = DynAccessor(128754)
            skillAmbushMaster = DynAccessor(128755)
            skillArmorPatching = DynAccessor(128756)
            skillBattleTempered = DynAccessor(128757)
            skillBrothersInArms = DynAccessor(128758)
            skillBulletproof = DynAccessor(128759)
            skillClutchBraking = DynAccessor(128760)
            skillCommanderBonus = DynAccessor(128761)
            skillCommanderCoordination = DynAccessor(128762)
            skillCommanderEmergency = DynAccessor(128763)
            skillCommanderEnemyShotPredictor = DynAccessor(128764)
            skillCommanderPractical = DynAccessor(128765)
            skillCommanderTutor = DynAccessor(128766)
            skillConcealment = DynAccessor(128767)
            skillDesignatedTarget = DynAccessor(128768)
            skillDriverMotorExpert = DynAccessor(128769)
            skillDriverRammingMaster = DynAccessor(128770)
            skillDriverReliablePlacement = DynAccessor(128771)
            skillEagleEye = DynAccessor(128772)
            skillEfficiency = DynAccessor(128773)
            skillFirefighting = DynAccessor(128774)
            skillGunnerArmorer = DynAccessor(128775)
            skillGunnerFocus = DynAccessor(128776)
            skillGunnerLoneWolf = DynAccessor(128777)
            skillGunnerQuickAiming = DynAccessor(128778)
            skillHoldLine = DynAccessor(128779)
            skillIntuition = DynAccessor(128780)
            skillJackOfAllTrades = DynAccessor(128781)
            skillLoaderAmmunitionImprove = DynAccessor(128782)
            skillLoaderMelee = DynAccessor(128783)
            skillLoaderPerfectCharge = DynAccessor(128784)
            skillMagMastery = DynAccessor(128785)
            skillOffRoadDriving = DynAccessor(128786)
            skillPointBlast = DynAccessor(128787)
            skillPreventativeMaintenance = DynAccessor(128788)
            skillRadiomanExpert = DynAccessor(128789)
            skillRadiomanInterference = DynAccessor(128790)
            skillRadiomanSideBySide = DynAccessor(128791)
            skillRadiomanSignalInterception = DynAccessor(128792)
            skillRepairs = DynAccessor(128793)
            skillSafeStowage = DynAccessor(128794)
            skillSecondChance = DynAccessor(128795)
            skillSituationalAwareness = DynAccessor(128796)
            skillSixthSense = DynAccessor(128797)
            skillSmoothRide = DynAccessor(128798)
            skillSnapShot = DynAccessor(128799)
            skillSniper = DynAccessor(128800)
            skillStaySharp = DynAccessor(128801)
            skillSuspensionRepair = DynAccessor(128802)
            skillThreatSearch = DynAccessor(128803)
            skillUntrainedPenalty = DynAccessor(128804)
            statConcealment = DynAccessor(128805)
            statFirepower = DynAccessor(128806)
            statMobility = DynAccessor(128807)
            statSpotting = DynAccessor(128808)
            statSurvivability = DynAccessor(128809)

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
                                bg_big = DynAccessor(128810)
                                bg_medium = DynAccessor(128811)
                                bg_small = DynAccessor(128812)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(128813)
                            bg_medium = DynAccessor(128814)
                            bg_small = DynAccessor(128815)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(128816)
        bomber = DynAccessor(128817)
        inspire = DynAccessor(128818)
        minefield = DynAccessor(128819)
        patrol = DynAccessor(128820)
        recon = DynAccessor(128821)
        resuply = DynAccessor(128822)
        sabotageSquad = DynAccessor(128823)
        smokeCloud = DynAccessor(128824)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(128825)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128826)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128827)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128828)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128829)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128830)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128831)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128832)

            c_193 = _c_193()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128833)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128834)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128835)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128836)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(128837)
        style_ch1_lvl3 = DynAccessor(128838)
        style_ch1_lvl4 = DynAccessor(128839)
        style_ch2_lvl2 = DynAccessor(128840)
        style_ch2_lvl3 = DynAccessor(128841)
        style_ch2_lvl4 = DynAccessor(128842)
        style_ch3_lvl2 = DynAccessor(128843)
        style_ch3_lvl3 = DynAccessor(128844)
        style_ch3_lvl4 = DynAccessor(128845)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(128846)
                    bg_small = DynAccessor(128847)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(128848)
                    bg_small = DynAccessor(128849)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(128850)
        clouds_1366 = DynAccessor(128851)
        clouds_1600 = DynAccessor(128852)
        clouds_1920 = DynAccessor(128853)
        clouds_2560 = DynAccessor(128854)
        spark_white = DynAccessor(128855)
        spark_yellow = DynAccessor(128856)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(128857)
        godRaysNew_130x130 = DynAccessor(128858)
        godRaysNew_1600x1600 = DynAccessor(128859)
        no_epic_defeat_draw_ribbon = DynAccessor(128860)
        no_epic_victory_ribbon = DynAccessor(128861)
        rankAnimation_first = DynAccessor(128862)
        rankAnimation_second = DynAccessor(128863)
        rankAnimation_third = DynAccessor(128864)
        speech = DynAccessor(128865)
        yearly_style_fifth = DynAccessor(128866)
        yearly_style_fifth_loop = DynAccessor(128867)
        yearly_style_fourth = DynAccessor(128868)
        yearly_style_fourth_loop = DynAccessor(128869)
        yearly_style_sixth = DynAccessor(128870)
        yearly_style_sixth_loop = DynAccessor(128871)
        yearly_style_third = DynAccessor(128872)
        yearly_style_third_loop = DynAccessor(128873)
        yearly_styles = DynAccessor(128874)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(128875)
            veteran_frame_big = DynAccessor(128876)
            veteran_frame_small = DynAccessor(128877)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(128878)
        example_2 = DynAccessor(128879)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(128880)
        vehicle_sparks_2 = DynAccessor(128881)
        vehicle_sparks_3 = DynAccessor(128882)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(128883)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(128884)
        sparks_orange = DynAccessor(128885)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128886)
                    bg_medium = DynAccessor(128887)
                    bg_small = DynAccessor(128888)

                adaptive = _adaptive()
                bg_big = DynAccessor(128889)
                bg_medium = DynAccessor(128890)
                bg_small = DynAccessor(128891)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128892)
                    bg_medium = DynAccessor(128893)
                    bg_small = DynAccessor(128894)

                adaptive = _adaptive()
                bg_big = DynAccessor(128895)
                bg_medium = DynAccessor(128896)
                bg_small = DynAccessor(128897)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128898)
                    bg_medium = DynAccessor(128899)
                    bg_small = DynAccessor(128900)

                adaptive = _adaptive()
                bg_big = DynAccessor(128901)
                bg_medium = DynAccessor(128902)
                bg_small = DynAccessor(128903)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128904)
                    bg_medium = DynAccessor(128905)
                    bg_small = DynAccessor(128906)

                adaptive = _adaptive()
                bg_big = DynAccessor(128907)
                bg_medium = DynAccessor(128908)
                bg_small = DynAccessor(128909)

            StPatrickEntryPoint = _StPatrickEntryPoint()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(128910)
            foreground_small = DynAccessor(128911)
            rays = DynAccessor(128912)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(128913)
            bg_2 = DynAccessor(128914)
            bg_3 = DynAccessor(128915)
            bg_4 = DynAccessor(128916)

        quants = _quants()
        rays = DynAccessor(128917)
        slide_overlay = DynAccessor(128918)

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
                        bronze_common = DynAccessor(128919)
                        bronze_rare = DynAccessor(128920)
                        gold_common = DynAccessor(128921)
                        gold_rare = DynAccessor(128922)
                        silver_common = DynAccessor(128923)
                        silver_rare = DynAccessor(128924)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(128925)
                        epic_small = DynAccessor(128926)
                        rare = DynAccessor(128927)
                        rare_small = DynAccessor(128928)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128929)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(128930)
                            gold = DynAccessor(128931)
                            silver = DynAccessor(128932)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128933)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(128934)
                        rare = DynAccessor(128935)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128936)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128937)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128938)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128939)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(128940)
                    compensationParticles = DynAccessor(128941)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(128942)
                        rare = DynAccessor(128943)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(128944)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(128945)
                        epic_small = DynAccessor(128946)
                        rare = DynAccessor(128947)
                        rare_small = DynAccessor(128948)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(128949)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128950)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128951)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128952)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128953)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128954)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(128955)
                    vehicles_29969 = DynAccessor(128956)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(128957)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(128958)
            glow = DynAccessor(128959)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(128960)
            operation_10_stage_10 = DynAccessor(128961)
            operation_10_stage_5 = DynAccessor(128962)
            operation_10_stage_7 = DynAccessor(128963)
            operation_8_stage_1 = DynAccessor(128964)
            operation_8_stage_10 = DynAccessor(128965)
            operation_8_stage_5 = DynAccessor(128966)
            operation_8_stage_8 = DynAccessor(128967)
            operation_9_stage_1 = DynAccessor(128968)
            operation_9_stage_12 = DynAccessor(128969)
            operation_9_stage_5 = DynAccessor(128970)
            operation_9_stage_8 = DynAccessor(128971)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(128972)
            new_campaign_glow = DynAccessor(128973)
            new_campaign_sparks = DynAccessor(128974)
            smoke = DynAccessor(128975)
            sparks = DynAccessor(128976)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(128977)
            intro_op_10 = DynAccessor(128978)
            intro_op_8 = DynAccessor(128979)
            intro_op_9 = DynAccessor(128980)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(128981)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(128982)
            operation_8 = DynAccessor(128983)
            operation_9 = DynAccessor(128984)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(128985)
        pet_rays = DynAccessor(128986)
        synergy_blick = DynAccessor(128987)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(128988)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(128989)
        epic_victory_ribbon = DynAccessor(128990)
        no_epic_defeat_draw_ribbon = DynAccessor(128991)
        no_epic_victory_ribbon = DynAccessor(128992)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(128993)
        cycle_legendary = DynAccessor(128994)
        intro_epic = DynAccessor(128995)
        intro_legendary = DynAccessor(128996)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(128997)
                single = DynAccessor(128998)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(128999)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129000)
                single = DynAccessor(129001)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129002)
                single = DynAccessor(129003)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(129004)
            icon_bg_effect = DynAccessor(129005)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(129006)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(129007)
        icon_bg_effect = DynAccessor(129008)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(129009)
        bg_hw_m = DynAccessor(129010)
        bg_hw_s = DynAccessor(129011)
        unlock_72x72 = DynAccessor(129012)

    user_missions = _user_missions()