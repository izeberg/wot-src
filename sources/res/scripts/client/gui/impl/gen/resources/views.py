from gui.impl.gen_utils import DynAccessor

class Views(DynAccessor):
    __slots__ = ()

    class _battle(DynAccessor):
        __slots__ = ()

        class _battleRoyale(DynAccessor):
            __slots__ = ()

            class _select_respawn(DynAccessor):
                __slots__ = ()
                SelectRespawn = DynAccessor(8)

            select_respawn = _select_respawn()

        battleRoyale = _battleRoyale()

        class _battle_notifier(DynAccessor):
            __slots__ = ()
            BattleNotifierView = DynAccessor(82)

        battle_notifier = _battle_notifier()

        class _battle_page(DynAccessor):
            __slots__ = ()
            EpicRespawnAmmunitionPanelView = DynAccessor(83)
            PersonalReservesTabView = DynAccessor(84)
            PrebattleAmmunitionPanelView = DynAccessor(85)
            PrebattleCarouselView = DynAccessor(86)

        battle_page = _battle_page()

        class _timer(DynAccessor):
            __slots__ = ()
            TimerView = DynAccessor(87)

        timer = _timer()

    battle = _battle()

    class _common(DynAccessor):
        __slots__ = ()

        class _context_menu_window(DynAccessor):
            __slots__ = ()

            class _context_menu_content(DynAccessor):
                __slots__ = ()
                ContextMenuContent = DynAccessor(9)

            context_menu_content = _context_menu_content()

            class _context_menu_window(DynAccessor):
                __slots__ = ()
                ContextMenuWindow = DynAccessor(10)

            context_menu_window = _context_menu_window()

        context_menu_window = _context_menu_window()

        class _dialog_view(DynAccessor):
            __slots__ = ()

            class _dialog_window(DynAccessor):
                __slots__ = ()
                DialogWindow = DynAccessor(11)

            dialog_window = _dialog_window()

            class _simple_dialog_content(DynAccessor):
                __slots__ = ()
                SimpleDialogContent = DynAccessor(12)

            simple_dialog_content = _simple_dialog_content()

            class _components(DynAccessor):
                __slots__ = ()

                class _balance_contents(DynAccessor):
                    __slots__ = ()
                    CommonBalanceContent = DynAccessor(13)

                balance_contents = _balance_contents()

                class _checkbox_content(DynAccessor):
                    __slots__ = ()
                    CheckBoxDialogContent = DynAccessor(14)

                checkbox_content = _checkbox_content()

                class _dialog_prices_content(DynAccessor):
                    __slots__ = ()
                    DialogPricesContent = DynAccessor(15)

                dialog_prices_content = _dialog_prices_content()

                class _dialog_prices_tooltip(DynAccessor):
                    __slots__ = ()
                    DialogPricesTooltip = DynAccessor(16)

                dialog_prices_tooltip = _dialog_prices_tooltip()

            components = _components()

        dialog_view = _dialog_view()

        class _drop_down_menu_window(DynAccessor):
            __slots__ = ()

            class _drop_down_menu_content(DynAccessor):
                __slots__ = ()
                DropDownMenuContent = DynAccessor(17)

            drop_down_menu_content = _drop_down_menu_content()

            class _drop_down_menu_window(DynAccessor):
                __slots__ = ()
                DropDownMenuWindow = DynAccessor(18)

            drop_down_menu_window = _drop_down_menu_window()

        drop_down_menu_window = _drop_down_menu_window()

        class _pop_over_window(DynAccessor):
            __slots__ = ()

            class _backport_pop_over(DynAccessor):
                __slots__ = ()
                BackportPopOverContent = DynAccessor(19)
                BackportPopOverWindow = DynAccessor(20)

            backport_pop_over = _backport_pop_over()

            class _pop_over_window(DynAccessor):
                __slots__ = ()
                PopOverWindow = DynAccessor(21)

            pop_over_window = _pop_over_window()

        pop_over_window = _pop_over_window()

        class _standard_window(DynAccessor):
            __slots__ = ()

            class _standard_window(DynAccessor):
                __slots__ = ()
                StandardWindow = DynAccessor(22)

            standard_window = _standard_window()

        standard_window = _standard_window()

        class _tooltip_window(DynAccessor):
            __slots__ = ()

            class _advanced_tooltip_content(DynAccessor):
                __slots__ = ()
                AdvandcedTooltipContent = DynAccessor(23)
                AdvandcedAnimatedTooltipContent = DynAccessor(24)

            advanced_tooltip_content = _advanced_tooltip_content()

            class _backport_tooltip_content(DynAccessor):
                __slots__ = ()
                BackportTooltipContent = DynAccessor(25)

            backport_tooltip_content = _backport_tooltip_content()

            class _loot_box_compensation_tooltip(DynAccessor):
                __slots__ = ()
                LootBoxCompensationTooltipContent = DynAccessor(26)
                CrewSkinsCompensationTooltipContent = DynAccessor(27)
                LootBoxVehicleCompensationTooltipContent = DynAccessor(28)

            loot_box_compensation_tooltip = _loot_box_compensation_tooltip()

            class _simple_tooltip_content(DynAccessor):
                __slots__ = ()
                SimpleTooltipContent = DynAccessor(29)
                SimpleTooltipHtmlContent = DynAccessor(30)

            simple_tooltip_content = _simple_tooltip_content()

            class _tooltip_window(DynAccessor):
                __slots__ = ()
                TooltipWindow = DynAccessor(31)

            tooltip_window = _tooltip_window()

        tooltip_window = _tooltip_window()
        BackportContextMenu = DynAccessor(88)
        Browser = DynAccessor(89)
        FadingCoverView = DynAccessor(90)

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            ReservesDisabledTooltip = DynAccessor(91)

        personal_reserves = _personal_reserves()

    common = _common()

    class _lobby(DynAccessor):
        __slots__ = ()

        class _battleRoyale(DynAccessor):
            __slots__ = ()

            class _event_info(DynAccessor):
                __slots__ = ()
                EventInfo = DynAccessor(32)

            event_info = _event_info()

            class _hangar_bottom_panel_cmp(DynAccessor):
                __slots__ = ()
                HangarBottomPanelCmp = DynAccessor(33)

            hangar_bottom_panel_cmp = _hangar_bottom_panel_cmp()

        battleRoyale = _battleRoyale()

        class _battle_pass(DynAccessor):
            __slots__ = ()

            class _trophy_device_confirm_dialog(DynAccessor):
                __slots__ = ()
                TrophyDeviceConfirmDialogContent = DynAccessor(34)

            trophy_device_confirm_dialog = _trophy_device_confirm_dialog()
            BattlePassAwardsView = DynAccessor(144)
            BattlePassBuyLevelView = DynAccessor(145)
            BattlePassBuyView = DynAccessor(146)
            BattlePassEntryPointView = DynAccessor(147)
            BattlePassHowToEarnPointsView = DynAccessor(148)
            BattlePassIntroView = DynAccessor(149)
            BattlePassProgressionsView = DynAccessor(150)
            BattlePassVehicleAwardView = DynAccessor(151)
            ChapterChoiceView = DynAccessor(152)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChapterConfirm = DynAccessor(153)

            dialogs = _dialogs()
            ExtraIntroView = DynAccessor(154)
            RewardsSelectionView = DynAccessor(155)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                AnimatedReward = DynAccessor(156)
                AwardsWidget = DynAccessor(157)
                BuyButtons = DynAccessor(158)
                ChapterBackground = DynAccessor(159)
                CurrencyReward = DynAccessor(160)
                Emblem = DynAccessor(161)
                FormatRemainingDate = DynAccessor(162)
                Header = DynAccessor(163)
                LoupeButton = DynAccessor(164)
                RewardsBlock = DynAccessor(165)
                ScrollWithLips = DynAccessor(166)
                Slider = DynAccessor(167)
                Title = DynAccessor(168)
                VehicleBonusList = DynAccessor(169)
                VehicleInfo = DynAccessor(170)
                VehicleList = DynAccessor(171)
                Video = DynAccessor(172)

            sharedComponents = _sharedComponents()
            StyleVideoView = DynAccessor(173)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattlePassCoinTooltipView = DynAccessor(174)
                BattlePassCompletedTooltipView = DynAccessor(175)
                BattlePassGoldMissionTooltipView = DynAccessor(176)
                BattlePassInProgressTooltipView = DynAccessor(177)
                BattlePassLockIconTooltipView = DynAccessor(178)
                BattlePassNoChapterTooltipView = DynAccessor(179)
                BattlePassNotStartedTooltipView = DynAccessor(180)
                BattlePassOnPauseTooltipView = DynAccessor(181)
                BattlePassPointsView = DynAccessor(182)
                BattlePassQuestsChainTooltipView = DynAccessor(183)
                BattlePassUpgradeStyleTooltipView = DynAccessor(184)
                BattleTypesTooltipView = DynAccessor(185)
                BuyStagesFooterTooltipView = DynAccessor(186)
                RandomQuestTooltip = DynAccessor(187)

                class _sharedComponents(DynAccessor):
                    __slots__ = ()
                    BlockCompleted = DynAccessor(188)
                    Chose = DynAccessor(189)
                    FinalLevel = DynAccessor(190)
                    IconTextBlock = DynAccessor(191)
                    PerBattlePointsTable = DynAccessor(192)
                    Point = DynAccessor(193)

                sharedComponents = _sharedComponents()
                VehiclePointsTooltipView = DynAccessor(194)

            tooltips = _tooltips()

        battle_pass = _battle_pass()

        class _blueprints(DynAccessor):
            __slots__ = ()

            class _fragments_balance_content(DynAccessor):
                __slots__ = ()
                FragmentsBalanceContent = DynAccessor(35)

            fragments_balance_content = _fragments_balance_content()

            class _blueprint_screen(DynAccessor):
                __slots__ = ()

                class _blueprint_screen(DynAccessor):
                    __slots__ = ()
                    BlueprintScreen = DynAccessor(36)

                blueprint_screen = _blueprint_screen()

            blueprint_screen = _blueprint_screen()
            Confirm = DynAccessor(201)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BlueprintsAlliancesTooltipView = DynAccessor(202)

            tooltips = _tooltips()

        blueprints = _blueprints()

        class _common(DynAccessor):
            __slots__ = ()

            class _congrats(DynAccessor):
                __slots__ = ()

                class _common_congrats_view(DynAccessor):
                    __slots__ = ()
                    CommonCongratsView = DynAccessor(37)

                common_congrats_view = _common_congrats_view()

            congrats = _congrats()
            AwardsView = DynAccessor(220)
            BrowserView = DynAccessor(221)
            SelectableRewardBase = DynAccessor(222)
            SelectSlotSpecDialog = DynAccessor(223)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExtendedTextTooltip = DynAccessor(224)
                SelectedRewardsTooltipView = DynAccessor(225)

            tooltips = _tooltips()

        common = _common()

        class _marathon(DynAccessor):
            __slots__ = ()

            class _marathon_reward_view(DynAccessor):
                __slots__ = ()
                MarathonRewardView = DynAccessor(38)

            marathon_reward_view = _marathon_reward_view()
            EntryPoint = DynAccessor(360)
            RewardWindow = DynAccessor(361)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RestRewardTooltip = DynAccessor(362)

            tooltips = _tooltips()

        marathon = _marathon()

        class _missions(DynAccessor):
            __slots__ = ()

            class _missions_tab_bar_view(DynAccessor):
                __slots__ = ()
                MissionsTabBarView = DynAccessor(39)

            missions_tab_bar_view = _missions_tab_bar_view()

            class _legacy(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()
                    BattleConditions = DynAccessor(364)
                    Countdown = DynAccessor(365)
                    PendingDots = DynAccessor(366)

                common = _common()
                Daily = DynAccessor(367)
                DailyQuestsTooltip = DynAccessor(368)
                RerollTooltip = DynAccessor(369)
                RerollTooltipWithCountdown = DynAccessor(370)

            legacy = _legacy()

        missions = _missions()

        class _nation_change(DynAccessor):
            __slots__ = ()

            class _nation_change_screen(DynAccessor):
                __slots__ = ()
                NationChangeScreen = DynAccessor(40)

            nation_change_screen = _nation_change_screen()

        nation_change = _nation_change()

        class _premacc(DynAccessor):
            __slots__ = ()

            class _daily_experience_view(DynAccessor):
                __slots__ = ()
                DailyExperiencePage = DynAccessor(41)

            daily_experience_view = _daily_experience_view()

            class _maps_blacklist_view(DynAccessor):
                __slots__ = ()
                MapsBlacklistView = DynAccessor(42)

            maps_blacklist_view = _maps_blacklist_view()

            class _piggybank(DynAccessor):
                __slots__ = ()
                Piggybank = DynAccessor(43)

            piggybank = _piggybank()

            class _squad_bonus_tooltip_content(DynAccessor):
                __slots__ = ()
                SquadBonusTooltipContent = DynAccessor(44)

            squad_bonus_tooltip_content = _squad_bonus_tooltip_content()

            class _dashboard(DynAccessor):
                __slots__ = ()

                class _prem_dashboard_parent_control_info(DynAccessor):
                    __slots__ = ()
                    PremDashboardParentControlInfoContent = DynAccessor(45)

                prem_dashboard_parent_control_info = _prem_dashboard_parent_control_info()

                class _piggy_bank_cards(DynAccessor):
                    __slots__ = ()

                    class _prem_piggy_bank(DynAccessor):
                        __slots__ = ()
                        PremPiggyBankCard = DynAccessor(46)

                    prem_piggy_bank = _prem_piggy_bank()

                    class _wot_plus_piggy_bank(DynAccessor):
                        __slots__ = ()
                        WotPlusPiggyBankCard = DynAccessor(47)

                    wot_plus_piggy_bank = _wot_plus_piggy_bank()

                piggy_bank_cards = _piggy_bank_cards()

            dashboard = _dashboard()

            class _maps_blacklist(DynAccessor):
                __slots__ = ()

                class _maps_blacklist_confirm_dialog(DynAccessor):
                    __slots__ = ()
                    MapsBlacklistConfirmDialogContent = DynAccessor(48)

                maps_blacklist_confirm_dialog = _maps_blacklist_confirm_dialog()

                class _maps_blacklist_tooltips(DynAccessor):
                    __slots__ = ()
                    MapsBlacklistInfoTooltipContent = DynAccessor(49)

                maps_blacklist_tooltips = _maps_blacklist_tooltips()

            maps_blacklist = _maps_blacklist()

        premacc = _premacc()

        class _progressive_reward(DynAccessor):
            __slots__ = ()

            class _progressive_reward_award(DynAccessor):
                __slots__ = ()
                ProgressiveRewardAward = DynAccessor(50)

            progressive_reward_award = _progressive_reward_award()

            class _progressive_reward_view(DynAccessor):
                __slots__ = ()
                ProgressiveRewardView = DynAccessor(51)

            progressive_reward_view = _progressive_reward_view()

        progressive_reward = _progressive_reward()

        class _ranked(DynAccessor):
            __slots__ = ()

            class _ranked_year_award(DynAccessor):
                __slots__ = ()
                RankedYearAward = DynAccessor(52)

            ranked_year_award = _ranked_year_award()
            EntryPoint = DynAccessor(443)
            QualificationRewardsView = DynAccessor(444)
            RankedHangarWidget = DynAccessor(445)
            RankedPostbattleStatusView = DynAccessor(446)
            RankedProgressionView = DynAccessor(447)
            RankedSelectableRewardView = DynAccessor(448)
            RankedSelectedRewardView = DynAccessor(449)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RankedBattlesRolesTooltipView = DynAccessor(450)

            tooltips = _tooltips()
            YearLeaderboardView = DynAccessor(451)

        ranked = _ranked()

        class _reward_window(DynAccessor):
            __slots__ = ()

            class _clan_reward_window_content(DynAccessor):
                __slots__ = ()
                ClanRewardWindowContent = DynAccessor(53)

            clan_reward_window_content = _clan_reward_window_content()

            class _piggy_bank_reward_window_content(DynAccessor):
                __slots__ = ()
                PiggyBankRewardWindowContent = DynAccessor(54)

            piggy_bank_reward_window_content = _piggy_bank_reward_window_content()

            class _reward_window_content(DynAccessor):
                __slots__ = ()
                RewardWindowContent = DynAccessor(55)

            reward_window_content = _reward_window_content()

            class _twitch_reward_window_content(DynAccessor):
                __slots__ = ()
                TwitchRewardWindowContent = DynAccessor(56)

            twitch_reward_window_content = _twitch_reward_window_content()

        reward_window = _reward_window()

        class _shop(DynAccessor):
            __slots__ = ()

            class _buy_vehicle_view(DynAccessor):
                __slots__ = ()
                BuyVehicleView = DynAccessor(57)

            buy_vehicle_view = _buy_vehicle_view()

        shop = _shop()

        class _tooltips(DynAccessor):
            __slots__ = ()

            class _clans(DynAccessor):
                __slots__ = ()
                ClanShortInfoTooltipContent = DynAccessor(58)

            clans = _clans()
            AdditionalRewardsTooltip = DynAccessor(536)
            QuestConditionsTooltip = DynAccessor(537)
            TankmanTooltipView = DynAccessor(538)
            VehPostProgressionEntryPointTooltip = DynAccessor(539)

        tooltips = _tooltips()

        class _video(DynAccessor):
            __slots__ = ()

            class _video_view(DynAccessor):
                __slots__ = ()
                VideoView = DynAccessor(59)

            video_view = _video_view()

        video = _video()

        class _account_completion(DynAccessor):
            __slots__ = ()
            AddCredentialsView = DynAccessor(109)
            CompleteView = DynAccessor(110)
            ConfirmCredentialsView = DynAccessor(111)
            ContactSupportView = DynAccessor(112)
            CurtainView = DynAccessor(113)
            EmptyView = DynAccessor(114)
            ErrorView = DynAccessor(115)
            RenamingCompleteView = DynAccessor(116)
            RenamingView = DynAccessor(117)

            class _tooltips(DynAccessor):
                __slots__ = ()
                HangarTooltip = DynAccessor(118)
                RenamingHangarTooltip = DynAccessor(119)

            tooltips = _tooltips()

        account_completion = _account_completion()

        class _account_dashboard(DynAccessor):
            __slots__ = ()
            AccountDashboard = DynAccessor(120)

        account_dashboard = _account_dashboard()

        class _achievements(DynAccessor):
            __slots__ = ()
            AchievementsMainView = DynAccessor(121)

            class _dialogs(DynAccessor):
                __slots__ = ()
                EditConfirm = DynAccessor(122)

            dialogs = _dialogs()
            EditView = DynAccessor(123)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AutoSettingTooltip = DynAccessor(124)
                BattlesKPITooltip = DynAccessor(125)
                EditingTooltip = DynAccessor(126)
                KPITooltip = DynAccessor(127)
                WOTPRMainTooltip = DynAccessor(128)
                WTRInfoTooltip = DynAccessor(129)
                WTRMainTooltip = DynAccessor(130)

            tooltips = _tooltips()

        achievements = _achievements()

        class _awards(DynAccessor):
            __slots__ = ()
            BadgeAwardView = DynAccessor(131)
            MultipleAwardsView = DynAccessor(132)

            class _tooltips(DynAccessor):
                __slots__ = ()
                VehicleForChooseTooltip = DynAccessor(133)

            tooltips = _tooltips()

        awards = _awards()

        class _battle_matters(DynAccessor):
            __slots__ = ()
            BattleMattersEntryPointView = DynAccessor(134)
            BattleMattersExchangeRewards = DynAccessor(135)
            BattleMattersMainRewardView = DynAccessor(136)
            BattleMattersMainView = DynAccessor(137)
            BattleMattersPausedView = DynAccessor(138)
            BattleMattersRewardsView = DynAccessor(139)
            BattleMattersVehicleSelectionView = DynAccessor(140)

            class _popovers(DynAccessor):
                __slots__ = ()
                BattleMattersFilterPopoverView = DynAccessor(141)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattleMattersEntryTooltipView = DynAccessor(142)
                BattleMattersTokenTooltipView = DynAccessor(143)

            tooltips = _tooltips()

        battle_matters = _battle_matters()

        class _battle_royale(DynAccessor):
            __slots__ = ()
            BattleResultView = DynAccessor(195)
            CommanderView = DynAccessor(196)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                CurrencyResolver = DynAccessor(197)
                PriceResolver = DynAccessor(198)

            sharedComponents = _sharedComponents()
            TechParametersVIew = DynAccessor(199)

        battle_royale = _battle_royale()

        class _black_market(DynAccessor):
            __slots__ = ()

            class _banner(DynAccessor):
                __slots__ = ()
                BlackMarketBannerView = DynAccessor(200)

            banner = _banner()

        black_market = _black_market()

        class _bootcamp(DynAccessor):
            __slots__ = ()
            BootcampExitView = DynAccessor(203)
            BootcampFinalRewardView = DynAccessor(204)
            BootcampNationView = DynAccessor(205)
            BootcampProgressView = DynAccessor(206)
            BootcampProgressWidget = DynAccessor(207)
            BootcampQuestWidget = DynAccessor(208)
            RewardsTooltip = DynAccessor(209)

        bootcamp = _bootcamp()

        class _collection(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(210)
            CollectionEntryPointView = DynAccessor(211)
            CollectionItemPreview = DynAccessor(212)
            CollectionsMainView = DynAccessor(213)
            CollectionView = DynAccessor(214)
            IntroView = DynAccessor(215)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CollectionItemTooltipView = DynAccessor(216)
                RewardTooltipView = DynAccessor(217)

            tooltips = _tooltips()

        collection = _collection()

        class _collective_goal(DynAccessor):
            __slots__ = ()
            CollectiveGoalEntryPointView = DynAccessor(218)

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(219)

            tooltips = _tooltips()

        collective_goal = _collective_goal()

        class _comp7(DynAccessor):
            __slots__ = ()
            Banner = DynAccessor(226)
            MainWidget = DynAccessor(227)
            MetaRootView = DynAccessor(228)
            NoVehiclesScreen = DynAccessor(229)
            RewardsScreen = DynAccessor(230)
            SeasonModifier = DynAccessor(231)

            class _tooltips(DynAccessor):
                __slots__ = ()
                DivisionTooltip = DynAccessor(232)
                FifthRankTooltip = DynAccessor(233)
                GeneralRankTooltip = DynAccessor(234)
                LastUpdateTooltip = DynAccessor(235)
                MainWidgetTooltip = DynAccessor(236)
                RankInactivityTooltip = DynAccessor(237)
                SeasonPointTooltip = DynAccessor(238)
                SixthRankTooltip = DynAccessor(239)

            tooltips = _tooltips()
            WhatsNewView = DynAccessor(240)

        comp7 = _comp7()

        class _craft_machine(DynAccessor):
            __slots__ = ()
            CraftmachineEntryPointView = DynAccessor(241)

        craft_machine = _craft_machine()

        class _crew(DynAccessor):
            __slots__ = ()
            BarracksView = DynAccessor(242)
            ChangeTankmanSkinView = DynAccessor(243)
            CrewHeaderTooltipView = DynAccessor(244)
            CrewIntroView = DynAccessor(245)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChangeTankmanTrainingDialog = DynAccessor(246)
                CrewBooksPurchaseDialog = DynAccessor(247)
                DismissOrRestoreTankmans = DynAccessor(248)
                DismissTankmanDialog = DynAccessor(249)
                DocumentChangeDialog = DynAccessor(250)
                EnlargeBarracksDialog = DynAccessor(251)
                PerksResetContent = DynAccessor(252)
                RecruitDialog = DynAccessor(253)
                RecruitNewTankmanDialog = DynAccessor(254)
                RestoreTankmanDialog = DynAccessor(255)
                RetrainDialog = DynAccessor(256)
                RoleChangeDialog = DynAccessor(257)
                SkinApplyDialog = DynAccessor(258)

            dialogs = _dialogs()
            HangarCrewWidget = DynAccessor(259)
            HelpView = DynAccessor(260)
            MemberChangeView = DynAccessor(261)

            class _personal_case(DynAccessor):
                __slots__ = ()

                class _component(DynAccessor):
                    __slots__ = ()
                    ScrollWithLips = DynAccessor(262)
                    TankmanInfoWrapper = DynAccessor(263)

                component = _component()
                PersonalDataView = DynAccessor(264)
                PersonalFileView = DynAccessor(265)
                ServiceRecordView = DynAccessor(266)

            personal_case = _personal_case()

            class _popovers(DynAccessor):
                __slots__ = ()
                FilterPopoverView = DynAccessor(267)

            popovers = _popovers()
            QuickTrainingView = DynAccessor(268)
            TankChangeView = DynAccessor(269)
            TankmanChangeAndRecruitView = DynAccessor(270)
            TankmanContainerView = DynAccessor(271)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AdvancedTooltipView = DynAccessor(272)
                BunksConfirmDiscountTooltip = DynAccessor(273)
                CrewPerksAdditionalTooltip = DynAccessor(274)
                CrewPerksTooltip = DynAccessor(275)
                DismissedToggleTooltip = DynAccessor(276)
                ExperienceStepperTooltip = DynAccessor(277)
                PerkAvailableTooltip = DynAccessor(278)
                PremiumVehicleTooltip = DynAccessor(279)
                QuickTrainingDiscountTooltip = DynAccessor(280)
                TankmanChangePreviewTooltip = DynAccessor(281)
                TankmanTooltip = DynAccessor(282)
                TrainingLevelTooltip = DynAccessor(283)
                VehCmpSkillsTooltip = DynAccessor(284)
                VehicleParamsTooltipView = DynAccessor(285)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                CrewWidget = DynAccessor(286)
                FilterPanelWidget = DynAccessor(287)
                PriceList = DynAccessor(288)
                TankmanInfo = DynAccessor(289)

            widgets = _widgets()

        crew = _crew()

        class _crystalsPromo(DynAccessor):
            __slots__ = ()
            CrystalsPromoView = DynAccessor(290)

        crystalsPromo = _crystalsPromo()

        class _currency_reserves(DynAccessor):
            __slots__ = ()
            CurrencyReserves = DynAccessor(291)
            ReservesAwardView = DynAccessor(292)

        currency_reserves = _currency_reserves()

        class _customization(DynAccessor):
            __slots__ = ()
            CustomizationCart = DynAccessor(293)

            class _progression_styles(DynAccessor):
                __slots__ = ()
                OnboardingView = DynAccessor(294)
                StageSwitcher = DynAccessor(295)

            progression_styles = _progression_styles()

            class _progressive_items_reward(DynAccessor):
                __slots__ = ()
                ProgressiveItemsUpgradeView = DynAccessor(296)

            progressive_items_reward = _progressive_items_reward()

            class _progressive_items_view(DynAccessor):
                __slots__ = ()
                ProgressiveItemsView = DynAccessor(297)

            progressive_items_view = _progressive_items_view()

            class _style_unlocked_view(DynAccessor):
                __slots__ = ()
                StyleUnlockedView = DynAccessor(298)

            style_unlocked_view = _style_unlocked_view()

        customization = _customization()

        class _daily(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                RerollButton = DynAccessor(299)

            common = _common()
            DailyIntroScreenView = DynAccessor(300)
            DailyQuestPremiumTabView = DynAccessor(301)
            DailyQuestRegularTabView = DynAccessor(302)
            DailyQuestRerollView = DynAccessor(303)
            DailyQuestsRegularView = DynAccessor(304)
            DailyQuestsView = DynAccessor(305)
            DailyQuestWidget = DynAccessor(306)
            PlayStreakTabView = DynAccessor(307)
            PlayStreakView = DynAccessor(308)

            class _tooltips(DynAccessor):
                __slots__ = ()
                DailyQuestTooltip = DynAccessor(309)
                LockedSubscriptionBonusTooltip = DynAccessor(310)
                ModeSelectorTooltip = DynAccessor(311)
                PeriodicRewardsTooltip = DynAccessor(312)
                RandomGoodieTooltip = DynAccessor(313)
                RandomRewardsTooltip = DynAccessor(314)
                RerollTooltip = DynAccessor(315)

            tooltips = _tooltips()
            WeeklyRewardScreen = DynAccessor(316)

        daily = _daily()

        class _debutBoxes(DynAccessor):
            __slots__ = ()
            DebutBoxesBadgeTooltipView = DynAccessor(317)

        debutBoxes = _debutBoxes()

        class _dedication(DynAccessor):
            __slots__ = ()
            DedicationRewardView = DynAccessor(318)

        dedication = _dedication()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            DedicationTooltip = DynAccessor(319)
            DogTagsView = DynAccessor(320)
            RankedEfficiencyTooltip = DynAccessor(321)
            ThreeMonthsTooltip = DynAccessor(322)
            TriumphTooltip = DynAccessor(323)

        dog_tags = _dog_tags()

        class _early_access(DynAccessor):
            __slots__ = ()
            EarlyAccessBuyView = DynAccessor(324)
            EarlyAccessEntryPointView = DynAccessor(325)
            EarlyAccessIntroView = DynAccessor(326)
            EarlyAccessQuestsView = DynAccessor(327)
            EarlyAccessRewardsView = DynAccessor(328)
            EarlyAccessVehicleView = DynAccessor(329)

            class _tooltips(DynAccessor):
                __slots__ = ()
                EarlyAccessCommonDescriptionTooltip = DynAccessor(330)
                EarlyAccessCompensationTooltip = DynAccessor(331)
                EarlyAccessCurrencyTooltipView = DynAccessor(332)
                EarlyAccessEntryPointPausedTooltip = DynAccessor(333)
                EarlyAccessEntryPointTooltipView = DynAccessor(334)
                EarlyAccessSimpleTooltipView = DynAccessor(335)
                EarlyAccessTokensStepperTooltip = DynAccessor(336)
                EarlyAccessVehicleCarouselPausedTooltip = DynAccessor(337)
                EarlyAccessVehicleLockedTooltip = DynAccessor(338)

            tooltips = _tooltips()

        early_access = _early_access()

        class _elite_window(DynAccessor):
            __slots__ = ()
            EliteView = DynAccessor(339)

        elite_window = _elite_window()

        class _excluded_maps(DynAccessor):
            __slots__ = ()
            ExcludedMapsView = DynAccessor(340)

        excluded_maps = _excluded_maps()

        class _frontline(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(341)

            class _dialogs(DynAccessor):
                __slots__ = ()
                BlankPrice = DynAccessor(342)

            dialogs = _dialogs()
            IntroScreen = DynAccessor(343)
            RewardsSelectionView = DynAccessor(344)

        frontline = _frontline()

        class _hangar(DynAccessor):
            __slots__ = ()

            class _subViews(DynAccessor):
                __slots__ = ()
                VehicleParams = DynAccessor(345)

            subViews = _subViews()
            VehicleParamsWidget = DynAccessor(346)

        hangar = _hangar()

        class _instructions(DynAccessor):
            __slots__ = ()
            BuyWindow = DynAccessor(347)
            SellWindow = DynAccessor(348)

        instructions = _instructions()

        class _mapbox(DynAccessor):
            __slots__ = ()
            MapBoxAwardsView = DynAccessor(349)
            MapBoxEntryPointView = DynAccessor(350)
            MapBoxIntro = DynAccessor(351)
            MapBoxProgression = DynAccessor(352)
            MapBoxRewardChoiceView = DynAccessor(353)
            MapBoxSurveyView = DynAccessor(354)

        mapbox = _mapbox()

        class _maps_training(DynAccessor):
            __slots__ = ()
            MapPointDescriptionTooltip = DynAccessor(355)
            MapsTrainingPage = DynAccessor(356)
            MapsTrainingQueue = DynAccessor(357)
            MapsTrainingResult = DynAccessor(358)
            ScenarioTooltip = DynAccessor(359)

        maps_training = _maps_training()

        class _matchmaker(DynAccessor):
            __slots__ = ()
            ActiveTestConfirmView = DynAccessor(363)

        matchmaker = _matchmaker()

        class _mode_selector(DynAccessor):
            __slots__ = ()
            BattleSessionView = DynAccessor(371)
            ModeSelectorView = DynAccessor(372)

            class _popovers(DynAccessor):
                __slots__ = ()
                RandomBattlePopover = DynAccessor(373)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                AlertTooltip = DynAccessor(374)

                class _common(DynAccessor):
                    __slots__ = ()
                    Divider = DynAccessor(375)
                    GradientDecorator = DynAccessor(376)

                common = _common()
                SimplyFormatTooltip = DynAccessor(377)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                BattleRoyaleProgressionWidget = DynAccessor(378)
                BattleRoyaleWidget = DynAccessor(379)
                EpicWidget = DynAccessor(380)
                RankedWidget = DynAccessor(381)

            widgets = _widgets()

        mode_selector = _mode_selector()

        class _notifications(DynAccessor):
            __slots__ = ()
            PlayStreakRewards = DynAccessor(382)

        notifications = _notifications()

        class _offers(DynAccessor):
            __slots__ = ()
            OfferBannerWindow = DynAccessor(383)
            OfferGiftsWindow = DynAccessor(384)
            OfferRewardWindow = DynAccessor(385)

        offers = _offers()

        class _paragons(DynAccessor):
            __slots__ = ()
            ChapterRewardsView = DynAccessor(386)

            class _common(DynAccessor):
                __slots__ = ()
                Header = DynAccessor(387)
                VehicleName = DynAccessor(388)

            common = _common()
            IntroView = DynAccessor(389)
            NavigationView = DynAccessor(390)
            ParagonsRewardsView = DynAccessor(391)
            ResetBranchView = DynAccessor(392)
            SelectRewardsView = DynAccessor(393)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BlueprintUniversalTooltip = DynAccessor(394)
                BranchSelectTooltip = DynAccessor(395)
                EntryPointTooltip = DynAccessor(396)
                PointsTooltip = DynAccessor(397)
                ResetBranchTooltip = DynAccessor(398)
                ResetButtonTooltip = DynAccessor(399)
                RewardsHeaderTooltip = DynAccessor(400)
                SelectedRewardsTooltip = DynAccessor(401)
                VehicleSelectTooltip = DynAccessor(402)

            tooltips = _tooltips()

        paragons = _paragons()

        class _personal_missions(DynAccessor):
            __slots__ = ()
            PersonalMissionsIntroVideoView = DynAccessor(403)
            PersonalMissionsIntroView = DynAccessor(404)
            PersonalMissionsMainQuestsView = DynAccessor(405)
            PersonalMissionsOperationsView = DynAccessor(406)
            PersonalMissionsQuestResetView = DynAccessor(407)
            PersonalMissionsRewardsSelectionView = DynAccessor(408)
            PersonalMissionsRewardsView = DynAccessor(409)
            PersonalMissionsVehicleView = DynAccessor(410)
            PersonalMissionsVideoRewardsView = DynAccessor(411)

            class _tooltips(DynAccessor):
                __slots__ = ()
                PersonalMissionsLastOperationTooltip = DynAccessor(412)
                PersonalMissionsOperationsTooltip = DynAccessor(413)
                PersonalMissionsQuestInfoTooltip = DynAccessor(414)
                PersonalMissionsQuestsTypeTooltip = DynAccessor(415)
                QuestCardTooltip = DynAccessor(416)
                RestRewardsTooltipView = DynAccessor(417)
                VehicleTabsTooltip = DynAccessor(418)

            tooltips = _tooltips()

        personal_missions = _personal_missions()

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            PersonalReservesTooltip = DynAccessor(419)
            PersonalReservesWidget = DynAccessor(420)
            ReserveCard = DynAccessor(421)
            ReserveCardTooltip = DynAccessor(422)
            ReserveGroup = DynAccessor(423)
            ReservesActivationView = DynAccessor(424)
            ReservesConversionView = DynAccessor(425)
            ReservesIntroView = DynAccessor(426)

        personal_reserves = _personal_reserves()

        class _platoon(DynAccessor):
            __slots__ = ()
            AlertTooltip = DynAccessor(427)
            MembersWindow = DynAccessor(428)
            PlatoonDropdown = DynAccessor(429)
            SearchingDropdown = DynAccessor(430)
            SettingsPopover = DynAccessor(431)

            class _subViews(DynAccessor):
                __slots__ = ()
                Chat = DynAccessor(432)
                SettingsContent = DynAccessor(433)
                TiersLimit = DynAccessor(434)

            subViews = _subViews()
            WTRTooltip = DynAccessor(435)

        platoon = _platoon()

        class _player_subscriptions(DynAccessor):
            __slots__ = ()
            PlayerSubscriptions = DynAccessor(436)
            SubscriptionItem = DynAccessor(437)
            SubscriptionRewardView = DynAccessor(438)

        player_subscriptions = _player_subscriptions()

        class _pm_announce(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                PersonalMissionsNewCampaignTooltipView = DynAccessor(439)
                PersonalMissionsOldCampaignTooltipView = DynAccessor(440)

            tooltips = _tooltips()

        pm_announce = _pm_announce()

        class _poll(DynAccessor):
            __slots__ = ()
            PollView = DynAccessor(441)

        poll = _poll()

        class _promo_code_reward_screen(DynAccessor):
            __slots__ = ()
            PromoCodeRewardScreenView = DynAccessor(442)

        promo_code_reward_screen = _promo_code_reward_screen()

        class _research(DynAccessor):
            __slots__ = ()
            BuyModuleDialogView = DynAccessor(452)
            InsufficientCreditsTooltip = DynAccessor(453)
            SoldModuleInfoTooltip = DynAccessor(454)

        research = _research()

        class _resource_well(DynAccessor):
            __slots__ = ()
            AwardView = DynAccessor(455)
            CompletedProgressionView = DynAccessor(456)
            EntryPoint = DynAccessor(457)
            IntroView = DynAccessor(458)
            NoSerialVehiclesConfirm = DynAccessor(459)
            NoVehiclesConfirm = DynAccessor(460)
            ProgressionView = DynAccessor(461)
            ResourcesLoadingConfirm = DynAccessor(462)
            ResourcesLoadingView = DynAccessor(463)

            class _sharedComponents(DynAccessor):
                __slots__ = ()

                class _award(DynAccessor):
                    __slots__ = ()
                    AdditionalReward = DynAccessor(464)
                    Footer = DynAccessor(465)
                    Header = DynAccessor(466)
                    Reward = DynAccessor(467)

                award = _award()
                Counter = DynAccessor(468)
                NoVehiclesState = DynAccessor(469)
                Resource = DynAccessor(470)
                VehicleCount = DynAccessor(471)
                VehicleInfo = DynAccessor(472)

            sharedComponents = _sharedComponents()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(473)
                MaxProgressTooltip = DynAccessor(474)
                ProgressTooltip = DynAccessor(475)
                RefundResourcesTooltip = DynAccessor(476)
                SerialNumberTooltip = DynAccessor(477)

            tooltips = _tooltips()

        resource_well = _resource_well()

        class _seniority_awards(DynAccessor):
            __slots__ = ()
            SeniorityAwardsView = DynAccessor(478)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                SeniorityAwardCoin = DynAccessor(479)

            sharedComponents = _sharedComponents()

        seniority_awards = _seniority_awards()

        class _shop_sales(DynAccessor):
            __slots__ = ()
            ShopSalesEntryPointView = DynAccessor(480)

        shop_sales = _shop_sales()

        class _stronghold(DynAccessor):
            __slots__ = ()
            StrongholdEntryPointView = DynAccessor(481)

        stronghold = _stronghold()

        class _subscription(DynAccessor):
            __slots__ = ()
            SubscriptionAwardView = DynAccessor(482)
            SubscriptionDailyQuestsIntro = DynAccessor(483)
            WotPlusIntroView = DynAccessor(484)
            WotPlusTooltip = DynAccessor(485)

        subscription = _subscription()

        class _tanksetup(DynAccessor):
            __slots__ = ()
            AmmunitionPanel = DynAccessor(486)

            class _common(DynAccessor):
                __slots__ = ()
                Action = DynAccessor(487)
                AutoRenewalDropdown = DynAccessor(488)
                CtaButtons = DynAccessor(489)
                DealPanel = DynAccessor(490)
                ExtraImage = DynAccessor(491)
                FormatColorTagText = DynAccessor(492)
                MaybeWrapper = DynAccessor(493)
                Price = DynAccessor(494)
                SetupApp = DynAccessor(495)
                ShortenedText = DynAccessor(496)
                Slider = DynAccessor(497)

                class _SlotParts(DynAccessor):
                    __slots__ = ()
                    Bonus = DynAccessor(498)
                    Container = DynAccessor(499)
                    Count = DynAccessor(500)
                    Inside = DynAccessor(501)
                    Level = DynAccessor(502)

                SlotParts = _SlotParts()
                Specializations = DynAccessor(503)
                Storage = DynAccessor(504)
                SwitchButton = DynAccessor(505)
                SwitchEquipment = DynAccessor(506)

                class _Transitions(DynAccessor):
                    __slots__ = ()
                    SlotTransitions = DynAccessor(507)

                Transitions = _Transitions()
                WeaponOccupancy = DynAccessor(508)

            common = _common()
            DeconstructionDeviceView = DynAccessor(509)

            class _dialogs(DynAccessor):
                __slots__ = ()
                Confirm = DynAccessor(510)
                ConfirmActionsWithEquipmentDialog = DynAccessor(511)
                DeconstructConfirm = DynAccessor(512)
                DeviceUpgradeDialog = DynAccessor(513)
                ExchangeToBuyItems = DynAccessor(514)
                ExchangeToUpgradeItems = DynAccessor(515)
                NeedRepair = DynAccessor(516)
                RefillShells = DynAccessor(517)
                Sell = DynAccessor(518)

                class _sub_views(DynAccessor):
                    __slots__ = ()
                    FrontlineConfirmFooterMoney = DynAccessor(519)
                    FrontlineConfirmIcons = DynAccessor(520)
                    FrontlineConfirmMultipleNames = DynAccessor(521)
                    FrontlineConfirmTitle = DynAccessor(522)

                sub_views = _sub_views()

            dialogs = _dialogs()
            HangarAmmunitionSetup = DynAccessor(523)
            IntroScreen = DynAccessor(524)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AbilitySkillAdditionalTooltip = DynAccessor(525)
                AbilitySkillTooltip = DynAccessor(526)
                DeconstructFromInventoryTooltip = DynAccessor(527)
                DeconstructFromVehicleTooltip = DynAccessor(528)
                SetupTabTooltipView = DynAccessor(529)
                WarningTooltipView = DynAccessor(530)

            tooltips = _tooltips()
            VehicleCompareAmmunitionPanel = DynAccessor(531)
            VehicleCompareAmmunitionSetup = DynAccessor(532)

        tanksetup = _tanksetup()

        class _techtree(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                ParagonsEntryPointTooltip = DynAccessor(533)
                ParagonsLockedTooltip = DynAccessor(534)

            tooltips = _tooltips()
            VehicleTechTree = DynAccessor(535)

        techtree = _techtree()

        class _universal_flag(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(540)

            tooltips = _tooltips()
            UniversalFlagEntryPointView = DynAccessor(541)

        universal_flag = _universal_flag()

        class _vehicle_compare(DynAccessor):
            __slots__ = ()
            CompareModificationsPanelView = DynAccessor(542)
            SelectSlotSpecCompareDialog = DynAccessor(543)

        vehicle_compare = _vehicle_compare()

        class _vehicle_preview(DynAccessor):
            __slots__ = ()

            class _buying_panel(DynAccessor):
                __slots__ = ()
                EarlyAccessPanel = DynAccessor(544)
                StyleBuyingPanel = DynAccessor(545)
                VPProgressionStylesBuyingPanel = DynAccessor(546)
                WellPanel = DynAccessor(547)

            buying_panel = _buying_panel()

            class _tooltips(DynAccessor):
                __slots__ = ()
                StatTrackTooltip = DynAccessor(548)

            tooltips = _tooltips()

            class _top_panel(DynAccessor):
                __slots__ = ()
                TopPanelTabs = DynAccessor(549)

            top_panel = _top_panel()

        vehicle_preview = _vehicle_preview()

        class _veh_post_progression(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                Bonus = DynAccessor(550)
                Description = DynAccessor(551)
                Grid = DynAccessor(552)
                PersistentBonuses = DynAccessor(553)
                Slide = DynAccessor(554)
                SlideContent = DynAccessor(555)
                Slider = DynAccessor(556)
                TextSplit = DynAccessor(557)

            common = _common()
            PostProgressionInfo = DynAccessor(558)
            PostProgressionIntro = DynAccessor(559)
            PostProgressionResearchSteps = DynAccessor(560)

            class _tooltip(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()
                    DisabledBlock = DynAccessor(561)
                    FeatureLevelSubtitle = DynAccessor(562)
                    Lock = DynAccessor(563)
                    NotEnoughCredits = DynAccessor(564)
                    PriceBlock = DynAccessor(565)
                    Separator = DynAccessor(566)

                common = _common()
                PairModificationTooltipView = DynAccessor(567)
                PostProgressionLevelTooltipView = DynAccessor(568)
                RoleSlotTooltipView = DynAccessor(569)
                SetupTooltipView = DynAccessor(570)

            tooltip = _tooltip()
            VehiclePostProgressionCmpView = DynAccessor(571)
            VehiclePostProgressionView = DynAccessor(572)

        veh_post_progression = _veh_post_progression()

    lobby = _lobby()

    class _test_check_box_view(DynAccessor):
        __slots__ = ()
        TestCheckBoxView = DynAccessor(60)

    test_check_box_view = _test_check_box_view()

    class _test_text_button_view(DynAccessor):
        __slots__ = ()
        TestTextButtonView = DynAccessor(61)

    test_text_button_view = _test_text_button_view()

    class _windows_layout_view(DynAccessor):
        __slots__ = ()
        WindowsLayountView = DynAccessor(62)

    windows_layout_view = _windows_layout_view()

    class _blend_mode(DynAccessor):
        __slots__ = ()

        class _blend_mode(DynAccessor):
            __slots__ = ()
            BlendMode = DynAccessor(63)

        blend_mode = _blend_mode()

    blend_mode = _blend_mode()

    class _demo_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _demo_window_content(DynAccessor):
                __slots__ = ()
                DemoWindowContent = DynAccessor(64)
                ImageProps = DynAccessor(65)

            demo_window_content = _demo_window_content()

            class _demo_window_details_panel(DynAccessor):
                __slots__ = ()
                DemoWindowDetailsPanel = DynAccessor(66)

            demo_window_details_panel = _demo_window_details_panel()

            class _demo_window_image_panel(DynAccessor):
                __slots__ = ()
                DemoWindowImagePanel = DynAccessor(67)

            demo_window_image_panel = _demo_window_image_panel()

            class _image_preview_window_content(DynAccessor):
                __slots__ = ()
                ImagePreviewWindowContent = DynAccessor(68)

            image_preview_window_content = _image_preview_window_content()

        views = _views()

    demo_view = _demo_view()

    class _examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_dialogs_view(DynAccessor):
                __slots__ = ()
                TestDialogsView = DynAccessor(69)

            test_dialogs_view = _test_dialogs_view()

            class _test_expr_functions_view(DynAccessor):
                __slots__ = ()
                TestExprFunctionsView = DynAccessor(70)

            test_expr_functions_view = _test_expr_functions_view()

            class _test_sub_view(DynAccessor):
                __slots__ = ()
                TestSubView = DynAccessor(71)

            test_sub_view = _test_sub_view()

            class _test_view(DynAccessor):
                __slots__ = ()
                TestView = DynAccessor(72)

            test_view = _test_view()

            class _unbound_example(DynAccessor):
                __slots__ = ()
                UnboundExample = DynAccessor(73)

            unbound_example = _unbound_example()

        views = _views()

    examples = _examples()

    class _list_examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _list_examples_empty_render_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesEmptyRenderWindowContent = DynAccessor(74)

            list_examples_empty_render_window_content = _list_examples_empty_render_window_content()

            class _list_examples_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesWindowContent = DynAccessor(75)

            list_examples_window_content = _list_examples_window_content()

        views = _views()

    list_examples = _list_examples()

    class _rotation_pivot_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_pivot_view(DynAccessor):
                __slots__ = ()
                RotationAndPivotTestView = DynAccessor(76)

            rotation_pivot_view = _rotation_pivot_view()

        views = _views()

    rotation_pivot_view = _rotation_pivot_view()

    class _rotation_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_view(DynAccessor):
                __slots__ = ()
                RotationTestView = DynAccessor(77)

            rotation_view = _rotation_view()

        views = _views()

    rotation_view = _rotation_view()

    class _scale_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _scale_view(DynAccessor):
                __slots__ = ()
                ScaleTestView = DynAccessor(78)

            scale_view = _scale_view()

        views = _views()

    scale_view = _scale_view()

    class _test_uikit_buttons_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_buttons_view(DynAccessor):
                __slots__ = ()
                TestUikitButtonsView = DynAccessor(79)

            test_uikit_buttons_view = _test_uikit_buttons_view()

        views = _views()

    test_uikit_buttons_view = _test_uikit_buttons_view()

    class _test_uikit_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_view(DynAccessor):
                __slots__ = ()
                TestUikitView = DynAccessor(80)

            test_uikit_view = _test_uikit_view()

        views = _views()

    test_uikit_view = _test_uikit_view()

    class _wtypes_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _wtypes_demo_window_content(DynAccessor):
                __slots__ = ()
                WtypesDemoWindowContent = DynAccessor(81)

            wtypes_demo_window_content = _wtypes_demo_window_content()

        views = _views()

    wtypes_view = _wtypes_view()

    class _dialogs(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            DialogTemplateGenericTooltip = DynAccessor(92)

        common = _common()
        DefaultDialog = DynAccessor(93)

        class _sub_views(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                SimpleText = DynAccessor(94)
                SinglePrice = DynAccessor(95)

            common = _common()

            class _content(DynAccessor):
                __slots__ = ()
                SelectOptionContent = DynAccessor(96)
                SimpleTextContent = DynAccessor(97)
                SinglePriceContent = DynAccessor(98)
                TextWithWarning = DynAccessor(99)

            content = _content()

            class _footer(DynAccessor):
                __slots__ = ()
                BRSinglePriceFooter = DynAccessor(100)
                SimpleTextFooter = DynAccessor(101)
                SinglePriceFooter = DynAccessor(102)

            footer = _footer()

            class _icon(DynAccessor):
                __slots__ = ()
                IconSet = DynAccessor(103)

            icon = _icon()

            class _title(DynAccessor):
                __slots__ = ()
                SimpleTextTitle = DynAccessor(104)

            title = _title()

            class _topRight(DynAccessor):
                __slots__ = ()
                BRMoneyBalance = DynAccessor(105)
                MoneyBalance = DynAccessor(106)

            topRight = _topRight()

        sub_views = _sub_views()

        class _widgets(DynAccessor):
            __slots__ = ()
            SinglePrice = DynAccessor(107)

        widgets = _widgets()

    dialogs = _dialogs()

    class _loading(DynAccessor):
        __slots__ = ()
        GameLoadingView = DynAccessor(108)

    loading = _loading()

    class _armory_yard(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                ArmoryYardBundlesView = DynAccessor(573)
                ArmoryYardBuyBundleView = DynAccessor(574)
                ArmoryYardBuyView = DynAccessor(575)
                ArmoryYardEntryPointView = DynAccessor(576)
                ArmoryYardIntroView = DynAccessor(577)
                ArmoryYardMainView = DynAccessor(578)
                ArmoryYardPostProgressionBuyView = DynAccessor(579)
                ArmoryYardRewardsView = DynAccessor(580)
                ArmoryYardShopBuyView = DynAccessor(581)
                ArmoryYardShopRewardsView = DynAccessor(582)
                ArmoryYardShopView = DynAccessor(583)
                ArmoryYardVideoRewardView = DynAccessor(584)
                ArmoryYardWidgetView = DynAccessor(585)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ArmoryYardCurrencyTooltipView = DynAccessor(586)
                    ArmoryYardSimpleTooltipView = DynAccessor(587)
                    ArmoryYardTokenStepperTooltipView = DynAccessor(588)
                    ArmoryYardWalletNotAvailableTooltipView = DynAccessor(589)
                    EntryPointActiveTooltipView = DynAccessor(590)
                    EntryPointBeforeProgressionTooltipView = DynAccessor(591)
                    EntryPointNotActiveTooltipView = DynAccessor(592)
                    RestRewardTooltipView = DynAccessor(593)
                    ShopCurrencyTooltipView = DynAccessor(594)
                    TaskConditionTooltipView = DynAccessor(595)

                tooltips = _tooltips()

            feature = _feature()

        lobby = _lobby()

    armory_yard = _armory_yard()

    class _battle_modifiers(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                ModifiersDomainTooltipView = DynAccessor(596)

            tooltips = _tooltips()

        lobby = _lobby()

    battle_modifiers = _battle_modifiers()

    class _battle_royale(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _views(DynAccessor):
                __slots__ = ()
                LeaveBattleView = DynAccessor(597)

            views = _views()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BrCoinTooltipView = DynAccessor(598)

                class _common(DynAccessor):
                    __slots__ = ()

                    class _LeaderBoard(DynAccessor):
                        __slots__ = ()
                        Column = DynAccessor(599)
                        Table = DynAccessor(600)

                    LeaderBoard = _LeaderBoard()
                    PriceBlock = DynAccessor(601)
                    RentPrice = DynAccessor(602)

                common = _common()
                LeaderboardRewardTooltipView = DynAccessor(603)
                RentIconTooltipView = DynAccessor(604)
                RespawnInfoTooltipView = DynAccessor(605)
                RewardCurrencyTooltipView = DynAccessor(606)
                TestDriveInfoTooltipView = DynAccessor(607)
                VehicleTooltipView = DynAccessor(608)
                WidgetTooltipView = DynAccessor(609)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                BattleRoyaleEntryPoint = DynAccessor(610)
                IntroView = DynAccessor(611)
                PreBattleView = DynAccessor(612)
                ProxyCurrencyView = DynAccessor(613)
                WidgetView = DynAccessor(614)

            views = _views()

        lobby = _lobby()

    battle_royale = _battle_royale()

    class _battle_royale_progression(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(615)
        ProgressionMainView = DynAccessor(616)

    battle_royale_progression = _battle_royale_progression()

    class _cosmic_event(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _cosmic_hud(DynAccessor):
                __slots__ = ()
                CosmicBattleHelpView = DynAccessor(617)
                CosmicReactHudView = DynAccessor(618)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    AbilityTooltip = DynAccessor(619)

                tooltips = _tooltips()

            cosmic_hud = _cosmic_hud()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _banner_entry_point(DynAccessor):
                __slots__ = ()
                CosmicBannerEntryPoint = DynAccessor(620)

            banner_entry_point = _banner_entry_point()

            class _cosmic_lobby_view(DynAccessor):
                __slots__ = ()
                CosmicLobbyView = DynAccessor(621)

            cosmic_lobby_view = _cosmic_lobby_view()

            class _cosmic_post_battle(DynAccessor):
                __slots__ = ()
                CosmicPostBattleView = DynAccessor(622)

            cosmic_post_battle = _cosmic_post_battle()

            class _queue_view(DynAccessor):
                __slots__ = ()
                QueueView = DynAccessor(623)

            queue_view = _queue_view()

            class _rewards_view(DynAccessor):
                __slots__ = ()
                RewardsView = DynAccessor(624)

            rewards_view = _rewards_view()

            class _tooltips(DynAccessor):
                __slots__ = ()
                CosmicSimpleTooltip = DynAccessor(625)
                CosmicTooltipDecorator = DynAccessor(626)
                DailyQuestsTooltip = DynAccessor(627)
                ProgressionEntryPointTooltip = DynAccessor(628)
                RulesEntryPointTooltip = DynAccessor(629)
                SpecificationTooltip = DynAccessor(630)
                VehicleAbilityTooltip = DynAccessor(631)
                VehicleSelectorTooltip = DynAccessor(632)
                VehicleShellTooltip = DynAccessor(633)

            tooltips = _tooltips()

        lobby = _lobby()

    cosmic_event = _cosmic_event()

    class _frontline(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            BannerView = DynAccessor(634)
            FrontlineContainerView = DynAccessor(635)
            InfoView = DynAccessor(636)
            ProgressView = DynAccessor(637)
            RewardsView = DynAccessor(638)
            SkillsView = DynAccessor(639)

            class _tooltips(DynAccessor):
                __slots__ = ()
                LevelReservesTooltip = DynAccessor(640)
                NotEnoughPointsTooltip = DynAccessor(641)
                SkillOrderTooltip = DynAccessor(642)

            tooltips = _tooltips()
            WelcomeView = DynAccessor(643)

        lobby = _lobby()

    frontline = _frontline()

    class _fun_random(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                FunRandomEntryPointView = DynAccessor(644)
                FunRandomHangarWidgetView = DynAccessor(645)
                FunRandomMapsView = DynAccessor(646)
                FunRandomModeSubSelector = DynAccessor(647)
                FunRandomModifiersPanel = DynAccessor(648)
                FunRandomProgression = DynAccessor(649)

            feature = _feature()

            class _tooltips(DynAccessor):
                __slots__ = ()
                FunRandomMapsDomainTooltip = DynAccessor(650)
                FunRandomProgressionTooltipView = DynAccessor(651)

            tooltips = _tooltips()

        lobby = _lobby()

    fun_random = _fun_random()

    class _gui_lootboxes(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _gui_lootboxes(DynAccessor):
                __slots__ = ()
                BonusProbabilitiesView = DynAccessor(652)
                EntryPointView = DynAccessor(653)
                KeysWelcomeScreen = DynAccessor(654)
                LootBoxesLoseRewardScreen = DynAccessor(655)
                LootboxRewardsView = DynAccessor(656)
                LootboxVideoRewardView = DynAccessor(657)
                OpenBoxErrorView = DynAccessor(658)

                class _shared(DynAccessor):
                    __slots__ = ()
                    AnimationControls = DynAccessor(659)
                    BacklitTransparentButton = DynAccessor(660)
                    BuyBoxFooter = DynAccessor(661)
                    CanvasSequence = DynAccessor(662)
                    CloseBtn = DynAccessor(663)
                    Compensation = DynAccessor(664)
                    CurrencyKey = DynAccessor(665)
                    Divider = DynAccessor(666)
                    Header = DynAccessor(667)
                    RotationReward = DynAccessor(668)
                    RotationVehicle = DynAccessor(669)
                    Video = DynAccessor(670)
                    VideoComponent = DynAccessor(671)

                shared = _shared()
                StorageView = DynAccessor(672)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    BonusGroupTooltip = DynAccessor(673)
                    CompensationTooltip = DynAccessor(674)
                    GuaranteedRewardTooltip = DynAccessor(675)
                    LootboxKeyTooltip = DynAccessor(676)
                    LootboxRotationTooltip = DynAccessor(677)
                    LootboxTooltip = DynAccessor(678)
                    LootboxTooltipExtended = DynAccessor(679)
                    ProbabilityButtonTooltip = DynAccessor(680)
                    ProbabilityGuaranteedRewardTooltip = DynAccessor(681)
                    ProbabilityStageButtonsTooltip = DynAccessor(682)

                tooltips = _tooltips()
                WelcomeScreen = DynAccessor(683)

            gui_lootboxes = _gui_lootboxes()

        lobby = _lobby()

    gui_lootboxes = _gui_lootboxes()

    class _portal(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            PortalHudWidgetView = DynAccessor(684)

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _battle_result(DynAccessor):
                __slots__ = ()
                PortalBattleResultView = DynAccessor(685)

            battle_result = _battle_result()
            ComplexityUnlockView = DynAccessor(686)
            MembersWindow = DynAccessor(687)
            PortalBannerEntryPoint = DynAccessor(688)
            PortalBattleQueueView = DynAccessor(689)
            PortalLobbyView = DynAccessor(690)
            PortalRewardsView = DynAccessor(691)
            PortalUpgradeInfoView = DynAccessor(692)
            PortalUpgradeResetView = DynAccessor(693)
            PortalUpgradeView = DynAccessor(694)
            ProgressionView = DynAccessor(695)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AbilitiesTooltip = DynAccessor(696)
                BannerTooltip = DynAccessor(697)
                BattleResultStatTooltip = DynAccessor(698)
                ComplexityTooltip = DynAccessor(699)
                ModulesTooltip = DynAccessor(700)
                ParamsTooltip = DynAccessor(701)
                ProgressTokenTooltip = DynAccessor(702)
                RepairKitTooltip = DynAccessor(703)
                ShellTooltip = DynAccessor(704)
                UpgradeInfoTooltip = DynAccessor(705)
                VehicleTooltip = DynAccessor(706)

            tooltips = _tooltips()
            VideoView = DynAccessor(707)

        lobby = _lobby()

    portal = _portal()

    class _story_mode(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            EpilogueWindow = DynAccessor(708)
            OnboardingBattleResultView = DynAccessor(709)
            PrebattleWindow = DynAccessor(710)

        battle = _battle()

        class _common(DynAccessor):
            __slots__ = ()
            CongratulationsWindow = DynAccessor(711)
            MedalTooltip = DynAccessor(712)
            OnboardingQueueView = DynAccessor(713)

        common = _common()

        class _lobby(DynAccessor):
            __slots__ = ()
            BattleResultView = DynAccessor(714)
            MissionSelectionView = DynAccessor(715)
            MissionTooltip = DynAccessor(716)

        lobby = _lobby()

    story_mode = _story_mode()

    class _survey(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _survey(DynAccessor):
                __slots__ = ()
                SurveyView = DynAccessor(717)

            survey = _survey()

        lobby = _lobby()

    survey = _survey()

    class _winback(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(718)

        class _lobby(DynAccessor):
            __slots__ = ()

            class _popovers(DynAccessor):
                __slots__ = ()
                WinbackLeaveModePopoverView = DynAccessor(719)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                CompensationTooltip = DynAccessor(720)
                ModeInfoTooltip = DynAccessor(721)
                SelectableRewardTooltip = DynAccessor(722)
                SelectedRewardsTooltip = DynAccessor(723)
                WidgetTooltipView = DynAccessor(724)

            tooltips = _tooltips()
            WinbackDailyQuestsIntroView = DynAccessor(725)
            WinbackIntroView = DynAccessor(726)
            WinbackLeaveModeDialogView = DynAccessor(727)
            WinbackRewardView = DynAccessor(728)
            WinbackSelectableRewardView = DynAccessor(729)
            WinbackWidgetView = DynAccessor(730)

        lobby = _lobby()
        ProgressionMainView = DynAccessor(731)

    winback = _winback()
    Anchor = DynAccessor(732)
    ArmoryYardDemoView = DynAccessor(733)

    class _child_views_demo(DynAccessor):
        __slots__ = ()
        ChildDemoView = DynAccessor(734)
        MainView = DynAccessor(735)

    child_views_demo = _child_views_demo()
    ClientgwMockView = DynAccessor(736)
    Comp7DemoPageView = DynAccessor(737)
    ComponentsDemo = DynAccessor(738)
    DataLayerDemoView = DynAccessor(739)
    DataTrackerDemo = DynAccessor(740)
    DemoContextMenu = DynAccessor(741)
    Easings = DynAccessor(742)
    GameLoadingDebugView = DynAccessor(743)
    GFCharset = DynAccessor(744)
    GFComponents = DynAccessor(745)
    GFDemoPopover = DynAccessor(746)
    GFDemoRichTooltipWindow = DynAccessor(747)
    GFDemoWindow = DynAccessor(748)
    GFHooksDemo = DynAccessor(749)
    GFInjectView = DynAccessor(750)
    GFInputCases = DynAccessor(751)
    GfMarkerDemoView = DynAccessor(752)
    GFSimpleTooltipWindow = DynAccessor(753)
    GFWebSubDemoWindow = DynAccessor(754)

    class _gf_dialogs_demo(DynAccessor):
        __slots__ = ()
        DefaultDialogProxy = DynAccessor(755)
        GFDialogsDemo = DynAccessor(756)

        class _sub_views(DynAccessor):
            __slots__ = ()
            DummyContent = DynAccessor(757)
            DummyFooter = DynAccessor(758)
            DummyIcon = DynAccessor(759)
            DummyStepper = DynAccessor(760)
            DummyTitle = DynAccessor(761)
            DummyTopRight = DynAccessor(762)

        sub_views = _sub_views()

    gf_dialogs_demo = _gf_dialogs_demo()

    class _gf_viewer(DynAccessor):
        __slots__ = ()
        GFViewerWindow = DynAccessor(763)

    gf_viewer = _gf_viewer()

    class _igb_demo(DynAccessor):
        __slots__ = ()
        BrowserFullscreenWindow = DynAccessor(764)
        BrowserWindow = DynAccessor(765)
        MainView = DynAccessor(766)

    igb_demo = _igb_demo()
    LocaleDemo = DynAccessor(767)
    MediaWrapperDemo = DynAccessor(768)
    MixBlendMode = DynAccessor(769)
    MixBlendModeAnimation = DynAccessor(770)
    ModeSelectorDemo = DynAccessor(771)
    ModeSelectorToolsetView = DynAccessor(772)

    class _mttv(DynAccessor):
        __slots__ = ()
        CustomView = DynAccessor(773)
        MttvEntityView = DynAccessor(774)
        MttvKeyframeInfoView = DynAccessor(775)
        MttvKeyframeView = DynAccessor(776)
        MttvTimelineView = DynAccessor(777)
        MttvToolsView = DynAccessor(778)

    mttv = _mttv()
    NewYearLevelUp = DynAccessor(779)
    PluralLocView = DynAccessor(780)
    PropsSupportDemo = DynAccessor(781)
    ReactSpringVizualizer = DynAccessor(782)
    SelectableRewardDemoView = DynAccessor(783)
    StructuralDataBindDemo = DynAccessor(784)

    class _sub_views_demo(DynAccessor):
        __slots__ = ()
        GFSubViewsDemo = DynAccessor(785)

        class _sub_views(DynAccessor):
            __slots__ = ()
            CustomizationCartProxy = DynAccessor(786)
            DailyProxy = DynAccessor(787)
            ProgressiveItemsViewProxy = DynAccessor(788)

        sub_views = _sub_views()

    sub_views_demo = _sub_views_demo()
    SurfaceView = DynAccessor(789)
    UILoggerDemo = DynAccessor(790)
    VideoSupportView = DynAccessor(791)
    W2CTestPageWindow = DynAccessor(792)