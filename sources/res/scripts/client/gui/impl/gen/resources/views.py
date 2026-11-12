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
            InfoBattleContextHint = DynAccessor(84)
            PersonalReservesTabView = DynAccessor(85)
            PrebattleAmmunitionPanelView = DynAccessor(86)
            PrebattleCarouselView = DynAccessor(87)
            SixthSenseContextHint = DynAccessor(88)
            SkillSelectPopover = DynAccessor(89)

        battle_page = _battle_page()

        class _timer(DynAccessor):
            __slots__ = ()
            TimerView = DynAccessor(90)

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
        BackportContextMenu = DynAccessor(91)
        Browser = DynAccessor(92)
        FadingCoverView = DynAccessor(93)

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            ReservesDisabledTooltip = DynAccessor(94)

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
            BattlePassAwardsView = DynAccessor(148)
            BattlePassBuyLevelView = DynAccessor(149)
            BattlePassBuyView = DynAccessor(150)
            BattlePassEntryPointView = DynAccessor(151)
            BattlePassHowToEarnPointsView = DynAccessor(152)
            BattlePassIntroView = DynAccessor(153)
            BattlePassProgressionsView = DynAccessor(154)
            BattlePassVehicleAwardView = DynAccessor(155)
            ChapterChoiceView = DynAccessor(156)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChapterConfirm = DynAccessor(157)

            dialogs = _dialogs()
            ExtraIntroView = DynAccessor(158)
            RewardsSelectionView = DynAccessor(159)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                AnimatedReward = DynAccessor(160)
                AwardsWidget = DynAccessor(161)
                BuyButtons = DynAccessor(162)
                ChapterBackground = DynAccessor(163)
                CurrencyReward = DynAccessor(164)
                Emblem = DynAccessor(165)
                FormatRemainingDate = DynAccessor(166)
                Header = DynAccessor(167)
                LoupeButton = DynAccessor(168)
                RewardsBlock = DynAccessor(169)
                ScrollWithLips = DynAccessor(170)
                Slider = DynAccessor(171)
                Title = DynAccessor(172)
                VehicleBonusList = DynAccessor(173)
                VehicleInfo = DynAccessor(174)
                VehicleList = DynAccessor(175)
                Video = DynAccessor(176)

            sharedComponents = _sharedComponents()
            StyleVideoView = DynAccessor(177)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattlePassCoinTooltipView = DynAccessor(178)
                BattlePassCompletedTooltipView = DynAccessor(179)
                BattlePassGoldMissionTooltipView = DynAccessor(180)
                BattlePassInProgressTooltipView = DynAccessor(181)
                BattlePassLockIconTooltipView = DynAccessor(182)
                BattlePassNoChapterTooltipView = DynAccessor(183)
                BattlePassNotStartedTooltipView = DynAccessor(184)
                BattlePassOnPauseTooltipView = DynAccessor(185)
                BattlePassPointsView = DynAccessor(186)
                BattlePassQuestsChainTooltipView = DynAccessor(187)
                BattlePassUpgradeStyleTooltipView = DynAccessor(188)
                BattleTypesTooltipView = DynAccessor(189)
                BuyStagesFooterTooltipView = DynAccessor(190)
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
            EntryPoint = DynAccessor(380)
            RewardWindow = DynAccessor(381)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RestRewardTooltip = DynAccessor(382)

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
                    BattleConditions = DynAccessor(384)
                    Countdown = DynAccessor(385)
                    PendingDots = DynAccessor(386)

                common = _common()
                Daily = DynAccessor(387)
                DailyQuestsTooltip = DynAccessor(388)
                RerollTooltip = DynAccessor(389)
                RerollTooltipWithCountdown = DynAccessor(390)

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
            EntryPoint = DynAccessor(468)
            QualificationRewardsView = DynAccessor(469)
            RankedHangarWidget = DynAccessor(470)
            RankedPostbattleStatusView = DynAccessor(471)
            RankedProgressionView = DynAccessor(472)
            RankedSelectableRewardView = DynAccessor(473)
            RankedSelectedRewardView = DynAccessor(474)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RankedBattlesRolesTooltipView = DynAccessor(475)

            tooltips = _tooltips()
            YearLeaderboardView = DynAccessor(476)

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
            AdditionalRewardsTooltip = DynAccessor(577)
            NewbieRestrictionsTooltip = DynAccessor(578)
            PreferredMapSlotRewardTooltip = DynAccessor(579)
            QuestConditionsTooltip = DynAccessor(580)
            TankmanTooltipView = DynAccessor(581)
            VehPostProgressionEntryPointTooltip = DynAccessor(582)

        tooltips = _tooltips()

        class _video(DynAccessor):
            __slots__ = ()

            class _video_view(DynAccessor):
                __slots__ = ()
                VideoView = DynAccessor(59)

            video_view = _video_view()
            VideoViewWebm = DynAccessor(616)

        video = _video()

        class _account_completion(DynAccessor):
            __slots__ = ()
            AddCredentialsView = DynAccessor(112)
            CompleteView = DynAccessor(113)
            ConfirmCredentialsView = DynAccessor(114)
            ContactSupportView = DynAccessor(115)
            CurtainView = DynAccessor(116)
            EmptyView = DynAccessor(117)
            ErrorView = DynAccessor(118)
            RenamingCompleteView = DynAccessor(119)
            RenamingView = DynAccessor(120)

            class _tooltips(DynAccessor):
                __slots__ = ()
                HangarTooltip = DynAccessor(121)
                RenamingHangarTooltip = DynAccessor(122)

            tooltips = _tooltips()

        account_completion = _account_completion()

        class _account_dashboard(DynAccessor):
            __slots__ = ()
            AccountDashboard = DynAccessor(123)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExcludedMapsRewardSlotsTooltipView = DynAccessor(124)

            tooltips = _tooltips()

        account_dashboard = _account_dashboard()

        class _achievements(DynAccessor):
            __slots__ = ()
            AchievementsMainView = DynAccessor(125)

            class _dialogs(DynAccessor):
                __slots__ = ()
                EditConfirm = DynAccessor(126)

            dialogs = _dialogs()
            EditView = DynAccessor(127)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AutoSettingTooltip = DynAccessor(128)
                BattlesKPITooltip = DynAccessor(129)
                EditingTooltip = DynAccessor(130)
                KPITooltip = DynAccessor(131)
                WOTPRMainTooltip = DynAccessor(132)
                WTRInfoTooltip = DynAccessor(133)
                WTRMainTooltip = DynAccessor(134)

            tooltips = _tooltips()

        achievements = _achievements()

        class _awards(DynAccessor):
            __slots__ = ()
            BadgeAwardView = DynAccessor(135)
            MultipleAwardsView = DynAccessor(136)

            class _tooltips(DynAccessor):
                __slots__ = ()
                VehicleForChooseTooltip = DynAccessor(137)

            tooltips = _tooltips()

        awards = _awards()

        class _battle_matters(DynAccessor):
            __slots__ = ()
            BattleMattersEntryPointView = DynAccessor(138)
            BattleMattersExchangeRewards = DynAccessor(139)
            BattleMattersMainRewardView = DynAccessor(140)
            BattleMattersMainView = DynAccessor(141)
            BattleMattersPausedView = DynAccessor(142)
            BattleMattersRewardsView = DynAccessor(143)
            BattleMattersVehicleSelectionView = DynAccessor(144)

            class _popovers(DynAccessor):
                __slots__ = ()
                BattleMattersFilterPopoverView = DynAccessor(145)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattleMattersEntryTooltipView = DynAccessor(146)
                BattleMattersTokenTooltipView = DynAccessor(147)

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

        class _black_market(DynAccessor):
            __slots__ = ()

            class _banner(DynAccessor):
                __slots__ = ()
                BlackMarketBannerView = DynAccessor(204)

            banner = _banner()

        black_market = _black_market()

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
            Comp7SkillSelectView = DynAccessor(231)
            MainWidget = DynAccessor(232)
            MetaRootView = DynAccessor(233)
            NoVehiclesScreen = DynAccessor(234)
            RewardsScreen = DynAccessor(235)
            SeasonModifier = DynAccessor(236)

            class _tooltips(DynAccessor):
                __slots__ = ()
                Comp7ChargeTooltip = DynAccessor(237)
                Comp7SkillTooltip = DynAccessor(238)
                DivisionTooltip = DynAccessor(239)
                GeneralRankTooltip = DynAccessor(240)
                MainWidgetTooltip = DynAccessor(241)
                RankInactivityTooltip = DynAccessor(242)
                SeasonPointTooltip = DynAccessor(243)

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
            ChangeTankmanSkinView = DynAccessor(247)
            CrewHeaderTooltipView = DynAccessor(248)
            CrewIntroView = DynAccessor(249)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChangeTankmanTrainingDialog = DynAccessor(250)
                CrewBooksPurchaseDialog = DynAccessor(251)
                DismissOrRestoreTankmans = DynAccessor(252)
                DismissTankmanDialog = DynAccessor(253)
                DocumentChangeDialog = DynAccessor(254)
                EnlargeBarracksDialog = DynAccessor(255)
                PerksResetContent = DynAccessor(256)
                RecruitDialog = DynAccessor(257)
                RecruitNewTankmanDialog = DynAccessor(258)
                RestoreTankmanDialog = DynAccessor(259)
                RetrainDialog = DynAccessor(260)
                RoleChangeDialog = DynAccessor(261)
                SkinApplyDialog = DynAccessor(262)

            dialogs = _dialogs()
            HangarCrewWidget = DynAccessor(263)
            HelpView = DynAccessor(264)
            MemberChangeView = DynAccessor(265)

            class _personal_case(DynAccessor):
                __slots__ = ()

                class _component(DynAccessor):
                    __slots__ = ()
                    ScrollWithLips = DynAccessor(266)
                    TankmanInfoWrapper = DynAccessor(267)

                component = _component()
                PersonalDataView = DynAccessor(268)
                PersonalFileView = DynAccessor(269)
                ServiceRecordView = DynAccessor(270)

            personal_case = _personal_case()

            class _popovers(DynAccessor):
                __slots__ = ()
                FilterPopoverView = DynAccessor(271)

            popovers = _popovers()
            QuickTrainingView = DynAccessor(272)
            TankChangeView = DynAccessor(273)
            TankmanChangeAndRecruitView = DynAccessor(274)
            TankmanContainerView = DynAccessor(275)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AdvancedTooltipView = DynAccessor(276)
                BunksConfirmDiscountTooltip = DynAccessor(277)
                CrewPerksAdditionalTooltip = DynAccessor(278)
                CrewPerksTooltip = DynAccessor(279)
                DismissedToggleTooltip = DynAccessor(280)
                ExperienceStepperTooltip = DynAccessor(281)
                PerkAvailableTooltip = DynAccessor(282)
                PremiumVehicleTooltip = DynAccessor(283)
                QuickTrainingDiscountTooltip = DynAccessor(284)
                TankmanChangePreviewTooltip = DynAccessor(285)
                TankmanTooltip = DynAccessor(286)
                TrainingLevelTooltip = DynAccessor(287)
                VehCmpSkillsTooltip = DynAccessor(288)
                VehicleParamsTooltipView = DynAccessor(289)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                CrewWidget = DynAccessor(290)
                FilterPanelWidget = DynAccessor(291)
                PriceList = DynAccessor(292)
                TankmanInfo = DynAccessor(293)

            widgets = _widgets()

        crew = _crew()

        class _crystalsPromo(DynAccessor):
            __slots__ = ()
            CrystalsPromoView = DynAccessor(294)

        crystalsPromo = _crystalsPromo()

        class _currency_reserves(DynAccessor):
            __slots__ = ()
            CurrencyReserves = DynAccessor(295)
            ReservesAwardView = DynAccessor(296)

        currency_reserves = _currency_reserves()

        class _customization(DynAccessor):
            __slots__ = ()
            CustomizationBinSubview = DynAccessor(297)
            CustomizationCart = DynAccessor(298)
            CustomizationCloseConfirmationDialog = DynAccessor(299)
            CustomizationMainView = DynAccessor(300)
            CustomizationMoneyBalance = DynAccessor(301)
            CustomizationStyleInfoView = DynAccessor(302)

            class _popovers(DynAccessor):
                __slots__ = ()
                CustomizationFilterPopoverView = DynAccessor(303)

            popovers = _popovers()

            class _progression_styles(DynAccessor):
                __slots__ = ()
                OnboardingView = DynAccessor(304)
                StageSwitcher = DynAccessor(305)

            progression_styles = _progression_styles()

            class _progressive_items_reward(DynAccessor):
                __slots__ = ()
                ProgressiveItemsUpgradeView = DynAccessor(306)

            progressive_items_reward = _progressive_items_reward()

            class _progressive_items_view(DynAccessor):
                __slots__ = ()
                ProgressiveItemsView = DynAccessor(307)

            progressive_items_view = _progressive_items_view()

            class _style_unlocked_view(DynAccessor):
                __slots__ = ()
                StyleUnlockedView = DynAccessor(308)

            style_unlocked_view = _style_unlocked_view()

        customization = _customization()

        class _customization_resource(DynAccessor):
            __slots__ = ()
            CustomizationResourceEntryPointView = DynAccessor(309)
            CustomizationResourceFilterPopoverView = DynAccessor(310)
            CustomizationResourceIntroPageView = DynAccessor(311)
            CustomizationResourceMainView = DynAccessor(312)
            CustomizationResourceRewardView = DynAccessor(313)
            CustomizationResourceVideoRewardView = DynAccessor(314)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CategoryTooltipView = DynAccessor(315)
                CustomizationResourceCurrencyTooltipView = DynAccessor(316)

            tooltips = _tooltips()

        customization_resource = _customization_resource()

        class _daily(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                RerollButton = DynAccessor(317)

            common = _common()
            DailyQuestPremiumTabView = DynAccessor(318)
            DailyQuestRegularTabView = DynAccessor(319)
            DailyQuestRerollView = DynAccessor(320)
            DailyQuestsRegularView = DynAccessor(321)
            DailyQuestsView = DynAccessor(322)
            DailyQuestWidget = DynAccessor(323)
            SerialEnterTabView = DynAccessor(324)
            SerialEnterView = DynAccessor(325)
            SessionProgressRewardScreen = DynAccessor(326)
            SessionProgressRewardsNotificationView = DynAccessor(327)

            class _tooltips(DynAccessor):
                __slots__ = ()
                DailyQuestTooltip = DynAccessor(328)
                LockedSubscriptionBonusTooltip = DynAccessor(329)
                ModeSelectorTooltip = DynAccessor(330)
                RerollTooltip = DynAccessor(331)
                SessionProgressRewardsCompensationTooltip = DynAccessor(332)
                SessionProgressRewardsTooltip = DynAccessor(333)

            tooltips = _tooltips()
            WeeklyRewardScreen = DynAccessor(334)

        daily = _daily()

        class _debutBoxes(DynAccessor):
            __slots__ = ()
            DebutBoxesBadgeTooltipView = DynAccessor(335)

        debutBoxes = _debutBoxes()

        class _dedication(DynAccessor):
            __slots__ = ()
            DedicationRewardView = DynAccessor(336)

        dedication = _dedication()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            DedicationTooltip = DynAccessor(337)
            DogTagsView = DynAccessor(338)
            RankedEfficiencyTooltip = DynAccessor(339)
            ThreeMonthsTooltip = DynAccessor(340)
            TriumphTooltip = DynAccessor(341)

        dog_tags = _dog_tags()

        class _early_access(DynAccessor):
            __slots__ = ()
            EarlyAccessBuyView = DynAccessor(342)
            EarlyAccessEntryPointView = DynAccessor(343)
            EarlyAccessIntroView = DynAccessor(344)
            EarlyAccessQuestsView = DynAccessor(345)
            EarlyAccessRewardsView = DynAccessor(346)
            EarlyAccessVehicleView = DynAccessor(347)

            class _tooltips(DynAccessor):
                __slots__ = ()
                EarlyAccessCommonDescriptionTooltip = DynAccessor(348)
                EarlyAccessCompensationTooltip = DynAccessor(349)
                EarlyAccessCurrencyTooltipView = DynAccessor(350)
                EarlyAccessEntryPointPausedTooltip = DynAccessor(351)
                EarlyAccessEntryPointTooltipView = DynAccessor(352)
                EarlyAccessSimpleTooltipView = DynAccessor(353)
                EarlyAccessTokensStepperTooltip = DynAccessor(354)
                EarlyAccessVehicleCarouselPausedTooltip = DynAccessor(355)
                EarlyAccessVehicleLockedTooltip = DynAccessor(356)

            tooltips = _tooltips()

        early_access = _early_access()

        class _elite_window(DynAccessor):
            __slots__ = ()
            EliteView = DynAccessor(357)

        elite_window = _elite_window()

        class _events_core_client(DynAccessor):
            __slots__ = ()

            class _video_view(DynAccessor):
                __slots__ = ()
                VideoView = DynAccessor(358)

            video_view = _video_view()

        events_core_client = _events_core_client()

        class _excluded_maps(DynAccessor):
            __slots__ = ()
            ExcludedMapsView = DynAccessor(359)

        excluded_maps = _excluded_maps()

        class _frontline(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(360)

            class _dialogs(DynAccessor):
                __slots__ = ()
                BlankPrice = DynAccessor(361)

            dialogs = _dialogs()
            IntroScreen = DynAccessor(362)
            RewardsSelectionView = DynAccessor(363)

        frontline = _frontline()

        class _hangar(DynAccessor):
            __slots__ = ()
            BattleModifiersPanelView = DynAccessor(364)

            class _subViews(DynAccessor):
                __slots__ = ()
                VehicleParams = DynAccessor(365)

            subViews = _subViews()
            VehicleParamsWidget = DynAccessor(366)

        hangar = _hangar()

        class _instructions(DynAccessor):
            __slots__ = ()
            BuyWindow = DynAccessor(367)
            SellWindow = DynAccessor(368)

        instructions = _instructions()

        class _mapbox(DynAccessor):
            __slots__ = ()
            MapBoxAwardsView = DynAccessor(369)
            MapBoxEntryPointView = DynAccessor(370)
            MapBoxIntro = DynAccessor(371)
            MapBoxProgression = DynAccessor(372)
            MapBoxRewardChoiceView = DynAccessor(373)
            MapBoxSurveyView = DynAccessor(374)

        mapbox = _mapbox()

        class _maps_training(DynAccessor):
            __slots__ = ()
            MapPointDescriptionTooltip = DynAccessor(375)
            MapsTrainingPage = DynAccessor(376)
            MapsTrainingQueue = DynAccessor(377)
            MapsTrainingResult = DynAccessor(378)
            ScenarioTooltip = DynAccessor(379)

        maps_training = _maps_training()

        class _matchmaker(DynAccessor):
            __slots__ = ()
            ActiveTestConfirmView = DynAccessor(383)

        matchmaker = _matchmaker()

        class _mode_selector(DynAccessor):
            __slots__ = ()
            BattleSessionView = DynAccessor(391)
            ModeSelectorView = DynAccessor(392)

            class _popovers(DynAccessor):
                __slots__ = ()
                RandomBattlePopover = DynAccessor(393)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                AlertTooltip = DynAccessor(394)

                class _common(DynAccessor):
                    __slots__ = ()
                    Divider = DynAccessor(395)
                    GradientDecorator = DynAccessor(396)

                common = _common()
                SimplyFormatTooltip = DynAccessor(397)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                BattleRoyaleProgressionWidget = DynAccessor(398)
                BattleRoyaleWidget = DynAccessor(399)
                EpicWidget = DynAccessor(400)
                RankedWidget = DynAccessor(401)
                StrongholdWidget = DynAccessor(402)

            widgets = _widgets()

        mode_selector = _mode_selector()

        class _offers(DynAccessor):
            __slots__ = ()
            OfferBannerWindow = DynAccessor(403)
            OfferGiftsWindow = DynAccessor(404)
            OfferRewardWindow = DynAccessor(405)

        offers = _offers()

        class _paragons(DynAccessor):
            __slots__ = ()

            class _banner(DynAccessor):
                __slots__ = ()
                BannerView = DynAccessor(406)

            banner = _banner()

            class _common(DynAccessor):
                __slots__ = ()
                DateTimer = DynAccessor(407)
                Header = DynAccessor(408)
                VehicleName = DynAccessor(409)
                Video = DynAccessor(410)

            common = _common()
            IntroView = DynAccessor(411)
            NavigationView = DynAccessor(412)

            class _notifications(DynAccessor):
                __slots__ = ()
                ParagonsCoinsNotificationView = DynAccessor(413)

            notifications = _notifications()
            ParagonsRewardsView = DynAccessor(414)
            ResetBranchView = DynAccessor(415)
            SelectRewardsView = DynAccessor(416)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BlueprintUniversalTooltip = DynAccessor(417)
                BranchSelectTooltip = DynAccessor(418)
                EntryPointTooltip = DynAccessor(419)
                ParagonsCarouselPointsTooltip = DynAccessor(420)
                PointsTooltip = DynAccessor(421)
                ResetBranchTooltip = DynAccessor(422)
                ResetButtonTooltip = DynAccessor(423)
                RewardsHeaderTooltip = DynAccessor(424)
                SeasonTooltip = DynAccessor(425)
                SelectedRewardsTooltip = DynAccessor(426)
                VehicleSelectTooltip = DynAccessor(427)

            tooltips = _tooltips()
            VideoRewardView = DynAccessor(428)

        paragons = _paragons()

        class _personal_missions(DynAccessor):
            __slots__ = ()
            PersonalMissionsIntroVideoView = DynAccessor(429)
            PersonalMissionsIntroView = DynAccessor(430)
            PersonalMissionsMainQuestsView = DynAccessor(431)
            PersonalMissionsOperationsView = DynAccessor(432)
            PersonalMissionsQuestResetView = DynAccessor(433)
            PersonalMissionsRewardsSelectionView = DynAccessor(434)
            PersonalMissionsRewardsView = DynAccessor(435)
            PersonalMissionsVehicleView = DynAccessor(436)
            PersonalMissionsVideoRewardsView = DynAccessor(437)

            class _tooltips(DynAccessor):
                __slots__ = ()
                PersonalMissionsLastOperationTooltip = DynAccessor(438)
                PersonalMissionsOperationsTooltip = DynAccessor(439)
                PersonalMissionsQuestInfoTooltip = DynAccessor(440)
                PersonalMissionsQuestsTypeTooltip = DynAccessor(441)
                QuestCardTooltip = DynAccessor(442)
                RestRewardsTooltipView = DynAccessor(443)
                VehicleTabsTooltip = DynAccessor(444)

            tooltips = _tooltips()

        personal_missions = _personal_missions()

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            PersonalReservesTooltip = DynAccessor(445)
            PersonalReservesWidget = DynAccessor(446)
            ReserveCard = DynAccessor(447)
            ReserveCardTooltip = DynAccessor(448)
            ReserveGroup = DynAccessor(449)
            ReservesActivationView = DynAccessor(450)
            ReservesIntroView = DynAccessor(451)

        personal_reserves = _personal_reserves()

        class _platoon(DynAccessor):
            __slots__ = ()
            AlertTooltip = DynAccessor(452)
            MembersWindow = DynAccessor(453)
            PlatoonDropdown = DynAccessor(454)
            SearchingDropdown = DynAccessor(455)
            SettingsPopover = DynAccessor(456)

            class _subViews(DynAccessor):
                __slots__ = ()
                Chat = DynAccessor(457)
                SettingsContent = DynAccessor(458)
                TiersLimit = DynAccessor(459)

            subViews = _subViews()
            WTRTooltip = DynAccessor(460)

        platoon = _platoon()

        class _player_subscriptions(DynAccessor):
            __slots__ = ()
            PlayerSubscriptions = DynAccessor(461)
            SubscriptionItem = DynAccessor(462)
            SubscriptionRewardView = DynAccessor(463)

        player_subscriptions = _player_subscriptions()

        class _pm_announce(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                PersonalMissionsNewCampaignTooltipView = DynAccessor(464)
                PersonalMissionsOldCampaignTooltipView = DynAccessor(465)

            tooltips = _tooltips()

        pm_announce = _pm_announce()

        class _poll(DynAccessor):
            __slots__ = ()
            PollView = DynAccessor(466)

        poll = _poll()

        class _promo_code_reward_screen(DynAccessor):
            __slots__ = ()
            PromoCodeRewardScreenView = DynAccessor(467)

        promo_code_reward_screen = _promo_code_reward_screen()

        class _research(DynAccessor):
            __slots__ = ()
            BuyModuleDialogView = DynAccessor(477)
            InsufficientCreditsTooltip = DynAccessor(478)
            SoldModuleInfoTooltip = DynAccessor(479)

        research = _research()

        class _resource_well(DynAccessor):
            __slots__ = ()
            AwardView = DynAccessor(480)
            CompletedProgressionView = DynAccessor(481)
            EntryPoint = DynAccessor(482)
            IntroView = DynAccessor(483)
            NoSerialVehiclesConfirm = DynAccessor(484)
            NoVehiclesConfirm = DynAccessor(485)
            ProgressionView = DynAccessor(486)
            ResourcesLoadingConfirm = DynAccessor(487)
            ResourcesLoadingView = DynAccessor(488)

            class _sharedComponents(DynAccessor):
                __slots__ = ()

                class _award(DynAccessor):
                    __slots__ = ()
                    AdditionalReward = DynAccessor(489)
                    Footer = DynAccessor(490)
                    Header = DynAccessor(491)
                    Reward = DynAccessor(492)

                award = _award()
                Counter = DynAccessor(493)
                NoVehiclesState = DynAccessor(494)
                Resource = DynAccessor(495)
                VehicleCount = DynAccessor(496)
                VehicleInfo = DynAccessor(497)

            sharedComponents = _sharedComponents()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(498)
                MaxProgressTooltip = DynAccessor(499)
                ProgressTooltip = DynAccessor(500)
                RefundResourcesTooltip = DynAccessor(501)
                SerialNumberTooltip = DynAccessor(502)

            tooltips = _tooltips()

        resource_well = _resource_well()

        class _seniority_awards(DynAccessor):
            __slots__ = ()
            SeniorityAwardsView = DynAccessor(503)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                SeniorityAwardCoin = DynAccessor(504)

            sharedComponents = _sharedComponents()

        seniority_awards = _seniority_awards()

        class _shop_sales(DynAccessor):
            __slots__ = ()
            ShopSalesEntryPointView = DynAccessor(505)

        shop_sales = _shop_sales()

        class _stronghold(DynAccessor):
            __slots__ = ()
            StrongholdEntryPointView = DynAccessor(506)
            StrongholdMainWidget = DynAccessor(507)
            StrongholdSelectableRewardView = DynAccessor(508)
            StrongholdSelectedRewardView = DynAccessor(509)

            class _tooltips(DynAccessor):
                __slots__ = ()
                StrongholdMainWidgetTooltip = DynAccessor(510)

            tooltips = _tooltips()

        stronghold = _stronghold()

        class _subscription(DynAccessor):
            __slots__ = ()
            SubscriptionAwardView = DynAccessor(511)
            SubscriptionDailyQuestsIntro = DynAccessor(512)
            WotPlusIntroView = DynAccessor(513)
            WotPlusTooltip = DynAccessor(514)

        subscription = _subscription()

        class _summer_sale(DynAccessor):
            __slots__ = ()
            EventCurrencyTooltip = DynAccessor(515)
            RandomVehicleTooltip = DynAccessor(516)
            SummerSaleEntryPointView = DynAccessor(517)
            SummerSaleIntroPageView = DynAccessor(518)
            SummerSaleMainView = DynAccessor(519)
            SummerSaleRewardsView = DynAccessor(520)

        summer_sale = _summer_sale()

        class _tanksetup(DynAccessor):
            __slots__ = ()
            AmmunitionPanel = DynAccessor(521)

            class _common(DynAccessor):
                __slots__ = ()
                Action = DynAccessor(522)
                AutoRenewalDropdown = DynAccessor(523)
                CtaButtons = DynAccessor(524)
                DealPanel = DynAccessor(525)
                ExtraImage = DynAccessor(526)
                FormatColorTagText = DynAccessor(527)
                MaybeWrapper = DynAccessor(528)
                Price = DynAccessor(529)
                SetupApp = DynAccessor(530)
                ShortenedText = DynAccessor(531)
                Slider = DynAccessor(532)

                class _SlotParts(DynAccessor):
                    __slots__ = ()
                    Bonus = DynAccessor(533)
                    Container = DynAccessor(534)
                    Count = DynAccessor(535)
                    Inside = DynAccessor(536)
                    Level = DynAccessor(537)

                SlotParts = _SlotParts()
                Specializations = DynAccessor(538)
                Storage = DynAccessor(539)
                SwitchButton = DynAccessor(540)
                SwitchEquipment = DynAccessor(541)

                class _Transitions(DynAccessor):
                    __slots__ = ()
                    SlotTransitions = DynAccessor(542)

                Transitions = _Transitions()
                WeaponOccupancy = DynAccessor(543)

            common = _common()
            DeconstructionDeviceView = DynAccessor(544)

            class _dialogs(DynAccessor):
                __slots__ = ()
                Confirm = DynAccessor(545)
                ConfirmActionsWithEquipmentDialog = DynAccessor(546)
                DeconstructConfirm = DynAccessor(547)
                DeviceUpgradeDialog = DynAccessor(548)
                ExchangeToBuyItems = DynAccessor(549)
                ExchangeToUpgradeItems = DynAccessor(550)
                NeedRepair = DynAccessor(551)
                RefillShells = DynAccessor(552)
                Restore = DynAccessor(553)
                Sell = DynAccessor(554)

                class _sub_views(DynAccessor):
                    __slots__ = ()
                    FrontlineConfirmFooterMoney = DynAccessor(555)
                    FrontlineConfirmIcons = DynAccessor(556)
                    FrontlineConfirmMultipleNames = DynAccessor(557)
                    FrontlineConfirmTitle = DynAccessor(558)

                sub_views = _sub_views()

            dialogs = _dialogs()
            HangarAmmunitionSetup = DynAccessor(559)
            IntroScreen = DynAccessor(560)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AbilitySkillAdditionalTooltip = DynAccessor(561)
                AbilitySkillTooltip = DynAccessor(562)
                DeconstructFromInventoryTooltip = DynAccessor(563)
                DeconstructFromVehicleTooltip = DynAccessor(564)
                SetupTabTooltipView = DynAccessor(565)
                WarningTooltipView = DynAccessor(566)

            tooltips = _tooltips()
            VehicleCompareAmmunitionPanel = DynAccessor(567)
            VehicleCompareAmmunitionSetup = DynAccessor(568)

        tanksetup = _tanksetup()

        class _techtree(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                ParagonsEntryPointTooltip = DynAccessor(569)
                ParagonsLockedTooltip = DynAccessor(570)

            tooltips = _tooltips()
            VehicleTechTree = DynAccessor(571)

        techtree = _techtree()

        class _telecom(DynAccessor):
            __slots__ = ()

            class _shared(DynAccessor):
                __slots__ = ()
                Header = DynAccessor(572)
                Hero = DynAccessor(573)
                Rewards = DynAccessor(574)

            shared = _shared()
            TelecomRewardsView = DynAccessor(575)
            TelecomView = DynAccessor(576)

        telecom = _telecom()

        class _universal_flag(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EntryPointTooltip = DynAccessor(583)

            tooltips = _tooltips()
            UniversalFlagEntryPointView = DynAccessor(584)

        universal_flag = _universal_flag()

        class _vehicle_compare(DynAccessor):
            __slots__ = ()
            CompareModificationsPanelView = DynAccessor(585)
            SelectSlotSpecCompareDialog = DynAccessor(586)

        vehicle_compare = _vehicle_compare()

        class _vehicle_preview(DynAccessor):
            __slots__ = ()

            class _buying_panel(DynAccessor):
                __slots__ = ()
                EarlyAccessPanel = DynAccessor(587)
                StyleBuyingPanel = DynAccessor(588)
                VPProgressionStylesBuyingPanel = DynAccessor(589)
                WellPanel = DynAccessor(590)

            buying_panel = _buying_panel()

            class _tooltips(DynAccessor):
                __slots__ = ()
                StatTrackTooltip = DynAccessor(591)

            tooltips = _tooltips()

            class _top_panel(DynAccessor):
                __slots__ = ()
                TopPanelTabs = DynAccessor(592)

            top_panel = _top_panel()

        vehicle_preview = _vehicle_preview()

        class _veh_post_progression(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                Bonus = DynAccessor(593)
                Description = DynAccessor(594)
                Grid = DynAccessor(595)
                PersistentBonuses = DynAccessor(596)
                Slide = DynAccessor(597)
                SlideContent = DynAccessor(598)
                Slider = DynAccessor(599)
                TextSplit = DynAccessor(600)

            common = _common()
            PostProgressionInfo = DynAccessor(601)
            PostProgressionIntro = DynAccessor(602)
            PostProgressionResearchSteps = DynAccessor(603)

            class _tooltip(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()
                    DisabledBlock = DynAccessor(604)
                    FeatureLevelSubtitle = DynAccessor(605)
                    Lock = DynAccessor(606)
                    NotEnoughCredits = DynAccessor(607)
                    PriceBlock = DynAccessor(608)
                    Separator = DynAccessor(609)

                common = _common()
                PairModificationTooltipView = DynAccessor(610)
                PostProgressionLevelTooltipView = DynAccessor(611)
                RoleSlotTooltipView = DynAccessor(612)
                SetupTooltipView = DynAccessor(613)

            tooltip = _tooltip()
            VehiclePostProgressionCmpView = DynAccessor(614)
            VehiclePostProgressionView = DynAccessor(615)

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
            DialogTemplateGenericTooltip = DynAccessor(95)

        common = _common()
        DefaultDialog = DynAccessor(96)

        class _sub_views(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                SimpleText = DynAccessor(97)
                SinglePrice = DynAccessor(98)

            common = _common()

            class _content(DynAccessor):
                __slots__ = ()
                SelectOptionContent = DynAccessor(99)
                SimpleTextContent = DynAccessor(100)
                SinglePriceContent = DynAccessor(101)
                TextWithWarning = DynAccessor(102)

            content = _content()

            class _footer(DynAccessor):
                __slots__ = ()
                BRSinglePriceFooter = DynAccessor(103)
                SimpleTextFooter = DynAccessor(104)
                SinglePriceFooter = DynAccessor(105)

            footer = _footer()

            class _icon(DynAccessor):
                __slots__ = ()
                IconSet = DynAccessor(106)

            icon = _icon()

            class _title(DynAccessor):
                __slots__ = ()
                SimpleTextTitle = DynAccessor(107)

            title = _title()

            class _topRight(DynAccessor):
                __slots__ = ()
                BRMoneyBalance = DynAccessor(108)
                MoneyBalance = DynAccessor(109)

            topRight = _topRight()

        sub_views = _sub_views()

        class _widgets(DynAccessor):
            __slots__ = ()
            SinglePrice = DynAccessor(110)

        widgets = _widgets()

    dialogs = _dialogs()

    class _loading(DynAccessor):
        __slots__ = ()
        GameLoadingView = DynAccessor(111)

    loading = _loading()

    class _armory_yard(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                ArmoryYardBundlesView = DynAccessor(617)
                ArmoryYardBuyBundleView = DynAccessor(618)
                ArmoryYardBuyView = DynAccessor(619)
                ArmoryYardEntryPointView = DynAccessor(620)
                ArmoryYardIntroView = DynAccessor(621)
                ArmoryYardMainView = DynAccessor(622)
                ArmoryYardPurchaseStageBuyView = DynAccessor(623)
                ArmoryYardRerollView = DynAccessor(624)
                ArmoryYardRewardsView = DynAccessor(625)
                ArmoryYardShopBuyView = DynAccessor(626)
                ArmoryYardShopRewardsView = DynAccessor(627)
                ArmoryYardShopView = DynAccessor(628)
                ArmoryYardVideoRewardView = DynAccessor(629)
                ArmoryYardWidgetView = DynAccessor(630)

                class _dev(DynAccessor):
                    __slots__ = ()
                    ArmoryYardAllQuestsView = DynAccessor(631)

                dev = _dev()
                GfVideoView = DynAccessor(632)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ArmoryYardCurrencyTooltipView = DynAccessor(633)
                    ArmoryYardSimpleTooltipView = DynAccessor(634)
                    ArmoryYardTokenStepperTooltipView = DynAccessor(635)
                    ArmoryYardWalletNotAvailableTooltipView = DynAccessor(636)
                    EntryPointActiveTooltipView = DynAccessor(637)
                    EntryPointBeforeProgressionTooltipView = DynAccessor(638)
                    EntryPointNotActiveTooltipView = DynAccessor(639)
                    RerollButtonTooltip = DynAccessor(640)
                    RerollDescriptionTooltipView = DynAccessor(641)
                    RerollInfoContainerTooltip = DynAccessor(642)
                    RestRewardTooltipView = DynAccessor(643)
                    ShopCurrencyTooltipView = DynAccessor(644)
                    TaskConditionTooltipView = DynAccessor(645)

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
                ModifiersDomainTooltipView = DynAccessor(646)

            tooltips = _tooltips()

        lobby = _lobby()

    battle_modifiers = _battle_modifiers()

    class _battle_royale(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _views(DynAccessor):
                __slots__ = ()
                LeaveBattleView = DynAccessor(647)

            views = _views()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BrCoinTooltipView = DynAccessor(648)

                class _common(DynAccessor):
                    __slots__ = ()

                    class _LeaderBoard(DynAccessor):
                        __slots__ = ()
                        Column = DynAccessor(649)
                        Table = DynAccessor(650)

                    LeaderBoard = _LeaderBoard()
                    PriceBlock = DynAccessor(651)
                    RentPrice = DynAccessor(652)

                common = _common()
                LeaderboardRewardTooltipView = DynAccessor(653)
                RentIconTooltipView = DynAccessor(654)
                RespawnInfoTooltipView = DynAccessor(655)
                RewardCurrencyTooltipView = DynAccessor(656)
                TestDriveInfoTooltipView = DynAccessor(657)
                VehicleTooltipView = DynAccessor(658)
                WidgetTooltipView = DynAccessor(659)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                BattleRoyaleEntryPoint = DynAccessor(660)
                IntroView = DynAccessor(661)
                PreBattleView = DynAccessor(662)
                ProxyCurrencyView = DynAccessor(663)
                WidgetView = DynAccessor(664)

            views = _views()

        lobby = _lobby()

    battle_royale = _battle_royale()

    class _battle_royale_progression(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(665)
        ProgressionMainView = DynAccessor(666)

    battle_royale_progression = _battle_royale_progression()

    class _cosmic_event(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _cosmic_hud(DynAccessor):
                __slots__ = ()
                CosmicBattleHelpView = DynAccessor(667)
                CosmicReactHudView = DynAccessor(668)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    AbilityTooltip = DynAccessor(669)

                tooltips = _tooltips()

            cosmic_hud = _cosmic_hud()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _banner_entry_point(DynAccessor):
                __slots__ = ()
                CosmicBannerEntryPoint = DynAccessor(670)

            banner_entry_point = _banner_entry_point()

            class _cosmic_lobby_view(DynAccessor):
                __slots__ = ()
                CosmicLobbyView = DynAccessor(671)

            cosmic_lobby_view = _cosmic_lobby_view()

            class _cosmic_post_battle(DynAccessor):
                __slots__ = ()
                CosmicPostBattleView = DynAccessor(672)

            cosmic_post_battle = _cosmic_post_battle()

            class _queue_view(DynAccessor):
                __slots__ = ()
                QueueView = DynAccessor(673)

            queue_view = _queue_view()

            class _rewards_view(DynAccessor):
                __slots__ = ()
                RewardsView = DynAccessor(674)

            rewards_view = _rewards_view()

            class _tooltips(DynAccessor):
                __slots__ = ()
                CosmicLootboxTooltipExtended = DynAccessor(675)
                CosmicSimpleTooltip = DynAccessor(676)
                CosmicTooltipDecorator = DynAccessor(677)
                DailyQuestsTimerTooltip = DynAccessor(678)
                DailyQuestsTooltip = DynAccessor(679)
                ProgressionEntryPointTooltip = DynAccessor(680)
                RulesEntryPointTooltip = DynAccessor(681)
                SpecificationTooltip = DynAccessor(682)
                VehicleAbilityTooltip = DynAccessor(683)
                VehicleSelectorTooltip = DynAccessor(684)
                VehicleShellTooltip = DynAccessor(685)

            tooltips = _tooltips()

            class _video_view(DynAccessor):
                __slots__ = ()
                VideoView = DynAccessor(686)

            video_view = _video_view()

        lobby = _lobby()

    cosmic_event = _cosmic_event()

    class _frontline(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            FLProgressionCmp = DynAccessor(687)
            QuestsTabView = DynAccessor(688)
            QuestView = DynAccessor(689)

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()
            BannerView = DynAccessor(690)
            FrontlineContainerView = DynAccessor(691)
            InfoView = DynAccessor(692)
            ProgressView = DynAccessor(693)
            RewardsView = DynAccessor(694)
            SupplyObjectsView = DynAccessor(695)
            TabInfoView = DynAccessor(696)

            class _tooltips(DynAccessor):
                __slots__ = ()
                LevelReservesTooltip = DynAccessor(697)
                NotEnoughPointsTooltip = DynAccessor(698)
                SkillOrderTooltip = DynAccessor(699)
                UnlockConditionsTooltip = DynAccessor(700)

            tooltips = _tooltips()
            WelcomeView = DynAccessor(701)

        lobby = _lobby()

    frontline = _frontline()

    class _fun_random(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                FunRandomEntryPointView = DynAccessor(702)
                FunRandomHangarWidgetView = DynAccessor(703)
                FunRandomMapsView = DynAccessor(704)
                FunRandomModeSubSelector = DynAccessor(705)
                FunRandomModifiersPanel = DynAccessor(706)
                FunRandomProgression = DynAccessor(707)

            feature = _feature()

            class _tooltips(DynAccessor):
                __slots__ = ()
                FunRandomMapsDomainTooltip = DynAccessor(708)
                FunRandomProgressionTooltipView = DynAccessor(709)

            tooltips = _tooltips()

        lobby = _lobby()

    fun_random = _fun_random()

    class _gui_lootboxes(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _gui_lootboxes(DynAccessor):
                __slots__ = ()
                BonusProbabilitiesView = DynAccessor(710)
                EntryPointView = DynAccessor(711)
                KeysWelcomeScreen = DynAccessor(712)
                LootboxesFullStatsView = DynAccessor(713)
                LootBoxesLoseRewardScreen = DynAccessor(714)
                LootBoxesShortStatsView = DynAccessor(715)
                LootboxOpenBySelectionView = DynAccessor(716)
                LootboxRewardsView = DynAccessor(717)
                LootboxVideoRewardView = DynAccessor(718)
                OpenBoxErrorView = DynAccessor(719)

                class _shared(DynAccessor):
                    __slots__ = ()
                    AnimationControls = DynAccessor(720)
                    BacklitTransparentButton = DynAccessor(721)
                    BuyBoxFooter = DynAccessor(722)
                    CanvasSequence = DynAccessor(723)
                    CloseBtn = DynAccessor(724)
                    Compensation = DynAccessor(725)
                    CurrencyKey = DynAccessor(726)
                    DeadlineWidget = DynAccessor(727)
                    Divider = DynAccessor(728)
                    EscBtn = DynAccessor(729)
                    Header = DynAccessor(730)
                    Lootbox = DynAccessor(731)
                    NyBoxWithToys = DynAccessor(732)
                    RotationReward = DynAccessor(733)
                    RotationStage = DynAccessor(734)
                    RotationVehicle = DynAccessor(735)
                    VehicleInfo = DynAccessor(736)
                    Video = DynAccessor(737)
                    VideoComponent = DynAccessor(738)
                    Vignette = DynAccessor(739)

                shared = _shared()
                StorageView = DynAccessor(740)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    BonusGroupTooltip = DynAccessor(741)
                    CompensationTooltip = DynAccessor(742)
                    DeadlineTooltip = DynAccessor(743)
                    GuaranteedRewardTooltip = DynAccessor(744)
                    LootboxKeyTooltip = DynAccessor(745)
                    LootboxRotationTooltip = DynAccessor(746)
                    LootboxTooltip = DynAccessor(747)
                    LootboxTooltipExtended = DynAccessor(748)
                    OtherRewardsTooltip = DynAccessor(749)
                    PlayersListTooltip = DynAccessor(750)
                    ProbabilityButtonTooltip = DynAccessor(751)
                    ProbabilityGuaranteedRewardTooltip = DynAccessor(752)
                    ProbabilityStageButtonsTooltip = DynAccessor(753)
                    StatisticButtonTooltip = DynAccessor(754)

                tooltips = _tooltips()
                WelcomeScreen = DynAccessor(755)

            gui_lootboxes = _gui_lootboxes()

        lobby = _lobby()

    gui_lootboxes = _gui_lootboxes()

    class _museum_of_glory(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                MuseumVehicleView = DynAccessor(756)

            feature = _feature()

        lobby = _lobby()

    museum_of_glory = _museum_of_glory()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _newbie_start_page(DynAccessor):
                __slots__ = ()
                NewbieStartPageView = DynAccessor(757)

            newbie_start_page = _newbie_start_page()

        lobby = _lobby()

    newbie_start_page = _newbie_start_page()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _new_year(DynAccessor):
                __slots__ = ()
                AtmosphereLevelUp = DynAccessor(758)

                class _common(DynAccessor):
                    __slots__ = ()
                    FormatTextWithColorTags = DynAccessor(759)
                    IncreaseAnimation = DynAccessor(760)
                    NyPopoverDecorator = DynAccessor(761)
                    Shards = DynAccessor(762)

                    class _slots(DynAccessor):
                        __slots__ = ()
                        BreakDecorationSlot = DynAccessor(763)
                        DecorationSlot = DynAccessor(764)
                        EmptySlot = DynAccessor(765)
                        PetDecorationSlot = DynAccessor(766)
                        SlotPlaceholders = DynAccessor(767)

                    slots = _slots()
                    TokensStepper = DynAccessor(768)
                    VehicleBonus = DynAccessor(769)

                common = _common()
                CustomizationLevelUpView = DynAccessor(770)
                EnvironmentChangeView = DynAccessor(771)
                EnvSwitcherBtnTip = DynAccessor(772)
                EnvSwitcherBtnView = DynAccessor(773)

                class _loot_box(DynAccessor):
                    __slots__ = ()
                    LootBoxEntryView = DynAccessor(774)

                loot_box = _loot_box()
                MainView = DynAccessor(775)
                NyDailyQuestsInfoView = DynAccessor(776)
                NyLeaderboardInfoView = DynAccessor(777)
                NyLeaderboardRecountView = DynAccessor(778)
                NyLeaderboardRewardView = DynAccessor(779)
                NyMainWidget = DynAccessor(780)
                NyPetRaidRewardView = DynAccessor(781)
                NyPetTvScreenView = DynAccessor(782)
                NyProgressView = DynAccessor(783)
                NyQuestsRewardView = DynAccessor(784)
                NyTamagotchiRaidView = DynAccessor(785)
                NyVideoRewardView = DynAccessor(786)
                OnboardingView = DynAccessor(787)

                class _popovers(DynAccessor):
                    __slots__ = ()
                    EnvSwitcherPopover = DynAccessor(788)
                    NyDecorationsPopover = DynAccessor(789)
                    NyLootBoxPopover = DynAccessor(790)
                    NyPetItemActivatePopover = DynAccessor(791)
                    VehicleFilterPopover = DynAccessor(792)

                popovers = _popovers()
                RobotTvRewardsView = DynAccessor(793)
                RobotTvScreenView = DynAccessor(794)

                class _tooltips(DynAccessor):
                    __slots__ = ()

                    class _common(DynAccessor):
                        __slots__ = ()
                        DecorationContent = DynAccessor(795)
                        DecorationFooter = DynAccessor(796)
                        DecorationHeader = DynAccessor(797)
                        MenuInfo = DynAccessor(798)

                    common = _common()
                    CommonTooltip = DynAccessor(799)
                    CustomizationZoneTooltip = DynAccessor(800)
                    LevelUpWidgetTooltip = DynAccessor(801)
                    MenuMachineTooltip = DynAccessor(802)
                    NyBlockActivitiesTooltip = DynAccessor(803)
                    NyBoxWithToysTooltip = DynAccessor(804)
                    NyCurrencyCompensationTooltip = DynAccessor(805)
                    NyCurrencyTooltip = DynAccessor(806)
                    NyDecorationStateTooltip = DynAccessor(807)
                    NyDecorationTooltip = DynAccessor(808)
                    NyDiscountRewardTooltip = DynAccessor(809)
                    NyMainWidgetTooltip = DynAccessor(810)
                    NyMarketplaceTokenTooltip = DynAccessor(811)
                    NyPetBonusTooltip = DynAccessor(812)
                    NyPetDecorationTooltip = DynAccessor(813)
                    NyPetIndicatorTooltip = DynAccessor(814)
                    NyPetInRaidTooltip = DynAccessor(815)
                    NyPetOverviewTooltip = DynAccessor(816)
                    NyPetRaidBoostTooltip = DynAccessor(817)
                    NyPetTokenStepperTooltip = DynAccessor(818)
                    NyShopUnavailableTooltip = DynAccessor(819)
                    NyTotalBonusTooltip = DynAccessor(820)
                    SelectedRewardsTooltip = DynAccessor(821)

                tooltips = _tooltips()
                VehicleSelectionView = DynAccessor(822)

                class _views(DynAccessor):
                    __slots__ = ()
                    BuyToyView = DynAccessor(823)

                views = _views()
                WeeklyRewardsView = DynAccessor(824)

            new_year = _new_year()

        lobby = _lobby()

    new_year = _new_year()

    class _story_mode(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            EpilogueWindow = DynAccessor(825)
            OnboardingBattleResultView = DynAccessor(826)
            PrebattleWindow = DynAccessor(827)

        battle = _battle()

        class _common(DynAccessor):
            __slots__ = ()
            CongratulationsWindow = DynAccessor(828)
            MedalTooltip = DynAccessor(829)
            OnboardingQueueView = DynAccessor(830)

        common = _common()

        class _lobby(DynAccessor):
            __slots__ = ()
            BattleResultView = DynAccessor(831)
            MissionSelectionView = DynAccessor(832)
            MissionTooltip = DynAccessor(833)

        lobby = _lobby()

    story_mode = _story_mode()

    class _survey(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _survey(DynAccessor):
                __slots__ = ()
                SurveyView = DynAccessor(834)

            survey = _survey()

        lobby = _lobby()

    survey = _survey()

    class _tank_academy(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tank_academy(DynAccessor):
                __slots__ = ()

                class _popovers(DynAccessor):
                    __slots__ = ()
                    TankAcademyFilterPopoverView = DynAccessor(835)

                popovers = _popovers()
                TankAcademyEntryPointView = DynAccessor(836)
                TankAcademyExchangeRewards = DynAccessor(837)
                TankAcademyMainView = DynAccessor(838)
                TankAcademyMigrationUpdatesView = DynAccessor(839)
                TankAcademyRewardsView = DynAccessor(840)
                TankAcademyVehiclesSelectionView = DynAccessor(841)
                TankAcademyWelcomeView = DynAccessor(842)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    TankAcademyEntryPointTooltipView = DynAccessor(843)

                tooltips = _tooltips()

            tank_academy = _tank_academy()

        lobby = _lobby()

    tank_academy = _tank_academy()

    class _winback(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                CompensationTooltip = DynAccessor(844)
                SelectableRewardTooltip = DynAccessor(845)
                SelectedRewardsTooltip = DynAccessor(846)
                WidgetTooltipView = DynAccessor(847)

            tooltips = _tooltips()
            WinbackIntroView = DynAccessor(848)
            WinbackRewardView = DynAccessor(849)
            WinbackSelectableRewardView = DynAccessor(850)
            WinbackWidgetView = DynAccessor(851)

        lobby = _lobby()
        ProgressionMainView = DynAccessor(852)

    winback = _winback()
    Anchor = DynAccessor(853)
    ArmoryYardDemoView = DynAccessor(854)
    BotsMenu = DynAccessor(855)

    class _child_views_demo(DynAccessor):
        __slots__ = ()
        ChildDemoView = DynAccessor(856)
        MainView = DynAccessor(857)

    child_views_demo = _child_views_demo()
    ClientgwMockView = DynAccessor(858)
    Comp7DemoPageView = DynAccessor(859)
    ComponentsDemo = DynAccessor(860)
    DataLayerDemoView = DynAccessor(861)
    DataTrackerDemo = DynAccessor(862)
    DemoContextMenu = DynAccessor(863)
    Easings = DynAccessor(864)
    GameLoadingDebugView = DynAccessor(865)
    GFCharset = DynAccessor(866)
    GFComponents = DynAccessor(867)
    GFDemoPopover = DynAccessor(868)
    GFDemoRichTooltipWindow = DynAccessor(869)
    GFDemoWindow = DynAccessor(870)
    GFHooksDemo = DynAccessor(871)
    GFInjectView = DynAccessor(872)
    GFInputCases = DynAccessor(873)
    GfMarkerDemoView = DynAccessor(874)
    GFSimpleTooltipWindow = DynAccessor(875)
    GFWebSubDemoWindow = DynAccessor(876)

    class _gf_dialogs_demo(DynAccessor):
        __slots__ = ()
        DefaultDialogProxy = DynAccessor(877)
        GFDialogsDemo = DynAccessor(878)

        class _sub_views(DynAccessor):
            __slots__ = ()
            DummyContent = DynAccessor(879)
            DummyFooter = DynAccessor(880)
            DummyIcon = DynAccessor(881)
            DummyStepper = DynAccessor(882)
            DummyTitle = DynAccessor(883)
            DummyTopRight = DynAccessor(884)

        sub_views = _sub_views()

    gf_dialogs_demo = _gf_dialogs_demo()

    class _gf_viewer(DynAccessor):
        __slots__ = ()
        GFViewerWindow = DynAccessor(885)

    gf_viewer = _gf_viewer()

    class _igb_demo(DynAccessor):
        __slots__ = ()
        BrowserFullscreenWindow = DynAccessor(886)
        BrowserWindow = DynAccessor(887)
        MainView = DynAccessor(888)

    igb_demo = _igb_demo()
    LocaleDemo = DynAccessor(889)
    MediaWrapperDemo = DynAccessor(890)
    MixBlendMode = DynAccessor(891)
    MixBlendModeAnimation = DynAccessor(892)
    ModeSelectorDemo = DynAccessor(893)
    ModeSelectorToolsetView = DynAccessor(894)

    class _mttv(DynAccessor):
        __slots__ = ()
        CustomView = DynAccessor(895)
        MttvEntityView = DynAccessor(896)
        MttvKeyframeInfoView = DynAccessor(897)
        MttvKeyframeView = DynAccessor(898)
        MttvTimelineView = DynAccessor(899)
        MttvToolsView = DynAccessor(900)

    mttv = _mttv()
    PluralLocView = DynAccessor(901)
    PropsSupportDemo = DynAccessor(902)
    ReactSpringVizualizer = DynAccessor(903)
    SelectableRewardDemoView = DynAccessor(904)
    StructuralDataBindDemo = DynAccessor(905)

    class _sub_views_demo(DynAccessor):
        __slots__ = ()
        GFSubViewsDemo = DynAccessor(906)

        class _sub_views(DynAccessor):
            __slots__ = ()
            CustomizationCartProxy = DynAccessor(907)
            DailyProxy = DynAccessor(908)
            ProgressiveItemsViewProxy = DynAccessor(909)

        sub_views = _sub_views()

    sub_views_demo = _sub_views_demo()
    SurfaceView = DynAccessor(910)
    UILoggerDemo = DynAccessor(911)
    VideoSupportView = DynAccessor(912)
    W2CTestPageWindow = DynAccessor(913)