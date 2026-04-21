from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(128740)
        bg_reward_screen = DynAccessor(128741)
        grade_change_particles = DynAccessor(128742)
        particles = DynAccessor(128743)
        up_particles = DynAccessor(128744)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(128745)
            crewCommander = DynAccessor(128746)
            crewDriver = DynAccessor(128747)
            crewGunner = DynAccessor(128748)
            crewLoader = DynAccessor(128749)
            crewRadioOperator = DynAccessor(128750)
            mentoringLicense = DynAccessor(128751)
            skillAdrenalineRush = DynAccessor(128752)
            skillAmbushMaster = DynAccessor(128753)
            skillArmorPatching = DynAccessor(128754)
            skillBattleTempered = DynAccessor(128755)
            skillBrothersInArms = DynAccessor(128756)
            skillBulletproof = DynAccessor(128757)
            skillClutchBraking = DynAccessor(128758)
            skillCommanderBonus = DynAccessor(128759)
            skillCommanderCoordination = DynAccessor(128760)
            skillCommanderEmergency = DynAccessor(128761)
            skillCommanderEnemyShotPredictor = DynAccessor(128762)
            skillCommanderPractical = DynAccessor(128763)
            skillCommanderTutor = DynAccessor(128764)
            skillConcealment = DynAccessor(128765)
            skillDesignatedTarget = DynAccessor(128766)
            skillDriverMotorExpert = DynAccessor(128767)
            skillDriverRammingMaster = DynAccessor(128768)
            skillDriverReliablePlacement = DynAccessor(128769)
            skillEagleEye = DynAccessor(128770)
            skillEfficiency = DynAccessor(128771)
            skillFirefighting = DynAccessor(128772)
            skillGunnerArmorer = DynAccessor(128773)
            skillGunnerFocus = DynAccessor(128774)
            skillGunnerLoneWolf = DynAccessor(128775)
            skillGunnerQuickAiming = DynAccessor(128776)
            skillHoldLine = DynAccessor(128777)
            skillIntuition = DynAccessor(128778)
            skillJackOfAllTrades = DynAccessor(128779)
            skillLoaderAmmunitionImprove = DynAccessor(128780)
            skillLoaderMelee = DynAccessor(128781)
            skillLoaderPerfectCharge = DynAccessor(128782)
            skillMagMastery = DynAccessor(128783)
            skillOffRoadDriving = DynAccessor(128784)
            skillPointBlast = DynAccessor(128785)
            skillPreventativeMaintenance = DynAccessor(128786)
            skillRadiomanExpert = DynAccessor(128787)
            skillRadiomanInterference = DynAccessor(128788)
            skillRadiomanSideBySide = DynAccessor(128789)
            skillRadiomanSignalInterception = DynAccessor(128790)
            skillRepairs = DynAccessor(128791)
            skillSafeStowage = DynAccessor(128792)
            skillSecondChance = DynAccessor(128793)
            skillSituationalAwareness = DynAccessor(128794)
            skillSixthSense = DynAccessor(128795)
            skillSmoothRide = DynAccessor(128796)
            skillSnapShot = DynAccessor(128797)
            skillSniper = DynAccessor(128798)
            skillStaySharp = DynAccessor(128799)
            skillSuspensionRepair = DynAccessor(128800)
            skillThreatSearch = DynAccessor(128801)
            skillUntrainedPenalty = DynAccessor(128802)
            statConcealment = DynAccessor(128803)
            statFirepower = DynAccessor(128804)
            statMobility = DynAccessor(128805)
            statSpotting = DynAccessor(128806)
            statSurvivability = DynAccessor(128807)

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
                                bg_big = DynAccessor(128808)
                                bg_medium = DynAccessor(128809)
                                bg_small = DynAccessor(128810)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(128811)
                            bg_medium = DynAccessor(128812)
                            bg_small = DynAccessor(128813)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(128814)
        bomber = DynAccessor(128815)
        inspire = DynAccessor(128816)
        minefield = DynAccessor(128817)
        patrol = DynAccessor(128818)
        recon = DynAccessor(128819)
        resuply = DynAccessor(128820)
        sabotageSquad = DynAccessor(128821)
        smokeCloud = DynAccessor(128822)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(128823)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128824)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128825)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128826)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128827)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128828)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128829)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128830)

            c_193 = _c_193()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128831)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128832)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128833)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128834)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(128835)
        style_ch1_lvl3 = DynAccessor(128836)
        style_ch1_lvl4 = DynAccessor(128837)
        style_ch2_lvl2 = DynAccessor(128838)
        style_ch2_lvl3 = DynAccessor(128839)
        style_ch2_lvl4 = DynAccessor(128840)
        style_ch3_lvl2 = DynAccessor(128841)
        style_ch3_lvl3 = DynAccessor(128842)
        style_ch3_lvl4 = DynAccessor(128843)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(128844)
                    bg_small = DynAccessor(128845)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(128846)
                    bg_small = DynAccessor(128847)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(128848)
        clouds_1366 = DynAccessor(128849)
        clouds_1600 = DynAccessor(128850)
        clouds_1920 = DynAccessor(128851)
        clouds_2560 = DynAccessor(128852)
        spark_white = DynAccessor(128853)
        spark_yellow = DynAccessor(128854)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(128855)
        godRaysNew_130x130 = DynAccessor(128856)
        godRaysNew_1600x1600 = DynAccessor(128857)
        no_epic_defeat_draw_ribbon = DynAccessor(128858)
        no_epic_victory_ribbon = DynAccessor(128859)
        rankAnimation_first = DynAccessor(128860)
        rankAnimation_second = DynAccessor(128861)
        rankAnimation_third = DynAccessor(128862)
        speech = DynAccessor(128863)
        yearly_style_fifth = DynAccessor(128864)
        yearly_style_fifth_loop = DynAccessor(128865)
        yearly_style_fourth = DynAccessor(128866)
        yearly_style_fourth_loop = DynAccessor(128867)
        yearly_style_sixth = DynAccessor(128868)
        yearly_style_sixth_loop = DynAccessor(128869)
        yearly_style_third = DynAccessor(128870)
        yearly_style_third_loop = DynAccessor(128871)
        yearly_styles = DynAccessor(128872)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(128873)
            veteran_frame_big = DynAccessor(128874)
            veteran_frame_small = DynAccessor(128875)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(128876)
        example_2 = DynAccessor(128877)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(128878)
        vehicle_sparks_2 = DynAccessor(128879)
        vehicle_sparks_3 = DynAccessor(128880)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(128881)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(128882)
        sparks_orange = DynAccessor(128883)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128884)
                    bg_medium = DynAccessor(128885)
                    bg_small = DynAccessor(128886)

                adaptive = _adaptive()
                bg_big = DynAccessor(128887)
                bg_medium = DynAccessor(128888)
                bg_small = DynAccessor(128889)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128890)
                    bg_medium = DynAccessor(128891)
                    bg_small = DynAccessor(128892)

                adaptive = _adaptive()
                bg_big = DynAccessor(128893)
                bg_medium = DynAccessor(128894)
                bg_small = DynAccessor(128895)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128896)
                    bg_medium = DynAccessor(128897)
                    bg_small = DynAccessor(128898)

                adaptive = _adaptive()
                bg_big = DynAccessor(128899)
                bg_medium = DynAccessor(128900)
                bg_small = DynAccessor(128901)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128902)
                    bg_medium = DynAccessor(128903)
                    bg_small = DynAccessor(128904)

                adaptive = _adaptive()
                bg_big = DynAccessor(128905)
                bg_medium = DynAccessor(128906)
                bg_small = DynAccessor(128907)

            StPatrickEntryPoint = _StPatrickEntryPoint()

            class _resourceWellEventBanner(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128908)
                    bg_medium = DynAccessor(128909)
                    bg_small = DynAccessor(128910)

                adaptive = _adaptive()
                bg_big = DynAccessor(128911)
                bg_medium = DynAccessor(128912)
                bg_small = DynAccessor(128913)

            resourceWellEventBanner = _resourceWellEventBanner()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(128914)
            foreground_small = DynAccessor(128915)
            rays = DynAccessor(128916)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(128917)
            bg_2 = DynAccessor(128918)
            bg_3 = DynAccessor(128919)
            bg_4 = DynAccessor(128920)

        quants = _quants()
        rays = DynAccessor(128921)
        slide_overlay = DynAccessor(128922)

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
                        bronze_common = DynAccessor(128923)
                        bronze_rare = DynAccessor(128924)
                        gold_common = DynAccessor(128925)
                        gold_rare = DynAccessor(128926)
                        silver_common = DynAccessor(128927)
                        silver_rare = DynAccessor(128928)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(128929)
                        epic_small = DynAccessor(128930)
                        rare = DynAccessor(128931)
                        rare_small = DynAccessor(128932)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128933)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(128934)
                            gold = DynAccessor(128935)
                            silver = DynAccessor(128936)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128937)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(128938)
                        rare = DynAccessor(128939)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128940)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128941)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128942)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128943)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(128944)
                    compensationParticles = DynAccessor(128945)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(128946)
                        rare = DynAccessor(128947)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(128948)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(128949)
                        epic_small = DynAccessor(128950)
                        rare = DynAccessor(128951)
                        rare_small = DynAccessor(128952)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(128953)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128954)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128955)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128956)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128957)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128958)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(128959)
                    vehicles_29969 = DynAccessor(128960)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(128961)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(128962)
            glow = DynAccessor(128963)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(128964)
            operation_10_stage_10 = DynAccessor(128965)
            operation_10_stage_5 = DynAccessor(128966)
            operation_10_stage_7 = DynAccessor(128967)
            operation_8_stage_1 = DynAccessor(128968)
            operation_8_stage_10 = DynAccessor(128969)
            operation_8_stage_5 = DynAccessor(128970)
            operation_8_stage_8 = DynAccessor(128971)
            operation_9_stage_1 = DynAccessor(128972)
            operation_9_stage_12 = DynAccessor(128973)
            operation_9_stage_5 = DynAccessor(128974)
            operation_9_stage_8 = DynAccessor(128975)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(128976)
            new_campaign_glow = DynAccessor(128977)
            new_campaign_sparks = DynAccessor(128978)
            smoke = DynAccessor(128979)
            sparks = DynAccessor(128980)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(128981)
            intro_op_10 = DynAccessor(128982)
            intro_op_8 = DynAccessor(128983)
            intro_op_9 = DynAccessor(128984)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(128985)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(128986)
            operation_8 = DynAccessor(128987)
            operation_9 = DynAccessor(128988)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(128989)
        pet_rays = DynAccessor(128990)
        synergy_blick = DynAccessor(128991)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(128992)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(128993)
        epic_victory_ribbon = DynAccessor(128994)
        no_epic_defeat_draw_ribbon = DynAccessor(128995)
        no_epic_victory_ribbon = DynAccessor(128996)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(128997)
        cycle_legendary = DynAccessor(128998)
        intro_epic = DynAccessor(128999)
        intro_legendary = DynAccessor(129000)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129001)
                single = DynAccessor(129002)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(129003)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129004)
                single = DynAccessor(129005)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129006)
                single = DynAccessor(129007)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(129008)
            icon_bg_effect = DynAccessor(129009)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(129010)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(129011)
        icon_bg_effect = DynAccessor(129012)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(129013)
        bg_hw_m = DynAccessor(129014)
        bg_hw_s = DynAccessor(129015)
        unlock_72x72 = DynAccessor(129016)

    user_missions = _user_missions()