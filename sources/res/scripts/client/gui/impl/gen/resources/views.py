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
            BattleNotifierView = DynAccessor(88)

        battle_notifier = _battle_notifier()

        class _battle_page(DynAccessor):
            __slots__ = ()
            EpicRespawnAmmunitionPanelView = DynAccessor(89)
            PersonalReservesTabView = DynAccessor(90)
            PrebattleAmmunitionPanelView = DynAccessor(91)
            PrebattleCarouselView = DynAccessor(92)

        battle_page = _battle_page()

        class _timer(DynAccessor):
            __slots__ = ()
            TimerView = DynAccessor(93)

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
        BackportContextMenu = DynAccessor(94)
        Browser = DynAccessor(95)
        FadingCoverView = DynAccessor(96)

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            ReservesDisabledTooltip = DynAccessor(97)

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
            BattlePassAwardsView = DynAccessor(150)
            BattlePassBuyLevelView = DynAccessor(151)
            BattlePassBuyView = DynAccessor(152)
            BattlePassDailyQuestsIntroView = DynAccessor(153)
            BattlePassEntryPointView = DynAccessor(154)
            BattlePassHowToEarnPointsView = DynAccessor(155)
            BattlePassIntroView = DynAccessor(156)
            BattlePassProgressionsView = DynAccessor(157)
            BattlePassVehicleAwardView = DynAccessor(158)
            ChapterChoiceView = DynAccessor(159)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChapterConfirm = DynAccessor(160)

            dialogs = _dialogs()
            ExtraIntroView = DynAccessor(161)
            RewardsSelectionView = DynAccessor(162)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                AnimatedReward = DynAccessor(163)
                AwardsWidget = DynAccessor(164)
                BuyButtons = DynAccessor(165)
                ChapterBackground = DynAccessor(166)
                CurrencyReward = DynAccessor(167)
                Emblem = DynAccessor(168)
                FormatRemainingDate = DynAccessor(169)
                Header = DynAccessor(170)
                LoupeButton = DynAccessor(171)
                RewardsBlock = DynAccessor(172)
                ScrollWithLips = DynAccessor(173)
                Slider = DynAccessor(174)
                Title = DynAccessor(175)
                VehicleBonusList = DynAccessor(176)
                VehicleInfo = DynAccessor(177)
                VehicleList = DynAccessor(178)

            sharedComponents = _sharedComponents()
            StyleVideoView = DynAccessor(179)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattlePassCoinTooltipView = DynAccessor(180)
                BattlePassCompletedTooltipView = DynAccessor(181)
                BattlePassGoldMissionTooltipView = DynAccessor(182)
                BattlePassInProgressTooltipView = DynAccessor(183)
                BattlePassLockIconTooltipView = DynAccessor(184)
                BattlePassNoChapterTooltipView = DynAccessor(185)
                BattlePassNotStartedTooltipView = DynAccessor(186)
                BattlePassOnPauseTooltipView = DynAccessor(187)
                BattlePassPointsView = DynAccessor(188)
                BattlePassQuestsChainTooltipView = DynAccessor(189)
                BattlePassUpgradeStyleTooltipView = DynAccessor(190)
                RandomQuestTooltip = DynAccessor(191)

                class _sharedComponents(DynAccessor):
                    __slots__ = ()
                    BlockCompleted = DynAccessor(192)
                    Chose = DynAccessor(193)
                    FinalLevel = DynAccessor(194)
                    IconTextBlock = DynAccessor(195)
                    PerBattlePointsTable = DynAccessor(196)
                    Point = DynAccessor(197)

                sharedComponents = _sharedComponents()
                VehiclePointsTooltipView = DynAccessor(198)

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
            Confirm = DynAccessor(205)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BlueprintsAlliancesTooltipView = DynAccessor(206)

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
            AwardsView = DynAccessor(224)
            BrowserView = DynAccessor(225)
            SelectableRewardBase = DynAccessor(226)
            SelectSlotSpecDialog = DynAccessor(227)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExtendedTextTooltip = DynAccessor(228)
                SelectedRewardsTooltipView = DynAccessor(229)

            tooltips = _tooltips()

        common = _common()

        class _marathon(DynAccessor):
            __slots__ = ()

            class _marathon_reward_view(DynAccessor):
                __slots__ = ()
                MarathonRewardView = DynAccessor(38)

            marathon_reward_view = _marathon_reward_view()
            EntryPoint = DynAccessor(341)
            RewardWindow = DynAccessor(342)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RestRewardTooltip = DynAccessor(343)

            tooltips = _tooltips()

        marathon = _marathon()

        class _missions(DynAccessor):
            __slots__ = ()

            class _missions_tab_bar_view(DynAccessor):
                __slots__ = ()
                MissionsTabBarView = DynAccessor(39)

            missions_tab_bar_view = _missions_tab_bar_view()

            class _common(DynAccessor):
                __slots__ = ()
                BattleConditions = DynAccessor(345)
                Countdown = DynAccessor(346)
                PendingDots = DynAccessor(347)

            common = _common()
            Daily = DynAccessor(348)
            DailyQuestsTooltip = DynAccessor(349)
            DailyQuestsWidget = DynAccessor(350)
            LockedSubscriptionBonusTooltip = DynAccessor(351)
            RerollTooltip = DynAccessor(352)
            RerollTooltipWithCountdown = DynAccessor(353)

        missions = _missions()

        class _nation_change(DynAccessor):
            __slots__ = ()

            class _nation_change_screen(DynAccessor):
                __slots__ = ()
                NationChangeScreen = DynAccessor(40)

            nation_change_screen = _nation_change_screen()

        nation_change = _nation_change()

        class _new_year(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()

                class _new_year_collections_tooltip_content(DynAccessor):
                    __slots__ = ()
                    NYCollectionsTooltipContent = DynAccessor(41)

                new_year_collections_tooltip_content = _new_year_collections_tooltip_content()

                class _new_year_parts_tooltip_content(DynAccessor):
                    __slots__ = ()
                    NewYearPartsTooltipContent = DynAccessor(42)

                new_year_parts_tooltip_content = _new_year_parts_tooltip_content()

                class _new_year_vehicle_bonus(DynAccessor):
                    __slots__ = ()
                    NewYearVehiclesBonus = DynAccessor(43)

                new_year_vehicle_bonus = _new_year_vehicle_bonus()

                class _ny_mega_toy_tooltip_content(DynAccessor):
                    __slots__ = ()
                    NyMegaToyTooltipContent = DynAccessor(44)

                ny_mega_toy_tooltip_content = _ny_mega_toy_tooltip_content()

                class _ny_regular_toy_tooltip_content(DynAccessor):
                    __slots__ = ()
                    NyRegularToyTooltipContent = DynAccessor(45)

                ny_regular_toy_tooltip_content = _ny_regular_toy_tooltip_content()

            tooltips = _tooltips()

        new_year = _new_year()

        class _premacc(DynAccessor):
            __slots__ = ()

            class _daily_experience_view(DynAccessor):
                __slots__ = ()
                DailyExperiencePage = DynAccessor(46)

            daily_experience_view = _daily_experience_view()

            class _maps_blacklist_view(DynAccessor):
                __slots__ = ()
                MapsBlacklistView = DynAccessor(47)

            maps_blacklist_view = _maps_blacklist_view()

            class _piggybank(DynAccessor):
                __slots__ = ()
                Piggybank = DynAccessor(48)

            piggybank = _piggybank()

            class _squad_bonus_tooltip_content(DynAccessor):
                __slots__ = ()
                SquadBonusTooltipContent = DynAccessor(49)

            squad_bonus_tooltip_content = _squad_bonus_tooltip_content()

            class _dashboard(DynAccessor):
                __slots__ = ()

                class _prem_dashboard_parent_control_info(DynAccessor):
                    __slots__ = ()
                    PremDashboardParentControlInfoContent = DynAccessor(50)

                prem_dashboard_parent_control_info = _prem_dashboard_parent_control_info()

                class _piggy_bank_cards(DynAccessor):
                    __slots__ = ()

                    class _prem_piggy_bank(DynAccessor):
                        __slots__ = ()
                        PremPiggyBankCard = DynAccessor(51)

                    prem_piggy_bank = _prem_piggy_bank()

                    class _wot_plus_piggy_bank(DynAccessor):
                        __slots__ = ()
                        WotPlusPiggyBankCard = DynAccessor(52)

                    wot_plus_piggy_bank = _wot_plus_piggy_bank()

                piggy_bank_cards = _piggy_bank_cards()

            dashboard = _dashboard()

            class _maps_blacklist(DynAccessor):
                __slots__ = ()

                class _maps_blacklist_confirm_dialog(DynAccessor):
                    __slots__ = ()
                    MapsBlacklistConfirmDialogContent = DynAccessor(53)

                maps_blacklist_confirm_dialog = _maps_blacklist_confirm_dialog()

                class _maps_blacklist_tooltips(DynAccessor):
                    __slots__ = ()
                    MapsBlacklistInfoTooltipContent = DynAccessor(54)

                maps_blacklist_tooltips = _maps_blacklist_tooltips()

            maps_blacklist = _maps_blacklist()

        premacc = _premacc()

        class _progressive_reward(DynAccessor):
            __slots__ = ()

            class _progressive_reward_award(DynAccessor):
                __slots__ = ()
                ProgressiveRewardAward = DynAccessor(55)

            progressive_reward_award = _progressive_reward_award()

            class _progressive_reward_view(DynAccessor):
                __slots__ = ()
                ProgressiveRewardView = DynAccessor(56)

            progressive_reward_view = _progressive_reward_view()

        progressive_reward = _progressive_reward()

        class _ranked(DynAccessor):
            __slots__ = ()

            class _ranked_year_award(DynAccessor):
                __slots__ = ()
                RankedYearAward = DynAccessor(57)

            ranked_year_award = _ranked_year_award()
            EntryPoint = DynAccessor(391)
            QualificationRewardsView = DynAccessor(392)
            RankedProgressionView = DynAccessor(393)
            RankedSelectableRewardView = DynAccessor(394)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RankedBattlesRolesTooltipView = DynAccessor(395)

            tooltips = _tooltips()
            YearLeaderboardView = DynAccessor(396)

        ranked = _ranked()

        class _reward_window(DynAccessor):
            __slots__ = ()

            class _clan_reward_window_content(DynAccessor):
                __slots__ = ()
                ClanRewardWindowContent = DynAccessor(58)

            clan_reward_window_content = _clan_reward_window_content()

            class _piggy_bank_reward_window_content(DynAccessor):
                __slots__ = ()
                PiggyBankRewardWindowContent = DynAccessor(59)

            piggy_bank_reward_window_content = _piggy_bank_reward_window_content()

            class _reward_window_content(DynAccessor):
                __slots__ = ()
                RewardWindowContent = DynAccessor(60)

            reward_window_content = _reward_window_content()

            class _twitch_reward_window_content(DynAccessor):
                __slots__ = ()
                TwitchRewardWindowContent = DynAccessor(61)

            twitch_reward_window_content = _twitch_reward_window_content()

        reward_window = _reward_window()

        class _shop(DynAccessor):
            __slots__ = ()

            class _buy_vehicle_view(DynAccessor):
                __slots__ = ()
                BuyVehicleView = DynAccessor(62)

            buy_vehicle_view = _buy_vehicle_view()

        shop = _shop()

        class _tooltips(DynAccessor):
            __slots__ = ()

            class _clans(DynAccessor):
                __slots__ = ()
                ClanShortInfoTooltipContent = DynAccessor(63)

            clans = _clans()

            class _loot_box_category_tooltip(DynAccessor):
                __slots__ = ()
                LootBoxCategoryTooltipContent = DynAccessor(64)

            loot_box_category_tooltip = _loot_box_category_tooltip()
            AdditionalRewardsTooltip = DynAccessor(480)
            TankmanTooltipView = DynAccessor(481)
            VehPostProgressionEntryPointTooltip = DynAccessor(482)

        tooltips = _tooltips()

        class _video(DynAccessor):
            __slots__ = ()

            class _video_view(DynAccessor):
                __slots__ = ()
                VideoView = DynAccessor(65)

            video_view = _video_view()

        video = _video()

        class _account_completion(DynAccessor):
            __slots__ = ()
            AddCredentialsView = DynAccessor(115)
            CompleteView = DynAccessor(116)
            ConfirmCredentialsView = DynAccessor(117)
            ContactSupportView = DynAccessor(118)
            CurtainView = DynAccessor(119)
            EmptyView = DynAccessor(120)
            ErrorView = DynAccessor(121)
            RenamingCompleteView = DynAccessor(122)
            RenamingView = DynAccessor(123)

            class _tooltips(DynAccessor):
                __slots__ = ()
                HangarTooltip = DynAccessor(124)
                RenamingHangarTooltip = DynAccessor(125)

            tooltips = _tooltips()

        account_completion = _account_completion()

        class _account_dashboard(DynAccessor):
            __slots__ = ()
            AccountDashboard = DynAccessor(126)

        account_dashboard = _account_dashboard()

        class _achievements(DynAccessor):
            __slots__ = ()
            AchievementsMainView = DynAccessor(127)

            class _dialogs(DynAccessor):
                __slots__ = ()
                EditConfirm = DynAccessor(128)

            dialogs = _dialogs()
            EditView = DynAccessor(129)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AutoSettingTooltip = DynAccessor(130)
                BattlesKPITooltip = DynAccessor(131)
                EditingTooltip = DynAccessor(132)
                KPITooltip = DynAccessor(133)
                WOTPRMainTooltip = DynAccessor(134)
                WTRInfoTooltip = DynAccessor(135)
                WTRMainTooltip = DynAccessor(136)

            tooltips = _tooltips()

        achievements = _achievements()

        class _awards(DynAccessor):
            __slots__ = ()
            BadgeAwardView = DynAccessor(137)
            MultipleAwardsView = DynAccessor(138)

            class _tooltips(DynAccessor):
                __slots__ = ()
                VehicleForChooseTooltip = DynAccessor(139)

            tooltips = _tooltips()

        awards = _awards()

        class _battle_matters(DynAccessor):
            __slots__ = ()
            BattleMattersEntryPointView = DynAccessor(140)
            BattleMattersExchangeRewards = DynAccessor(141)
            BattleMattersMainRewardView = DynAccessor(142)
            BattleMattersMainView = DynAccessor(143)
            BattleMattersPausedView = DynAccessor(144)
            BattleMattersRewardsView = DynAccessor(145)
            BattleMattersVehicleSelectionView = DynAccessor(146)

            class _popovers(DynAccessor):
                __slots__ = ()
                BattleMattersFilterPopoverView = DynAccessor(147)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattleMattersEntryTooltipView = DynAccessor(148)
                BattleMattersTokenTooltipView = DynAccessor(149)

            tooltips = _tooltips()

        battle_matters = _battle_matters()

        class _battle_royale(DynAccessor):
            __slots__ = ()
            BattleResultView = DynAccessor(199)
            CommanderView = DynAccessor(200)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                CurrencyResolver = DynAccessor(201)
                PriceResolver = DynAccessor(202)

            sharedComponents = _sharedComponents()
            TechParametersVIew = DynAccessor(203)

        battle_royale = _battle_royale()

        class _birthday2023(DynAccessor):
            __slots__ = ()
            BirthdayIntroScreen = DynAccessor(204)

        birthday2023 = _birthday2023()

        class _bootcamp(DynAccessor):
            __slots__ = ()
            BootcampExitView = DynAccessor(207)
            BootcampFinalRewardView = DynAccessor(208)
            BootcampNationView = DynAccessor(209)
            BootcampProgressView = DynAccessor(210)
            BootcampProgressWidget = DynAccessor(211)
            BootcampQuestWidget = DynAccessor(212)
            RewardsTooltip = DynAccessor(213)

        bootcamp = _bootcamp()

        class _collection(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(214)
            CollectionEntryPointView = DynAccessor(215)
            CollectionItemPreview = DynAccessor(216)
            CollectionsMainView = DynAccessor(217)
            CollectionView = DynAccessor(218)
            IntroView = DynAccessor(219)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CollectionItemTooltipView = DynAccessor(220)
                RewardTooltipView = DynAccessor(221)

            tooltips = _tooltips()

        collection = _collection()

        class _collective_goal(DynAccessor):
            __slots__ = ()
            CollectiveGoalEntryPointView = DynAccessor(222)

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(223)

            tooltips = _tooltips()

        collective_goal = _collective_goal()

        class _comp7(DynAccessor):
            __slots__ = ()
            Banner = DynAccessor(230)
            MainWidget = DynAccessor(231)
            MetaRootView = DynAccessor(232)
            NoVehiclesScreen = DynAccessor(233)
            RewardsScreen = DynAccessor(234)
            SeasonModifier = DynAccessor(235)

            class _tooltips(DynAccessor):
                __slots__ = ()
                DivisionTooltip = DynAccessor(236)
                FifthRankTooltip = DynAccessor(237)
                GeneralRankTooltip = DynAccessor(238)
                LastUpdateTooltip = DynAccessor(239)
                MainWidgetTooltip = DynAccessor(240)
                RankInactivityTooltip = DynAccessor(241)
                SeasonPointTooltip = DynAccessor(242)
                SixthRankTooltip = DynAccessor(243)

            tooltips = _tooltips()
            WhatsNewView = DynAccessor(244)

        comp7 = _comp7()

        class _craft_machine(DynAccessor):
            __slots__ = ()
            CraftmachineEntryPointView = DynAccessor(245)

        craft_machine = _craft_machine()

        class _crew(DynAccessor):
            __slots__ = ()
            BarracksView = DynAccessor(246)
            CrewHeaderTooltipView = DynAccessor(247)
            CrewIntroView = DynAccessor(248)

            class _dialogs(DynAccessor):
                __slots__ = ()
                CrewBooksPurchaseDialog = DynAccessor(249)
                DismissTankmanDialog = DynAccessor(250)
                DocumentChangeDialog = DynAccessor(251)
                EnlargeBarracksDialog = DynAccessor(252)
                PerksResetContent = DynAccessor(253)
                RecruitDialog = DynAccessor(254)
                RecruitNewTankmanDialog = DynAccessor(255)
                RestoreTankmanDialog = DynAccessor(256)
                RetrainDialog = DynAccessor(257)
                RoleChangeDialog = DynAccessor(258)
                SkinApplyDialog = DynAccessor(259)

            dialogs = _dialogs()
            HangarCrewWidget = DynAccessor(260)
            HelpView = DynAccessor(261)
            MemberChangeView = DynAccessor(262)

            class _personal_case(DynAccessor):
                __slots__ = ()

                class _component(DynAccessor):
                    __slots__ = ()
                    ScrollWithLips = DynAccessor(263)
                    TankmanInfoWrapper = DynAccessor(264)

                component = _component()
                PersonalDataView = DynAccessor(265)
                PersonalFileView = DynAccessor(266)
                ServiceRecordView = DynAccessor(267)

            personal_case = _personal_case()

            class _popovers(DynAccessor):
                __slots__ = ()
                FilterPopoverView = DynAccessor(268)

            popovers = _popovers()
            QuickTrainingView = DynAccessor(269)
            TankChangeView = DynAccessor(270)
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
                TankmanTooltip = DynAccessor(281)
                TrainingLevelTooltip = DynAccessor(282)
                VehCmpSkillsTooltip = DynAccessor(283)
                VehicleParamsTooltipView = DynAccessor(284)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                CrewWidget = DynAccessor(285)
                FilterPanelWidget = DynAccessor(286)
                PriceList = DynAccessor(287)
                TankmanInfo = DynAccessor(288)

            widgets = _widgets()

        crew = _crew()

        class _crystalsPromo(DynAccessor):
            __slots__ = ()
            CrystalsPromoView = DynAccessor(289)

        crystalsPromo = _crystalsPromo()

        class _currency_reserves(DynAccessor):
            __slots__ = ()
            CurrencyReserves = DynAccessor(290)
            ReservesAwardView = DynAccessor(291)

        currency_reserves = _currency_reserves()

        class _customization(DynAccessor):
            __slots__ = ()
            CustomizationCart = DynAccessor(292)

            class _progression_styles(DynAccessor):
                __slots__ = ()
                OnboardingView = DynAccessor(293)
                StageSwitcher = DynAccessor(294)

            progression_styles = _progression_styles()

            class _progressive_items_reward(DynAccessor):
                __slots__ = ()
                ProgressiveItemsUpgradeView = DynAccessor(295)

            progressive_items_reward = _progressive_items_reward()

            class _progressive_items_view(DynAccessor):
                __slots__ = ()
                ProgressiveItemsView = DynAccessor(296)

            progressive_items_view = _progressive_items_view()

            class _style_unlocked_view(DynAccessor):
                __slots__ = ()
                StyleUnlockedView = DynAccessor(297)

            style_unlocked_view = _style_unlocked_view()

        customization = _customization()

        class _debutBoxes(DynAccessor):
            __slots__ = ()
            DebutBoxesBadgeTooltipView = DynAccessor(298)

        debutBoxes = _debutBoxes()

        class _dedication(DynAccessor):
            __slots__ = ()
            DedicationRewardView = DynAccessor(299)

        dedication = _dedication()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            DedicationTooltip = DynAccessor(300)
            DogTagsView = DynAccessor(301)
            RankedEfficiencyTooltip = DynAccessor(302)
            ThreeMonthsTooltip = DynAccessor(303)
            TriumphTooltip = DynAccessor(304)

        dog_tags = _dog_tags()

        class _early_access(DynAccessor):
            __slots__ = ()
            EarlyAccessBuyView = DynAccessor(305)
            EarlyAccessEntryPointView = DynAccessor(306)
            EarlyAccessIntroView = DynAccessor(307)
            EarlyAccessQuestsView = DynAccessor(308)
            EarlyAccessRewardsView = DynAccessor(309)
            EarlyAccessVehicleView = DynAccessor(310)

            class _tooltips(DynAccessor):
                __slots__ = ()
                EarlyAccessCommonDescriptionTooltip = DynAccessor(311)
                EarlyAccessCompensationTooltip = DynAccessor(312)
                EarlyAccessCurrencyTooltipView = DynAccessor(313)
                EarlyAccessEntryPointPausedTooltip = DynAccessor(314)
                EarlyAccessEntryPointTooltipView = DynAccessor(315)
                EarlyAccessSimpleTooltipView = DynAccessor(316)
                EarlyAccessTokensStepperTooltip = DynAccessor(317)
                EarlyAccessVehicleCarouselPausedTooltip = DynAccessor(318)
                EarlyAccessVehicleLockedTooltip = DynAccessor(319)

            tooltips = _tooltips()

        early_access = _early_access()

        class _elite_window(DynAccessor):
            __slots__ = ()
            EliteView = DynAccessor(320)

        elite_window = _elite_window()

        class _excluded_maps(DynAccessor):
            __slots__ = ()
            ExcludedMapsView = DynAccessor(321)

        excluded_maps = _excluded_maps()

        class _frontline(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(322)

            class _dialogs(DynAccessor):
                __slots__ = ()
                BlankPrice = DynAccessor(323)

            dialogs = _dialogs()
            IntroScreen = DynAccessor(324)
            RewardsSelectionView = DynAccessor(325)

        frontline = _frontline()

        class _hangar(DynAccessor):
            __slots__ = ()

            class _subViews(DynAccessor):
                __slots__ = ()
                VehicleParams = DynAccessor(326)

            subViews = _subViews()
            VehicleParamsWidget = DynAccessor(327)

        hangar = _hangar()

        class _instructions(DynAccessor):
            __slots__ = ()
            BuyWindow = DynAccessor(328)
            SellWindow = DynAccessor(329)

        instructions = _instructions()

        class _mapbox(DynAccessor):
            __slots__ = ()
            MapBoxAwardsView = DynAccessor(330)
            MapBoxEntryPointView = DynAccessor(331)
            MapBoxIntro = DynAccessor(332)
            MapBoxProgression = DynAccessor(333)
            MapBoxRewardChoiceView = DynAccessor(334)
            MapBoxSurveyView = DynAccessor(335)

        mapbox = _mapbox()

        class _maps_training(DynAccessor):
            __slots__ = ()
            MapPointDescriptionTooltip = DynAccessor(336)
            MapsTrainingPage = DynAccessor(337)
            MapsTrainingQueue = DynAccessor(338)
            MapsTrainingResult = DynAccessor(339)
            ScenarioTooltip = DynAccessor(340)

        maps_training = _maps_training()

        class _matchmaker(DynAccessor):
            __slots__ = ()
            ActiveTestConfirmView = DynAccessor(344)

        matchmaker = _matchmaker()

        class _mode_selector(DynAccessor):
            __slots__ = ()
            BattleSessionView = DynAccessor(354)
            ModeSelectorView = DynAccessor(355)

            class _popovers(DynAccessor):
                __slots__ = ()
                RandomBattlePopover = DynAccessor(356)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                AlertTooltip = DynAccessor(357)

                class _common(DynAccessor):
                    __slots__ = ()
                    Divider = DynAccessor(358)
                    GradientDecorator = DynAccessor(359)

                common = _common()
                SimplyFormatTooltip = DynAccessor(360)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                BattleRoyaleProgressionWidget = DynAccessor(361)
                BattleRoyaleWidget = DynAccessor(362)
                EpicWidget = DynAccessor(363)
                RankedWidget = DynAccessor(364)

            widgets = _widgets()

        mode_selector = _mode_selector()

        class _offers(DynAccessor):
            __slots__ = ()
            OfferBannerWindow = DynAccessor(365)
            OfferGiftsWindow = DynAccessor(366)
            OfferRewardWindow = DynAccessor(367)

        offers = _offers()

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            PersonalReservesTooltip = DynAccessor(368)
            PersonalReservesWidget = DynAccessor(369)
            ReserveCard = DynAccessor(370)
            ReserveCardTooltip = DynAccessor(371)
            ReserveGroup = DynAccessor(372)
            ReservesActivationView = DynAccessor(373)
            ReservesConversionView = DynAccessor(374)
            ReservesIntroView = DynAccessor(375)

        personal_reserves = _personal_reserves()

        class _platoon(DynAccessor):
            __slots__ = ()
            AlertTooltip = DynAccessor(376)
            MembersWindow = DynAccessor(377)
            PlatoonDropdown = DynAccessor(378)
            SearchingDropdown = DynAccessor(379)
            SettingsPopover = DynAccessor(380)

            class _subViews(DynAccessor):
                __slots__ = ()
                Chat = DynAccessor(381)
                SettingsContent = DynAccessor(382)
                TiersLimit = DynAccessor(383)

            subViews = _subViews()
            WTRTooltip = DynAccessor(384)

        platoon = _platoon()

        class _player_subscriptions(DynAccessor):
            __slots__ = ()
            PlayerSubscriptions = DynAccessor(385)
            SubscriptionItem = DynAccessor(386)
            SubscriptionRewardView = DynAccessor(387)

        player_subscriptions = _player_subscriptions()

        class _pm_announce(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                PersonalMissionsNewCampaignTooltipView = DynAccessor(388)
                PersonalMissionsOldCampaignTooltipView = DynAccessor(389)

            tooltips = _tooltips()

        pm_announce = _pm_announce()

        class _poll(DynAccessor):
            __slots__ = ()
            PollView = DynAccessor(390)

        poll = _poll()

        class _research(DynAccessor):
            __slots__ = ()
            BuyModuleDialogView = DynAccessor(397)
            InsufficientCreditsTooltip = DynAccessor(398)
            SoldModuleInfoTooltip = DynAccessor(399)

        research = _research()

        class _resource_well(DynAccessor):
            __slots__ = ()
            AwardView = DynAccessor(400)
            CompletedProgressionView = DynAccessor(401)
            EntryPoint = DynAccessor(402)
            IntroView = DynAccessor(403)
            NoSerialVehiclesConfirm = DynAccessor(404)
            NoVehiclesConfirm = DynAccessor(405)
            ProgressionView = DynAccessor(406)
            ResourcesLoadingConfirm = DynAccessor(407)
            ResourcesLoadingView = DynAccessor(408)

            class _sharedComponents(DynAccessor):
                __slots__ = ()

                class _award(DynAccessor):
                    __slots__ = ()
                    AdditionalReward = DynAccessor(409)
                    Footer = DynAccessor(410)
                    Header = DynAccessor(411)
                    Reward = DynAccessor(412)

                award = _award()
                Counter = DynAccessor(413)
                NoVehiclesState = DynAccessor(414)
                Resource = DynAccessor(415)
                VehicleCount = DynAccessor(416)
                VehicleInfo = DynAccessor(417)

            sharedComponents = _sharedComponents()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(418)
                MaxProgressTooltip = DynAccessor(419)
                ProgressTooltip = DynAccessor(420)
                RefundResourcesTooltip = DynAccessor(421)
                SerialNumberTooltip = DynAccessor(422)

            tooltips = _tooltips()

        resource_well = _resource_well()

        class _seniority_awards(DynAccessor):
            __slots__ = ()
            SeniorityAwardsNotificationView = DynAccessor(423)
            SeniorityAwardsView = DynAccessor(424)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                SeniorityAwardCoin = DynAccessor(425)

            sharedComponents = _sharedComponents()

        seniority_awards = _seniority_awards()

        class _shop_sales(DynAccessor):
            __slots__ = ()
            ShopSalesEntryPointView = DynAccessor(426)

        shop_sales = _shop_sales()

        class _stronghold(DynAccessor):
            __slots__ = ()
            StrongholdEntryPointView = DynAccessor(427)

        stronghold = _stronghold()

        class _subscription(DynAccessor):
            __slots__ = ()
            SubscriptionAwardView = DynAccessor(428)
            SubscriptionDailyQuestsIntro = DynAccessor(429)
            WotPlusIntroView = DynAccessor(430)
            WotPlusTooltip = DynAccessor(431)

        subscription = _subscription()

        class _tanksetup(DynAccessor):
            __slots__ = ()
            AmmunitionPanel = DynAccessor(432)

            class _common(DynAccessor):
                __slots__ = ()
                Action = DynAccessor(433)
                CtaButtons = DynAccessor(434)
                DealPanel = DynAccessor(435)
                ExtraImage = DynAccessor(436)
                FormatColorTagText = DynAccessor(437)
                MaybeWrapper = DynAccessor(438)
                Price = DynAccessor(439)
                SetupApp = DynAccessor(440)
                ShortenedText = DynAccessor(441)
                Slider = DynAccessor(442)

                class _SlotParts(DynAccessor):
                    __slots__ = ()
                    Bonus = DynAccessor(443)
                    Container = DynAccessor(444)
                    Count = DynAccessor(445)
                    Inside = DynAccessor(446)
                    Level = DynAccessor(447)

                SlotParts = _SlotParts()
                Specializations = DynAccessor(448)
                Storage = DynAccessor(449)
                SwitchButton = DynAccessor(450)
                SwitchEquipment = DynAccessor(451)

                class _Transitions(DynAccessor):
                    __slots__ = ()
                    SlotTransitions = DynAccessor(452)

                Transitions = _Transitions()
                WeaponOccupancy = DynAccessor(453)

            common = _common()
            DeconstructionDeviceView = DynAccessor(454)

            class _dialogs(DynAccessor):
                __slots__ = ()
                Confirm = DynAccessor(455)
                ConfirmActionsWithEquipmentDialog = DynAccessor(456)
                DeconstructConfirm = DynAccessor(457)
                DeviceUpgradeDialog = DynAccessor(458)
                ExchangeToBuyItems = DynAccessor(459)
                ExchangeToUpgradeItems = DynAccessor(460)
                NeedRepair = DynAccessor(461)
                RefillShells = DynAccessor(462)
                Sell = DynAccessor(463)

                class _sub_views(DynAccessor):
                    __slots__ = ()
                    FrontlineConfirmFooterMoney = DynAccessor(464)
                    FrontlineConfirmIcons = DynAccessor(465)
                    FrontlineConfirmMultipleNames = DynAccessor(466)
                    FrontlineConfirmTitle = DynAccessor(467)

                sub_views = _sub_views()

            dialogs = _dialogs()
            HangarAmmunitionSetup = DynAccessor(468)
            IntroScreen = DynAccessor(469)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AbilitySkillAdditionalTooltip = DynAccessor(470)
                AbilitySkillTooltip = DynAccessor(471)
                DeconstructFromInventoryTooltip = DynAccessor(472)
                DeconstructFromVehicleTooltip = DynAccessor(473)
                SetupTabTooltipView = DynAccessor(474)
                WarningTooltipView = DynAccessor(475)

            tooltips = _tooltips()
            VehicleCompareAmmunitionPanel = DynAccessor(476)
            VehicleCompareAmmunitionSetup = DynAccessor(477)

        tanksetup = _tanksetup()

        class _techtree(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                ParagonsEntryPointTooltip = DynAccessor(478)

            tooltips = _tooltips()
            VehicleTechTree = DynAccessor(479)

        techtree = _techtree()

        class _vehicle_compare(DynAccessor):
            __slots__ = ()
            CompareModificationsPanelView = DynAccessor(483)
            SelectSlotSpecCompareDialog = DynAccessor(484)

        vehicle_compare = _vehicle_compare()

        class _vehicle_preview(DynAccessor):
            __slots__ = ()

            class _buying_panel(DynAccessor):
                __slots__ = ()
                EarlyAccessPanel = DynAccessor(485)
                StyleBuyingPanel = DynAccessor(486)
                VPProgressionStylesBuyingPanel = DynAccessor(487)
                WellPanel = DynAccessor(488)

            buying_panel = _buying_panel()

            class _top_panel(DynAccessor):
                __slots__ = ()
                TopPanelTabs = DynAccessor(489)

            top_panel = _top_panel()

        vehicle_preview = _vehicle_preview()

        class _veh_post_progression(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                Bonus = DynAccessor(490)
                Description = DynAccessor(491)
                Grid = DynAccessor(492)
                PersistentBonuses = DynAccessor(493)
                Slide = DynAccessor(494)
                SlideContent = DynAccessor(495)
                Slider = DynAccessor(496)
                TextSplit = DynAccessor(497)

            common = _common()
            PostProgressionInfo = DynAccessor(498)
            PostProgressionIntro = DynAccessor(499)
            PostProgressionResearchSteps = DynAccessor(500)

            class _tooltip(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()
                    DisabledBlock = DynAccessor(501)
                    FeatureLevelSubtitle = DynAccessor(502)
                    Lock = DynAccessor(503)
                    NotEnoughCredits = DynAccessor(504)
                    PriceBlock = DynAccessor(505)
                    Separator = DynAccessor(506)

                common = _common()
                PairModificationTooltipView = DynAccessor(507)
                PostProgressionLevelTooltipView = DynAccessor(508)
                RoleSlotTooltipView = DynAccessor(509)
                SetupTooltipView = DynAccessor(510)

            tooltip = _tooltip()
            VehiclePostProgressionCmpView = DynAccessor(511)
            VehiclePostProgressionView = DynAccessor(512)

        veh_post_progression = _veh_post_progression()

    lobby = _lobby()

    class _test_check_box_view(DynAccessor):
        __slots__ = ()
        TestCheckBoxView = DynAccessor(66)

    test_check_box_view = _test_check_box_view()

    class _test_text_button_view(DynAccessor):
        __slots__ = ()
        TestTextButtonView = DynAccessor(67)

    test_text_button_view = _test_text_button_view()

    class _windows_layout_view(DynAccessor):
        __slots__ = ()
        WindowsLayountView = DynAccessor(68)

    windows_layout_view = _windows_layout_view()

    class _blend_mode(DynAccessor):
        __slots__ = ()

        class _blend_mode(DynAccessor):
            __slots__ = ()
            BlendMode = DynAccessor(69)

        blend_mode = _blend_mode()

    blend_mode = _blend_mode()

    class _demo_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _demo_window_content(DynAccessor):
                __slots__ = ()
                DemoWindowContent = DynAccessor(70)
                ImageProps = DynAccessor(71)

            demo_window_content = _demo_window_content()

            class _demo_window_details_panel(DynAccessor):
                __slots__ = ()
                DemoWindowDetailsPanel = DynAccessor(72)

            demo_window_details_panel = _demo_window_details_panel()

            class _demo_window_image_panel(DynAccessor):
                __slots__ = ()
                DemoWindowImagePanel = DynAccessor(73)

            demo_window_image_panel = _demo_window_image_panel()

            class _image_preview_window_content(DynAccessor):
                __slots__ = ()
                ImagePreviewWindowContent = DynAccessor(74)

            image_preview_window_content = _image_preview_window_content()

        views = _views()

    demo_view = _demo_view()

    class _examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_dialogs_view(DynAccessor):
                __slots__ = ()
                TestDialogsView = DynAccessor(75)

            test_dialogs_view = _test_dialogs_view()

            class _test_expr_functions_view(DynAccessor):
                __slots__ = ()
                TestExprFunctionsView = DynAccessor(76)

            test_expr_functions_view = _test_expr_functions_view()

            class _test_sub_view(DynAccessor):
                __slots__ = ()
                TestSubView = DynAccessor(77)

            test_sub_view = _test_sub_view()

            class _test_view(DynAccessor):
                __slots__ = ()
                TestView = DynAccessor(78)

            test_view = _test_view()

            class _unbound_example(DynAccessor):
                __slots__ = ()
                UnboundExample = DynAccessor(79)

            unbound_example = _unbound_example()

        views = _views()

    examples = _examples()

    class _list_examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _list_examples_empty_render_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesEmptyRenderWindowContent = DynAccessor(80)

            list_examples_empty_render_window_content = _list_examples_empty_render_window_content()

            class _list_examples_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesWindowContent = DynAccessor(81)

            list_examples_window_content = _list_examples_window_content()

        views = _views()

    list_examples = _list_examples()

    class _rotation_pivot_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_pivot_view(DynAccessor):
                __slots__ = ()
                RotationAndPivotTestView = DynAccessor(82)

            rotation_pivot_view = _rotation_pivot_view()

        views = _views()

    rotation_pivot_view = _rotation_pivot_view()

    class _rotation_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_view(DynAccessor):
                __slots__ = ()
                RotationTestView = DynAccessor(83)

            rotation_view = _rotation_view()

        views = _views()

    rotation_view = _rotation_view()

    class _scale_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _scale_view(DynAccessor):
                __slots__ = ()
                ScaleTestView = DynAccessor(84)

            scale_view = _scale_view()

        views = _views()

    scale_view = _scale_view()

    class _test_uikit_buttons_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_buttons_view(DynAccessor):
                __slots__ = ()
                TestUikitButtonsView = DynAccessor(85)

            test_uikit_buttons_view = _test_uikit_buttons_view()

        views = _views()

    test_uikit_buttons_view = _test_uikit_buttons_view()

    class _test_uikit_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_view(DynAccessor):
                __slots__ = ()
                TestUikitView = DynAccessor(86)

            test_uikit_view = _test_uikit_view()

        views = _views()

    test_uikit_view = _test_uikit_view()

    class _wtypes_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _wtypes_demo_window_content(DynAccessor):
                __slots__ = ()
                WtypesDemoWindowContent = DynAccessor(87)

            wtypes_demo_window_content = _wtypes_demo_window_content()

        views = _views()

    wtypes_view = _wtypes_view()

    class _dialogs(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            DialogTemplateGenericTooltip = DynAccessor(98)

        common = _common()
        DefaultDialog = DynAccessor(99)

        class _sub_views(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                SimpleText = DynAccessor(100)
                SinglePrice = DynAccessor(101)

            common = _common()

            class _content(DynAccessor):
                __slots__ = ()
                SelectOptionContent = DynAccessor(102)
                SimpleTextContent = DynAccessor(103)
                SinglePriceContent = DynAccessor(104)
                TextWithWarning = DynAccessor(105)

            content = _content()

            class _footer(DynAccessor):
                __slots__ = ()
                BRSinglePriceFooter = DynAccessor(106)
                SimpleTextFooter = DynAccessor(107)
                SinglePriceFooter = DynAccessor(108)

            footer = _footer()

            class _icon(DynAccessor):
                __slots__ = ()
                IconSet = DynAccessor(109)

            icon = _icon()

            class _title(DynAccessor):
                __slots__ = ()
                SimpleTextTitle = DynAccessor(110)

            title = _title()

            class _topRight(DynAccessor):
                __slots__ = ()
                BRMoneyBalance = DynAccessor(111)
                MoneyBalance = DynAccessor(112)

            topRight = _topRight()

        sub_views = _sub_views()

        class _widgets(DynAccessor):
            __slots__ = ()
            SinglePrice = DynAccessor(113)

        widgets = _widgets()

    dialogs = _dialogs()

    class _loading(DynAccessor):
        __slots__ = ()
        GameLoadingView = DynAccessor(114)

    loading = _loading()

    class _armory_yard(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                ArmoryYardBundlesView = DynAccessor(513)
                ArmoryYardBuyBundleView = DynAccessor(514)
                ArmoryYardBuyView = DynAccessor(515)
                ArmoryYardEntryPointView = DynAccessor(516)
                ArmoryYardIntroView = DynAccessor(517)
                ArmoryYardMainView = DynAccessor(518)
                ArmoryYardPostProgressionBuyView = DynAccessor(519)
                ArmoryYardRewardsView = DynAccessor(520)
                ArmoryYardShopBuyView = DynAccessor(521)
                ArmoryYardShopRewardsView = DynAccessor(522)
                ArmoryYardShopView = DynAccessor(523)
                ArmoryYardVideoRewardView = DynAccessor(524)
                ArmoryYardWidgetView = DynAccessor(525)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ArmoryYardCurrencyTooltipView = DynAccessor(526)
                    ArmoryYardSimpleTooltipView = DynAccessor(527)
                    ArmoryYardTokenStepperTooltipView = DynAccessor(528)
                    ArmoryYardWalletNotAvailableTooltipView = DynAccessor(529)
                    EntryPointActiveTooltipView = DynAccessor(530)
                    EntryPointBeforeProgressionTooltipView = DynAccessor(531)
                    EntryPointNotActiveTooltipView = DynAccessor(532)
                    RestRewardTooltipView = DynAccessor(533)
                    ShopCurrencyTooltipView = DynAccessor(534)

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
                ModifiersDomainTooltipView = DynAccessor(535)

            tooltips = _tooltips()

        lobby = _lobby()

    battle_modifiers = _battle_modifiers()

    class _battle_royale(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _views(DynAccessor):
                __slots__ = ()
                LeaveBattleView = DynAccessor(536)

            views = _views()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BrCoinTooltipView = DynAccessor(537)

                class _common(DynAccessor):
                    __slots__ = ()

                    class _LeaderBoard(DynAccessor):
                        __slots__ = ()
                        Column = DynAccessor(538)
                        Table = DynAccessor(539)

                    LeaderBoard = _LeaderBoard()
                    PriceBlock = DynAccessor(540)
                    RentPrice = DynAccessor(541)

                common = _common()
                LeaderboardRewardTooltipView = DynAccessor(542)
                RentIconTooltipView = DynAccessor(543)
                RespawnInfoTooltipView = DynAccessor(544)
                RewardCurrencyTooltipView = DynAccessor(545)
                TestDriveInfoTooltipView = DynAccessor(546)
                VehicleTooltipView = DynAccessor(547)
                WidgetTooltipView = DynAccessor(548)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                BattleRoyaleEntryPoint = DynAccessor(549)
                IntroView = DynAccessor(550)
                PreBattleView = DynAccessor(551)
                ProxyCurrencyView = DynAccessor(552)
                WidgetView = DynAccessor(553)

            views = _views()

        lobby = _lobby()

    battle_royale = _battle_royale()

    class _battle_royale_progression(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(554)
        ProgressionMainView = DynAccessor(555)

    battle_royale_progression = _battle_royale_progression()

    class _cosmic_event(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _cosmic_hud(DynAccessor):
                __slots__ = ()
                CosmicBattleHelpView = DynAccessor(556)
                CosmicReactHudView = DynAccessor(557)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    AbilityTooltip = DynAccessor(558)

                tooltips = _tooltips()

            cosmic_hud = _cosmic_hud()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _banner_entry_point(DynAccessor):
                __slots__ = ()
                CosmicBannerEntryPoint = DynAccessor(559)

            banner_entry_point = _banner_entry_point()

            class _cosmic_lobby_view(DynAccessor):
                __slots__ = ()
                CosmicLobbyView = DynAccessor(560)

            cosmic_lobby_view = _cosmic_lobby_view()

            class _cosmic_post_battle(DynAccessor):
                __slots__ = ()
                CosmicPostBattleView = DynAccessor(561)

            cosmic_post_battle = _cosmic_post_battle()

            class _queue_view(DynAccessor):
                __slots__ = ()
                QueueView = DynAccessor(562)

            queue_view = _queue_view()

            class _rewards_view(DynAccessor):
                __slots__ = ()
                RewardsView = DynAccessor(563)

            rewards_view = _rewards_view()

        lobby = _lobby()

    cosmic_event = _cosmic_event()

    class _frontline(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            BannerView = DynAccessor(564)
            FrontlineContainerView = DynAccessor(565)
            InfoView = DynAccessor(566)
            ProgressView = DynAccessor(567)
            RewardsView = DynAccessor(568)
            SkillsView = DynAccessor(569)

            class _tooltips(DynAccessor):
                __slots__ = ()
                LevelReservesTooltip = DynAccessor(570)
                NotEnoughPointsTooltip = DynAccessor(571)
                SkillOrderTooltip = DynAccessor(572)

            tooltips = _tooltips()
            WelcomeView = DynAccessor(573)

        lobby = _lobby()

    frontline = _frontline()

    class _fun_random(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                FunRandomEntryPointView = DynAccessor(574)
                FunRandomHangarWidgetView = DynAccessor(575)
                FunRandomModeSubSelector = DynAccessor(576)
                FunRandomProgression = DynAccessor(577)

            feature = _feature()

            class _tooltips(DynAccessor):
                __slots__ = ()
                FunRandomProgressionTooltipView = DynAccessor(578)

            tooltips = _tooltips()

        lobby = _lobby()

    fun_random = _fun_random()

    class _gui_lootboxes(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _gui_lootboxes(DynAccessor):
                __slots__ = ()
                BonusProbabilitiesView = DynAccessor(579)
                EntryPointView = DynAccessor(580)
                KeysWelcomeScreen = DynAccessor(581)
                LootBoxesLoseRewardScreen = DynAccessor(582)
                LootboxRewardsView = DynAccessor(583)
                LootboxVideoRewardView = DynAccessor(584)
                OpenBoxErrorView = DynAccessor(585)

                class _shared(DynAccessor):
                    __slots__ = ()
                    AnimationControls = DynAccessor(586)
                    BacklitTransparentButton = DynAccessor(587)
                    BuyBoxFooter = DynAccessor(588)
                    CanvasSequence = DynAccessor(589)
                    CloseBtn = DynAccessor(590)
                    Compensation = DynAccessor(591)
                    CurrencyKey = DynAccessor(592)
                    Divider = DynAccessor(593)
                    Header = DynAccessor(594)
                    NyBoxWithToys = DynAccessor(595)
                    RotationVehicle = DynAccessor(596)
                    Video = DynAccessor(597)
                    VideoComponent = DynAccessor(598)

                shared = _shared()
                StorageView = DynAccessor(599)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    BonusGroupTooltip = DynAccessor(600)
                    CompensationTooltip = DynAccessor(601)
                    GuaranteedRewardTooltip = DynAccessor(602)
                    LootboxKeyTooltip = DynAccessor(603)
                    LootboxRotationTooltip = DynAccessor(604)
                    LootboxTooltip = DynAccessor(605)
                    ProbabilityButtonTooltip = DynAccessor(606)
                    ProbabilityGuaranteedRewardTooltip = DynAccessor(607)
                    ProbabilityStageButtonsTooltip = DynAccessor(608)

                tooltips = _tooltips()
                WelcomeScreen = DynAccessor(609)

            gui_lootboxes = _gui_lootboxes()

        lobby = _lobby()

    gui_lootboxes = _gui_lootboxes()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _new_year(DynAccessor):
                __slots__ = ()
                AtmosphereLevelUp = DynAccessor(610)

                class _common(DynAccessor):
                    __slots__ = ()
                    BreakButton = DynAccessor(611)
                    ChallengeButton = DynAccessor(612)
                    FormatTextWithColorTags = DynAccessor(613)
                    IncreaseAnimation = DynAccessor(614)
                    NyPopoverDecorator = DynAccessor(615)
                    Shards = DynAccessor(616)

                    class _slots(DynAccessor):
                        __slots__ = ()
                        BreakDecorationSlot = DynAccessor(617)
                        DecorationSlot = DynAccessor(618)
                        EmptySlot = DynAccessor(619)
                        SlotPlaceholders = DynAccessor(620)

                    slots = _slots()
                    VehicleBonus = DynAccessor(621)

                common = _common()
                CustomizationLevelUpView = DynAccessor(622)

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    CollectionPrice = DynAccessor(623)
                    LevelsRange = DynAccessor(624)
                    ShardsBalance = DynAccessor(625)

                dialogs = _dialogs()
                ExtraSlotLevelUpView = DynAccessor(626)

                class _loot_box(DynAccessor):
                    __slots__ = ()
                    LootBoxEntryView = DynAccessor(627)

                loot_box = _loot_box()
                MainView = DynAccessor(628)
                NyMainWidget = DynAccessor(629)
                NYQuestEntryPointView = DynAccessor(630)
                NyQuestsRewardView = DynAccessor(631)
                OnboardingView = DynAccessor(632)

                class _popovers(DynAccessor):
                    __slots__ = ()
                    NyBreakFilterPopover = DynAccessor(633)
                    NyDecorationsPopover = DynAccessor(634)
                    NyLootBoxPopover = DynAccessor(635)
                    VehicleFilterPopover = DynAccessor(636)

                popovers = _popovers()
                RobotTvScreenView = DynAccessor(637)

                class _tooltips(DynAccessor):
                    __slots__ = ()

                    class _common(DynAccessor):
                        __slots__ = ()
                        DecorationContent = DynAccessor(638)
                        DecorationFooter = DynAccessor(639)
                        DecorationHeader = DynAccessor(640)
                        MenuInfo = DynAccessor(641)

                    common = _common()
                    CommonTooltip = DynAccessor(642)
                    CustomizationZoneTooltip = DynAccessor(643)
                    LevelUpWidgetTooltip = DynAccessor(644)
                    MenuMachineTooltip = DynAccessor(645)
                    NyAlbumDecorationTooltip = DynAccessor(646)
                    NyBoxWithToysTooltip = DynAccessor(647)
                    NyCollectionBonusTooltip = DynAccessor(648)
                    NyCurrencyCompensationTooltip = DynAccessor(649)
                    NyCurrencyTooltip = DynAccessor(650)
                    NyDecorationStateTooltip = DynAccessor(651)
                    NyDecorationTooltip = DynAccessor(652)
                    NyDiscountRewardTooltip = DynAccessor(653)
                    NyMainWidgetTooltip = DynAccessor(654)
                    NyMarketplaceTokenTooltip = DynAccessor(655)
                    NyMenuCollectionsTooltip = DynAccessor(656)
                    NyMenuShardsTooltip = DynAccessor(657)
                    NyPetDecorationTooltip = DynAccessor(658)
                    NYQuestEntryPointTooltip = DynAccessor(659)
                    NyQuestModeTooltip = DynAccessor(660)
                    NyShardsTooltip = DynAccessor(661)
                    NyShopUnavailableTooltip = DynAccessor(662)
                    NyTotalBonusTooltip = DynAccessor(663)
                    SelectedRewardsTooltip = DynAccessor(664)

                tooltips = _tooltips()
                VehicleSelectionView = DynAccessor(665)
                VideoRewardView = DynAccessor(666)

                class _views(DynAccessor):
                    __slots__ = ()
                    BuyToyView = DynAccessor(667)

                views = _views()

            new_year = _new_year()

        lobby = _lobby()

    new_year = _new_year()

    class _story_mode(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            EpilogueWindow = DynAccessor(668)
            OnboardingBattleResultView = DynAccessor(669)
            PrebattleWindow = DynAccessor(670)

        battle = _battle()

        class _common(DynAccessor):
            __slots__ = ()
            CongratulationsWindow = DynAccessor(671)
            MedalTooltip = DynAccessor(672)
            OnboardingQueueView = DynAccessor(673)

        common = _common()

        class _lobby(DynAccessor):
            __slots__ = ()
            BattleResultView = DynAccessor(674)
            MissionSelectionView = DynAccessor(675)
            MissionTooltip = DynAccessor(676)

        lobby = _lobby()

    story_mode = _story_mode()

    class _survey(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _survey(DynAccessor):
                __slots__ = ()
                SurveyView = DynAccessor(677)

            survey = _survey()

        lobby = _lobby()

    survey = _survey()

    class _winback(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(678)

        class _lobby(DynAccessor):
            __slots__ = ()

            class _popovers(DynAccessor):
                __slots__ = ()
                WinbackLeaveModePopoverView = DynAccessor(679)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                CompensationTooltip = DynAccessor(680)
                MainRewardTooltip = DynAccessor(681)
                ModeInfoTooltip = DynAccessor(682)
                SelectableRewardTooltip = DynAccessor(683)
                SelectedRewardsTooltip = DynAccessor(684)
                WidgetTooltipView = DynAccessor(685)

            tooltips = _tooltips()
            WinbackDailyQuestsIntroView = DynAccessor(686)
            WinbackIntroView = DynAccessor(687)
            WinbackLeaveModeDialogView = DynAccessor(688)
            WinbackRewardView = DynAccessor(689)
            WinbackSelectableRewardView = DynAccessor(690)
            WinbackWidgetView = DynAccessor(691)

        lobby = _lobby()
        ProgressionMainView = DynAccessor(692)

    winback = _winback()
    Anchor = DynAccessor(693)
    ArmoryYardDemoView = DynAccessor(694)

    class _child_views_demo(DynAccessor):
        __slots__ = ()
        ChildDemoView = DynAccessor(695)
        MainView = DynAccessor(696)

    child_views_demo = _child_views_demo()
    Comp7DemoPageView = DynAccessor(697)
    ComponentsDemo = DynAccessor(698)
    DataLayerDemoView = DynAccessor(699)
    DataTrackerDemo = DynAccessor(700)
    DemoContextMenu = DynAccessor(701)
    Easings = DynAccessor(702)
    GameLoadingDebugView = DynAccessor(703)
    GFCharset = DynAccessor(704)
    GFComponents = DynAccessor(705)
    GFDemoPopover = DynAccessor(706)
    GFDemoRichTooltipWindow = DynAccessor(707)
    GFDemoWindow = DynAccessor(708)
    GFHooksDemo = DynAccessor(709)
    GFInjectView = DynAccessor(710)
    GFInputCases = DynAccessor(711)
    GFSimpleTooltipWindow = DynAccessor(712)
    GFWebSubDemoWindow = DynAccessor(713)

    class _gf_dialogs_demo(DynAccessor):
        __slots__ = ()
        DefaultDialogProxy = DynAccessor(714)
        GFDialogsDemo = DynAccessor(715)

        class _sub_views(DynAccessor):
            __slots__ = ()
            DummyContent = DynAccessor(716)
            DummyFooter = DynAccessor(717)
            DummyIcon = DynAccessor(718)
            DummyStepper = DynAccessor(719)
            DummyTitle = DynAccessor(720)
            DummyTopRight = DynAccessor(721)

        sub_views = _sub_views()

    gf_dialogs_demo = _gf_dialogs_demo()

    class _gf_viewer(DynAccessor):
        __slots__ = ()
        GFViewerWindow = DynAccessor(722)

    gf_viewer = _gf_viewer()

    class _igb_demo(DynAccessor):
        __slots__ = ()
        BrowserFullscreenWindow = DynAccessor(723)
        BrowserWindow = DynAccessor(724)
        MainView = DynAccessor(725)

    igb_demo = _igb_demo()
    LocaleDemo = DynAccessor(726)
    MediaWrapperDemo = DynAccessor(727)
    MixBlendMode = DynAccessor(728)
    MixBlendModeAnimation = DynAccessor(729)
    ModeSelectorDemo = DynAccessor(730)
    ModeSelectorToolsetView = DynAccessor(731)
    PluralLocView = DynAccessor(732)
    PropsSupportDemo = DynAccessor(733)
    ReactSpringVizualizer = DynAccessor(734)
    SelectableRewardDemoView = DynAccessor(735)
    StructuralDataBindDemo = DynAccessor(736)

    class _sub_views_demo(DynAccessor):
        __slots__ = ()
        GFSubViewsDemo = DynAccessor(737)

        class _sub_views(DynAccessor):
            __slots__ = ()
            CustomizationCartProxy = DynAccessor(738)
            DailyProxy = DynAccessor(739)
            ProgressiveItemsViewProxy = DynAccessor(740)

        sub_views = _sub_views()

    sub_views_demo = _sub_views_demo()
    SurfaceView = DynAccessor(741)
    UILoggerDemo = DynAccessor(742)
    VideoSupportView = DynAccessor(743)
    W2CTestPageWindow = DynAccessor(744)
    WgcgMockView = DynAccessor(745)

    class _wgtv(DynAccessor):
        __slots__ = ()
        WgtvEntityView = DynAccessor(746)
        WgtvKeyframeInfoView = DynAccessor(747)
        WgtvKeyframeView = DynAccessor(748)
        WgtvTimelineView = DynAccessor(749)
        WgtvToolsView = DynAccessor(750)

    wgtv = _wgtv()