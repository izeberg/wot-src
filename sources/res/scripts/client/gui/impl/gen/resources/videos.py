from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()

    class _achievements(DynAccessor):
        __slots__ = ()
        bg_advanced_achievements = DynAccessor(128749)
        bg_reward_screen = DynAccessor(128750)
        grade_change_particles = DynAccessor(128751)
        particles = DynAccessor(128752)
        up_particles = DynAccessor(128753)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            bonusPerkUnlock = DynAccessor(128754)
            crewCommander = DynAccessor(128755)
            crewDriver = DynAccessor(128756)
            crewGunner = DynAccessor(128757)
            crewLoader = DynAccessor(128758)
            crewRadioOperator = DynAccessor(128759)
            mentoringLicense = DynAccessor(128760)
            skillAdrenalineRush = DynAccessor(128761)
            skillAmbushMaster = DynAccessor(128762)
            skillArmorPatching = DynAccessor(128763)
            skillBattleTempered = DynAccessor(128764)
            skillBrothersInArms = DynAccessor(128765)
            skillBulletproof = DynAccessor(128766)
            skillClutchBraking = DynAccessor(128767)
            skillCommanderBonus = DynAccessor(128768)
            skillCommanderCoordination = DynAccessor(128769)
            skillCommanderEmergency = DynAccessor(128770)
            skillCommanderEnemyShotPredictor = DynAccessor(128771)
            skillCommanderPractical = DynAccessor(128772)
            skillCommanderTutor = DynAccessor(128773)
            skillConcealment = DynAccessor(128774)
            skillDesignatedTarget = DynAccessor(128775)
            skillDriverMotorExpert = DynAccessor(128776)
            skillDriverRammingMaster = DynAccessor(128777)
            skillDriverReliablePlacement = DynAccessor(128778)
            skillEagleEye = DynAccessor(128779)
            skillEfficiency = DynAccessor(128780)
            skillFirefighting = DynAccessor(128781)
            skillGunnerArmorer = DynAccessor(128782)
            skillGunnerFocus = DynAccessor(128783)
            skillGunnerLoneWolf = DynAccessor(128784)
            skillGunnerQuickAiming = DynAccessor(128785)
            skillHoldLine = DynAccessor(128786)
            skillIntuition = DynAccessor(128787)
            skillJackOfAllTrades = DynAccessor(128788)
            skillLoaderAmmunitionImprove = DynAccessor(128789)
            skillLoaderMelee = DynAccessor(128790)
            skillLoaderPerfectCharge = DynAccessor(128791)
            skillMagMastery = DynAccessor(128792)
            skillOffRoadDriving = DynAccessor(128793)
            skillPointBlast = DynAccessor(128794)
            skillPreventativeMaintenance = DynAccessor(128795)
            skillRadiomanExpert = DynAccessor(128796)
            skillRadiomanInterference = DynAccessor(128797)
            skillRadiomanSideBySide = DynAccessor(128798)
            skillRadiomanSignalInterception = DynAccessor(128799)
            skillRepairs = DynAccessor(128800)
            skillSafeStowage = DynAccessor(128801)
            skillSecondChance = DynAccessor(128802)
            skillSituationalAwareness = DynAccessor(128803)
            skillSixthSense = DynAccessor(128804)
            skillSmoothRide = DynAccessor(128805)
            skillSnapShot = DynAccessor(128806)
            skillSniper = DynAccessor(128807)
            skillStaySharp = DynAccessor(128808)
            skillSuspensionRepair = DynAccessor(128809)
            skillThreatSearch = DynAccessor(128810)
            skillUntrainedPenalty = DynAccessor(128811)
            statConcealment = DynAccessor(128812)
            statFirepower = DynAccessor(128813)
            statMobility = DynAccessor(128814)
            statSpotting = DynAccessor(128815)
            statSurvivability = DynAccessor(128816)

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
                                bg_big = DynAccessor(128817)
                                bg_medium = DynAccessor(128818)
                                bg_small = DynAccessor(128819)

                            adaptive = _adaptive()
                            bg_big = DynAccessor(128820)
                            bg_medium = DynAccessor(128821)
                            bg_small = DynAccessor(128822)

                        FunRandomEntryPoint = _FunRandomEntryPoint()

                    event = _event()

                hangarEventBanners = _hangarEventBanners()

            fall_tanks = _fall_tanks()

        modes = _modes()

    asset_packs = _asset_packs()

    class _battleAblity(DynAccessor):
        __slots__ = ()
        artillery = DynAccessor(128823)
        bomber = DynAccessor(128824)
        inspire = DynAccessor(128825)
        minefield = DynAccessor(128826)
        patrol = DynAccessor(128827)
        recon = DynAccessor(128828)
        resuply = DynAccessor(128829)
        sabotageSquad = DynAccessor(128830)
        smokeCloud = DynAccessor(128831)

    battleAblity = _battleAblity()

    class _battle_pass(DynAccessor):
        __slots__ = ()

        class _chapter_choice(DynAccessor):
            __slots__ = ()
            activeAnimation = DynAccessor(128832)

            class _c_180(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128833)

            c_180 = _c_180()

            class _c_181(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128834)

            c_181 = _c_181()

            class _c_182(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128835)

            c_182 = _c_182()

            class _c_183(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128836)

            c_183 = _c_183()

            class _c_191(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128837)

            c_191 = _c_191()

            class _c_192(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128838)

            c_192 = _c_192()

            class _c_193(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128839)

            c_193 = _c_193()

            class _default_1(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128840)

            default_1 = _default_1()

            class _default_2(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128841)

            default_2 = _default_2()

            class _default_3(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128842)

            default_3 = _default_3()

            class _default_4(DynAccessor):
                __slots__ = ()
                idle = DynAccessor(128843)

            default_4 = _default_4()

        chapter_choice = _chapter_choice()
        style_ch1_lvl2 = DynAccessor(128844)
        style_ch1_lvl3 = DynAccessor(128845)
        style_ch1_lvl4 = DynAccessor(128846)
        style_ch2_lvl2 = DynAccessor(128847)
        style_ch2_lvl3 = DynAccessor(128848)
        style_ch2_lvl4 = DynAccessor(128849)
        style_ch3_lvl2 = DynAccessor(128850)
        style_ch3_lvl3 = DynAccessor(128851)
        style_ch3_lvl4 = DynAccessor(128852)

        class _widget(DynAccessor):
            __slots__ = ()

            class _background(DynAccessor):
                __slots__ = ()

                class _season_18(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(128853)
                    bg_small = DynAccessor(128854)

                season_18 = _season_18()

                class _season_19(DynAccessor):
                    __slots__ = ()
                    bg = DynAccessor(128855)
                    bg_small = DynAccessor(128856)

                season_19 = _season_19()

            background = _background()

        widget = _widget()

    battle_pass = _battle_pass()

    class _clan_supply(DynAccessor):
        __slots__ = ()
        clouds_1024 = DynAccessor(128857)
        clouds_1366 = DynAccessor(128858)
        clouds_1600 = DynAccessor(128859)
        clouds_1920 = DynAccessor(128860)
        clouds_2560 = DynAccessor(128861)
        spark_white = DynAccessor(128862)
        spark_yellow = DynAccessor(128863)

    clan_supply = _clan_supply()

    class _comp7(DynAccessor):
        __slots__ = ()
        divine_glow = DynAccessor(128864)
        godRaysNew_130x130 = DynAccessor(128865)
        godRaysNew_1600x1600 = DynAccessor(128866)
        no_epic_defeat_draw_ribbon = DynAccessor(128867)
        no_epic_victory_ribbon = DynAccessor(128868)
        rankAnimation_first = DynAccessor(128869)
        rankAnimation_second = DynAccessor(128870)
        rankAnimation_third = DynAccessor(128871)
        speech = DynAccessor(128872)
        yearly_style_fifth = DynAccessor(128873)
        yearly_style_fifth_loop = DynAccessor(128874)
        yearly_style_fourth = DynAccessor(128875)
        yearly_style_fourth_loop = DynAccessor(128876)
        yearly_style_sixth = DynAccessor(128877)
        yearly_style_sixth_loop = DynAccessor(128878)
        yearly_style_third = DynAccessor(128879)
        yearly_style_third_loop = DynAccessor(128880)
        yearly_styles = DynAccessor(128881)

    comp7 = _comp7()

    class _crew(DynAccessor):
        __slots__ = ()

        class _profile(DynAccessor):
            __slots__ = ()
            veteran_blick = DynAccessor(128882)
            veteran_frame_big = DynAccessor(128883)
            veteran_frame_small = DynAccessor(128884)

        profile = _profile()

    crew = _crew()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(128885)
        example_2 = DynAccessor(128886)

    development = _development()

    class _dogtags(DynAccessor):
        __slots__ = ()
        vehicle_sparks_1 = DynAccessor(128887)
        vehicle_sparks_2 = DynAccessor(128888)
        vehicle_sparks_3 = DynAccessor(128889)

    dogtags = _dogtags()

    class _flHangarWidget(DynAccessor):
        __slots__ = ()
        bg_meta = DynAccessor(128890)

    flHangarWidget = _flHangarWidget()

    class _flProgressionScreen(DynAccessor):
        __slots__ = ()
        badge_reflection = DynAccessor(128891)
        sparks_orange = DynAccessor(128892)

    flProgressionScreen = _flProgressionScreen()

    class _hangarEventBanners(DynAccessor):
        __slots__ = ()

        class _event(DynAccessor):
            __slots__ = ()

            class _BattleRoyaleEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128893)
                    bg_medium = DynAccessor(128894)
                    bg_small = DynAccessor(128895)

                adaptive = _adaptive()
                bg_big = DynAccessor(128896)
                bg_medium = DynAccessor(128897)
                bg_small = DynAccessor(128898)

            BattleRoyaleEntryPoint = _BattleRoyaleEntryPoint()

            class _EpicBattlesEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128899)
                    bg_medium = DynAccessor(128900)
                    bg_small = DynAccessor(128901)

                adaptive = _adaptive()
                bg_big = DynAccessor(128902)
                bg_medium = DynAccessor(128903)
                bg_small = DynAccessor(128904)

            EpicBattlesEntryPoint = _EpicBattlesEntryPoint()

            class _LSEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128905)
                    bg_medium = DynAccessor(128906)
                    bg_small = DynAccessor(128907)

                adaptive = _adaptive()
                bg_big = DynAccessor(128908)
                bg_medium = DynAccessor(128909)
                bg_small = DynAccessor(128910)

            LSEntryPoint = _LSEntryPoint()

            class _StPatrickEntryPoint(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128911)
                    bg_medium = DynAccessor(128912)
                    bg_small = DynAccessor(128913)

                adaptive = _adaptive()
                bg_big = DynAccessor(128914)
                bg_medium = DynAccessor(128915)
                bg_small = DynAccessor(128916)

            StPatrickEntryPoint = _StPatrickEntryPoint()

            class _resourceWellEventBanner(DynAccessor):
                __slots__ = ()

                class _adaptive(DynAccessor):
                    __slots__ = ()
                    bg_big = DynAccessor(128917)
                    bg_medium = DynAccessor(128918)
                    bg_small = DynAccessor(128919)

                adaptive = _adaptive()
                bg_big = DynAccessor(128920)
                bg_medium = DynAccessor(128921)
                bg_small = DynAccessor(128922)

            resourceWellEventBanner = _resourceWellEventBanner()

        event = _event()

    hangarEventBanners = _hangarEventBanners()

    class _header_footer(DynAccessor):
        __slots__ = ()

        class _battle_button(DynAccessor):
            __slots__ = ()
            foreground_large = DynAccessor(128923)
            foreground_small = DynAccessor(128924)
            rays = DynAccessor(128925)

        battle_button = _battle_button()

    header_footer = _header_footer()

    class _last_stand(DynAccessor):
        __slots__ = ()

        class _quants(DynAccessor):
            __slots__ = ()
            bg_1 = DynAccessor(128926)
            bg_2 = DynAccessor(128927)
            bg_3 = DynAccessor(128928)
            bg_4 = DynAccessor(128929)

        quants = _quants()
        rays = DynAccessor(128930)
        slide_overlay = DynAccessor(128931)

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
                        bronze_common = DynAccessor(128932)
                        bronze_rare = DynAccessor(128933)
                        gold_common = DynAccessor(128934)
                        gold_rare = DynAccessor(128935)
                        silver_common = DynAccessor(128936)
                        silver_rare = DynAccessor(128937)

                    openingBoxVideo = _openingBoxVideo()

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(128938)
                        epic_small = DynAccessor(128939)
                        rare = DynAccessor(128940)
                        rare_small = DynAccessor(128941)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128942)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            bronze = DynAccessor(128943)
                            gold = DynAccessor(128944)
                            silver = DynAccessor(128945)

                        box = _box()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128946)

                noBoxesView = _noBoxesView()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(128947)
                        rare = DynAccessor(128948)

                    openingBoxVideo = _openingBoxVideo()

                awardViews = _awardViews()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128949)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128950)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128951)

                        hover = _hover()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128952)

                noBoxesView = _noBoxesView()

            battlePass = _battlePass()

            class _default(DynAccessor):
                __slots__ = ()

                class _awardViews(DynAccessor):
                    __slots__ = ()
                    compensationGlow = DynAccessor(128953)
                    compensationParticles = DynAccessor(128954)

                    class _openingBoxVideo(DynAccessor):
                        __slots__ = ()
                        common = DynAccessor(128955)
                        rare = DynAccessor(128956)

                    openingBoxVideo = _openingBoxVideo()
                    rareGlow = DynAccessor(128957)

                    class _raritySimpleAnimations(DynAccessor):
                        __slots__ = ()
                        epic = DynAccessor(128958)
                        epic_small = DynAccessor(128959)
                        rare = DynAccessor(128960)
                        rare_small = DynAccessor(128961)

                    raritySimpleAnimations = _raritySimpleAnimations()

                awardViews = _awardViews()

                class _entryPoint(DynAccessor):
                    __slots__ = ()
                    glow = DynAccessor(128962)

                entryPoint = _entryPoint()

                class _hasBoxesView(DynAccessor):
                    __slots__ = ()

                    class _layers(DynAccessor):
                        __slots__ = ()

                        class _background(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128963)

                        background = _background()

                        class _box(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128964)

                        box = _box()

                        class _hover(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128965)

                        hover = _hover()

                        class _idle(DynAccessor):
                            __slots__ = ()
                            default = DynAccessor(128966)

                        idle = _idle()

                    layers = _layers()

                hasBoxesView = _hasBoxesView()

                class _noBoxesView(DynAccessor):
                    __slots__ = ()
                    background = DynAccessor(128967)

                noBoxesView = _noBoxesView()

            default = _default()

        customizable = _customizable()

        class _events(DynAccessor):
            __slots__ = ()

            class _anniversaryCN(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(128968)
                    vehicles_29969 = DynAccessor(128969)

                rarityOverlay = _rarityOverlay()

            anniversaryCN = _anniversaryCN()

            class _battlePass(DynAccessor):
                __slots__ = ()

                class _rarityOverlay(DynAccessor):
                    __slots__ = ()
                    lootBox_24040101 = DynAccessor(128970)

                rarityOverlay = _rarityOverlay()

            battlePass = _battlePass()

        events = _events()

    lootbox = _lootbox()

    class _open_bundle(DynAccessor):
        __slots__ = ()

        class _default(DynAccessor):
            __slots__ = ()
            attachmentsSetGlow = DynAccessor(128971)
            glow = DynAccessor(128972)

        default = _default()

    open_bundle = _open_bundle()

    class _personal_missions_30(DynAccessor):
        __slots__ = ()

        class _assembling_screen(DynAccessor):
            __slots__ = ()
            operation_10_stage_1 = DynAccessor(128973)
            operation_10_stage_10 = DynAccessor(128974)
            operation_10_stage_5 = DynAccessor(128975)
            operation_10_stage_7 = DynAccessor(128976)
            operation_8_stage_1 = DynAccessor(128977)
            operation_8_stage_10 = DynAccessor(128978)
            operation_8_stage_5 = DynAccessor(128979)
            operation_8_stage_8 = DynAccessor(128980)
            operation_9_stage_1 = DynAccessor(128981)
            operation_9_stage_12 = DynAccessor(128982)
            operation_9_stage_5 = DynAccessor(128983)
            operation_9_stage_8 = DynAccessor(128984)

        assembling_screen = _assembling_screen()

        class _campaign_selector(DynAccessor):
            __slots__ = ()
            bugs = DynAccessor(128985)
            new_campaign_glow = DynAccessor(128986)
            new_campaign_sparks = DynAccessor(128987)
            smoke = DynAccessor(128988)
            sparks = DynAccessor(128989)

        campaign_selector = _campaign_selector()

        class _intro_screens(DynAccessor):
            __slots__ = ()
            intro = DynAccessor(128990)
            intro_op_10 = DynAccessor(128991)
            intro_op_8 = DynAccessor(128992)
            intro_op_9 = DynAccessor(128993)

        intro_screens = _intro_screens()

        class _main(DynAccessor):
            __slots__ = ()
            detail_glow = DynAccessor(128994)

        main = _main()

        class _rewards_screen(DynAccessor):
            __slots__ = ()
            operation_10 = DynAccessor(128995)
            operation_8 = DynAccessor(128996)
            operation_9 = DynAccessor(128997)

        rewards_screen = _rewards_screen()

    personal_missions_30 = _personal_missions_30()

    class _pet_system(DynAccessor):
        __slots__ = ()
        glow = DynAccessor(128998)
        pet_rays = DynAccessor(128999)
        synergy_blick = DynAccessor(129000)

    pet_system = _pet_system()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(129001)

    platoon = _platoon()

    class _post_battle(DynAccessor):
        __slots__ = ()
        epic_defeat_draw_ribbon = DynAccessor(129002)
        epic_victory_ribbon = DynAccessor(129003)
        no_epic_defeat_draw_ribbon = DynAccessor(129004)
        no_epic_victory_ribbon = DynAccessor(129005)

    post_battle = _post_battle()

    class _rarity(DynAccessor):
        __slots__ = ()
        cycle_epic = DynAccessor(129006)
        cycle_legendary = DynAccessor(129007)
        intro_epic = DynAccessor(129008)
        intro_legendary = DynAccessor(129009)

    rarity = _rarity()

    class _skillTree(DynAccessor):
        __slots__ = ()

        class _perks(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129010)
                single = DynAccessor(129011)

            common = _common()

            class _final(DynAccessor):
                __slots__ = ()
                standard = DynAccessor(129012)

            final = _final()

            class _major(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129013)
                single = DynAccessor(129014)

            major = _major()

            class _special(DynAccessor):
                __slots__ = ()
                chain = DynAccessor(129015)
                single = DynAccessor(129016)

            special = _special()

        perks = _perks()

    skillTree = _skillTree()

    class _st_patrick(DynAccessor):
        __slots__ = ()

        class _umg(DynAccessor):
            __slots__ = ()
            card_effect = DynAccessor(129017)
            icon_bg_effect = DynAccessor(129018)

        umg = _umg()

    st_patrick = _st_patrick()

    class _story_mode(DynAccessor):
        __slots__ = ()
        v_icon_fire = DynAccessor(129019)

    story_mode = _story_mode()

    class _umg(DynAccessor):
        __slots__ = ()
        card_effect = DynAccessor(129020)
        icon_bg_effect = DynAccessor(129021)

    umg = _umg()

    class _user_missions(DynAccessor):
        __slots__ = ()
        bg_hw_l = DynAccessor(129022)
        bg_hw_m = DynAccessor(129023)
        bg_hw_s = DynAccessor(129024)
        unlock_72x72 = DynAccessor(129025)

    user_missions = _user_missions()