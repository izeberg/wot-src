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
            BattleNotifierView = DynAccessor(74)

        battle_notifier = _battle_notifier()

        class _battle_page(DynAccessor):
            __slots__ = ()
            EpicRespawnAmmunitionPanelView = DynAccessor(75)
            PersonalReservesTabView = DynAccessor(76)
            PrebattleAmmunitionPanelView = DynAccessor(77)
            TabView = DynAccessor(78)

        battle_page = _battle_page()

        class _death_cam(DynAccessor):
            __slots__ = ()
            DeathCamHudView = DynAccessor(79)
            DeathCamUIView = DynAccessor(80)
            MarkerView = DynAccessor(81)

        death_cam = _death_cam()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            DogTagMarkerView = DynAccessor(82)

        dog_tags = _dog_tags()

        class _postmortem_panel(DynAccessor):
            __slots__ = ()
            PostmortemPanelView = DynAccessor(83)

        postmortem_panel = _postmortem_panel()

        class _prebattle(DynAccessor):
            __slots__ = ()
            PrebattleHintsView = DynAccessor(84)

        prebattle = _prebattle()

        class _timer(DynAccessor):
            __slots__ = ()
            TimerView = DynAccessor(85)

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
        BackportContextMenu = DynAccessor(86)
        Browser = DynAccessor(87)
        FadingCoverView = DynAccessor(88)
        HintButton = DynAccessor(89)

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            ReservesDisabledTooltip = DynAccessor(90)

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

        battleRoyale = _battleRoyale()

        class _battle_pass(DynAccessor):
            __slots__ = ()

            class _trophy_device_confirm_dialog(DynAccessor):
                __slots__ = ()
                TrophyDeviceConfirmDialogContent = DynAccessor(33)

            trophy_device_confirm_dialog = _trophy_device_confirm_dialog()
            BattlePassAwardsView = DynAccessor(145)
            BattlePassBuyLevelView = DynAccessor(146)
            BattlePassBuyView = DynAccessor(147)
            BattlePassEntryPointView = DynAccessor(148)
            BattlePassHowToEarnPointsView = DynAccessor(149)
            BattlePassIntroView = DynAccessor(150)
            BattlePassProgressionsView = DynAccessor(151)
            BattlePassVehicleAwardView = DynAccessor(152)
            ChapterChoiceView = DynAccessor(153)

            class _dialogs(DynAccessor):
                __slots__ = ()
                ChapterConfirm = DynAccessor(154)

            dialogs = _dialogs()
            ExtraIntroView = DynAccessor(155)
            FullscreenVideoView = DynAccessor(156)
            HolidayFinalView = DynAccessor(157)
            MainView = DynAccessor(158)
            PostProgressionView = DynAccessor(159)
            RewardsSelectionView = DynAccessor(160)
            RewardsViewContent = DynAccessor(161)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                AnimatedReward = DynAccessor(162)
                AttachmentOverlay = DynAccessor(163)
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
                TankmanSkills = DynAccessor(175)
                Title = DynAccessor(176)
                VehicleBonusList = DynAccessor(177)
                VehicleInfo = DynAccessor(178)
                VehicleList = DynAccessor(179)

            sharedComponents = _sharedComponents()
            TankmenVoiceoverView = DynAccessor(180)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattlePassCoinTooltipView = DynAccessor(181)
                BattlePassCompletedTooltipView = DynAccessor(182)
                BattlePassGoldMissionTooltipView = DynAccessor(183)
                BattlePassInProgressTooltipView = DynAccessor(184)
                BattlePassLockIconTooltipView = DynAccessor(185)
                BattlePassNoChapterTooltipView = DynAccessor(186)
                BattlePassOnPauseTooltipView = DynAccessor(187)
                BattlePassPointsView = DynAccessor(188)
                BattlePassQuestsChainTooltipView = DynAccessor(189)
                BattlePassTalerTooltip = DynAccessor(190)
                BattlePassUpgradeStyleTooltipView = DynAccessor(191)
                CrewMemberSkillTooltip = DynAccessor(192)
                RandomQuestTooltip = DynAccessor(193)

                class _sharedComponents(DynAccessor):
                    __slots__ = ()
                    BlockCompleted = DynAccessor(194)
                    Chose = DynAccessor(195)
                    FinalLevel = DynAccessor(196)
                    IconTextBlock = DynAccessor(197)
                    PerBattlePointsTable = DynAccessor(198)
                    Point = DynAccessor(199)
                    Rewards = DynAccessor(200)
                    Separator = DynAccessor(201)

                sharedComponents = _sharedComponents()
                VehiclePointsTooltipView = DynAccessor(202)

            tooltips = _tooltips()

        battle_pass = _battle_pass()

        class _blueprints(DynAccessor):
            __slots__ = ()

            class _fragments_balance_content(DynAccessor):
                __slots__ = ()
                FragmentsBalanceContent = DynAccessor(34)

            fragments_balance_content = _fragments_balance_content()

            class _blueprint_screen(DynAccessor):
                __slots__ = ()

                class _blueprint_screen(DynAccessor):
                    __slots__ = ()
                    BlueprintScreen = DynAccessor(35)

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
                    CommonCongratsView = DynAccessor(36)

                common_congrats_view = _common_congrats_view()

            congrats = _congrats()
            AwardsView = DynAccessor(215)
            BrowserView = DynAccessor(216)
            RewardSelection = DynAccessor(217)
            SelectableRewardBase = DynAccessor(218)
            SelectSlotSpecDialog = DynAccessor(219)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExtendedTextTooltip = DynAccessor(220)
                SelectedRewardsTooltipView = DynAccessor(221)
                SimpleIconTooltip = DynAccessor(222)

            tooltips = _tooltips()

        common = _common()

        class _marathon(DynAccessor):
            __slots__ = ()

            class _marathon_reward_view(DynAccessor):
                __slots__ = ()
                MarathonRewardView = DynAccessor(37)

            marathon_reward_view = _marathon_reward_view()
            EntryPoint = DynAccessor(354)
            RewardWindow = DynAccessor(355)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RestRewardTooltip = DynAccessor(356)

            tooltips = _tooltips()

        marathon = _marathon()

        class _missions(DynAccessor):
            __slots__ = ()

            class _missions_tab_bar_view(DynAccessor):
                __slots__ = ()
                MissionsTabBarView = DynAccessor(38)

            missions_tab_bar_view = _missions_tab_bar_view()

            class _common(DynAccessor):
                __slots__ = ()
                BattleConditions = DynAccessor(358)
                Countdown = DynAccessor(359)
                PendingDots = DynAccessor(360)

            common = _common()
            Daily = DynAccessor(361)
            DailyQuestsTooltip = DynAccessor(362)
            DailyQuestsWidget = DynAccessor(363)
            RerollTooltip = DynAccessor(364)
            RerollTooltipWithCountdown = DynAccessor(365)

        missions = _missions()

        class _nation_change(DynAccessor):
            __slots__ = ()

            class _nation_change_screen(DynAccessor):
                __slots__ = ()
                NationChangeScreen = DynAccessor(39)

            nation_change_screen = _nation_change_screen()

        nation_change = _nation_change()

        class _premacc(DynAccessor):
            __slots__ = ()

            class _piggybank(DynAccessor):
                __slots__ = ()
                Piggybank = DynAccessor(40)

            piggybank = _piggybank()

            class _dashboard(DynAccessor):
                __slots__ = ()

                class _prem_dashboard_parent_control_info(DynAccessor):
                    __slots__ = ()
                    PremDashboardParentControlInfoContent = DynAccessor(41)

                prem_dashboard_parent_control_info = _prem_dashboard_parent_control_info()

                class _piggy_bank_cards(DynAccessor):
                    __slots__ = ()

                    class _prem_piggy_bank(DynAccessor):
                        __slots__ = ()
                        PremPiggyBankCard = DynAccessor(42)

                    prem_piggy_bank = _prem_piggy_bank()

                    class _wot_plus_piggy_bank(DynAccessor):
                        __slots__ = ()
                        WotPlusPiggyBankCard = DynAccessor(43)

                    wot_plus_piggy_bank = _wot_plus_piggy_bank()

                piggy_bank_cards = _piggy_bank_cards()

            dashboard = _dashboard()

            class _tooltips(DynAccessor):
                __slots__ = ()
                SquadBonusTooltip = DynAccessor(405)

            tooltips = _tooltips()

        premacc = _premacc()

        class _progressive_reward(DynAccessor):
            __slots__ = ()

            class _progressive_reward_award(DynAccessor):
                __slots__ = ()
                ProgressiveRewardAward = DynAccessor(44)

            progressive_reward_award = _progressive_reward_award()

            class _progressive_reward_view(DynAccessor):
                __slots__ = ()
                ProgressiveRewardView = DynAccessor(45)

            progressive_reward_view = _progressive_reward_view()

        progressive_reward = _progressive_reward()

        class _ranked(DynAccessor):
            __slots__ = ()

            class _ranked_year_award(DynAccessor):
                __slots__ = ()
                RankedYearAward = DynAccessor(46)

            ranked_year_award = _ranked_year_award()
            EntryPoint = DynAccessor(414)
            QualificationRewardsView = DynAccessor(415)
            RankedSelectableRewardView = DynAccessor(416)

            class _tooltips(DynAccessor):
                __slots__ = ()
                RankedBattlesRolesTooltipView = DynAccessor(417)

            tooltips = _tooltips()
            YearLeaderboardView = DynAccessor(418)

        ranked = _ranked()

        class _reward_window(DynAccessor):
            __slots__ = ()

            class _clan_reward_window_content(DynAccessor):
                __slots__ = ()
                ClanRewardWindowContent = DynAccessor(47)

            clan_reward_window_content = _clan_reward_window_content()

            class _piggy_bank_reward_window_content(DynAccessor):
                __slots__ = ()
                PiggyBankRewardWindowContent = DynAccessor(48)

            piggy_bank_reward_window_content = _piggy_bank_reward_window_content()

            class _reward_window_content(DynAccessor):
                __slots__ = ()
                RewardWindowContent = DynAccessor(49)

            reward_window_content = _reward_window_content()

            class _twitch_reward_window_content(DynAccessor):
                __slots__ = ()
                TwitchRewardWindowContent = DynAccessor(50)

            twitch_reward_window_content = _twitch_reward_window_content()

        reward_window = _reward_window()

        class _tooltips(DynAccessor):
            __slots__ = ()

            class _clans(DynAccessor):
                __slots__ = ()
                ClanShortInfoTooltipContent = DynAccessor(51)

            clans = _clans()
            AdditionalRewardsTooltip = DynAccessor(476)
            BattleResultsStatsTooltipView = DynAccessor(477)
            TankmanTooltipView = DynAccessor(478)
            VehPostProgressionEntryPointTooltip = DynAccessor(479)

        tooltips = _tooltips()

        class _account_completion(DynAccessor):
            __slots__ = ()
            AddCredentialsView = DynAccessor(111)
            ConfirmCredentialsView = DynAccessor(112)
            CurtainView = DynAccessor(113)
            SteamEmailConfirmRewardsView = DynAccessor(114)

            class _tooltips(DynAccessor):
                __slots__ = ()
                HangarTooltip = DynAccessor(115)

            tooltips = _tooltips()

        account_completion = _account_completion()

        class _account_dashboard(DynAccessor):
            __slots__ = ()
            AccountDashboard = DynAccessor(116)
            DailyExperienceView = DynAccessor(117)

        account_dashboard = _account_dashboard()

        class _achievements(DynAccessor):
            __slots__ = ()
            AchievementsMainView = DynAccessor(118)
            CatalogView = DynAccessor(119)

            class _dialogs(DynAccessor):
                __slots__ = ()
                EditConfirm = DynAccessor(120)

            dialogs = _dialogs()
            EarningPopUpView = DynAccessor(121)
            EditView = DynAccessor(122)
            RewardView = DynAccessor(123)

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
                RewardCompensationTooltip = DynAccessor(133)
                VehicleForChooseTooltip = DynAccessor(134)

            tooltips = _tooltips()

        awards = _awards()

        class _battle_matters(DynAccessor):
            __slots__ = ()
            BattleMattersEntryPointView = DynAccessor(135)
            BattleMattersExchangeRewards = DynAccessor(136)
            BattleMattersMainRewardView = DynAccessor(137)
            BattleMattersMainView = DynAccessor(138)
            BattleMattersPausedView = DynAccessor(139)
            BattleMattersRewardsView = DynAccessor(140)
            BattleMattersVehicleSelectionView = DynAccessor(141)

            class _popovers(DynAccessor):
                __slots__ = ()
                BattleMattersFilterPopoverView = DynAccessor(142)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                BattleMattersEntryTooltipView = DynAccessor(143)
                BattleMattersTokenTooltipView = DynAccessor(144)

            tooltips = _tooltips()

        battle_matters = _battle_matters()

        class _battle_royale(DynAccessor):
            __slots__ = ()

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                CurrencyResolver = DynAccessor(203)
                PriceResolver = DynAccessor(204)

            sharedComponents = _sharedComponents()

        battle_royale = _battle_royale()

        class _clan_supply(DynAccessor):
            __slots__ = ()
            ClanSupply = DynAccessor(207)
            RewardsView = DynAccessor(208)

        clan_supply = _clan_supply()

        class _collection(DynAccessor):
            __slots__ = ()
            AwardsView = DynAccessor(209)
            CollectionItemPreview = DynAccessor(210)
            CollectionsMainView = DynAccessor(211)
            CollectionView = DynAccessor(212)
            IntroView = DynAccessor(213)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CollectionItemTooltipView = DynAccessor(214)

            tooltips = _tooltips()

        collection = _collection()

        class _craft_machine(DynAccessor):
            __slots__ = ()
            CraftmachineEntryPointView = DynAccessor(223)

        craft_machine = _craft_machine()

        class _crew(DynAccessor):
            __slots__ = ()
            BarracksView = DynAccessor(224)
            ConversionConfirmView = DynAccessor(225)
            CrewHeaderTooltipView = DynAccessor(226)
            CrewPostProgressionView = DynAccessor(227)

            class _dialogs(DynAccessor):
                __slots__ = ()
                CrewBooksPurchaseDialog = DynAccessor(228)
                DismissTankmanDialog = DynAccessor(229)
                DocumentChangeDialog = DynAccessor(230)
                EnlargeBarracksDialog = DynAccessor(231)
                FillAllPerksDialog = DynAccessor(232)
                MentorAssignmentDialog = DynAccessor(233)
                PerksResetDialog = DynAccessor(234)
                RecruitConfirmIrrelevantDialog = DynAccessor(235)
                RecruitDialog = DynAccessor(236)
                RecruitNewTankmanDialog = DynAccessor(237)
                RestoreTankmanDialog = DynAccessor(238)
                RetrainMassiveDialog = DynAccessor(239)
                RetrainPremiumVehicleDialog = DynAccessor(240)
                RetrainSingleDialog = DynAccessor(241)
                SkillsTrainingConfirmDialog = DynAccessor(242)
                SkinApplyDialog = DynAccessor(243)

            dialogs = _dialogs()
            HangarCrewWidget = DynAccessor(244)
            HelpView = DynAccessor(245)
            JunkTankmenView = DynAccessor(246)
            MemberChangeView = DynAccessor(247)
            MentorAssigmentView = DynAccessor(248)

            class _personal_case(DynAccessor):
                __slots__ = ()
                PersonalDataView = DynAccessor(249)
                PersonalFileView = DynAccessor(250)
                ServiceRecordView = DynAccessor(251)

            personal_case = _personal_case()

            class _popovers(DynAccessor):
                __slots__ = ()
                FilterPopoverView = DynAccessor(252)

            popovers = _popovers()
            QuickTrainingView = DynAccessor(253)
            SkillsTrainingView = DynAccessor(254)
            TankChangeView = DynAccessor(255)
            TankmanContainerView = DynAccessor(256)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AdvancedTooltipView = DynAccessor(257)
                BonusPerksTooltip = DynAccessor(258)
                BunksConfirmDiscountTooltip = DynAccessor(259)
                ConversionTooltip = DynAccessor(260)
                CrewBookMouseTooltip = DynAccessor(261)
                CrewPerksAdditionalTooltip = DynAccessor(262)
                CrewPerksTooltip = DynAccessor(263)
                DirectiveConversionTooltip = DynAccessor(264)
                DismissedToggleTooltip = DynAccessor(265)
                EmptySkillTooltip = DynAccessor(266)
                ExperienceStepperTooltip = DynAccessor(267)
                MentorAssignmentTooltip = DynAccessor(268)
                MentoringLicenseTooltip = DynAccessor(269)
                PostProgressionTooltip = DynAccessor(270)
                PremiumVehicleTooltip = DynAccessor(271)
                QualificationTooltip = DynAccessor(272)
                QuickTrainingDiscountTooltip = DynAccessor(273)
                QuickTrainingLostXpTooltip = DynAccessor(274)
                SkillsEfficiencyTooltip = DynAccessor(275)
                SkillUntrainedAdditionalTooltip = DynAccessor(276)
                SkillUntrainedTooltip = DynAccessor(277)
                SortingDropdownTooltip = DynAccessor(278)
                SpecializationWotPlusTooltip = DynAccessor(279)
                TankmanTooltip = DynAccessor(280)
                VehCmpSkillsTooltip = DynAccessor(281)
                VehicleParamsTooltipView = DynAccessor(282)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                CrewBannerWidget = DynAccessor(283)
                CrewWidget = DynAccessor(284)
                FilterPanelWidget = DynAccessor(285)
                PriceList = DynAccessor(286)
                TankmanInfo = DynAccessor(287)

            widgets = _widgets()

        crew = _crew()

        class _crystalsPromo(DynAccessor):
            __slots__ = ()
            CrystalsPromoView = DynAccessor(288)

        crystalsPromo = _crystalsPromo()

        class _currency_reserves(DynAccessor):
            __slots__ = ()
            CurrencyReserves = DynAccessor(289)
            ReservesAwardView = DynAccessor(290)

        currency_reserves = _currency_reserves()

        class _customization(DynAccessor):
            __slots__ = ()
            CustomizationCart = DynAccessor(291)
            CustomizationRarityRewardScreen = DynAccessor(292)

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

            class _vehicles_sidebar(DynAccessor):
                __slots__ = ()
                VehiclesSidebar = DynAccessor(298)

            vehicles_sidebar = _vehicles_sidebar()

        customization = _customization()

        class _dedication(DynAccessor):
            __slots__ = ()
            DedicationRewardView = DynAccessor(299)

        dedication = _dedication()

        class _dog_tags(DynAccessor):
            __slots__ = ()
            AnimatedDogTagGradeTooltip = DynAccessor(300)
            AnimatedDogTagsView = DynAccessor(301)
            CatalogAnimatedDogTagTooltip = DynAccessor(302)
            CustomizationConfirmDialog = DynAccessor(303)
            DedicationTooltip = DynAccessor(304)
            DogTagsView = DynAccessor(305)
            RankedEfficiencyTooltip = DynAccessor(306)
            ThreeMonthsTooltip = DynAccessor(307)
            TriumphTooltip = DynAccessor(308)

        dog_tags = _dog_tags()

        class _excluded_maps(DynAccessor):
            __slots__ = ()
            ExcludedMapsTooltip = DynAccessor(309)
            ExcludedMapsView = DynAccessor(310)

        excluded_maps = _excluded_maps()

        class _frontline(DynAccessor):
            __slots__ = ()

            class _dialogs(DynAccessor):
                __slots__ = ()
                BlankPrice = DynAccessor(311)

            dialogs = _dialogs()
            IntroScreen = DynAccessor(312)
            RewardsSelectionView = DynAccessor(313)

        frontline = _frontline()

        class _hangar(DynAccessor):
            __slots__ = ()
            BuyVehicleView = DynAccessor(314)

            class _notifications(DynAccessor):
                __slots__ = ()
                PunishmentView = DynAccessor(315)

            notifications = _notifications()

            class _subViews(DynAccessor):
                __slots__ = ()
                VehicleParams = DynAccessor(316)

            subViews = _subViews()
            VehicleParamsWidget = DynAccessor(317)

        hangar = _hangar()

        class _instructions(DynAccessor):
            __slots__ = ()
            BuyWindow = DynAccessor(318)
            SellWindow = DynAccessor(319)

        instructions = _instructions()

        class _live_ops_web_events(DynAccessor):
            __slots__ = ()
            EntryPoint = DynAccessor(320)
            EntryPointTooltip = DynAccessor(321)

        live_ops_web_events = _live_ops_web_events()

        class _lootbox_system(DynAccessor):
            __slots__ = ()
            AutoOpenView = DynAccessor(322)

            class _baseComponents(DynAccessor):
                __slots__ = ()
                AnimationCheckbox = DynAccessor(323)
                AutoCleanVideo = DynAccessor(324)
                BigButton = DynAccessor(325)

                class _common(DynAccessor):
                    __slots__ = ()
                    AlertIcon = DynAccessor(326)
                    Icon = DynAccessor(327)

                common = _common()
                Loader = DynAccessor(328)
                LoupeButton = DynAccessor(329)
                PurchaseButton = DynAccessor(330)
                ScrollWithLips = DynAccessor(331)
                SubTitle = DynAccessor(332)
                TankName = DynAccessor(333)
                Title = DynAccessor(334)
                VehicleInfo = DynAccessor(335)

            baseComponents = _baseComponents()
            EntryPointView = DynAccessor(336)
            InfoPage = DynAccessor(337)
            MainView = DynAccessor(338)

            class _tooltips(DynAccessor):
                __slots__ = ()
                BoxCompensationTooltip = DynAccessor(339)
                BoxTooltip = DynAccessor(340)
                EntryPointTooltip = DynAccessor(341)
                GuaranteedRewardInfoTooltip = DynAccessor(342)
                RandomNationalBonusTooltipView = DynAccessor(343)
                StatisticsCategoryTooltipView = DynAccessor(344)

            tooltips = _tooltips()

        lootbox_system = _lootbox_system()

        class _mapbox(DynAccessor):
            __slots__ = ()
            MapBoxAwardsView = DynAccessor(345)
            MapBoxEntryPointView = DynAccessor(346)
            MapBoxIntro = DynAccessor(347)
            MapBoxProgression = DynAccessor(348)
            MapBoxSurveyView = DynAccessor(349)

        mapbox = _mapbox()

        class _maps_training(DynAccessor):
            __slots__ = ()
            MapsTrainingPage = DynAccessor(350)
            MapsTrainingQueue = DynAccessor(351)
            MapsTrainingResult = DynAccessor(352)
            ScenarioTooltip = DynAccessor(353)

        maps_training = _maps_training()

        class _matchmaker(DynAccessor):
            __slots__ = ()
            ActiveTestConfirmView = DynAccessor(357)

        matchmaker = _matchmaker()

        class _mode_selector(DynAccessor):
            __slots__ = ()
            BattleSessionView = DynAccessor(366)
            ModeSelectorView = DynAccessor(367)

            class _tooltips(DynAccessor):
                __slots__ = ()
                AlertTooltip = DynAccessor(368)

                class _common(DynAccessor):
                    __slots__ = ()
                    Divider = DynAccessor(369)
                    GradientDecorator = DynAccessor(370)

                common = _common()
                SimplyFormatTooltip = DynAccessor(371)

            tooltips = _tooltips()

            class _widgets(DynAccessor):
                __slots__ = ()
                BattleRoyaleProgressionWidget = DynAccessor(372)
                BattleRoyaleWidget = DynAccessor(373)
                EpicWidget = DynAccessor(374)
                RankedWidget = DynAccessor(375)

            widgets = _widgets()

        mode_selector = _mode_selector()

        class _offers(DynAccessor):
            __slots__ = ()
            OfferBannerWindow = DynAccessor(376)
            OfferGiftsWindow = DynAccessor(377)
            OfferRewardWindow = DynAccessor(378)

        offers = _offers()

        class _personal_exchange_rates(DynAccessor):
            __slots__ = ()
            AllPersonalExchangesView = DynAccessor(379)
            ExperienceExchangeView = DynAccessor(380)
            GoldExchangeView = DynAccessor(381)

            class _tooltips(DynAccessor):
                __slots__ = ()
                ExchangeLimitTooltip = DynAccessor(382)
                ExchangeRateTooltip = DynAccessor(383)

            tooltips = _tooltips()

        personal_exchange_rates = _personal_exchange_rates()

        class _personal_reserves(DynAccessor):
            __slots__ = ()
            BoosterTooltip = DynAccessor(384)
            PersonalReservesTooltip = DynAccessor(385)
            PersonalReservesWidget = DynAccessor(386)
            QuestBoosterTooltip = DynAccessor(387)
            ReserveCard = DynAccessor(388)
            ReserveCardTooltip = DynAccessor(389)
            ReserveGroup = DynAccessor(390)
            ReservesActivationView = DynAccessor(391)
            ReservesIntroView = DynAccessor(392)

        personal_reserves = _personal_reserves()

        class _platoon(DynAccessor):
            __slots__ = ()
            AlertTooltip = DynAccessor(393)
            MembersWindow = DynAccessor(394)
            PlatoonDropdown = DynAccessor(395)
            SearchingDropdown = DynAccessor(396)
            SettingsPopover = DynAccessor(397)

            class _subViews(DynAccessor):
                __slots__ = ()
                Chat = DynAccessor(398)
                SettingsContent = DynAccessor(399)
                TiersLimit = DynAccessor(400)

            subViews = _subViews()
            WTRTooltip = DynAccessor(401)

        platoon = _platoon()

        class _player_subscriptions(DynAccessor):
            __slots__ = ()
            PlayerSubscriptions = DynAccessor(402)
            SubscriptionItem = DynAccessor(403)
            SubscriptionRewardView = DynAccessor(404)

        player_subscriptions = _player_subscriptions()

        class _prestige(DynAccessor):
            __slots__ = ()

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                PrestigeProgressSymbol = DynAccessor(406)
                PrestigeProgressTab = DynAccessor(407)

            sharedComponents = _sharedComponents()

            class _tooltips(DynAccessor):
                __slots__ = ()
                EliteLevelGradesTooltip = DynAccessor(408)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                GlobalOnboardingView = DynAccessor(409)
                PrestigeHangarEntryPoint = DynAccessor(410)
                PrestigeProfileTechniqueEmblemView = DynAccessor(411)
                PrestigeProfileTechniqueView = DynAccessor(412)
                PrestigeRewardView = DynAccessor(413)

            views = _views()

        prestige = _prestige()

        class _research(DynAccessor):
            __slots__ = ()
            BuyModuleDialogView = DynAccessor(419)
            InsufficientCreditsTooltip = DynAccessor(420)
            SoldModuleInfoTooltip = DynAccessor(421)

        research = _research()

        class _seniority_awards(DynAccessor):
            __slots__ = ()
            SeniorityAwardsTooltip = DynAccessor(422)
            SeniorityAwardsView = DynAccessor(423)
            SeniorityVehiclesAwardsView = DynAccessor(424)

            class _sharedComponents(DynAccessor):
                __slots__ = ()
                FormatGradientText = DynAccessor(425)
                SeniorityAwardCoin = DynAccessor(426)
                SeniorityAwardsScroll = DynAccessor(427)
                SeniorityAwardsViewFooter = DynAccessor(428)
                SeniorityAwardsViewHeader = DynAccessor(429)

            sharedComponents = _sharedComponents()

        seniority_awards = _seniority_awards()

        class _subscription(DynAccessor):
            __slots__ = ()
            SubscriptionAwardView = DynAccessor(430)
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
                DemountKit = DynAccessor(436)
                ExtraImage = DynAccessor(437)
                FormatColorTagText = DynAccessor(438)
                Location = DynAccessor(439)
                MaybeWrapper = DynAccessor(440)
                Price = DynAccessor(441)
                SetupApp = DynAccessor(442)
                ShortenedText = DynAccessor(443)
                Slider = DynAccessor(444)

                class _SlotParts(DynAccessor):
                    __slots__ = ()
                    Bonus = DynAccessor(445)
                    Container = DynAccessor(446)
                    Count = DynAccessor(447)
                    Inside = DynAccessor(448)
                    Level = DynAccessor(449)

                SlotParts = _SlotParts()
                Specializations = DynAccessor(450)
                SwitchButton = DynAccessor(451)
                SwitchEquipment = DynAccessor(452)

                class _Transitions(DynAccessor):
                    __slots__ = ()
                    SlotTransitions = DynAccessor(453)

                Transitions = _Transitions()
                WeaponOccupancy = DynAccessor(454)

            common = _common()
            DeconstructionDeviceView = DynAccessor(455)

            class _dialogs(DynAccessor):
                __slots__ = ()
                Confirm = DynAccessor(456)
                ConfirmActionsWithEquipmentDialog = DynAccessor(457)
                DeconstructConfirm = DynAccessor(458)
                DeviceUpgradeDialog = DynAccessor(459)
                ExchangeToApplyEasyTankEquip = DynAccessor(460)
                ExchangeToBuyItems = DynAccessor(461)
                ExchangeToUpgradeItems = DynAccessor(462)
                NeedRepair = DynAccessor(463)
                RefillShells = DynAccessor(464)
                Sell = DynAccessor(465)

            dialogs = _dialogs()
            EasyTankEquipView = DynAccessor(466)
            HangarAmmunitionSetup = DynAccessor(467)
            IntroScreen = DynAccessor(468)

            class _tooltips(DynAccessor):
                __slots__ = ()
                DeconstructFromInventoryTooltip = DynAccessor(469)
                DeconstructFromVehicleTooltip = DynAccessor(470)
                PopularLoadoutsTooltip = DynAccessor(471)
                SetupTabTooltipView = DynAccessor(472)
                WarningTooltipView = DynAccessor(473)

            tooltips = _tooltips()
            VehicleCompareAmmunitionPanel = DynAccessor(474)
            VehicleCompareAmmunitionSetup = DynAccessor(475)

        tanksetup = _tanksetup()

        class _vehicle_compare(DynAccessor):
            __slots__ = ()
            CompareModificationsPanelView = DynAccessor(480)
            CompareSkillsPanelView = DynAccessor(481)
            SelectSlotSpecCompareDialog = DynAccessor(482)
            SkillSelectView = DynAccessor(483)

            class _tooltips(DynAccessor):
                __slots__ = ()
                CrewRolesTooltip = DynAccessor(484)

            tooltips = _tooltips()

        vehicle_compare = _vehicle_compare()

        class _vehicle_preview(DynAccessor):
            __slots__ = ()

            class _buying_panel(DynAccessor):
                __slots__ = ()
                StyleBuyingPanel = DynAccessor(485)
                VPProgressionStylesBuyingPanel = DynAccessor(486)

            buying_panel = _buying_panel()

            class _tabs(DynAccessor):
                __slots__ = ()
                CrewTabView = DynAccessor(487)

            tabs = _tabs()

            class _top_panel(DynAccessor):
                __slots__ = ()
                TopPanelTabs = DynAccessor(488)

            top_panel = _top_panel()

        vehicle_preview = _vehicle_preview()

        class _veh_post_progression(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                Bonus = DynAccessor(489)
                Description = DynAccessor(490)
                Grid = DynAccessor(491)
                PersistentBonuses = DynAccessor(492)
                Slide = DynAccessor(493)
                SlideContent = DynAccessor(494)
                Slider = DynAccessor(495)
                TextSplit = DynAccessor(496)

            common = _common()
            PostProgressionInfo = DynAccessor(497)
            PostProgressionIntro = DynAccessor(498)
            PostProgressionResearchSteps = DynAccessor(499)

            class _tooltip(DynAccessor):
                __slots__ = ()

                class _common(DynAccessor):
                    __slots__ = ()
                    DisabledBlock = DynAccessor(500)
                    FeatureLevelSubtitle = DynAccessor(501)
                    Lock = DynAccessor(502)
                    NotEnoughCredits = DynAccessor(503)
                    PriceBlock = DynAccessor(504)
                    Separator = DynAccessor(505)

                common = _common()
                PairModificationTooltipView = DynAccessor(506)
                PostProgressionLevelTooltipView = DynAccessor(507)
                RoleSlotTooltipView = DynAccessor(508)
                SetupTooltipView = DynAccessor(509)

            tooltip = _tooltip()
            VehiclePostProgressionCmpView = DynAccessor(510)
            VehiclePostProgressionView = DynAccessor(511)

        veh_post_progression = _veh_post_progression()

        class _winback(DynAccessor):
            __slots__ = ()

            class _popovers(DynAccessor):
                __slots__ = ()
                WinbackLeaveModePopoverView = DynAccessor(512)

            popovers = _popovers()

            class _tooltips(DynAccessor):
                __slots__ = ()
                MainRewardTooltip = DynAccessor(513)
                ModeInfoTooltip = DynAccessor(514)
                SelectableRewardTooltip = DynAccessor(515)
                SelectedRewardsTooltip = DynAccessor(516)

            tooltips = _tooltips()
            WinbackDailyQuestsIntroView = DynAccessor(517)
            WinbackLeaveModeDialogView = DynAccessor(518)
            WinbackRewardView = DynAccessor(519)
            WinbackSelectableRewardView = DynAccessor(520)

        winback = _winback()

    lobby = _lobby()

    class _test_check_box_view(DynAccessor):
        __slots__ = ()
        TestCheckBoxView = DynAccessor(52)

    test_check_box_view = _test_check_box_view()

    class _test_text_button_view(DynAccessor):
        __slots__ = ()
        TestTextButtonView = DynAccessor(53)

    test_text_button_view = _test_text_button_view()

    class _windows_layout_view(DynAccessor):
        __slots__ = ()
        WindowsLayountView = DynAccessor(54)

    windows_layout_view = _windows_layout_view()

    class _blend_mode(DynAccessor):
        __slots__ = ()

        class _blend_mode(DynAccessor):
            __slots__ = ()
            BlendMode = DynAccessor(55)

        blend_mode = _blend_mode()

    blend_mode = _blend_mode()

    class _demo_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _demo_window_content(DynAccessor):
                __slots__ = ()
                DemoWindowContent = DynAccessor(56)
                ImageProps = DynAccessor(57)

            demo_window_content = _demo_window_content()

            class _demo_window_details_panel(DynAccessor):
                __slots__ = ()
                DemoWindowDetailsPanel = DynAccessor(58)

            demo_window_details_panel = _demo_window_details_panel()

            class _demo_window_image_panel(DynAccessor):
                __slots__ = ()
                DemoWindowImagePanel = DynAccessor(59)

            demo_window_image_panel = _demo_window_image_panel()

            class _image_preview_window_content(DynAccessor):
                __slots__ = ()
                ImagePreviewWindowContent = DynAccessor(60)

            image_preview_window_content = _image_preview_window_content()

        views = _views()

    demo_view = _demo_view()

    class _examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_dialogs_view(DynAccessor):
                __slots__ = ()
                TestDialogsView = DynAccessor(61)

            test_dialogs_view = _test_dialogs_view()

            class _test_expr_functions_view(DynAccessor):
                __slots__ = ()
                TestExprFunctionsView = DynAccessor(62)

            test_expr_functions_view = _test_expr_functions_view()

            class _test_sub_view(DynAccessor):
                __slots__ = ()
                TestSubView = DynAccessor(63)

            test_sub_view = _test_sub_view()

            class _test_view(DynAccessor):
                __slots__ = ()
                TestView = DynAccessor(64)

            test_view = _test_view()

            class _unbound_example(DynAccessor):
                __slots__ = ()
                UnboundExample = DynAccessor(65)

            unbound_example = _unbound_example()

        views = _views()

    examples = _examples()

    class _list_examples(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _list_examples_empty_render_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesEmptyRenderWindowContent = DynAccessor(66)

            list_examples_empty_render_window_content = _list_examples_empty_render_window_content()

            class _list_examples_window_content(DynAccessor):
                __slots__ = ()
                ListExamplesWindowContent = DynAccessor(67)

            list_examples_window_content = _list_examples_window_content()

        views = _views()

    list_examples = _list_examples()

    class _rotation_pivot_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_pivot_view(DynAccessor):
                __slots__ = ()
                RotationAndPivotTestView = DynAccessor(68)

            rotation_pivot_view = _rotation_pivot_view()

        views = _views()

    rotation_pivot_view = _rotation_pivot_view()

    class _rotation_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _rotation_view(DynAccessor):
                __slots__ = ()
                RotationTestView = DynAccessor(69)

            rotation_view = _rotation_view()

        views = _views()

    rotation_view = _rotation_view()

    class _scale_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _scale_view(DynAccessor):
                __slots__ = ()
                ScaleTestView = DynAccessor(70)

            scale_view = _scale_view()

        views = _views()

    scale_view = _scale_view()

    class _test_uikit_buttons_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_buttons_view(DynAccessor):
                __slots__ = ()
                TestUikitButtonsView = DynAccessor(71)

            test_uikit_buttons_view = _test_uikit_buttons_view()

        views = _views()

    test_uikit_buttons_view = _test_uikit_buttons_view()

    class _test_uikit_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _test_uikit_view(DynAccessor):
                __slots__ = ()
                TestUikitView = DynAccessor(72)

            test_uikit_view = _test_uikit_view()

        views = _views()

    test_uikit_view = _test_uikit_view()

    class _wtypes_view(DynAccessor):
        __slots__ = ()

        class _views(DynAccessor):
            __slots__ = ()

            class _wtypes_demo_window_content(DynAccessor):
                __slots__ = ()
                WtypesDemoWindowContent = DynAccessor(73)

            wtypes_demo_window_content = _wtypes_demo_window_content()

        views = _views()

    wtypes_view = _wtypes_view()

    class _dialogs(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            DialogTemplateGenericTooltip = DynAccessor(91)

        common = _common()
        DefaultDialog = DynAccessor(92)

        class _sub_views(DynAccessor):
            __slots__ = ()

            class _common(DynAccessor):
                __slots__ = ()
                SimpleText = DynAccessor(93)
                SinglePrice = DynAccessor(94)

            common = _common()

            class _content(DynAccessor):
                __slots__ = ()
                SelectOptionContent = DynAccessor(95)
                SimpleTextContent = DynAccessor(96)
                SinglePriceContent = DynAccessor(97)
                TextWithWarning = DynAccessor(98)

            content = _content()

            class _footer(DynAccessor):
                __slots__ = ()
                BRSinglePriceFooter = DynAccessor(99)
                SimpleTextFooter = DynAccessor(100)
                SinglePriceFooter = DynAccessor(101)

            footer = _footer()

            class _icon(DynAccessor):
                __slots__ = ()
                MultipleIconsSet = DynAccessor(102)

            icon = _icon()

            class _title(DynAccessor):
                __slots__ = ()
                SimpleTextTitle = DynAccessor(103)

            title = _title()

            class _topRight(DynAccessor):
                __slots__ = ()
                BRMoneyBalance = DynAccessor(104)
                MoneyBalance = DynAccessor(105)

            topRight = _topRight()

        sub_views = _sub_views()

        class _widgets(DynAccessor):
            __slots__ = ()
            IconSet = DynAccessor(106)
            MoneyBalance = DynAccessor(107)
            SinglePrice = DynAccessor(108)
            WarningText = DynAccessor(109)

        widgets = _widgets()

    dialogs = _dialogs()

    class _loading(DynAccessor):
        __slots__ = ()
        GameLoadingView = DynAccessor(110)

    loading = _loading()

    class _mono(DynAccessor):
        __slots__ = ()

        class _dialogs(DynAccessor):
            __slots__ = ()
            research_confirm_dialog = DynAccessor(521)

        dialogs = _dialogs()

        class _hangar(DynAccessor):
            __slots__ = ()
            footer = DynAccessor(522)
            header = DynAccessor(523)
            main = DynAccessor(524)

            class _overlays(DynAccessor):
                __slots__ = ()
                playlist = DynAccessor(525)

            overlays = _overlays()
            tooltips = DynAccessor(526)
            vehicle_tooltip = DynAccessor(527)

        hangar = _hangar()

        class _lobby(DynAccessor):
            __slots__ = ()
            elite_window = DynAccessor(528)

            class _veh_skill_tree(DynAccessor):
                __slots__ = ()
                comparison = DynAccessor(529)

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    alternate_configuration = DynAccessor(530)

                dialogs = _dialogs()
                intro_page = DynAccessor(531)

                class _notifications(DynAccessor):
                    __slots__ = ()
                    perk_available = DynAccessor(532)

                notifications = _notifications()
                rarity_reward_screen = DynAccessor(533)
                reward_screen = DynAccessor(534)

            veh_skill_tree = _veh_skill_tree()

        lobby = _lobby()

        class _lootbox(DynAccessor):
            __slots__ = ()
            auto_open = DynAccessor(535)
            info_page = DynAccessor(536)
            main = DynAccessor(537)

            class _tooltips(DynAccessor):
                __slots__ = ()
                box_compensation = DynAccessor(538)
                box_tooltip = DynAccessor(539)
                entry_point = DynAccessor(540)
                guaranteed_reward_info = DynAccessor(541)
                random_national_bonus = DynAccessor(542)
                statistics_category = DynAccessor(543)

            tooltips = _tooltips()

        lootbox = _lootbox()

        class _personal_missions_30(DynAccessor):
            __slots__ = ()
            assembling_video = DynAccessor(544)
            campaign_selector = DynAccessor(545)
            intro_screen = DynAccessor(546)
            main = DynAccessor(547)
            rewards = DynAccessor(548)

            class _tooltips(DynAccessor):
                __slots__ = ()
                missions_category_tooltip = DynAccessor(549)
                mission_progress_tooltip = DynAccessor(550)
                param_tooltip = DynAccessor(551)

            tooltips = _tooltips()

        personal_missions_30 = _personal_missions_30()

        class _post_battle(DynAccessor):
            __slots__ = ()
            flag = DynAccessor(552)
            random = DynAccessor(553)

            class _tooltips(DynAccessor):
                __slots__ = ()
                critical_damage = DynAccessor(554)

            tooltips = _tooltips()

        post_battle = _post_battle()

        class _stronghold_event(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                event_banner_tooltip = DynAccessor(555)

            tooltips = _tooltips()

        stronghold_event = _stronghold_event()

        class _tech_tree(DynAccessor):
            __slots__ = ()
            main = DynAccessor(556)

        tech_tree = _tech_tree()

        class _template(DynAccessor):
            __slots__ = ()
            main = DynAccessor(557)

        template = _template()

        class _tooltips(DynAccessor):
            __slots__ = ()
            tooltips = DynAccessor(558)

        tooltips = _tooltips()

        class _user_missions(DynAccessor):
            __slots__ = ()

            class _hub(DynAccessor):
                __slots__ = ()
                mission_hub_intro_view = DynAccessor(560)

            hub = _hub(559)
            info_page = DynAccessor(561)

            class _tooltips(DynAccessor):
                __slots__ = ()
                all_quests_done_tooltip = DynAccessor(562)
                daily_quest_tooltip = DynAccessor(563)
                daily_reroll_tooltip = DynAccessor(564)
                param_tooltip = DynAccessor(565)
                pm3_banner_tooltip = DynAccessor(566)
                weekly_quest_tooltip = DynAccessor(567)

            tooltips = _tooltips()

        user_missions = _user_missions()

        class _vehicle_hub(DynAccessor):
            __slots__ = ()
            main = DynAccessor(568)

            class _tooltips(DynAccessor):
                __slots__ = ()
                armor_tooltip = DynAccessor(569)
                back_to_main_progression_tooltip = DynAccessor(570)
                perk_tooltip = DynAccessor(571)
                prestige_reward_tooltip = DynAccessor(572)
                vanity_entry_point_tooltip = DynAccessor(573)

            tooltips = _tooltips()

        vehicle_hub = _vehicle_hub()

        class _demos(DynAccessor):
            __slots__ = ()
            data_layer = DynAccessor(767)

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
                                tooltips = DynAccessor(769)

                            param_tooltip = _param_tooltip()

                        pages = _pages()

                    tech_ui = _tech_ui()

                pages = _pages()

            entry = _entry(768)

            class _notifications(DynAccessor):
                __slots__ = ()
                test_notification = DynAccessor(770)

            notifications = _notifications()

        demos = _demos()

    mono = _mono()

    class _battle_modifiers(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _tooltips(DynAccessor):
                __slots__ = ()
                ModifiersDomainTooltipView = DynAccessor(574)

            tooltips = _tooltips()

        lobby = _lobby()

    battle_modifiers = _battle_modifiers()

    class _battle_royale(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()

            class _views(DynAccessor):
                __slots__ = ()
                LeaveBattleView = DynAccessor(575)

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
                        Column = DynAccessor(576)
                        Table = DynAccessor(577)

                    LeaderBoard = _LeaderBoard()

                common = _common()
                LeaderboardRewardTooltipView = DynAccessor(578)
                RewardCurrencyTooltipView = DynAccessor(579)
                VehicleTooltipView = DynAccessor(580)

            tooltips = _tooltips()

            class _views(DynAccessor):
                __slots__ = ()
                BattleResultView = DynAccessor(581)
                PreBattleView = DynAccessor(582)

            views = _views()

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                hangar = DynAccessor(583)
                info_page = DynAccessor(584)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ability = DynAccessor(585)
                    all_quests_done_tooltip = DynAccessor(586)
                    banner = DynAccessor(587)
                    battle_selector = DynAccessor(588)
                    ceasefire = DynAccessor(589)
                    commander = DynAccessor(590)
                    progression_quest = DynAccessor(591)
                    progression_widget = DynAccessor(592)
                    respawn = DynAccessor(593)
                    shop_button = DynAccessor(594)
                    upgrades_button = DynAccessor(595)
                    vehicle = DynAccessor(596)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    battle_royale = _battle_royale()

    class _battle_royale_progression(DynAccessor):
        __slots__ = ()
        BattleQuestAwardsView = DynAccessor(597)

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                battle_quest_awards_view = DynAccessor(598)

            lobby = _lobby()

        mono = _mono()
        ProgressionMainView = DynAccessor(599)

    battle_royale_progression = _battle_royale_progression()

    class _comp7(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            Comp7BattleCard = DynAccessor(600)
            MembersWindow = DynAccessor(601)
            PlatoonDropdown = DynAccessor(602)
            RewardsSelectionScreen = DynAccessor(603)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    purchase_dialog = DynAccessor(604)

                dialogs = _dialogs()
                grand_tournament_widget = DynAccessor(605)
                hangar = DynAccessor(606)
                intro_screen = DynAccessor(607)
                meta_root_view = DynAccessor(608)
                no_vehicles_screen = DynAccessor(609)
                rewards_screen = DynAccessor(610)
                season_statistics = DynAccessor(611)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    crew_members_tooltip = DynAccessor(612)
                    division_tooltip = DynAccessor(613)
                    entry_point_tooltip = DynAccessor(614)
                    fifth_rank_tooltip = DynAccessor(615)
                    general_rank_tooltip = DynAccessor(616)
                    last_update_tooltip = DynAccessor(617)
                    progression_tooltip = DynAccessor(618)
                    rank_compatibility_tooltip = DynAccessor(619)
                    rank_inactivity_tooltip = DynAccessor(620)
                    season_point_tooltip = DynAccessor(621)
                    sixth_rank_tooltip = DynAccessor(622)
                    style3d_tooltip = DynAccessor(623)
                    weekly_quest_widget_tooltip = DynAccessor(624)

                tooltips = _tooltips()
                tournaments_widget = DynAccessor(625)
                whats_new_view = DynAccessor(626)

            lobby = _lobby()

        mono = _mono()

    comp7 = _comp7()

    class _comp7_light(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            Comp7LightBattleCard = DynAccessor(627)
            MembersWindow = DynAccessor(628)
            PlatoonDropdown = DynAccessor(629)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                battle_quest_awards_view = DynAccessor(630)
                entry_point_tooltip = DynAccessor(631)
                hangar = DynAccessor(632)
                intro_screen = DynAccessor(633)
                leaderboard_reward_tooltip_view = DynAccessor(634)
                no_vehicles_screen = DynAccessor(635)
                progression_main_view = DynAccessor(636)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    all_quests_done_tooltip = DynAccessor(637)
                    battle_quest_tooltip = DynAccessor(638)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    comp7_light = _comp7_light()

    class _frontline(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            WelcomeView = DynAccessor(639)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()

                class _dialogs(DynAccessor):
                    __slots__ = ()
                    battle_abilities_confirm_dialog = DynAccessor(640)

                dialogs = _dialogs()
                hangar = DynAccessor(641)
                info_view = DynAccessor(642)
                post_battle_rewards_view = DynAccessor(643)
                progression_screen = DynAccessor(644)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    banner_tooltip = DynAccessor(645)
                    battle_ability_alt_tooltip = DynAccessor(646)
                    battle_ability_tooltip = DynAccessor(647)
                    level_reserves_tooltip = DynAccessor(648)
                    skill_order_tooltip = DynAccessor(649)

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
                FunRandomModeSubSelector = DynAccessor(650)

            feature = _feature()

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _lobby(DynAccessor):
                __slots__ = ()
                battle_results = DynAccessor(651)
                hangar = DynAccessor(652)
                progression = DynAccessor(653)
                rewards = DynAccessor(654)
                tier_list = DynAccessor(655)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    battle_results_economic_tooltip = DynAccessor(656)
                    entry_point_tooltip = DynAccessor(657)
                    loot_box_tooltip = DynAccessor(658)
                    progression_tooltip = DynAccessor(659)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    fun_random = _fun_random()

    class _halloween(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            MembersWindow = DynAccessor(660)

        lobby = _lobby()

        class _mono(DynAccessor):
            __slots__ = ()

            class _battle(DynAccessor):
                __slots__ = ()
                battle_loading = DynAccessor(661)
                help = DynAccessor(662)
                tab_screen = DynAccessor(663)

            battle = _battle()

            class _lobby(DynAccessor):
                __slots__ = ()
                ammunition_setup = DynAccessor(664)
                attachments_reward_view = DynAccessor(665)
                battle_result = DynAccessor(666)
                bundles_shop = DynAccessor(667)
                comparison = DynAccessor(668)
                crew_showcase = DynAccessor(669)
                decrypt = DynAccessor(670)
                difficulty_congrat = DynAccessor(671)
                hangar = DynAccessor(672)
                king_reward_congrat = DynAccessor(673)
                meta_intro = DynAccessor(674)

                class _notifications(DynAccessor):
                    __slots__ = ()
                    crew_reward_notification = DynAccessor(675)

                notifications = _notifications()
                pre_battle_queue_view = DynAccessor(676)
                promo = DynAccessor(677)
                reward_path = DynAccessor(678)
                reward_selection = DynAccessor(679)

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    ability_tooltip = DynAccessor(680)
                    banner_tooltip = DynAccessor(681)
                    daily_quests_tooltip = DynAccessor(682)
                    difficulty_tooltip = DynAccessor(683)
                    key_tooltip = DynAccessor(684)
                    mission_tooltip = DynAccessor(685)
                    simple_format_tooltip = DynAccessor(686)

                tooltips = _tooltips()

            lobby = _lobby()

        mono = _mono()

    halloween = _halloween()

    class _resource_well(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()

            class _feature(DynAccessor):
                __slots__ = ()
                AwardView = DynAccessor(687)
                CompletedProgressionView = DynAccessor(688)
                EntryPoint = DynAccessor(689)
                NoSerialVehiclesConfirm = DynAccessor(690)
                NoVehiclesConfirm = DynAccessor(691)
                ProgressionView = DynAccessor(692)
                ResourcesLoadingConfirm = DynAccessor(693)
                ResourcesLoadingView = DynAccessor(694)

                class _sharedComponents(DynAccessor):
                    __slots__ = ()

                    class _award(DynAccessor):
                        __slots__ = ()
                        AdditionalReward = DynAccessor(695)
                        Footer = DynAccessor(696)
                        Header = DynAccessor(697)
                        Reward = DynAccessor(698)

                    award = _award()
                    Counter = DynAccessor(699)
                    NoVehiclesState = DynAccessor(700)
                    Resource = DynAccessor(701)
                    VehicleCount = DynAccessor(702)
                    VehicleInfo = DynAccessor(703)

                sharedComponents = _sharedComponents()

                class _tooltips(DynAccessor):
                    __slots__ = ()
                    EntryPointTooltip = DynAccessor(704)
                    MaxProgressTooltip = DynAccessor(705)
                    ProgressTooltip = DynAccessor(706)
                    RefundResourcesTooltip = DynAccessor(707)
                    SerialNumberTooltip = DynAccessor(708)

                tooltips = _tooltips()
                WellPanel = DynAccessor(709)

            feature = _feature()

        lobby = _lobby()

    resource_well = _resource_well()

    class _server_side_replay(DynAccessor):
        __slots__ = ()

        class _lobby(DynAccessor):
            __slots__ = ()
            MetaReplaysView = DynAccessor(710)

            class _popovers(DynAccessor):
                __slots__ = ()
                ReplaysFilterPopover = DynAccessor(711)

            popovers = _popovers()

        lobby = _lobby()

    server_side_replay = _server_side_replay()

    class _story_mode(DynAccessor):
        __slots__ = ()

        class _battle(DynAccessor):
            __slots__ = ()
            EpilogueWindow = DynAccessor(712)
            OnboardingBattleResultView = DynAccessor(713)
            PrebattleWindow = DynAccessor(714)

        battle = _battle()

        class _common(DynAccessor):
            __slots__ = ()
            BadgeTooltip = DynAccessor(715)
            CongratulationsWindow = DynAccessor(716)
            MedalTooltip = DynAccessor(717)
            OnboardingQueueView = DynAccessor(718)

        common = _common()

        class _lobby(DynAccessor):
            __slots__ = ()
            BattleResultStatTooltip = DynAccessor(719)
            BattleResultView = DynAccessor(720)
            DifficultyTooltip = DynAccessor(721)
            EventBannerTooltip = DynAccessor(722)
            EventWelcomeView = DynAccessor(723)
            MissionSelectionView = DynAccessor(724)
            MissionTooltip = DynAccessor(725)
            NewbieAdvertisingView = DynAccessor(726)
            NewbieBannerTooltip = DynAccessor(727)

        lobby = _lobby()

    story_mode = _story_mode()
    Anchor = DynAccessor(728)

    class _child_views_demo(DynAccessor):
        __slots__ = ()
        ChildDemoView = DynAccessor(729)
        MainView = DynAccessor(730)

    child_views_demo = _child_views_demo()
    Comp7DemoPageView = DynAccessor(731)
    ComponentsDemo = DynAccessor(732)
    DataLayerDemoView = DynAccessor(733)
    DataTrackerDemo = DynAccessor(734)
    DeathCamDemoView = DynAccessor(735)
    DemoContextMenu = DynAccessor(736)
    Easings = DynAccessor(737)
    GameLoadingDebugView = DynAccessor(738)
    GFCharset = DynAccessor(739)
    GFComponents = DynAccessor(740)
    GFDemoPopover = DynAccessor(741)
    GFDemoRichTooltipWindow = DynAccessor(742)
    GFDemoWindow = DynAccessor(743)
    GFHooksDemo = DynAccessor(744)
    GFInjectView = DynAccessor(745)
    GFInputCases = DynAccessor(746)
    GFSimpleTooltipWindow = DynAccessor(747)
    GFWebSubDemoWindow = DynAccessor(748)

    class _gf_dialogs_demo(DynAccessor):
        __slots__ = ()
        DefaultDialogProxy = DynAccessor(749)
        GFDialogsDemo = DynAccessor(750)

        class _sub_views(DynAccessor):
            __slots__ = ()
            DummyContent = DynAccessor(751)
            DummyFooter = DynAccessor(752)
            DummyIcon = DynAccessor(753)
            DummyStepper = DynAccessor(754)
            DummyTitle = DynAccessor(755)
            DummyTopRight = DynAccessor(756)

        sub_views = _sub_views()

    gf_dialogs_demo = _gf_dialogs_demo()

    class _gf_viewer(DynAccessor):
        __slots__ = ()
        GFViewerWindow = DynAccessor(757)

    gf_viewer = _gf_viewer()

    class _igb_demo(DynAccessor):
        __slots__ = ()
        BrowserFullscreenWindow = DynAccessor(758)
        BrowserWindow = DynAccessor(759)
        MainView = DynAccessor(760)

    igb_demo = _igb_demo()
    LocaleDemo = DynAccessor(761)
    MediaWrapperDemo = DynAccessor(762)
    MixBlendMode = DynAccessor(763)
    MixBlendModeAnimation = DynAccessor(764)
    ModeSelectorDemo = DynAccessor(765)
    ModeSelectorToolsetView = DynAccessor(766)
    ParallaxExample = DynAccessor(771)
    ParallaxViewer = DynAccessor(772)
    PluralLocView = DynAccessor(773)
    PropsSupportDemo = DynAccessor(774)
    ReactSpringVizualizer = DynAccessor(775)
    SelectableRewardDemoView = DynAccessor(776)
    StructuralDataBindDemo = DynAccessor(777)

    class _sub_views_demo(DynAccessor):
        __slots__ = ()
        GFSubViewsDemo = DynAccessor(778)

        class _sub_views(DynAccessor):
            __slots__ = ()
            CustomizationCartProxy = DynAccessor(779)
            DailyProxy = DynAccessor(780)
            ProgressiveItemsViewProxy = DynAccessor(781)

        sub_views = _sub_views()

    sub_views_demo = _sub_views_demo()
    UILoggerDemo = DynAccessor(782)
    VideoSupportView = DynAccessor(783)
    W2CTestPageWindow = DynAccessor(784)
    WgcgMockView = DynAccessor(785)