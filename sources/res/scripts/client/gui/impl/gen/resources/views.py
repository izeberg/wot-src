from gui.impl.gen_utils import DynAccessor

class Views(DynAccessor):
    __slots__ = ()

    class _battle(DynAccessor):
        __slots__ = ()

        class _battleRoyale(DynAccessor):
            __slots__ = ()

            class _select_respawn(DynAccessor):
                __slots__ = ()
                SelectRespawn = DynAccessor(9)

            select_respawn = _select_respawn()

        battleRoyale = _battleRoyale()

        class _battle_notifier(DynAccessor):
            __slots__ = ()
            BattleNotifierView = DynAccessor(76)

        battle_notifier = _battle_notifier()

        class _battle_page(DynAccessor):
            __slots__ = ()
            EpicRespawnAmmunitionPanelView = DynAccessor(77)
            PersonalReservesTabView = DynAccessor(78)
            PrebattleAmmunitionPanelView = DynAccessor(79)
            TabView = DynAccessor(80)

        battle_page = _battle_page()

        class _death_cam(DynAccessor):
            __slots__ = ()
            DeathCamHudView = DynAccessor(81)
            DeathCamUIView = DynAccessor(82)
            MarkerView = DynAccessor(83)

        death_cam = _death_cam()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            DogTagMarkerView = DynAccessor(84)

        dog_tags = _dog_tags()

        class _postmortem_panel(DynAccessor):
            __slots__ = ()
            PostmortemPanelView = DynAccessor(85)

        postmortem_panel = _postmortem_panel()

        class _prebattle(DynAccessor):
            __slots__ = ()
            PrebattleHintsView = DynAccessor(86)

        prebattle = _prebattle()

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
                ContextMenuContent = DynAccessor(10)

            context_menu_content = _context_menu_content()

            class _context_menu_window(DynAccessor):
                __slots__ = ()
                ContextMenuWindow = DynAccessor(11)

            context_menu_window = _context_menu_window()

        context_menu_window = _context_menu_window()

        class _dialog_view(DynAccessor):
            __slots__ = ()

            class _dialog_window(DynAccessor):
                __slots__ = ()
                DialogWindow = DynAccessor(12)

            dialog_window = _dialog_window()

            class _simple_dialog_content(DynAccessor):
                __slots__ = ()
                SimpleDialogContent = DynAccessor(13)

            simple_dialog_content = _simple_dialog_content()

            class _components(DynAccessor):
                __slots__ = ()

                class _balance_contents(DynAccessor):
                    __slots__ = ()
                    CommonBalanceContent = DynAccessor(14)

                balance_contents = _balance_contents()

                class _checkbox_content(DynAccessor):
                    __slots__ = ()
                    CheckBoxDialogContent = DynAccessor(15)

                checkbox_content = _checkbox_content()

                class _dialog_prices_content(DynAccessor):
                    __slots__ = ()
                    DialogPricesContent = DynAccessor(16)

                dialog_prices_content = _dialog_prices_content()

                class _dialog_prices_tooltip(DynAccessor):
                    __slots__ = ()
                    DialogPricesTooltip = DynAccessor(17)

                dialog_prices_tooltip = _dialog_prices_tooltip()

            components = _components()

        dialog_view = _dialog_view()

        class _drop_down_menu_window(DynAccessor):
            __slots__ = ()

            class _drop_down_menu_content(DynAccessor):
                __slots__ = ()
                DropDownMenuContent = DynAccessor(18)

            drop_down_menu_content = _drop_down_menu_content()

            class _drop_down_menu_window(DynAccessor):
                __slots__ = ()
                DropDownMenuWindow = DynAccessor(19)

            drop_down_menu_window = _drop_down_menu_window()

        drop_down_menu_window = _drop_down_menu_window()

        class _pop_over_window(DynAccessor):
            __slots__ = ()

            class _backport_pop_over(DynAccessor):
                __slots__ = ()
                BackportPopOverContent = DynAccessor(20)
                BackportPopOverWindow = DynAccessor(21)

            backport_pop_over = _backport_pop_over()

            class _pop_over_window(DynAccessor):
                __slots__ = ()
                PopOverWindow = DynAccessor(22)

            pop_over_window = _pop_over_window()

        pop_over_window = _pop_over_window()

        class _standard_window(DynAccessor):
            __slots__ = ()

            class _standard_window(DynAccessor):
                __slots__ = ()
                StandardWindow = DynAccessor(23)

            standard_window = _standard_window()

        standard_window = _standard_window()

        class _tooltip_window(DynAccessor):
            __slots__ = ()

            class _advanced_tooltip_content(DynAccessor):
                __slots__ = ()
                AdvandcedTooltipContent = DynAccessor(24)
                AdvandcedAnimatedTooltipContent = DynAccessor(25)

            advanced_tooltip_content = _advanced_tooltip_content()

            class _backport_tooltip_content(DynAccessor):
                __slots__ = ()
                BackportTooltipContent = DynAccessor(26)

            backport_tooltip_content = _backport_tooltip_content()

            class _loot_box_compensation_tooltip(DynAccessor):
                __slots__ = ()
                LootBoxCompensationTooltipContent = DynAccessor(27)
                CrewSkinsCompensationTooltipContent = DynAccessor(28)
                LootBoxVehicleCompensationTooltipContent = DynAccessor(29)

            loot_box_compensation_tooltip = _loot_box_compensation_tooltip()

            class _simple_tooltip_content(DynAccessor):
                __slots__ = ()
                SimpleTooltipContent = DynAccessor(30)
                SimpleTooltipHtmlContent = DynAccessor(31)

            simple_tooltip_content = _simple_tooltip_content()

            class _tooltip_window(DynAccessor):
                __slots__ = ()
                TooltipWindow = DynAccessor(32)

            tooltip_window = _tooltip_window()

        tooltip_window = _tooltip_window()
        BackportContextMenu = DynAccessor(88)
        Browser = DynAccessor(89)
        FadingCoverView = DynAccessor(90)
        HintButton = DynAccessor(91)

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            ReservesDisabledTooltip = DynAccessor(92)

        personal_reserves = _personal_reserves()

    common = _common()

    class _lobby(DynAccessor):
        __slots__ = ()

        class _battleRoyale(DynAccessor):
            __slots__ = ()

            class _event_info(DynAccessor):
                __slots__ = ()
                EventInfo = DynAccessor(33)

            event_info = _event_info()

        battleRoyale = _battleRoyale()

        class _battle_pass(DynAccessor):
            __slots__ = ()

            class _trophy_device_confirm_dialog(DynAccessor):
                __slots__ = ()
                TrophyDeviceConfirmDialogContent = DynAccessor(34)

            trophy_device_confirm_dialog = _trophy_device_confirm_dialog()
            BattlePassAwardsView = DynAccessor(147)
            BattlePassBuyLevelView = DynAccessor(148)
            BattlePassBuyView = DynAccessor(149)
            BattlePassEntryPointView = DynAccessor(150)
            BattlePassHowToEarnPointsView = DynAccessor(151)
            BattlePassIntroView = DynAccessor(152)
            BattlePassProgressionsView = DynAccessor(153)
            BattlePassVehicleAwardView = DynAccessor(154)
            ChapterChoiceView = DynAccessor(155)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChapterConfirm = DynAccessor(156)

            dialogs = _dialogs()
            ExtraIntroView = DynAccessor(157)
            FullscreenVideoView = DynAccessor(158)
            HolidayFinalView = DynAccessor(159)
            MainView = DynAccessor(160)
            PostProgressionView = DynAccessor(161)
            RewardsSelectionView = DynAccessor(162)
            RewardsViewContent = DynAccessor(163)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                AnimatedReward = DynAccessor(164)
                AttachmentOverlay = DynAccessor(165)
                AwardsWidget = DynAccessor(166)
                BuyButtons = DynAccessor(167)
                ChapterBackground = DynAccessor(168)
                CurrencyReward = DynAccessor(169)
                Emblem = DynAccessor(170)
                FormatRemainingDate = DynAccessor(171)
                Header = DynAccessor(172)
                LoupeButton = DynAccessor(173)
                RewardsBlock = DynAccessor(174)
                ScrollWithLips = DynAccessor(175)
                Slider = DynAccessor(176)
                TankmanSkills = DynAccessor(177)
                Title = DynAccessor(178)
                VehicleBonusList = DynAccessor(179)
                VehicleInfo = DynAccessor(180)
                VehicleList = DynAccessor(181)

            sharedComponents = _sharedComponents()
            TankmenVoiceoverView = DynAccessor(182)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattlePassCoinTooltipView = DynAccessor(183)
                BattlePassCompletedTooltipView = DynAccessor(184)
                BattlePassGoldMissionTooltipView = DynAccessor(185)
                BattlePassInProgressTooltipView = DynAccessor(186)
                BattlePassLockIconTooltipView = DynAccessor(187)
                BattlePassNoChapterTooltipView = DynAccessor(188)
                BattlePassOnPauseTooltipView = DynAccessor(189)
                BattlePassPointsView = DynAccessor(190)
                BattlePassQuestsChainTooltipView = DynAccessor(191)
                BattlePassTalerTooltip = DynAccessor(192)
                BattlePassUpgradeStyleTooltipView = DynAccessor(193)
                CrewMemberSkillTooltip = DynAccessor(194)
                RandomQuestTooltip = DynAccessor(195)

                class _sharedComponents(DynAccessor):
                    __slots__ = ()
                    BlockCompleted = DynAccessor(196)
                    Chose = DynAccessor(197)
                    FinalLevel = DynAccessor(198)
                    IconTextBlock = DynAccessor(199)
                    PerBattlePointsTable = DynAccessor(200)
                    Point = DynAccessor(201)
                    Rewards = DynAccessor(202)
                    Separator = DynAccessor(203)

                sharedComponents = _sharedComponents()
                VehiclePointsTooltipView = DynAccessor(204)

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
            Confirm = DynAccessor(207)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BlueprintsAlliancesTooltipView = DynAccessor(208)

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
            AwardsView = DynAccessor(217)
            BrowserView = DynAccessor(218)
            RewardSelection = DynAccessor(219)
            SelectableRewardBase = DynAccessor(220)
            SelectSlotSpecDialog = DynAccessor(221)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExtendedTextTooltip = DynAccessor(222)
                SelectedRewardsTooltipView = DynAccessor(223)
                SimpleIconTooltip = DynAccessor(224)

            tooltips = _tooltips()

        common = _common()

        class _marathon(DynAccessor):
            __slots__ = ()

            class _marathon_reward_view(DynAccessor):
                __slots__ = ()
                MarathonRewardView = DynAccessor(38)

            marathon_reward_view = _marathon_reward_view()
            EntryPoint = DynAccessor(356)
            RewardWindow = DynAccessor(357)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RestRewardTooltip = DynAccessor(358)

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
                BattleConditions = DynAccessor(360)
                Countdown = DynAccessor(361)
                PendingDots = DynAccessor(362)

            common = _common()
            Daily = DynAccessor(363)
            DailyQuestsTooltip = DynAccessor(364)
            DailyQuestsWidget = DynAccessor(365)
            RerollTooltip = DynAccessor(366)
            RerollTooltipWithCountdown = DynAccessor(367)

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

            class _piggybank(DynAccessor):
                __slots__ = ()
                Piggybank = DynAccessor(41)

            piggybank = _piggybank()

            class _dashboard(DynAccessor):
                __slots__ = ()

                class _prem_dashboard_parent_control_info(DynAccessor):
                    __slots__ = ()
                    PremDashboardParentControlInfoContent = DynAccessor(42)

                prem_dashboard_parent_control_info = _prem_dashboard_parent_control_info()

                class _piggy_bank_cards(DynAccessor):
                    __slots__ = ()

                    class _prem_piggy_bank(DynAccessor):
                        __slots__ = ()
                        PremPiggyBankCard = DynAccessor(43)

                    prem_piggy_bank = _prem_piggy_bank()

                    class _wot_plus_piggy_bank(DynAccessor):
                        __slots__ = ()
                        WotPlusPiggyBankCard = DynAccessor(44)

                    wot_plus_piggy_bank = _wot_plus_piggy_bank()

                piggy_bank_cards = _piggy_bank_cards()

            dashboard = _dashboard()

            class _tooltips(DynAccessor):
                __slots__ = ()
                SquadBonusTooltip = DynAccessor(408)

            tooltips = _tooltips()

        premacc = _premacc()

        class _progressive_reward(DynAccessor):
            __slots__ = ()

            class _progressive_reward_award(DynAccessor):
                __slots__ = ()
                ProgressiveRewardAward = DynAccessor(45)

            progressive_reward_award = _progressive_reward_award()

            class _progressive_reward_view(DynAccessor):
                __slots__ = ()
                ProgressiveRewardView = DynAccessor(46)

            progressive_reward_view = _progressive_reward_view()

        progressive_reward = _progressive_reward()

        class _ranked(DynAccessor):
            __slots__ = ()

            class _ranked_year_award(DynAccessor):
                __slots__ = ()
                RankedYearAward = DynAccessor(47)

            ranked_year_award = _ranked_year_award()
            EntryPoint = DynAccessor(417)
            QualificationRewardsView = DynAccessor(418)
            RankedSelectableRewardView = DynAccessor(419)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RankedBattlesRolesTooltipView = DynAccessor(420)

            tooltips = _tooltips()
            YearLeaderboardView = DynAccessor(421)

        ranked = _ranked()

        class _reward_window(DynAccessor):
            __slots__ = ()

            class _clan_reward_window_content(DynAccessor):
                __slots__ = ()
                ClanRewardWindowContent = DynAccessor(48)

            clan_reward_window_content = _clan_reward_window_content()

            class _piggy_bank_reward_window_content(DynAccessor):
                __slots__ = ()
                PiggyBankRewardWindowContent = DynAccessor(49)

            piggy_bank_reward_window_content = _piggy_bank_reward_window_content()

            class _reward_window_content(DynAccessor):
                __slots__ = ()
                RewardWindowContent = DynAccessor(50)

            reward_window_content = _reward_window_content()

            class _twitch_reward_window_content(DynAccessor):
                __slots__ = ()
                TwitchRewardWindowContent = DynAccessor(51)

            twitch_reward_window_content = _twitch_reward_window_content()

        reward_window = _reward_window()

        class _tooltips(DynAccessor):
            __slots__ = ()

            class _clans(DynAccessor):
                __slots__ = ()
                ClanShortInfoTooltipContent = DynAccessor(52)

            clans = _clans()

            class _loot_box_category_tooltip(DynAccessor):
                __slots__ = ()
                LootBoxCategoryTooltipContent = DynAccessor(53)

            loot_box_category_tooltip = _loot_box_category_tooltip()
            AdditionalRewardsTooltip = DynAccessor(471)
            BattleResultsStatsTooltipView = DynAccessor(472)
            TankmanTooltipView = DynAccessor(473)
            VehPostProgressionEntryPointTooltip = DynAccessor(474)

        tooltips = _tooltips()

        class _account_completion(DynAccessor):
            __slots__ = ()
            AddCredentialsView = DynAccessor(113)
            ConfirmCredentialsView = DynAccessor(114)
            CurtainView = DynAccessor(115)
            SteamEmailConfirmRewardsView = DynAccessor(116)

            class _tooltips(DynAccessor):
                __slots__ = ()
                HangarTooltip = DynAccessor(117)

            tooltips = _tooltips()

        account_completion = _account_completion()

        class _account_dashboard(DynAccessor):
            __slots__ = ()
            AccountDashboard = DynAccessor(118)
            DailyExperienceView = DynAccessor(119)

        account_dashboard = _account_dashboard()

        class _achievements(DynAccessor):
            __slots__ = ()
            AchievementsMainView = DynAccessor(120)
            CatalogView = DynAccessor(121)

            class _dialogs(DynAccessor):
                __slots__ = ()
                EditConfirm = DynAccessor(122)

            dialogs = _dialogs()
            EarningPopUpView = DynAccessor(123)
            EditView = DynAccessor(124)
            RewardView = DynAccessor(125)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AutoSettingTooltip = DynAccessor(126)
                BattlesKPITooltip = DynAccessor(127)
                EditingTooltip = DynAccessor(128)
                KPITooltip = DynAccessor(129)
                WOTPRMainTooltip = DynAccessor(130)
                WTRInfoTooltip = DynAccessor(131)
                WTRMainTooltip = DynAccessor(132)

            tooltips = _tooltips()

        achievements = _achievements()

        class _awards(DynAccessor):
            __slots__ = ()
            BadgeAwardView = DynAccessor(133)
            MultipleAwardsView = DynAccessor(134)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RewardCompensationTooltip = DynAccessor(135)
                VehicleForChooseTooltip = DynAccessor(136)

            tooltips = _tooltips()

        awards = _awards()

        class _battle_matters(DynAccessor):
            __slots__ = ()
            BattleMattersEntryPointView = DynAccessor(137)
            BattleMattersExchangeRewards = DynAccessor(138)
            BattleMattersMainRewardView = DynAccessor(139)
            BattleMattersMainView = DynAccessor(140)
            BattleMattersPausedView = DynAccessor(141)
            BattleMattersRewardsView = DynAccessor(142)
            BattleMattersVehicleSelectionView = DynAccessor(143)

            class _popovers(DynAccessor):
                __slots__ = ()
                BattleMattersFilterPopoverView = DynAccessor(144)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattleMattersEntryTooltipView = DynAccessor(145)
                BattleMattersTokenTooltipView = DynAccessor(146)

            tooltips = _tooltips()

        battle_matters = _battle_matters()

        class _battle_royale(DynAccessor):
            __slots__ = ()

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                CurrencyResolver = DynAccessor(205)
                PriceResolver = DynAccessor(206)

            sharedComponents = _sharedComponents()

        battle_royale = _battle_royale()

        class _clan_supply(DynAccessor):
            __slots__ = ()
            ClanSupply = DynAccessor(209)
            RewardsView = DynAccessor(210)

        clan_supply = _clan_supply()

        class _collection(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(211)
            CollectionItemPreview = DynAccessor(212)
            CollectionsMainView = DynAccessor(213)
            CollectionView = DynAccessor(214)
            IntroView = DynAccessor(215)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CollectionItemTooltipView = DynAccessor(216)

            tooltips = _tooltips()

        collection = _collection()

        class _craft_machine(DynAccessor):
            __slots__ = ()
            CraftmachineEntryPointView = DynAccessor(225)

        craft_machine = _craft_machine()

        class _crew(DynAccessor):
            __slots__ = ()
            BarracksView = DynAccessor(226)
            ConversionConfirmView = DynAccessor(227)
            CrewHeaderTooltipView = DynAccessor(228)
            CrewPostProgressionView = DynAccessor(229)

            class _dialogs(DynAccessor):
                __slots__ = ()
                CrewBooksPurchaseDialog = DynAccessor(230)
                DismissTankmanDialog = DynAccessor(231)
                DocumentChangeDialog = DynAccessor(232)
                EnlargeBarracksDialog = DynAccessor(233)
                FillAllPerksDialog = DynAccessor(234)
                MentorAssignmentDialog = DynAccessor(235)
                PerksResetDialog = DynAccessor(236)
                RecruitConfirmIrrelevantDialog = DynAccessor(237)
                RecruitDialog = DynAccessor(238)
                RecruitNewTankmanDialog = DynAccessor(239)
                RestoreTankmanDialog = DynAccessor(240)
                RetrainMassiveDialog = DynAccessor(241)
                RetrainPremiumVehicleDialog = DynAccessor(242)
                RetrainSingleDialog = DynAccessor(243)
                SkillsTrainingConfirmDialog = DynAccessor(244)
                SkinApplyDialog = DynAccessor(245)

            dialogs = _dialogs()
            HangarCrewWidget = DynAccessor(246)
            HelpView = DynAccessor(247)
            JunkTankmenView = DynAccessor(248)
            MemberChangeView = DynAccessor(249)
            MentorAssigmentView = DynAccessor(250)

            class _personal_case(DynAccessor):
                __slots__ = ()
                PersonalDataView = DynAccessor(251)
                PersonalFileView = DynAccessor(252)
                ServiceRecordView = DynAccessor(253)

            personal_case = _personal_case()

            class _popovers(DynAccessor):
                __slots__ = ()
                FilterPopoverView = DynAccessor(254)

            popovers = _popovers()
            QuickTrainingView = DynAccessor(255)
            SkillsTrainingView = DynAccessor(256)
            TankChangeView = DynAccessor(257)
            TankmanContainerView = DynAccessor(258)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AdvancedTooltipView = DynAccessor(259)
                BonusPerksTooltip = DynAccessor(260)
                BunksConfirmDiscountTooltip = DynAccessor(261)
                ConversionTooltip = DynAccessor(262)
                CrewBookMouseTooltip = DynAccessor(263)
                CrewPerksAdditionalTooltip = DynAccessor(264)
                CrewPerksTooltip = DynAccessor(265)
                DirectiveConversionTooltip = DynAccessor(266)
                DismissedToggleTooltip = DynAccessor(267)
                EmptySkillTooltip = DynAccessor(268)
                ExperienceStepperTooltip = DynAccessor(269)
                MentorAssignmentTooltip = DynAccessor(270)
                MentoringLicenseTooltip = DynAccessor(271)
                PostProgressionTooltip = DynAccessor(272)
                PremiumVehicleTooltip = DynAccessor(273)
                QualificationTooltip = DynAccessor(274)
                QuickTrainingDiscountTooltip = DynAccessor(275)
                QuickTrainingLostXpTooltip = DynAccessor(276)
                SkillsEfficiencyTooltip = DynAccessor(277)
                SkillUntrainedAdditionalTooltip = DynAccessor(278)
                SkillUntrainedTooltip = DynAccessor(279)
                SortingDropdownTooltip = DynAccessor(280)
                SpecializationWotPlusTooltip = DynAccessor(281)
                TankmanTooltip = DynAccessor(282)
                VehCmpSkillsTooltip = DynAccessor(283)
                VehicleParamsTooltipView = DynAccessor(284)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                CrewBannerWidget = DynAccessor(285)
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
            CustomizationRarityRewardScreen = DynAccessor(294)

            class _progression_styles(DynAccessor):
                __slots__ = ()
                OnboardingView = DynAccessor(295)
                StageSwitcher = DynAccessor(296)

            progression_styles = _progression_styles()

            class _progressive_items_reward(DynAccessor):
                __slots__ = ()
                ProgressiveItemsUpgradeView = DynAccessor(297)

            progressive_items_reward = _progressive_items_reward()

            class _progressive_items_view(DynAccessor):
                __slots__ = ()
                ProgressiveItemsView = DynAccessor(298)

            progressive_items_view = _progressive_items_view()

            class _style_unlocked_view(DynAccessor):
                __slots__ = ()
                StyleUnlockedView = DynAccessor(299)

            style_unlocked_view = _style_unlocked_view()

            class _vehicles_sidebar(DynAccessor):
                __slots__ = ()
                VehiclesSidebar = DynAccessor(300)

            vehicles_sidebar = _vehicles_sidebar()

        customization = _customization()

        class _dedication(DynAccessor):
            __slots__ = ()
            DedicationRewardView = DynAccessor(301)

        dedication = _dedication()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            AnimatedDogTagGradeTooltip = DynAccessor(302)
            AnimatedDogTagsView = DynAccessor(303)
            CatalogAnimatedDogTagTooltip = DynAccessor(304)
            CustomizationConfirmDialog = DynAccessor(305)
            DedicationTooltip = DynAccessor(306)
            DogTagsView = DynAccessor(307)
            RankedEfficiencyTooltip = DynAccessor(308)
            ThreeMonthsTooltip = DynAccessor(309)
            TriumphTooltip = DynAccessor(310)

        dog_tags = _dog_tags()

        class _excluded_maps(DynAccessor):
            __slots__ = ()
            ExcludedMapsTooltip = DynAccessor(311)
            ExcludedMapsView = DynAccessor(312)

        excluded_maps = _excluded_maps()

        class _frontline(DynAccessor):
            __slots__ = ()

            class _dialogs(DynAccessor):
                __slots__ = ()
                BlankPrice = DynAccessor(313)

            dialogs = _dialogs()
            IntroScreen = DynAccessor(314)
            RewardsSelectionView = DynAccessor(315)

        frontline = _frontline()

        class _hangar(DynAccessor):
            __slots__ = ()
            BuyVehicleView = DynAccessor(316)

            class _notifications(DynAccessor):
                __slots__ = ()
                PunishmentView = DynAccessor(317)

            notifications = _notifications()

            class _subViews(DynAccessor):
                __slots__ = ()
                VehicleParams = DynAccessor(318)

            subViews = _subViews()
            VehicleParamsWidget = DynAccessor(319)

        hangar = _hangar()

        class _instructions(DynAccessor):
            __slots__ = ()
            BuyWindow = DynAccessor(320)
            SellWindow = DynAccessor(321)

        instructions = _instructions()

        class _live_ops_web_events(DynAccessor):
            __slots__ = ()
            EntryPoint = DynAccessor(322)
            EntryPointTooltip = DynAccessor(323)

        live_ops_web_events = _live_ops_web_events()

        class _lootbox_system(DynAccessor):
            __slots__ = ()
            AutoOpenView = DynAccessor(324)

            class _baseComponents(DynAccessor):
                __slots__ = ()
                AnimationCheckbox = DynAccessor(325)
                AutoCleanVideo = DynAccessor(326)
                BigButton = DynAccessor(327)

                class _common(DynAccessor):
                    __slots__ = ()
                    AlertIcon = DynAccessor(328)
                    Icon = DynAccessor(329)

                common = _common()
                Loader = DynAccessor(330)
                LoupeButton = DynAccessor(331)
                PurchaseButton = DynAccessor(332)
                ScrollWithLips = DynAccessor(333)
                SubTitle = DynAccessor(334)
                TankName = DynAccessor(335)
                Title = DynAccessor(336)
                VehicleInfo = DynAccessor(337)

            baseComponents = _baseComponents()
            EntryPointView = DynAccessor(338)
            InfoPage = DynAccessor(339)
            MainView = DynAccessor(340)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BoxCompensationTooltip = DynAccessor(341)
                BoxTooltip = DynAccessor(342)
                EntryPointTooltip = DynAccessor(343)
                GuaranteedRewardInfoTooltip = DynAccessor(344)
                RandomNationalBonusTooltipView = DynAccessor(345)
                StatisticsCategoryTooltipView = DynAccessor(346)

            tooltips = _tooltips()

        lootbox_system = _lootbox_system()

        class _mapbox(DynAccessor):
            __slots__ = ()
            MapBoxAwardsView = DynAccessor(347)
            MapBoxEntryPointView = DynAccessor(348)
            MapBoxIntro = DynAccessor(349)
            MapBoxProgression = DynAccessor(350)
            MapBoxSurveyView = DynAccessor(351)

        mapbox = _mapbox()

        class _maps_training(DynAccessor):
            __slots__ = ()
            MapsTrainingPage = DynAccessor(352)
            MapsTrainingQueue = DynAccessor(353)
            MapsTrainingResult = DynAccessor(354)
            ScenarioTooltip = DynAccessor(355)

        maps_training = _maps_training()

        class _matchmaker(DynAccessor):
            __slots__ = ()
            ActiveTestConfirmView = DynAccessor(359)

        matchmaker = _matchmaker()

        class _mode_selector(DynAccessor):
            __slots__ = ()
            BattleSessionView = DynAccessor(368)
            ModeSelectorView = DynAccessor(369)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AlertTooltip = DynAccessor(370)

                class _common(DynAccessor):
                    __slots__ = ()
                    Divider = DynAccessor(371)
                    GradientDecorator = DynAccessor(372)

                common = _common()
                SimplyFormatTooltip = DynAccessor(373)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                BattleRoyaleProgressionWidget = DynAccessor(374)
                BattleRoyaleWidget = DynAccessor(375)
                EpicWidget = DynAccessor(376)
                RankedWidget = DynAccessor(377)

            widgets = _widgets()

        mode_selector = _mode_selector()

        class _new_year(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                FormatTextWithColorTags = DynAccessor(378)

            common = _common()

        new_year = _new_year()

        class _offers(DynAccessor):
            __slots__ = ()
            OfferBannerWindow = DynAccessor(379)
            OfferGiftsWindow = DynAccessor(380)
            OfferRewardWindow = DynAccessor(381)

        offers = _offers()

        class _personal_exchange_rates(DynAccessor):
            __slots__ = ()
            AllPersonalExchangesView = DynAccessor(382)
            ExperienceExchangeView = DynAccessor(383)
            GoldExchangeView = DynAccessor(384)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExchangeLimitTooltip = DynAccessor(385)
                ExchangeRateTooltip = DynAccessor(386)

            tooltips = _tooltips()

        personal_exchange_rates = _personal_exchange_rates()

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            BoosterTooltip = DynAccessor(387)
            PersonalReservesTooltip = DynAccessor(388)
            PersonalReservesWidget = DynAccessor(389)
            QuestBoosterTooltip = DynAccessor(390)
            ReserveCard = DynAccessor(391)
            ReserveCardTooltip = DynAccessor(392)
            ReserveGroup = DynAccessor(393)
            ReservesActivationView = DynAccessor(394)
            ReservesIntroView = DynAccessor(395)

        personal_reserves = _personal_reserves()

        class _platoon(DynAccessor):
            __slots__ = ()
            AlertTooltip = DynAccessor(396)
            MembersWindow = DynAccessor(397)
            PlatoonDropdown = DynAccessor(398)
            SearchingDropdown = DynAccessor(399)
            SettingsPopover = DynAccessor(400)

            class _subViews(DynAccessor):
                __slots__ = ()
                Chat = DynAccessor(401)
                SettingsContent = DynAccessor(402)
                TiersLimit = DynAccessor(403)

            subViews = _subViews()
            WTRTooltip = DynAccessor(404)

        platoon = _platoon()

        class _player_subscriptions(DynAccessor):
            __slots__ = ()
            PlayerSubscriptions = DynAccessor(405)
            SubscriptionItem = DynAccessor(406)
            SubscriptionRewardView = DynAccessor(407)

        player_subscriptions = _player_subscriptions()

        class _prestige(DynAccessor):
            __slots__ = ()

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                PrestigeProgressSymbol = DynAccessor(409)
                PrestigeProgressTab = DynAccessor(410)

            sharedComponents = _sharedComponents()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EliteLevelGradesTooltip = DynAccessor(411)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                GlobalOnboardingView = DynAccessor(412)
                PrestigeHangarEntryPoint = DynAccessor(413)
                PrestigeProfileTechniqueEmblemView = DynAccessor(414)
                PrestigeProfileTechniqueView = DynAccessor(415)
                PrestigeRewardView = DynAccessor(416)

            views = _views()

        prestige = _prestige()

        class _research(DynAccessor):
            __slots__ = ()
            BuyModuleDialogView = DynAccessor(422)
            InsufficientCreditsTooltip = DynAccessor(423)
            SoldModuleInfoTooltip = DynAccessor(424)

        research = _research()

        class _subscription(DynAccessor):
            __slots__ = ()
            SubscriptionAwardView = DynAccessor(425)
            WotPlusTooltip = DynAccessor(426)

        subscription = _subscription()

        class _tanksetup(DynAccessor):
            __slots__ = ()
            AmmunitionPanel = DynAccessor(427)

            class _common(DynAccessor):
                __slots__ = ()
                Action = DynAccessor(428)
                CtaButtons = DynAccessor(429)
                DealPanel = DynAccessor(430)
                DemountKit = DynAccessor(431)
                ExtraImage = DynAccessor(432)
                FormatColorTagText = DynAccessor(433)
                Location = DynAccessor(434)
                MaybeWrapper = DynAccessor(435)
                Price = DynAccessor(436)
                SetupApp = DynAccessor(437)
                ShortenedText = DynAccessor(438)
                Slider = DynAccessor(439)

                class _SlotParts(DynAccessor):
                    __slots__ = ()
                    Bonus = DynAccessor(440)
                    Container = DynAccessor(441)
                    Count = DynAccessor(442)
                    Inside = DynAccessor(443)
                    Level = DynAccessor(444)

                SlotParts = _SlotParts()
                Specializations = DynAccessor(445)
                SwitchButton = DynAccessor(446)
                SwitchEquipment = DynAccessor(447)

                class _Transitions(DynAccessor):
                    __slots__ = ()
                    SlotTransitions = DynAccessor(448)

                Transitions = _Transitions()
                WeaponOccupancy = DynAccessor(449)

            common = _common()
            DeconstructionDeviceView = DynAccessor(450)

            class _dialogs(DynAccessor):
                __slots__ = ()
                Confirm = DynAccessor(451)
                ConfirmActionsWithEquipmentDialog = DynAccessor(452)
                DeconstructConfirm = DynAccessor(453)
                DeviceUpgradeDialog = DynAccessor(454)
                ExchangeToApplyEasyTankEquip = DynAccessor(455)
                ExchangeToBuyItems = DynAccessor(456)
                ExchangeToUpgradeItems = DynAccessor(457)
                NeedRepair = DynAccessor(458)
                RefillShells = DynAccessor(459)
                Sell = DynAccessor(460)

            dialogs = _dialogs()
            EasyTankEquipView = DynAccessor(461)
            HangarAmmunitionSetup = DynAccessor(462)
            IntroScreen = DynAccessor(463)

            class _tooltips(DynAccessor):
                __slots__ = ()
                DeconstructFromInventoryTooltip = DynAccessor(464)
                DeconstructFromVehicleTooltip = DynAccessor(465)
                PopularLoadoutsTooltip = DynAccessor(466)
                SetupTabTooltipView = DynAccessor(467)
                WarningTooltipView = DynAccessor(468)

            tooltips = _tooltips()
            VehicleCompareAmmunitionPanel = DynAccessor(469)
            VehicleCompareAmmunitionSetup = DynAccessor(470)

        tanksetup = _tanksetup()

        class _vehicle_compare(DynAccessor):
            __slots__ = ()
            CompareModificationsPanelView = DynAccessor(475)
            CompareSkillsPanelView = DynAccessor(476)
            SelectSlotSpecCompareDialog = DynAccessor(477)
            SkillSelectView = DynAccessor(478)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CrewRolesTooltip = DynAccessor(479)

            tooltips = _tooltips()

        vehicle_compare = _vehicle_compare()

        class _vehicle_preview(DynAccessor):
            __slots__ = ()

            class _buying_panel(DynAccessor):
                __slots__ = ()
                StyleBuyingPanel = DynAccessor(480)
                VPProgressionStylesBuyingPanel = DynAccessor(481)

            buying_panel = _buying_panel()

            class _tabs(DynAccessor):
                __slots__ = ()
                CrewTabView = DynAccessor(482)

            tabs = _tabs()

            class _top_panel(DynAccessor):
                __slots__ = ()
                TopPanelTabs = DynAccessor(483)

            top_panel = _top_panel()

        vehicle_preview = _vehicle_preview()

        class _veh_post_progression(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                Bonus = DynAccessor(484)
                Description = DynAccessor(485)
                Grid = DynAccessor(486)
                PersistentBonuses = DynAccessor(487)
                Slide = DynAccessor(488)
                SlideContent = DynAccessor(489)
                Slider = DynAccessor(490)
                TextSplit = DynAccessor(491)

            common = _common()
            PostProgressionInfo = DynAccessor(492)
            PostProgressionIntro = DynAccessor(493)
            PostProgressionResearchSteps = DynAccessor(494)

            class _tooltip(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()
                    DisabledBlock = DynAccessor(495)
                    FeatureLevelSubtitle = DynAccessor(496)
                    Lock = DynAccessor(497)
                    NotEnoughCredits = DynAccessor(498)
                    PriceBlock = DynAccessor(499)
                    Separator = DynAccessor(500)

                common = _common()
                PairModificationTooltipView = DynAccessor(501)
                PostProgressionLevelTooltipView = DynAccessor(502)
                RoleSlotTooltipView = DynAccessor(503)
                SetupTooltipView = DynAccessor(504)

            tooltip = _tooltip()
            VehiclePostProgressionCmpView = DynAccessor(505)
            VehiclePostProgressionView = DynAccessor(506)

        veh_post_progression = _veh_post_progression()

        class _winback(DynAccessor):
            __slots__ = ()

            class _popovers(DynAccessor):
                __slots__ = ()
                WinbackLeaveModePopoverView = DynAccessor(507)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                MainRewardTooltip = DynAccessor(508)
                ModeInfoTooltip = DynAccessor(509)
                SelectableRewardTooltip = DynAccessor(510)
                SelectedRewardsTooltip = DynAccessor(511)

            tooltips = _tooltips()
            WinbackDailyQuestsIntroView = DynAccessor(512)
            WinbackLeaveModeDialogView = DynAccessor(513)
            WinbackRewardView = DynAccessor(514)
            WinbackSelectableRewardView = DynAccessor(515)

        winback = _winback()

    lobby = _lobby()

    class _test_check_box_view(DynAccessor):
        __slots__ = ()
        TestCheckBoxView = DynAccessor(54)

    test_check_box_view = _test_check_box_view()

    class _test_text_button_view(DynAccessor):
        __slots__ = ()
        TestTextButtonView = DynAccessor(55)

    test_text_button_view = _test_text_button_view()

    class _windows_layout_view(DynAccessor):
        __slots__ = ()
        WindowsLayountView = DynAccessor(56)

    windows_layout_view = _windows_layout_view()

    class _blend_mode(DynAccessor):
        __slots__ = ()

        class _blend_mode(DynAccessor):
            __slots__ = ()
            BlendMode = DynAccessor(57)

        blend_mode = _blend_mode()

    blend_mode = _blend_mode()

    class _demo_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _demo_window_content(DynAccessor):
                __slots__ = ()
                DemoWindowContent = DynAccessor(58)
                ImageProps = DynAccessor(59)

            demo_window_content = _demo_window_content()

            class _demo_window_details_panel(DynAccessor):
                __slots__ = ()
                DemoWindowDetailsPanel = DynAccessor(60)

            demo_window_details_panel = _demo_window_details_panel()

            class _demo_window_image_panel(DynAccessor):
                __slots__ = ()
                DemoWindowImagePanel = DynAccessor(61)

            demo_window_image_panel = _demo_window_image_panel()

            class _image_preview_window_content(DynAccessor):
                __slots__ = ()
                ImagePreviewWindowContent = DynAccessor(62)

            image_preview_window_content = _image_preview_window_content()

        views = _views()

    demo_view = _demo_view()

    class _examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_dialogs_view(DynAccessor):
                __slots__ = ()
                TestDialogsView = DynAccessor(63)

            test_dialogs_view = _test_dialogs_view()

            class _test_expr_functions_view(DynAccessor):
                __slots__ = ()
                TestExprFunctionsView = DynAccessor(64)

            test_expr_functions_view = _test_expr_functions_view()

            class _test_sub_view(DynAccessor):
                __slots__ = ()
                TestSubView = DynAccessor(65)

            test_sub_view = _test_sub_view()

            class _test_view(DynAccessor):
                __slots__ = ()
                TestView = DynAccessor(66)

            test_view = _test_view()

            class _unbound_example(DynAccessor):
                __slots__ = ()
                UnboundExample = DynAccessor(67)

            unbound_example = _unbound_example()

        views = _views()

    examples = _examples()

    class _list_examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _list_examples_empty_render_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesEmptyRenderWindowContent = DynAccessor(68)

            list_examples_empty_render_window_content = _list_examples_empty_render_window_content()

            class _list_examples_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesWindowContent = DynAccessor(69)

            list_examples_window_content = _list_examples_window_content()

        views = _views()

    list_examples = _list_examples()

    class _rotation_pivot_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_pivot_view(DynAccessor):
                __slots__ = ()
                RotationAndPivotTestView = DynAccessor(70)

            rotation_pivot_view = _rotation_pivot_view()

        views = _views()

    rotation_pivot_view = _rotation_pivot_view()

    class _rotation_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_view(DynAccessor):
                __slots__ = ()
                RotationTestView = DynAccessor(71)

            rotation_view = _rotation_view()

        views = _views()

    rotation_view = _rotation_view()

    class _scale_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _scale_view(DynAccessor):
                __slots__ = ()
                ScaleTestView = DynAccessor(72)

            scale_view = _scale_view()

        views = _views()

    scale_view = _scale_view()

    class _test_uikit_buttons_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_buttons_view(DynAccessor):
                __slots__ = ()
                TestUikitButtonsView = DynAccessor(73)

            test_uikit_buttons_view = _test_uikit_buttons_view()

        views = _views()

    test_uikit_buttons_view = _test_uikit_buttons_view()

    class _test_uikit_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_view(DynAccessor):
                __slots__ = ()
                TestUikitView = DynAccessor(74)

            test_uikit_view = _test_uikit_view()

        views = _views()

    test_uikit_view = _test_uikit_view()

    class _wtypes_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _wtypes_demo_window_content(DynAccessor):
                __slots__ = ()
                WtypesDemoWindowContent = DynAccessor(75)

            wtypes_demo_window_content = _wtypes_demo_window_content()

        views = _views()

    wtypes_view = _wtypes_view()

    class _dialogs(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            DialogTemplateGenericTooltip = DynAccessor(93)

        common = _common()
        DefaultDialog = DynAccessor(94)

        class _sub_views(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                SimpleText = DynAccessor(95)
                SinglePrice = DynAccessor(96)

            common = _common()

            class _content(DynAccessor):
                __slots__ = ()
                SelectOptionContent = DynAccessor(97)
                SimpleTextContent = DynAccessor(98)
                SinglePriceContent = DynAccessor(99)
                TextWithWarning = DynAccessor(100)

            content = _content()

            class _footer(DynAccessor):
                __slots__ = ()
                BRSinglePriceFooter = DynAccessor(101)
                SimpleTextFooter = DynAccessor(102)
                SinglePriceFooter = DynAccessor(103)

            footer = _footer()

            class _icon(DynAccessor):
                __slots__ = ()
                MultipleIconsSet = DynAccessor(104)

            icon = _icon()

            class _title(DynAccessor):
                __slots__ = ()
                SimpleTextTitle = DynAccessor(105)

            title = _title()

            class _topRight(DynAccessor):
                __slots__ = ()
                BRMoneyBalance = DynAccessor(106)
                MoneyBalance = DynAccessor(107)

            topRight = _topRight()

        sub_views = _sub_views()

        class _widgets(DynAccessor):
            __slots__ = ()
            IconSet = DynAccessor(108)
            MoneyBalance = DynAccessor(109)
            SinglePrice = DynAccessor(110)
            WarningText = DynAccessor(111)

        widgets = _widgets()

    dialogs = _dialogs()

    class _loading(DynAccessor):
        __slots__ = ()
        GameLoadingView = DynAccessor(112)

    loading = _loading()

    class _mono(DynAccessor):
        __slots__ = ()

        class _dialogs(DynAccessor):
            __slots__ = ()
            research_confirm_dialog = DynAccessor(516)

        dialogs = _dialogs()

        class _hangar(DynAccessor):
            __slots__ = ()
            footer = DynAccessor(517)
            header = DynAccessor(518)
            main = DynAccessor(519)

            class _overlays(DynAccessor):
                __slots__ = ()
                playlist = DynAccessor(520)

            overlays = _overlays()
            tooltips = DynAccessor(521)
            vehicle_tooltip = DynAccessor(522)

        hangar = _hangar()

        class _holiday_ops(DynAccessor):
            __slots__ = ()
            atmosphere_level_up = DynAccessor(523)
            celebrity_animation_view = DynAccessor(524)
            challenge_stories_view = DynAccessor(525)

            class _dialogs(DynAccessor):
                __slots__ = ()

                class _challenge(DynAccessor):
                    __slots__ = ()
                    bundle_purchase_dialog = DynAccessor(526)
                    buy_celebrity_quest_item_dialog = DynAccessor(527)
                    discount_dialog = DynAccessor(528)

                challenge = _challenge()

                class _converter(DynAccessor):
                    __slots__ = ()
                    resources_convert_dialog = DynAccessor(529)

                converter = _converter()

                class _gift_machine(DynAccessor):
                    __slots__ = ()
                    gift_machine_coin_purchase_dialog = DynAccessor(530)

                gift_machine = _gift_machine()

                class _hangar_name(DynAccessor):
                    __slots__ = ()
                    name_change_dialog = DynAccessor(531)

                hangar_name = _hangar_name()

                class _marketplace(DynAccessor):
                    __slots__ = ()
                    market_purchase_dialog = DynAccessor(532)

                marketplace = _marketplace()

            dialogs = _dialogs()
            gift_machine_display = DynAccessor(533)
            hangar_name = DynAccessor(534)
            ho_gift_machine_loot_list = DynAccessor(535)
            info_view = DynAccessor(536)
            main = DynAccessor(537)

            class _notifications(DynAccessor):
                __slots__ = ()
                ho_assignments_rewards = DynAccessor(538)
                ho_attached3drewards = DynAccessor(539)
                ho_challenge_rewards = DynAccessor(540)
                ho_dog_mission_completed = DynAccessor(541)
                ho_dog_reminder = DynAccessor(542)
                ho_new_reward_kit = DynAccessor(543)
                ho_piggy_bank_multiple_rewards = DynAccessor(544)
                ho_piggy_bank_single_reward = DynAccessor(545)
                ho_receiving_awards = DynAccessor(546)
                ho_resources_reminder = DynAccessor(547)
                ho_sack_rare_loot = DynAccessor(548)

            notifications = _notifications()
            pet_purchase_overlay = DynAccessor(549)
            pet_reward_view = DynAccessor(550)

            class _popovers(DynAccessor):
                __slots__ = ()
                ho_economic_bonus_popover = DynAccessor(551)
                ho_resources_convert_popover = DynAccessor(552)

            popovers = _popovers()
            surprise_gift_view = DynAccessor(553)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ho_challenge_token_tooltip = DynAccessor(554)
                ho_customization_object_tooltip = DynAccessor(555)
                ho_decoration_tooltip = DynAccessor(556)
                ho_decoration_unavailable_tooltip = DynAccessor(557)
                ho_discount_reward_tooltip = DynAccessor(558)
                ho_dog_decoration_tooltip = DynAccessor(559)
                ho_economic_bonus_simple_tooltip = DynAccessor(560)
                ho_economic_bonus_tooltip = DynAccessor(561)
                ho_friends_tooltips = DynAccessor(562)
                ho_gift_machine_token_tooltip = DynAccessor(563)
                ho_guest_tooltip = DynAccessor(564)
                ho_main_widget_tooltip = DynAccessor(565)
                ho_marketplace_token_tooltip = DynAccessor(566)
                ho_market_card_tooltip = DynAccessor(567)
                ho_market_discount_tooltip = DynAccessor(568)
                ho_market_lack_the_res_tooltip = DynAccessor(569)
                ho_menu_gift_tooltip = DynAccessor(570)
                ho_random_resource_tooltip = DynAccessor(571)
                ho_resource_box_tooltip = DynAccessor(572)
                ho_resource_collector_tooltip = DynAccessor(573)
                ho_resource_converter_info_tooltip = DynAccessor(574)
                ho_resource_list_tooltip = DynAccessor(575)
                ho_resource_shop_tooltip = DynAccessor(576)
                ho_resource_tooltip = DynAccessor(577)
                ho_reward_kit_restriction_tooltip = DynAccessor(578)
                ho_sacks_tooltip = DynAccessor(579)
                ho_sack_random_reward_tooltip = DynAccessor(580)
                ho_slot_locked_tooltip = DynAccessor(581)
                ho_surprise_banner_tooltip = DynAccessor(582)
                ho_widget_bonus_tooltip = DynAccessor(583)

            tooltips = _tooltips()

        holiday_ops = _holiday_ops()

        class _holiday_ops_marker(DynAccessor):
            __slots__ = ()
            ho_customization_object_marker = DynAccessor(584)
            ho_dog_marker = DynAccessor(585)
            ho_headquarters_marker = DynAccessor(586)
            ho_resource_marker = DynAccessor(587)
            ho_terminal_marker = DynAccessor(588)
            ho_total_resource_marker = DynAccessor(589)

        holiday_ops_marker = _holiday_ops_marker()

        class _lobby(DynAccessor):
            __slots__ = ()
            elite_window = DynAccessor(590)

            class _veh_skill_tree(DynAccessor):
                __slots__ = ()
                comparison = DynAccessor(591)

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    alternate_configuration = DynAccessor(592)

                dialogs = _dialogs()
                intro_page = DynAccessor(593)

                class _notifications(DynAccessor):
                    __slots__ = ()
                    perk_available = DynAccessor(594)

                notifications = _notifications()
                rarity_reward_screen = DynAccessor(595)
                reward_screen = DynAccessor(596)

            veh_skill_tree = _veh_skill_tree()

        lobby = _lobby()

        class _lootbox(DynAccessor):
            __slots__ = ()
            auto_open = DynAccessor(597)
            info_page = DynAccessor(598)
            main = DynAccessor(599)

            class _tooltips(DynAccessor):
                __slots__ = ()
                box_compensation = DynAccessor(600)
                box_tooltip = DynAccessor(601)
                entry_point = DynAccessor(602)
                guaranteed_reward_info = DynAccessor(603)
                random_national_bonus = DynAccessor(604)
                statistics_category = DynAccessor(605)

            tooltips = _tooltips()

        lootbox = _lootbox()

        class _personal_missions_30(DynAccessor):
            __slots__ = ()
            assembling_video = DynAccessor(606)
            campaign_selector = DynAccessor(607)
            intro_screen = DynAccessor(608)
            main = DynAccessor(609)
            rewards = DynAccessor(610)

            class _tooltips(DynAccessor):
                __slots__ = ()
                missions_category_tooltip = DynAccessor(611)
                mission_progress_tooltip = DynAccessor(612)
                param_tooltip = DynAccessor(613)

            tooltips = _tooltips()

        personal_missions_30 = _personal_missions_30()

        class _pet_system(DynAccessor):
            __slots__ = ()
            event_view = DynAccessor(614)
            fullscreen_event_view = DynAccessor(615)
            info_page = DynAccessor(616)
            pet_house_marker = DynAccessor(617)
            pet_storage = DynAccessor(618)

            class _tooltips(DynAccessor):
                __slots__ = ()
                pet_storage_tooltip = DynAccessor(619)
                pet_tooltip = DynAccessor(620)
                synergy_tooltip = DynAccessor(621)

            tooltips = _tooltips()

        pet_system = _pet_system()

        class _post_battle(DynAccessor):
            __slots__ = ()
            flag = DynAccessor(622)
            random = DynAccessor(623)

            class _tooltips(DynAccessor):
                __slots__ = ()
                critical_damage = DynAccessor(624)

            tooltips = _tooltips()

        post_battle = _post_battle()

        class _seniority_awards(DynAccessor):
            __slots__ = ()

            class _notifications(DynAccessor):
                __slots__ = ()
                manual_claim = DynAccessor(625)
                tokens = DynAccessor(626)
                vehicles = DynAccessor(627)

            notifications = _notifications()
            rewards = DynAccessor(628)

            class _tooltips(DynAccessor):
                __slots__ = ()
                seniority_tooltip = DynAccessor(629)

            tooltips = _tooltips()
            vehicle_rewards = DynAccessor(630)

        seniority_awards = _seniority_awards()

        class _stronghold_event(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                event_banner_tooltip = DynAccessor(631)

            tooltips = _tooltips()

        stronghold_event = _stronghold_event()

        class _tech_tree(DynAccessor):
            __slots__ = ()
            main = DynAccessor(632)

        tech_tree = _tech_tree()

        class _template(DynAccessor):
            __slots__ = ()
            main = DynAccessor(633)

        template = _template()

        class _tooltips(DynAccessor):
            __slots__ = ()
            tooltips = DynAccessor(634)

        tooltips = _tooltips()

        class _user_missions(DynAccessor):
            __slots__ = ()
            ho_resources_intro_view = DynAccessor(635)

            class _hub(DynAccessor):
                __slots__ = ()
                mission_hub_intro_view = DynAccessor(637)

            hub = _hub(636)
            info_page = DynAccessor(638)

            class _tooltips(DynAccessor):
                __slots__ = ()
                all_quests_done_tooltip = DynAccessor(639)
                daily_quest_tooltip = DynAccessor(640)
                daily_reroll_tooltip = DynAccessor(641)
                param_tooltip = DynAccessor(642)
                pm3_banner_tooltip = DynAccessor(643)
                weekly_quest_tooltip = DynAccessor(644)

            tooltips = _tooltips()

        user_missions = _user_missions()

        class _vehicle_hub(DynAccessor):
            __slots__ = ()
            main = DynAccessor(645)

            class _tooltips(DynAccessor):
                __slots__ = ()
                armor_tooltip = DynAccessor(646)
                back_to_main_progression_tooltip = DynAccessor(647)
                perk_tooltip = DynAccessor(648)
                prestige_reward_tooltip = DynAccessor(649)
                vanity_entry_point_tooltip = DynAccessor(650)

            tooltips = _tooltips()

        vehicle_hub = _vehicle_hub()

        class _demos(DynAccessor):
            __slots__ = ()
            data_layer = DynAccessor(846)

            class _entry(DynAccessor):
                __slots__ = ()

                class _pages(DynAccessor):
                    __slots__ = ()

                    class _tech_ui(DynAccessor):
                        __slots__ = ()

                        class _pages(DynAccessor):
                            __slots__ = ()

                            class _param_tooltip(DynAccessor):
                                __slots__ = ()
                                tooltips = DynAccessor(848)

                            param_tooltip = _param_tooltip()

                        pages = _pages()

                    tech_ui = _tech_ui()

                pages = _pages()

            entry = _entry(847)

            class _notifications(DynAccessor):
                __slots__ = ()
                test_notification = DynAccessor(849)

            notifications = _notifications()

        demos = _demos()

    mono = _mono()

    class _advent_calendar(DynAccessor):
        __slots__ = ()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                intro_screen_view = DynAccessor(651)
                main_view = DynAccessor(652)

                class _markers(DynAccessor):
                    __slots__ = ()
                    entry_point_marker = DynAccessor(653)

                markers = _markers()
                notification_view = DynAccessor(654)
                purchase_dialog_view = DynAccessor(655)
                reward_view = DynAccessor(656)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    advent_calendar_all_rewards_tooltip = DynAccessor(657)
                    advent_calendar_big_loot_box_tooltip = DynAccessor(658)
                    advent_calendar_simple_tooltip = DynAccessor(659)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    advent_calendar = _advent_calendar()

    class _battle_modifiers(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                ModifiersDomainTooltipView = DynAccessor(660)

            tooltips = _tooltips()

        lobby = _lobby()

    battle_modifiers = _battle_modifiers()

    class _battle_royale(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _views(DynAccessor):
                __slots__ = ()
                LeaveBattleView = DynAccessor(661)

            views = _views()

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()

                    class _LeaderBoard(DynAccessor):
                        __slots__ = ()
                        Column = DynAccessor(662)
                        Table = DynAccessor(663)

                    LeaderBoard = _LeaderBoard()

                common = _common()
                LeaderboardRewardTooltipView = DynAccessor(664)
                RewardCurrencyTooltipView = DynAccessor(665)
                VehicleTooltipView = DynAccessor(666)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                BattleResultView = DynAccessor(667)
                PreBattleView = DynAccessor(668)

            views = _views()

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                hangar = DynAccessor(669)
                info_page = DynAccessor(670)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ability = DynAccessor(671)
                    all_quests_done_tooltip = DynAccessor(672)
                    banner = DynAccessor(673)
                    battle_selector = DynAccessor(674)
                    ceasefire = DynAccessor(675)
                    commander = DynAccessor(676)
                    progression_quest = DynAccessor(677)
                    progression_widget = DynAccessor(678)
                    respawn = DynAccessor(679)
                    shop_button = DynAccessor(680)
                    upgrades_button = DynAccessor(681)
                    vehicle = DynAccessor(682)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    battle_royale = _battle_royale()

    class _battle_royale_progression(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(683)

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                battle_quest_awards_view = DynAccessor(684)

            lobby = _lobby()

        mono = _mono()
        ProgressionMainView = DynAccessor(685)

    battle_royale_progression = _battle_royale_progression()

    class _comp7(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            Comp7BattleCard = DynAccessor(686)
            MembersWindow = DynAccessor(687)
            PlatoonDropdown = DynAccessor(688)
            RewardsSelectionScreen = DynAccessor(689)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    purchase_dialog = DynAccessor(690)

                dialogs = _dialogs()
                hangar = DynAccessor(691)
                intro_screen = DynAccessor(692)
                meta_root_view = DynAccessor(693)
                no_vehicles_screen = DynAccessor(694)
                rewards_screen = DynAccessor(695)
                season_statistics = DynAccessor(696)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    crew_members_tooltip = DynAccessor(697)
                    division_tooltip = DynAccessor(698)
                    entry_point_tooltip = DynAccessor(699)
                    fifth_rank_tooltip = DynAccessor(700)
                    general_rank_tooltip = DynAccessor(701)
                    last_update_tooltip = DynAccessor(702)
                    progression_tooltip = DynAccessor(703)
                    rank_compatibility_tooltip = DynAccessor(704)
                    rank_inactivity_tooltip = DynAccessor(705)
                    season_point_tooltip = DynAccessor(706)
                    sixth_rank_tooltip = DynAccessor(707)
                    style3d_tooltip = DynAccessor(708)
                    tournament_entry_point_tooltip = DynAccessor(709)
                    weekly_quest_widget_tooltip = DynAccessor(710)

                tooltips = _tooltips()
                wci = DynAccessor(711)
                whats_new_view = DynAccessor(712)

            lobby = _lobby()

        mono = _mono()

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            Comp7LightBattleCard = DynAccessor(713)
            MembersWindow = DynAccessor(714)
            PlatoonDropdown = DynAccessor(715)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                battle_quest_awards_view = DynAccessor(716)
                entry_point_tooltip = DynAccessor(717)
                hangar = DynAccessor(718)
                intro_screen = DynAccessor(719)
                leaderboard_reward_tooltip_view = DynAccessor(720)
                no_vehicles_screen = DynAccessor(721)
                progression_main_view = DynAccessor(722)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    all_quests_done_tooltip = DynAccessor(723)
                    battle_quest_tooltip = DynAccessor(724)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    comp7_light = _comp7_light()

    class _frontline(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            WelcomeView = DynAccessor(725)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    battle_abilities_confirm_dialog = DynAccessor(726)

                dialogs = _dialogs()
                hangar = DynAccessor(727)
                info_view = DynAccessor(728)
                post_battle_rewards_view = DynAccessor(729)
                progression_screen = DynAccessor(730)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    banner_tooltip = DynAccessor(731)
                    battle_ability_alt_tooltip = DynAccessor(732)
                    battle_ability_tooltip = DynAccessor(733)
                    level_reserves_tooltip = DynAccessor(734)
                    skill_order_tooltip = DynAccessor(735)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    frontline = _frontline()

    class _fun_random(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                FunRandomModeSubSelector = DynAccessor(736)

            feature = _feature()

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                battle_results = DynAccessor(737)
                hangar = DynAccessor(738)
                progression = DynAccessor(739)
                rewards = DynAccessor(740)
                tier_list = DynAccessor(741)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    battle_results_economic_tooltip = DynAccessor(742)
                    entry_point_tooltip = DynAccessor(743)
                    loot_box_tooltip = DynAccessor(744)
                    progression_tooltip = DynAccessor(745)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    fun_random = _fun_random()

    class _grinch(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            GrinchHelpView = DynAccessor(746)
            GrinchHudView = DynAccessor(747)

        battle = _battle()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _banner_entry_point(DynAccessor):
                __slots__ = ()
                GrinchBannerEntryPoint = DynAccessor(748)

            banner_entry_point = _banner_entry_point()

            class _platoon(DynAccessor):
                __slots__ = ()
                MembersWindow = DynAccessor(749)

            platoon = _platoon()

            class _post_battle(DynAccessor):
                __slots__ = ()
                PostBattleView = DynAccessor(750)

            post_battle = _post_battle()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EventBannerTooltip = DynAccessor(751)

            tooltips = _tooltips()

        lobby = _lobby()

    grinch = _grinch()

    class _grinch_progression(DynAccessor):
        __slots__ = ()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                attachments_reward_view = DynAccessor(752)
                game_board = DynAccessor(753)
                info_view = DynAccessor(754)
                intro_video = DynAccessor(755)

                class _markers(DynAccessor):
                    __slots__ = ()
                    grinch_progression_marker = DynAccessor(756)

                markers = _markers()

                class _notifications(DynAccessor):
                    __slots__ = ()
                    gp_style_reward = DynAccessor(757)

                notifications = _notifications()

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ability_tooltip = DynAccessor(758)
                    chapters_info_tooltip = DynAccessor(759)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    grinch_progression = _grinch_progression()

    class _one_time_gift(DynAccessor):
        __slots__ = ()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                confirm_selection_view = DynAccessor(760)
                one_time_gift_quest_tooltip = DynAccessor(761)
                one_time_gift_view = DynAccessor(762)
                otg_event_banner_tooltip = DynAccessor(763)
                reward_available_notification_view = DynAccessor(764)
                tooltips = DynAccessor(765)

            lobby = _lobby()

        mono = _mono()

    one_time_gift = _one_time_gift()

    class _resource_well(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                AwardView = DynAccessor(766)
                CompletedProgressionView = DynAccessor(767)
                EntryPoint = DynAccessor(768)
                NoSerialVehiclesConfirm = DynAccessor(769)
                NoVehiclesConfirm = DynAccessor(770)
                ProgressionView = DynAccessor(771)
                ResourcesLoadingConfirm = DynAccessor(772)
                ResourcesLoadingView = DynAccessor(773)

                class _sharedComponents(DynAccessor):
                    __slots__ = ()

                    class _award(DynAccessor):
                        __slots__ = ()
                        AdditionalReward = DynAccessor(774)
                        Footer = DynAccessor(775)
                        Header = DynAccessor(776)
                        Reward = DynAccessor(777)

                    award = _award()
                    Counter = DynAccessor(778)
                    NoVehiclesState = DynAccessor(779)
                    Resource = DynAccessor(780)
                    VehicleCount = DynAccessor(781)
                    VehicleInfo = DynAccessor(782)

                sharedComponents = _sharedComponents()

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    EntryPointTooltip = DynAccessor(783)
                    MaxProgressTooltip = DynAccessor(784)
                    ProgressTooltip = DynAccessor(785)
                    RefundResourcesTooltip = DynAccessor(786)
                    SerialNumberTooltip = DynAccessor(787)

                tooltips = _tooltips()
                WellPanel = DynAccessor(788)

            feature = _feature()

        lobby = _lobby()

    resource_well = _resource_well()

    class _server_side_replay(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            MetaReplaysView = DynAccessor(789)

            class _popovers(DynAccessor):
                __slots__ = ()
                ReplaysFilterPopover = DynAccessor(790)

            popovers = _popovers()

        lobby = _lobby()

    server_side_replay = _server_side_replay()

    class _story_mode(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            EpilogueWindow = DynAccessor(791)
            OnboardingBattleResultView = DynAccessor(792)
            PrebattleWindow = DynAccessor(793)

        battle = _battle()

        class _common(DynAccessor):
            __slots__ = ()
            BadgeTooltip = DynAccessor(794)
            CongratulationsWindow = DynAccessor(795)
            MedalTooltip = DynAccessor(796)
            OnboardingQueueView = DynAccessor(797)

        common = _common()

        class _lobby(DynAccessor):
            __slots__ = ()
            BattleResultStatTooltip = DynAccessor(798)
            BattleResultView = DynAccessor(799)
            DifficultyTooltip = DynAccessor(800)
            EventBannerTooltip = DynAccessor(801)
            EventWelcomeView = DynAccessor(802)
            MissionSelectionView = DynAccessor(803)
            MissionTooltip = DynAccessor(804)
            NewbieAdvertisingView = DynAccessor(805)
            NewbieBannerTooltip = DynAccessor(806)

        lobby = _lobby()

    story_mode = _story_mode()
    Anchor = DynAccessor(807)

    class _child_views_demo(DynAccessor):
        __slots__ = ()
        ChildDemoView = DynAccessor(808)
        MainView = DynAccessor(809)

    child_views_demo = _child_views_demo()
    Comp7DemoPageView = DynAccessor(810)
    ComponentsDemo = DynAccessor(811)
    DataLayerDemoView = DynAccessor(812)
    DataTrackerDemo = DynAccessor(813)
    DeathCamDemoView = DynAccessor(814)
    DemoContextMenu = DynAccessor(815)
    Easings = DynAccessor(816)
    GameLoadingDebugView = DynAccessor(817)
    GFCharset = DynAccessor(818)
    GFComponents = DynAccessor(819)
    GFDemoPopover = DynAccessor(820)
    GFDemoRichTooltipWindow = DynAccessor(821)
    GFDemoWindow = DynAccessor(822)
    GFHooksDemo = DynAccessor(823)
    GFInjectView = DynAccessor(824)
    GFInputCases = DynAccessor(825)
    GFSimpleTooltipWindow = DynAccessor(826)
    GFWebSubDemoWindow = DynAccessor(827)

    class _gf_dialogs_demo(DynAccessor):
        __slots__ = ()
        DefaultDialogProxy = DynAccessor(828)
        GFDialogsDemo = DynAccessor(829)

        class _sub_views(DynAccessor):
            __slots__ = ()
            DummyContent = DynAccessor(830)
            DummyFooter = DynAccessor(831)
            DummyIcon = DynAccessor(832)
            DummyStepper = DynAccessor(833)
            DummyTitle = DynAccessor(834)
            DummyTopRight = DynAccessor(835)

        sub_views = _sub_views()

    gf_dialogs_demo = _gf_dialogs_demo()

    class _gf_viewer(DynAccessor):
        __slots__ = ()
        GFViewerWindow = DynAccessor(836)

    gf_viewer = _gf_viewer()

    class _igb_demo(DynAccessor):
        __slots__ = ()
        BrowserFullscreenWindow = DynAccessor(837)
        BrowserWindow = DynAccessor(838)
        MainView = DynAccessor(839)

    igb_demo = _igb_demo()
    LocaleDemo = DynAccessor(840)
    MediaWrapperDemo = DynAccessor(841)
    MixBlendMode = DynAccessor(842)
    MixBlendModeAnimation = DynAccessor(843)
    ModeSelectorDemo = DynAccessor(844)
    ModeSelectorToolsetView = DynAccessor(845)
    ParallaxExample = DynAccessor(850)
    ParallaxViewer = DynAccessor(851)
    PluralLocView = DynAccessor(852)
    PropsSupportDemo = DynAccessor(853)
    ReactSpringVizualizer = DynAccessor(854)
    SelectableRewardDemoView = DynAccessor(855)
    StructuralDataBindDemo = DynAccessor(856)

    class _sub_views_demo(DynAccessor):
        __slots__ = ()
        GFSubViewsDemo = DynAccessor(857)

        class _sub_views(DynAccessor):
            __slots__ = ()
            CustomizationCartProxy = DynAccessor(858)
            DailyProxy = DynAccessor(859)
            ProgressiveItemsViewProxy = DynAccessor(860)

        sub_views = _sub_views()

    sub_views_demo = _sub_views_demo()
    UILoggerDemo = DynAccessor(861)
    VideoSupportView = DynAccessor(862)
    W2CTestPageWindow = DynAccessor(863)
    WgcgMockView = DynAccessor(864)