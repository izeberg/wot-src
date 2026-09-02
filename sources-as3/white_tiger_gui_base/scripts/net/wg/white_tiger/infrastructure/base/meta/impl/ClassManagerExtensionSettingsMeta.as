package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.gui.lobby.settings.AdvancedGraphicContentForm;
   import net.wg.gui.lobby.settings.AdvancedGraphicSettingsForm;
   import net.wg.gui.lobby.settings.AimSettings;
   import net.wg.gui.lobby.settings.AimSettingsBase;
   import net.wg.gui.lobby.settings.ArmorFlashlightContent;
   import net.wg.gui.lobby.settings.ControlsSettings;
   import net.wg.gui.lobby.settings.ControlsSettingsBase;
   import net.wg.gui.lobby.settings.DisabledTabsOverlay;
   import net.wg.gui.lobby.settings.GameSettings;
   import net.wg.gui.lobby.settings.GameSettingsContent;
   import net.wg.gui.lobby.settings.GraphicSettings;
   import net.wg.gui.lobby.settings.GraphicSettingsBase;
   import net.wg.gui.lobby.settings.ISettingsAimForm;
   import net.wg.gui.lobby.settings.MarkerSettings;
   import net.wg.gui.lobby.settings.MarkerSettingsBase;
   import net.wg.gui.lobby.settings.ScreenSettingsForm;
   import net.wg.gui.lobby.settings.SettingsArcadeForm;
   import net.wg.gui.lobby.settings.SettingsArmorFlashlightForm;
   import net.wg.gui.lobby.settings.SettingsArtyForm;
   import net.wg.gui.lobby.settings.SettingsBaseView;
   import net.wg.gui.lobby.settings.SettingsChangesMap;
   import net.wg.gui.lobby.settings.SettingsContourForm;
   import net.wg.gui.lobby.settings.SettingsMarkersForm;
   import net.wg.gui.lobby.settings.SettingsNewCountersForm;
   import net.wg.gui.lobby.settings.SettingsSniperForm;
   import net.wg.gui.lobby.settings.SettingsWindow;
   import net.wg.gui.lobby.settings.SoundCommonForm;
   import net.wg.gui.lobby.settings.SoundSettings;
   import net.wg.gui.lobby.settings.SoundSettingsBase;
   import net.wg.gui.lobby.settings.SoundSpecialForm;
   import net.wg.gui.lobby.settings.SoundVivoxForm;
   import net.wg.gui.lobby.settings.components.KeyInput;
   import net.wg.gui.lobby.settings.components.KeysItemRenderer;
   import net.wg.gui.lobby.settings.components.KeysScrollingList;
   import net.wg.gui.lobby.settings.components.LimitedUISettingBlock;
   import net.wg.gui.lobby.settings.components.RadioButtonBar;
   import net.wg.gui.lobby.settings.components.SettingsStepSlider;
   import net.wg.gui.lobby.settings.components.SoundDeviceButtonBar;
   import net.wg.gui.lobby.settings.components.SoundDeviceTabButton;
   import net.wg.gui.lobby.settings.components.SoundVoiceWaves;
   import net.wg.gui.lobby.settings.components.evnts.KeyInputEvents;
   import net.wg.gui.lobby.settings.components.evnts.LimitedUIEvent;
   import net.wg.gui.lobby.settings.config.ControlsFactory;
   import net.wg.gui.lobby.settings.config.SettingsConfigHelper;
   import net.wg.gui.lobby.settings.events.AlternativeVoiceEvent;
   import net.wg.gui.lobby.settings.events.SettingViewEvent;
   import net.wg.gui.lobby.settings.events.SettingsGroupEvent;
   import net.wg.gui.lobby.settings.events.SettingsSubVewEvent;
   import net.wg.gui.lobby.settings.feedback.FeedbackBaseForm;
   import net.wg.gui.lobby.settings.feedback.FeedbackSettings;
   import net.wg.gui.lobby.settings.feedback.borderMap.BattleBorderMapBorderContainer;
   import net.wg.gui.lobby.settings.feedback.borderMap.BattleBorderMapForm;
   import net.wg.gui.lobby.settings.feedback.damageIndicator.DamageIndicatorExtended;
   import net.wg.gui.lobby.settings.feedback.damageIndicator.DamageIndicatorForm;
   import net.wg.gui.lobby.settings.feedback.damageIndicator.DamageIndicatorsContainer;
   import net.wg.gui.lobby.settings.feedback.damageLog.DamageLogPanelForm;
   import net.wg.gui.lobby.settings.feedback.damageLog.ScreenSizeAlert;
   import net.wg.gui.lobby.settings.feedback.damageLog.data.SettingsDamageLogData;
   import net.wg.gui.lobby.settings.feedback.questsProgress.QuestsProgressControls;
   import net.wg.gui.lobby.settings.feedback.questsProgress.QuestsProgressForm;
   import net.wg.gui.lobby.settings.feedback.questsProgress.ScorePanelControls;
   import net.wg.gui.lobby.settings.feedback.ribbons.BattleEfficiencyControlsGroupContent;
   import net.wg.gui.lobby.settings.feedback.ribbons.BattleRibbonsForm;
   import net.wg.gui.lobby.settings.feedback.ribbons.ControlsContainer;
   import net.wg.gui.lobby.settings.feedback.ribbons.ControlsGroup;
   import net.wg.gui.lobby.settings.feedback.ribbons.CrewPerksGroupContent;
   import net.wg.gui.lobby.settings.feedback.ribbons.DamageControlsGroupContent;
   import net.wg.gui.lobby.settings.feedback.ribbons.GroupContent;
   import net.wg.gui.lobby.settings.feedback.ribbons.InfoView;
   import net.wg.gui.lobby.settings.feedback.ribbons.SettingsRibbonContainer;
   import net.wg.gui.lobby.settings.feedback.ribbons.SettingsRibbonItem;
   import net.wg.gui.lobby.settings.feedback.ribbons.data.RibbonItemData;
   import net.wg.gui.lobby.settings.vo.AnonymizerExtraVO;
   import net.wg.gui.lobby.settings.vo.CheckboxVo;
   import net.wg.gui.lobby.settings.vo.ColorFilerSettingsVo;
   import net.wg.gui.lobby.settings.vo.CursorTabsDataVo;
   import net.wg.gui.lobby.settings.vo.DevMapsVO;
   import net.wg.gui.lobby.settings.vo.IncreaseEffectsContrastVO;
   import net.wg.gui.lobby.settings.vo.MarkerTabsDataVo;
   import net.wg.gui.lobby.settings.vo.SettingsControlProp;
   import net.wg.gui.lobby.settings.vo.SettingsKeyProp;
   import net.wg.gui.lobby.settings.vo.SettingsNewCountersVo;
   import net.wg.gui.lobby.settings.vo.SettingsTabNewCounterVo;
   import net.wg.gui.lobby.settings.vo.SettingsViewData;
   import net.wg.gui.lobby.settings.vo.SimpleExtraVO;
   import net.wg.gui.lobby.settings.vo.TabsDataVo;
   import net.wg.gui.lobby.settings.vo.VisitedCounters;
   import net.wg.gui.lobby.settings.vo.base.SettingsDataIncomeVo;
   import net.wg.gui.lobby.settings.vo.base.SettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.ControlsSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.FeedbackSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.GameSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.GraphicSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.SettingConfigDataVo;
   import net.wg.gui.lobby.settings.vo.config.SoundSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsArcadeDataVo;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsArmorFlashlightDataVo;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsArtyDataVo;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsContourDataVo;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.aim.AimSettingsSniperDataVo;
   import net.wg.gui.lobby.settings.vo.config.feedback.BattleBorderMapDataVo;
   import net.wg.gui.lobby.settings.vo.config.feedback.BattleEventInfoDataVo;
   import net.wg.gui.lobby.settings.vo.config.feedback.DamageIndicatorDataVo;
   import net.wg.gui.lobby.settings.vo.config.feedback.DamageLogPanelDataVo;
   import net.wg.gui.lobby.settings.vo.config.feedback.QuestsProgressDataVo;
   import net.wg.gui.lobby.settings.vo.config.marker.MarkerAllySettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.marker.MarkerDeadSettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.marker.MarkerEnemySettingsDataVo;
   import net.wg.gui.lobby.settings.vo.config.marker.MarkerSettingsDataVo;
   import net.wg.white_tiger.gui.lobby.settings.WhiteTigerSettingsWindow;
   import net.wg.white_tiger.gui.lobby.settings.components.SettingLabel;
   
   public class ClassManagerExtensionSettingsMeta
   {
      
      public static const NET_WG_WHITE_TIGER_GUI_LOBBY_SETTINGS_WHITETIGERSETTINGSWINDOW:Class = WhiteTigerSettingsWindow;
      
      public static const NET_WG_WHITE_TIGER_GUI_LOBBY_SETTINGS_COMPONENTS_SETTINGLABEL:Class = SettingLabel;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_ADVANCEDGRAPHICCONTENTFORM:Class = AdvancedGraphicContentForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_ADVANCEDGRAPHICSETTINGSFORM:Class = AdvancedGraphicSettingsForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_AIMSETTINGS:Class = AimSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_AIMSETTINGSBASE:Class = AimSettingsBase;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_ARMORFLASHLIGHTCONTENT:Class = ArmorFlashlightContent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_CONTROLSSETTINGS:Class = ControlsSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_CONTROLSSETTINGSBASE:Class = ControlsSettingsBase;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_DISABLEDTABSOVERLAY:Class = DisabledTabsOverlay;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_GAMESETTINGS:Class = GameSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_GAMESETTINGSCONTENT:Class = GameSettingsContent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_GRAPHICSETTINGS:Class = GraphicSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_GRAPHICSETTINGSBASE:Class = GraphicSettingsBase;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_ISETTINGSAIMFORM:Class = ISettingsAimForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_MARKERSETTINGS:Class = MarkerSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_MARKERSETTINGSBASE:Class = MarkerSettingsBase;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SCREENSETTINGSFORM:Class = ScreenSettingsForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSARCADEFORM:Class = SettingsArcadeForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSARMORFLASHLIGHTFORM:Class = SettingsArmorFlashlightForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSARTYFORM:Class = SettingsArtyForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSBASEVIEW:Class = SettingsBaseView;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSCHANGESMAP:Class = SettingsChangesMap;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSCONTOURFORM:Class = SettingsContourForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSMARKERSFORM:Class = SettingsMarkersForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSNEWCOUNTERSFORM:Class = SettingsNewCountersForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSSNIPERFORM:Class = SettingsSniperForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SETTINGSWINDOW:Class = SettingsWindow;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SOUNDCOMMONFORM:Class = SoundCommonForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SOUNDSETTINGS:Class = SoundSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SOUNDSETTINGSBASE:Class = SoundSettingsBase;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SOUNDSPECIALFORM:Class = SoundSpecialForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_SOUNDVIVOXFORM:Class = SoundVivoxForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_KEYINPUT:Class = KeyInput;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_KEYSITEMRENDERER:Class = KeysItemRenderer;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_KEYSSCROLLINGLIST:Class = KeysScrollingList;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_LIMITEDUISETTINGBLOCK:Class = LimitedUISettingBlock;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_RADIOBUTTONBAR:Class = RadioButtonBar;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_SETTINGSSTEPSLIDER:Class = SettingsStepSlider;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_SOUNDDEVICEBUTTONBAR:Class = SoundDeviceButtonBar;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_SOUNDDEVICETABBUTTON:Class = SoundDeviceTabButton;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_SOUNDVOICEWAVES:Class = SoundVoiceWaves;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_EVNTS_KEYINPUTEVENTS:Class = KeyInputEvents;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_COMPONENTS_EVNTS_LIMITEDUIEVENT:Class = LimitedUIEvent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_CONFIG_CONTROLSFACTORY:Class = ControlsFactory;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_CONFIG_SETTINGSCONFIGHELPER:Class = SettingsConfigHelper;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_EVENTS_ALTERNATIVEVOICEEVENT:Class = AlternativeVoiceEvent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_EVENTS_SETTINGSGROUPEVENT:Class = SettingsGroupEvent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_EVENTS_SETTINGSSUBVEWEVENT:Class = SettingsSubVewEvent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_EVENTS_SETTINGVIEWEVENT:Class = SettingViewEvent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_FEEDBACKBASEFORM:Class = FeedbackBaseForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_FEEDBACKSETTINGS:Class = FeedbackSettings;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_BORDERMAP_BATTLEBORDERMAPBORDERCONTAINER:Class = BattleBorderMapBorderContainer;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_BORDERMAP_BATTLEBORDERMAPFORM:Class = BattleBorderMapForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_DAMAGEINDICATOR_DAMAGEINDICATOREXTENDED:Class = DamageIndicatorExtended;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_DAMAGEINDICATOR_DAMAGEINDICATORFORM:Class = DamageIndicatorForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_DAMAGEINDICATOR_DAMAGEINDICATORSCONTAINER:Class = DamageIndicatorsContainer;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_DAMAGELOG_DAMAGELOGPANELFORM:Class = DamageLogPanelForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_DAMAGELOG_SCREENSIZEALERT:Class = ScreenSizeAlert;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_DAMAGELOG_DATA_SETTINGSDAMAGELOGDATA:Class = SettingsDamageLogData;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_QUESTSPROGRESS_QUESTSPROGRESSCONTROLS:Class = QuestsProgressControls;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_QUESTSPROGRESS_QUESTSPROGRESSFORM:Class = QuestsProgressForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_QUESTSPROGRESS_SCOREPANELCONTROLS:Class = ScorePanelControls;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_BATTLEEFFICIENCYCONTROLSGROUPCONTENT:Class = BattleEfficiencyControlsGroupContent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_BATTLERIBBONSFORM:Class = BattleRibbonsForm;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_CONTROLSCONTAINER:Class = ControlsContainer;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_CONTROLSGROUP:Class = ControlsGroup;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_CREWPERKSGROUPCONTENT:Class = CrewPerksGroupContent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_DAMAGECONTROLSGROUPCONTENT:Class = DamageControlsGroupContent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_GROUPCONTENT:Class = GroupContent;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_INFOVIEW:Class = InfoView;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_SETTINGSRIBBONCONTAINER:Class = SettingsRibbonContainer;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_SETTINGSRIBBONITEM:Class = SettingsRibbonItem;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_FEEDBACK_RIBBONS_DATA_RIBBONITEMDATA:Class = RibbonItemData;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_ANONYMIZEREXTRAVO:Class = AnonymizerExtraVO;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CHECKBOXVO:Class = CheckboxVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_COLORFILERSETTINGSVO:Class = ColorFilerSettingsVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CURSORTABSDATAVO:Class = CursorTabsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_DEVMAPSVO:Class = DevMapsVO;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_INCREASEEFFECTSCONTRASTVO:Class = IncreaseEffectsContrastVO;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_MARKERTABSDATAVO:Class = MarkerTabsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_SETTINGSCONTROLPROP:Class = SettingsControlProp;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_SETTINGSKEYPROP:Class = SettingsKeyProp;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_SETTINGSNEWCOUNTERSVO:Class = SettingsNewCountersVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_SETTINGSTABNEWCOUNTERVO:Class = SettingsTabNewCounterVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_SETTINGSVIEWDATA:Class = SettingsViewData;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_SIMPLEEXTRAVO:Class = SimpleExtraVO;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_TABSDATAVO:Class = TabsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_VISITEDCOUNTERS:Class = VisitedCounters;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_BASE_SETTINGSDATAINCOMEVO:Class = SettingsDataIncomeVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_BASE_SETTINGSDATAVO:Class = SettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_CONTROLSSETTINGSDATAVO:Class = ControlsSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_FEEDBACKSETTINGSDATAVO:Class = FeedbackSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_GAMESETTINGSDATAVO:Class = GameSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_GRAPHICSETTINGSDATAVO:Class = GraphicSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_SETTINGCONFIGDATAVO:Class = SettingConfigDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_SOUNDSETTINGSDATAVO:Class = SoundSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_AIM_AIMSETTINGSARCADEDATAVO:Class = AimSettingsArcadeDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_AIM_AIMSETTINGSARMORFLASHLIGHTDATAVO:Class = AimSettingsArmorFlashlightDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_AIM_AIMSETTINGSARTYDATAVO:Class = AimSettingsArtyDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_AIM_AIMSETTINGSCONTOURDATAVO:Class = AimSettingsContourDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_AIM_AIMSETTINGSDATAVO:Class = AimSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_AIM_AIMSETTINGSSNIPERDATAVO:Class = AimSettingsSniperDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_FEEDBACK_BATTLEBORDERMAPDATAVO:Class = BattleBorderMapDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_FEEDBACK_BATTLEEVENTINFODATAVO:Class = BattleEventInfoDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_FEEDBACK_DAMAGEINDICATORDATAVO:Class = DamageIndicatorDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_FEEDBACK_DAMAGELOGPANELDATAVO:Class = DamageLogPanelDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_FEEDBACK_QUESTSPROGRESSDATAVO:Class = QuestsProgressDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_MARKER_MARKERALLYSETTINGSDATAVO:Class = MarkerAllySettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_MARKER_MARKERDEADSETTINGSDATAVO:Class = MarkerDeadSettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_MARKER_MARKERENEMYSETTINGSDATAVO:Class = MarkerEnemySettingsDataVo;
      
      public static const NET_WG_GUI_LOBBY_SETTINGS_VO_CONFIG_MARKER_MARKERSETTINGSDATAVO:Class = MarkerSettingsDataVo;
       
      
      public function ClassManagerExtensionSettingsMeta()
      {
         super();
      }
   }
}
