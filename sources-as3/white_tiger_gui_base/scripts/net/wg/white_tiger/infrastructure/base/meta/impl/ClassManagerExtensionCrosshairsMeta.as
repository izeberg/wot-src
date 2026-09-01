package net.wg.white_tiger.infrastructure.base.meta.impl
{
   import net.wg.gui.components.crosshairPanel.CrosshairArcade;
   import net.wg.gui.components.crosshairPanel.CrosshairAverageDamageContainer;
   import net.wg.gui.components.crosshairPanel.CrosshairAverageDamageField;
   import net.wg.gui.components.crosshairPanel.CrosshairBase;
   import net.wg.gui.components.crosshairPanel.CrosshairDistanceContainer;
   import net.wg.gui.components.crosshairPanel.CrosshairDistanceField;
   import net.wg.gui.components.crosshairPanel.CrosshairNetSeparator;
   import net.wg.gui.components.crosshairPanel.CrosshairPanelContainer;
   import net.wg.gui.components.crosshairPanel.CrosshairPanelEvent;
   import net.wg.gui.components.crosshairPanel.CrosshairPanelSniperCameraTransitionFx;
   import net.wg.gui.components.crosshairPanel.CrosshairPostmortem;
   import net.wg.gui.components.crosshairPanel.CrosshairSniper;
   import net.wg.gui.components.crosshairPanel.CrosshairStrategic;
   import net.wg.gui.components.crosshairPanel.CrosshairWithCassette;
   import net.wg.gui.components.crosshairPanel.GunMarkersManager;
   import net.wg.gui.components.crosshairPanel.ICrosshair;
   import net.wg.gui.components.crosshairPanel.ICrosshairPanelContainer;
   import net.wg.gui.components.crosshairPanel.VO.CrosshairSettingsVO;
   import net.wg.gui.components.crosshairPanel.VO.GunMarkerIndicatorVO;
   import net.wg.gui.components.crosshairPanel.VO.ShotFlyTimeVO;
   import net.wg.gui.components.crosshairPanel.components.CrosshairClipQuantityBar;
   import net.wg.gui.components.crosshairPanel.components.CrosshairClipQuantityBarContainer;
   import net.wg.gui.components.crosshairPanel.components.artyScale.ArtyIndicationScale;
   import net.wg.gui.components.crosshairPanel.components.artyShot.ArtyShotIndicator;
   import net.wg.gui.components.crosshairPanel.components.artyShot.ArtyShotIndicatorText;
   import net.wg.gui.components.crosshairPanel.components.artyShot.ArtyShotIndicatorsPanel;
   import net.wg.gui.components.crosshairPanel.components.autoloader.AutoloaderIndicator;
   import net.wg.gui.components.crosshairPanel.components.autoloader.AutoloaderShellsCassette;
   import net.wg.gui.components.crosshairPanel.components.autoloader.AutoloaderTimer;
   import net.wg.gui.components.crosshairPanel.components.autoloader.AutoloaderTimerText;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicator;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorElement;
   import net.wg.gui.components.crosshairPanel.components.autoloader.BoostIndicatorStateParamsVO;
   import net.wg.gui.components.crosshairPanel.components.controllableLoader.ControllableReloadCassette;
   import net.wg.gui.components.crosshairPanel.components.controllableLoader.ControllableReloadShellProgressBar;
   import net.wg.gui.components.crosshairPanel.components.extraShotClip.ExtraShotClipBar;
   import net.wg.gui.components.crosshairPanel.components.extraShotClip.ExtraShotClipCursor;
   import net.wg.gui.components.crosshairPanel.components.extraShotClip.ExtraShotClipPanel;
   import net.wg.gui.components.crosshairPanel.components.extraShotClip.ExtraShotShellProgressBar;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.AccuracyGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.AccuracyGunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.ChargeGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.ChargeGunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.DualGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.DualGunMarkerDebug;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerAimDamage;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerArtillery;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerDebug;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerDebugStrategic;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixing;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingAccuracyGun;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingChargeGun;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingChargeableBurst;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingDualGun;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingDualGunSniper;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingSolid;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingStepPoints;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingTwinGun;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerMixingWithoutProgress;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerStrategic;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.GunMarkerTag;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.IGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.IGunMarkerDispersion;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.IGunMarkerMixing;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.PenetrationFX;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.TwinGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.TwinGunMarkerDebug;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.TwinGunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.ZoomingAimDamage;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher.AuxiliaryRocketLauncherGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher.AuxiliaryRocketLauncherGunMarkerDebug;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher.AuxiliaryRocketLauncherGunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher.AuxiliaryRocketLauncherGunMarkerTag;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher.AuxiliaryRocketLauncherGunMarkerTagClip;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.auxiliaryRocketLauncher.IAuxiliaryRocketLauncherGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.constants.GunMarkerConsts;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.ColorsProvider;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotGunMarker;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotGunMarkerDispersionCircle;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotGunMarkerMixing;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotReloadController;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.LowChargeShotReloadEvent;
   import net.wg.gui.components.crosshairPanel.components.gunMarker.lowChargeShot.MarkerDrawer;
   import net.wg.gui.components.crosshairPanel.components.gunStack.ReloadBoostBorder;
   import net.wg.gui.components.crosshairPanel.components.shared.ShellProgressBar;
   import net.wg.gui.components.crosshairPanel.components.shellCalibrationClip.ShellCalibrationClipBar;
   import net.wg.gui.components.crosshairPanel.components.shellCalibrationClip.ShellCalibrationClipPanel;
   import net.wg.gui.components.crosshairPanel.components.shellCalibrationClip.ShellCalibrationProgressBar;
   import net.wg.gui.components.crosshairPanel.components.shellCalibrationClip.ShellCalibrationState;
   import net.wg.gui.components.crosshairPanel.components.speedometer.Speedometer;
   import net.wg.gui.components.crosshairPanel.components.speedometer.SpeedometerWarningAnim;
   import net.wg.gui.components.crosshairPanel.constants.CrosshairConsts;
   import net.wg.white_tiger.gui.components.crosshairPanel.ArcadePlasmaIndicator;
   import net.wg.white_tiger.gui.components.crosshairPanel.BasePlasmaIndicator;
   import net.wg.white_tiger.gui.components.crosshairPanel.IWhiteTigerCrosshair;
   import net.wg.white_tiger.gui.components.crosshairPanel.PlasmaDamageTF;
   import net.wg.white_tiger.gui.components.crosshairPanel.SniperPlasmaIndicator;
   import net.wg.white_tiger.gui.components.crosshairPanel.WhiteTigerCrosshairArcade;
   import net.wg.white_tiger.gui.components.crosshairPanel.WhiteTigerCrosshairPanelContainer;
   import net.wg.white_tiger.gui.components.crosshairPanel.WhiteTigerCrosshairSniper;
   import net.wg.white_tiger.gui.components.crosshairPanel.WhiteTigerGunMarkerDispersionCircle;
   
   public class ClassManagerExtensionCrosshairsMeta
   {
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_ARCADEPLASMAINDICATOR:Class = ArcadePlasmaIndicator;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_BASEPLASMAINDICATOR:Class = BasePlasmaIndicator;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_IWHITETIGERCROSSHAIR:Class = IWhiteTigerCrosshair;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_PLASMADAMAGETF:Class = PlasmaDamageTF;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_SNIPERPLASMAINDICATOR:Class = SniperPlasmaIndicator;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_WHITETIGERCROSSHAIRARCADE:Class = WhiteTigerCrosshairArcade;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_WHITETIGERCROSSHAIRPANELCONTAINER:Class = WhiteTigerCrosshairPanelContainer;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_WHITETIGERCROSSHAIRSNIPER:Class = WhiteTigerCrosshairSniper;
      
      public static const NET_WG_WHITE_TIGER_GUI_COMPONENTS_CROSSHAIRPANEL_WHITETIGERGUNMARKERDISPERSIONCIRCLE:Class = WhiteTigerGunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRARCADE:Class = CrosshairArcade;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRAVERAGEDAMAGECONTAINER:Class = CrosshairAverageDamageContainer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRAVERAGEDAMAGEFIELD:Class = CrosshairAverageDamageField;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRBASE:Class = CrosshairBase;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRDISTANCECONTAINER:Class = CrosshairDistanceContainer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRDISTANCEFIELD:Class = CrosshairDistanceField;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRNETSEPARATOR:Class = CrosshairNetSeparator;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRPANELCONTAINER:Class = CrosshairPanelContainer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRPANELEVENT:Class = CrosshairPanelEvent;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRPANELSNIPERCAMERATRANSITIONFX:Class = CrosshairPanelSniperCameraTransitionFx;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRPOSTMORTEM:Class = CrosshairPostmortem;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRSNIPER:Class = CrosshairSniper;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRSTRATEGIC:Class = CrosshairStrategic;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CROSSHAIRWITHCASSETTE:Class = CrosshairWithCassette;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_GUNMARKERSMANAGER:Class = GunMarkersManager;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_ICROSSHAIR:Class = ICrosshair;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_ICROSSHAIRPANELCONTAINER:Class = ICrosshairPanelContainer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_CROSSHAIRCLIPQUANTITYBAR:Class = CrosshairClipQuantityBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_CROSSHAIRCLIPQUANTITYBARCONTAINER:Class = CrosshairClipQuantityBarContainer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_ARTYSCALE_ARTYINDICATIONSCALE:Class = ArtyIndicationScale;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_ARTYSHOT_ARTYSHOTINDICATOR:Class = ArtyShotIndicator;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_ARTYSHOT_ARTYSHOTINDICATORSPANEL:Class = ArtyShotIndicatorsPanel;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_ARTYSHOT_ARTYSHOTINDICATORTEXT:Class = ArtyShotIndicatorText;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_AUTOLOADERINDICATOR:Class = AutoloaderIndicator;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_AUTOLOADERSHELLSCASSETTE:Class = AutoloaderShellsCassette;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_AUTOLOADERTIMER:Class = AutoloaderTimer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_AUTOLOADERTIMERTEXT:Class = AutoloaderTimerText;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_BOOSTINDICATOR:Class = BoostIndicator;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_BOOSTINDICATORELEMENT:Class = BoostIndicatorElement;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_AUTOLOADER_BOOSTINDICATORSTATEPARAMSVO:Class = BoostIndicatorStateParamsVO;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_CONTROLLABLELOADER_CONTROLLABLERELOADCASSETTE:Class = ControllableReloadCassette;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_CONTROLLABLELOADER_CONTROLLABLERELOADSHELLPROGRESSBAR:Class = ControllableReloadShellProgressBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_EXTRASHOTCLIP_EXTRASHOTCLIPBAR:Class = ExtraShotClipBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_EXTRASHOTCLIP_EXTRASHOTCLIPCURSOR:Class = ExtraShotClipCursor;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_EXTRASHOTCLIP_EXTRASHOTCLIPPANEL:Class = ExtraShotClipPanel;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_EXTRASHOTCLIP_EXTRASHOTSHELLPROGRESSBAR:Class = ExtraShotShellProgressBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_ACCURACYGUNMARKER:Class = AccuracyGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_ACCURACYGUNMARKERDISPERSIONCIRCLE:Class = AccuracyGunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_CHARGEGUNMARKER:Class = ChargeGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_CHARGEGUNMARKERDISPERSIONCIRCLE:Class = ChargeGunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_DUALGUNMARKER:Class = DualGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_DUALGUNMARKERDEBUG:Class = DualGunMarkerDebug;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKER:Class = GunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERAIMDAMAGE:Class = GunMarkerAimDamage;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERARTILLERY:Class = GunMarkerArtillery;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERDEBUG:Class = GunMarkerDebug;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERDEBUGSTRATEGIC:Class = GunMarkerDebugStrategic;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERDISPERSIONCIRCLE:Class = GunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXING:Class = GunMarkerMixing;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGACCURACYGUN:Class = GunMarkerMixingAccuracyGun;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGCHARGEABLEBURST:Class = GunMarkerMixingChargeableBurst;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGCHARGEGUN:Class = GunMarkerMixingChargeGun;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGDUALGUN:Class = GunMarkerMixingDualGun;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGDUALGUNSNIPER:Class = GunMarkerMixingDualGunSniper;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGSOLID:Class = GunMarkerMixingSolid;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGSTEPPOINTS:Class = GunMarkerMixingStepPoints;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGTWINGUN:Class = GunMarkerMixingTwinGun;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERMIXINGWITHOUTPROGRESS:Class = GunMarkerMixingWithoutProgress;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERSTRATEGIC:Class = GunMarkerStrategic;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_GUNMARKERTAG:Class = GunMarkerTag;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_IGUNMARKER:Class = IGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_IGUNMARKERDISPERSION:Class = IGunMarkerDispersion;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_IGUNMARKERMIXING:Class = IGunMarkerMixing;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_PENETRATIONFX:Class = PenetrationFX;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_TWINGUNMARKER:Class = TwinGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_TWINGUNMARKERDEBUG:Class = TwinGunMarkerDebug;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_TWINGUNMARKERDISPERSIONCIRCLE:Class = TwinGunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_ZOOMINGAIMDAMAGE:Class = ZoomingAimDamage;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_AUXILIARYROCKETLAUNCHER_AUXILIARYROCKETLAUNCHERGUNMARKER:Class = AuxiliaryRocketLauncherGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_AUXILIARYROCKETLAUNCHER_AUXILIARYROCKETLAUNCHERGUNMARKERDEBUG:Class = AuxiliaryRocketLauncherGunMarkerDebug;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_AUXILIARYROCKETLAUNCHER_AUXILIARYROCKETLAUNCHERGUNMARKERDISPERSIONCIRCLE:Class = AuxiliaryRocketLauncherGunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_AUXILIARYROCKETLAUNCHER_AUXILIARYROCKETLAUNCHERGUNMARKERTAG:Class = AuxiliaryRocketLauncherGunMarkerTag;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_AUXILIARYROCKETLAUNCHER_AUXILIARYROCKETLAUNCHERGUNMARKERTAGCLIP:Class = AuxiliaryRocketLauncherGunMarkerTagClip;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_AUXILIARYROCKETLAUNCHER_IAUXILIARYROCKETLAUNCHERGUNMARKER:Class = IAuxiliaryRocketLauncherGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_CONSTANTS_GUNMARKERCONSTS:Class = GunMarkerConsts;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_COLORSPROVIDER:Class = ColorsProvider;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_LOWCHARGESHOTGUNMARKER:Class = LowChargeShotGunMarker;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_LOWCHARGESHOTGUNMARKERDISPERSIONCIRCLE:Class = LowChargeShotGunMarkerDispersionCircle;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_LOWCHARGESHOTGUNMARKERMIXING:Class = LowChargeShotGunMarkerMixing;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_LOWCHARGESHOTRELOADCONTROLLER:Class = LowChargeShotReloadController;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_LOWCHARGESHOTRELOADEVENT:Class = LowChargeShotReloadEvent;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNMARKER_LOWCHARGESHOT_MARKERDRAWER:Class = MarkerDrawer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_GUNSTACK_RELOADBOOSTBORDER:Class = ReloadBoostBorder;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SHARED_SHELLPROGRESSBAR:Class = ShellProgressBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SHELLCALIBRATIONCLIP_SHELLCALIBRATIONCLIPBAR:Class = ShellCalibrationClipBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SHELLCALIBRATIONCLIP_SHELLCALIBRATIONCLIPPANEL:Class = ShellCalibrationClipPanel;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SHELLCALIBRATIONCLIP_SHELLCALIBRATIONPROGRESSBAR:Class = ShellCalibrationProgressBar;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SHELLCALIBRATIONCLIP_SHELLCALIBRATIONSTATE:Class = ShellCalibrationState;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SPEEDOMETER_SPEEDOMETER:Class = Speedometer;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_COMPONENTS_SPEEDOMETER_SPEEDOMETERWARNINGANIM:Class = SpeedometerWarningAnim;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_CONSTANTS_CROSSHAIRCONSTS:Class = CrosshairConsts;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_VO_CROSSHAIRSETTINGSVO:Class = CrosshairSettingsVO;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_VO_GUNMARKERINDICATORVO:Class = GunMarkerIndicatorVO;
      
      public static const NET_WG_GUI_COMPONENTS_CROSSHAIRPANEL_VO_SHOTFLYTIMEVO:Class = ShotFlyTimeVO;
       
      
      public function ClassManagerExtensionCrosshairsMeta()
      {
         super();
      }
   }
}
