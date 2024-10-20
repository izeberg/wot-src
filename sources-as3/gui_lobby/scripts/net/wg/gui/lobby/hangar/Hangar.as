package net.wg.gui.lobby.hangar
{
   import fl.motion.easing.Quadratic;
   import flash.display.DisplayObject;
   import flash.display.InteractiveObject;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.display.Stage;
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.ui.Keyboard;
   import flash.utils.Dictionary;
   import net.wg.data.Aliases;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.BATTLEROYALE_ALIASES;
   import net.wg.data.constants.generated.DAILY_QUESTS_WIDGET_CONSTANTS;
   import net.wg.data.constants.generated.HANGAR_ALIASES;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.gui.components.miniclient.HangarMiniClientComponent;
   import net.wg.gui.events.LobbyEvent;
   import net.wg.gui.lobby.battleRoyale.HangarComponentsContainer;
   import net.wg.gui.lobby.battleRoyale.events.BattleTypeSelectorEvent;
   import net.wg.gui.lobby.hangar.alertMessage.AlertMessageBlock;
   import net.wg.gui.lobby.hangar.ammunitionPanel.AmmunitionPanel;
   import net.wg.gui.lobby.hangar.ammunitionPanel.data.AmmunitionPanelVO;
   import net.wg.gui.lobby.hangar.ammunitionPanelInject.AmmunitionPanelInject;
   import net.wg.gui.lobby.hangar.ammunitionPanelInject.events.AmmunitionPanelInjectEvents;
   import net.wg.gui.lobby.hangar.eventEntryPoint.HangarEventEntriesContainer;
   import net.wg.gui.lobby.hangar.interfaces.IHangar;
   import net.wg.gui.lobby.hangar.interfaces.IVehicleParameters;
   import net.wg.gui.lobby.hangar.tcarousel.TankCarousel;
   import net.wg.gui.lobby.post.Teaser;
   import net.wg.gui.lobby.post.TeaserEvent;
   import net.wg.gui.lobby.post.data.TeaserVO;
   import net.wg.gui.notification.events.NotificationLayoutEvent;
   import net.wg.gui.tutorial.components.TutorialClip;
   import net.wg.infrastructure.base.meta.impl.HangarMeta;
   import net.wg.infrastructure.events.FocusRequestEvent;
   import net.wg.infrastructure.interfaces.ITutorialCustomComponent;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.utils.IGameInputManager;
   import net.wg.utils.IUtils;
   import net.wg.utils.StageSizeBoundaries;
   import net.wg.utils.helpLayout.IHelpLayout;
   import scaleform.clik.events.ComponentEvent;
   import scaleform.clik.events.InputEvent;
   import scaleform.clik.motion.Tween;
   import scaleform.clik.ui.InputDetails;
   
   public class Hangar extends HangarMeta implements IHangar, ITutorialCustomComponent
   {
      
      private static const INVALIDATE_CAROUSEL_SIZE:String = "InvalidateCarouselSize";
      
      private static const INVALIDATE_AMMUNITION_PANEL_SIZE:String = "InvalidateAmmunitionPanelSize";
      
      private static const INVALIDATE_EVENT_LOOT_BOXES_VISIBLE:String = "invalidateEventLootBoxesVisible";
      
      private static const INVALIDATE_COMP7_MODIFIERS_VISIBILITY:String = "invalidComp7Modifiers";
      
      private static const INVALIDATE_CAROUSEL_BANNER_VISIBILITY:String = "invalidCarouselBanner";
      
      private static const INVALIDATE_PRESTIGE_WIDGET_VISIBILITY:String = "invalidPrestigeProgress";
      
      private static const INVALIDATE_HEADER_ANIMATION:String = "invalidHeaderAnimation";
      
      private static const ENTRY_CONT_POSITION_INVALID:String = "entryContPositionInvalid";
      
      private static const PARAMS_POSITION_INVALID:String = "paramsPositionInvalid";
      
      private static const CAROUSEL_NAME:String = "carousel";
      
      private static const CAROUSEL_EVENT_ENTRY_NAME:String = "carouselEventEntryContainer";
      
      private static const PARAMS_TOP_MARGIN:int = 3;
      
      private static const PARAMS_BOTTOM_MARGIN:int = 80;
      
      private static const TOP_MARGIN:int = 33;
      
      private static const MINI_CLIENT_GAP:int = 1;
      
      private static const ANIM_SPEED_TIME:int = 600;
      
      private static const TEASER_SHOW_X_OFFSET:int = 10;
      
      private static const TEASER_SHOW_SMALL_X_OFFSET:int = -110;
      
      private static const TEASER_HIDE_SMALL_X_OFFSET:int = -355;
      
      private static const SM_CAROUSEL_PADDING:int = 12;
      
      private static const SM_AMMUNITION_PANEL_PADDING:int = 86;
      
      private static const SM_THRESHOLD_X:int = 1360;
      
      private static const SM_PADDING_X:int = 5;
      
      private static const ALERT_MESSAGE_GAP:int = 40;
      
      private static const RIGHT_MARGIN:int = 5;
      
      private static const BR_UNBOUND_HEADER_TOP_MARGIN:int = 17;
      
      private static const VEH_RESEARCH_PANEL_Y:int = 45;
      
      private static const VEH_RESEARCH_PANEL_OFFSET:int = 37;
      
      private static const DQ_WIDGET_NORMAL_HEIGHT:int = 184;
      
      private static const DQ_WIDGET_MINI_HEIGHT:int = 60;
      
      private static const DQ_WIDGET_MICRO_HEIGHT:int = 58;
      
      private static const DQ_WIDGET_NORMAL_LAYOUT_CAROUSEL_THRESHOLD:int = 699;
      
      private static const DQ_WIDGET_WIDTH_THRESHOLD:int = 1200;
      
      private static const DQ_WIDGET_VERTICAL_OFFSET:int = 15;
      
      private static const DQ_WIDGET_VERTICAL_OFFSET_SINGLE:int = 20;
      
      private static const DQ_WIDGET_VERTICAL_OFFSET_SINGLE_NO_CAROUSEL:int = -7;
      
      private static const DQ_WIDGET_VERTICAL_OFFSET_MINI:int = 37;
      
      private static const DQ_WIDGET_VERTICAL_OFFSET_MICRO:int = 36;
      
      private static const DQ_WIDGET_HORIZONTAL_MARGIN:int = 0;
      
      private static const COMP7_MODIFIERS_PANEL_INJECT_WIDTH:int = 354;
      
      private static const COMP7_MODIFIERS_PANEL_INJECT_HEIGHT:int = 58;
      
      private static const COMP7_MODIFIERS_PANEL_INJECT_OFFSET_Y:int = 2;
      
      private static const COMP7_MODIFIERS_PANEL_INJECT_OFFSET_X:int = 1;
      
      private static const CAROUSEL_BANNER_OFFSET_X:int = -15;
      
      private static const CAROUSEL_BANNER_OFFSET_Y:int = -12;
      
      private static const PARAMS_SMALL_SCREEN_BOTTOM_MARGIN:int = 98;
      
      private static const AMMUNITION_PANEL_OFFSET_Y:int = 4;
      
      private static const AMMUNITION_PANEL_INJECT_OFFSET_RIGHT:int = 5;
      
      private static const AMMUNITION_PANEL_INJECT_OFFSET_TOP:int = 7;
      
      private static const AMMUNITION_PANEL_INJECT_FACTOR:int = 1;
      
      private static const AMMUNITION_PANEL_INJECT_FACTOR_X2:int = 2;
      
      private static const WIDGETS_OFFSET_Y:int = 84;
      
      private static const CAROUSEL_EVENT_ENTRY_X_OFFSET:int = 0;
      
      private static const CAROUSEL_EVENT_ENTRY_Y_OFFSET:int = 110;
      
      private static const HELP_LAYOUT_ADDITIONAL_WIDTH:int = -30;
       
      
      public var vehResearchPanel:ResearchPanel;
      
      public var vehResearchBG:TutorialClip;
      
      public var params:IVehicleParameters;
      
      public var ammunitionPanel:AmmunitionPanel;
      
      public var ammunitionPanelInject:AmmunitionPanelInject;
      
      public var bottomBg:TutorialClip;
      
      public var carouselContainer:TutorialClip;
      
      public var switchModePanel:SwitchModePanel;
      
      public var prestigeBg:TutorialClip;
      
      public var teaser:Teaser;
      
      public var dqWidget:DailyQuestWidget;
      
      public var carouselEventEntry:CarouselEventEntry = null;
      
      public var crewPanelInject:CrewPanelInject;
      
      public var prestigeProgressInject:PrestigeProgressInject = null;
      
      private var _header:HangarHeader;
      
      private var _carousel:TankCarousel;
      
      private var _isControlsVisible:Boolean = false;
      
      private var _carouselAlias:String;
      
      private var _alertMessageBlock:AlertMessageBlock;
      
      private var _miniClient:HangarMiniClientComponent;
      
      private var _gameInputMgr:IGameInputManager;
      
      private var _toolTipMgr:ITooltipMgr;
      
      private var _utils:IUtils;
      
      private var _helpLayout:IHelpLayout;
      
      private var _hangarContentHelper:HangarContentHelper;
      
      private var _teaserX:int = 0;
      
      private var _teaserOffsetX:int = 0;
      
      private var _tweenTeaser:Tween;
      
      private var _isTeaserShow:Boolean;
      
      private var _hangarViewSwitchAnimator:HangarAmunitionSwitchAnimator;
      
      private var _isVisibleByAnimator:Boolean = true;
      
      private var _isVisible:Boolean = true;
      
      private var _comp7ModifiersPanelInject:GFInjectComponent = null;
      
      private var _carouselBanner:CarouselBannerInject = null;
      
      private var _appStage:Stage;
      
      private var _topMargin:int = 0;
      
      private var _currentWidgetLayout:int = 99;
      
      private var _forcedWidgetLayout:int = -1;
      
      private var _widgetInitialized:Boolean;
      
      private var _widgetSizes:Dictionary;
      
      private var _battleRoyaleComponents:HangarComponentsContainer = null;
      
      private var _eventsEntryContainer:HangarEventEntriesContainer = null;
      
      private var _carouselEventEntryContainer:Sprite = null;
      
      private var _carouselEventEntryVisible:Boolean = true;
      
      private var _carouselVisible:Boolean = true;
      
      private var _isBRBattleTypeSelectorVisible:Boolean = false;
      
      private var _isBRSpaceLoaded:Boolean = false;
      
      public function Hangar()
      {
         this._gameInputMgr = App.gameInputMgr;
         this._toolTipMgr = App.toolTipMgr;
         this._utils = App.utils;
         this._helpLayout = App.utils.helpLayout;
         this._appStage = App.stage;
         super();
         _deferredDispose = true;
         this.switchModePanel.visible = false;
         this.params.snapHeightToRenderers = false;
         this._hangarContentHelper = new HangarContentHelper(this);
         this.setupWidgetSizes();
         this._eventsEntryContainer = new HangarEventEntriesContainer();
         this._eventsEntryContainer.name = HANGAR_ALIASES.ENTRIES_CONTAINER;
         this._eventsEntryContainer.addEventListener(Event.RESIZE,this.onEventsEntryContainerResizeHandler);
         this._eventsEntryContainer.visible = false;
         addChildAt(this._eventsEntryContainer,getChildIndex(this.carouselContainer) + 1);
         this._carouselEventEntryContainer = new Sprite();
         addChild(this._carouselEventEntryContainer);
         this._carouselEventEntryContainer.name = CAROUSEL_EVENT_ENTRY_NAME;
         this._header = this._utils.classFactory.getComponent(Linkages.HANGAR_HEADER,HangarHeader);
         this._header.name = HANGAR_ALIASES.HEADER;
         addChildAt(this._header,numChildren);
      }
      
      public static function getAdditionalHelpLayoutOffset() : int
      {
         return Math.min(HELP_LAYOUT_ADDITIONAL_WIDTH + (App.appWidth - StageSizeBoundaries.WIDTH_1024 >> 1),0);
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         var _loc3_:Rectangle = null;
         _originalWidth = param1;
         _originalHeight = param2;
         setSize(param1,param2);
         if(this.carousel != null)
         {
            this.carousel.updateStage(param1,param2);
            this.updateCarouselPosition();
         }
         if(this.bottomBg != null)
         {
            this.bottomBg.x = 0;
            this.bottomBg.y = _originalHeight >> 0;
            this.bottomBg.width = _originalWidth;
         }
         this.alignToCenter(this.switchModePanel);
         this.alignToCenter(this._miniClient);
         if(this.header != null)
         {
            this.header.x = param1 >> 1;
         }
         if(this._alertMessageBlock)
         {
            this._alertMessageBlock.x = _width - this._alertMessageBlock.width >> 1;
         }
         if(this.vehResearchPanel != null)
         {
            this.vehResearchPanel.x = param1;
            _loc3_ = this.vehResearchBG.getBounds(this.vehResearchBG);
            this.vehResearchBG.x = param1 - _loc3_.x - _loc3_.width - RIGHT_MARGIN >> 0;
         }
         this._helpLayout.hide();
         invalidate(ENTRY_CONT_POSITION_INVALID);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerFlashComponentS(this.crewPanelInject,HANGAR_ALIASES.CREW_PANEL_INJECT);
         registerFlashComponentS(this.ammunitionPanel,HANGAR_ALIASES.AMMUNITION_PANEL);
         registerFlashComponentS(this.ammunitionPanelInject,HANGAR_ALIASES.AMMUNITION_PANEL_INJECT);
         registerFlashComponentS(this.switchModePanel,Aliases.SWITCH_MODE_PANEL);
         registerFlashComponentS(this.params,HANGAR_ALIASES.VEHICLE_PARAMETERS);
         registerFlashComponentS(this.dqWidget,Aliases.DAILY_QUEST_WIDGET);
         registerFlashComponentS(this._eventsEntryContainer,HANGAR_ALIASES.ENTRIES_CONTAINER);
         registerFlashComponentS(this._header,HANGAR_ALIASES.HEADER);
         this._appStage.addEventListener(HangarAmunitionSwitchAnimator.AMMUNITION_VIEW_HIDE_ANIM_COMPLETE,this.onAmmunitionViewHideAnimCompleteHandler);
         this.ammunitionPanelInject.addEventListener(Event.RESIZE,this.onAmmunitionPanelInjectResizeHandler);
         this.ammunitionPanelInject.addEventListener(AmmunitionPanelInjectEvents.HELP_LAYOUT_CHANGED,this.onAmmunitionPanelInjectHelpLayoutChangedHandler);
         addEventListener(CrewDropDownEvent.SHOW_DROP_DOWN,this.onHangarShowDropDownHandler);
         if(this.vehResearchPanel != null)
         {
            registerFlashComponentS(this.vehResearchPanel,HANGAR_ALIASES.RESEARCH_PANEL);
         }
         this.updateElementsPosition();
         this.updateHeaderMargin();
      }
      
      override protected function onBeforeDispose() : void
      {
         App.tutorialMgr.removeListenersFromCustomTutorialComponent(this);
         this._eventsEntryContainer.removeEventListener(Event.RESIZE,this.onEventsEntryContainerResizeHandler);
         this.ammunitionPanelInject.removeEventListener(Event.RESIZE,this.onAmmunitionPanelInjectResizeHandler);
         this.ammunitionPanelInject.removeEventListener(AmmunitionPanelInjectEvents.HELP_LAYOUT_CHANGED,this.onAmmunitionPanelInjectHelpLayoutChangedHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.handleEscapeHandler);
         this._appStage.dispatchEvent(new LobbyEvent(LobbyEvent.UNREGISTER_DRAGGING));
         this._appStage.removeEventListener(HangarAmunitionSwitchAnimator.AMMUNITION_VIEW_HIDE_ANIM_COMPLETE,this.onAmmunitionViewHideAnimCompleteHandler);
         removeEventListener(CrewDropDownEvent.SHOW_DROP_DOWN,this.onHangarShowDropDownHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.F1,KeyboardEvent.KEY_DOWN,this.showLayoutHandler);
         this._gameInputMgr.clearKeyHandler(Keyboard.F1,KeyboardEvent.KEY_UP,this.closeLayoutHandler);
         this.ammunitionPanel.removeEventListener(Event.RESIZE,this.onAmmunitionPanelResizeHandler);
         this.ammunitionPanel.removeEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onAmmunitionPanelRequestFocusHandler);
         this.vehResearchPanel.removeEventListener(Event.RESIZE,this.onVehResearchPanelResizeHandler);
         this.params.removeEventListener(Event.RESIZE,this.onParamsResizeHandler);
         this.teaser.removeEventListener(TeaserEvent.TEASER_CLICK,this.onTeaserTeaserClickHandler);
         this.teaser.removeEventListener(TeaserEvent.HIDE,this.onTeaserHideHandler);
         this.switchModePanel.removeEventListener(ComponentEvent.SHOW,this.onSwitchModePanelShowHandler);
         this.switchModePanel.removeEventListener(ComponentEvent.HIDE,this.onSwitchModePanelHideHandler);
         this.carousel.removeEventListener(Event.RESIZE,this.onCarouselResizeHandler);
         if(this._hangarViewSwitchAnimator)
         {
            this._hangarViewSwitchAnimator.dispose();
            this._hangarViewSwitchAnimator = null;
         }
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.tryRemoveBattleRoyaleContainer();
         this.removeComp7ModifiersPanel();
         this.removePrestigeWidgetPanel();
         this.bottomBg.dispose();
         this.bottomBg = null;
         this.teaser.dispose();
         this.teaser = null;
         if(this._tweenTeaser)
         {
            this._tweenTeaser.paused = true;
            this._tweenTeaser.dispose();
            this._tweenTeaser = null;
         }
         this._miniClient = null;
         this.vehResearchPanel = null;
         this.vehResearchBG.dispose();
         this.vehResearchBG = null;
         this.crewPanelInject = null;
         this.params = null;
         this.ammunitionPanel = null;
         this.ammunitionPanelInject = null;
         this._carousel = null;
         this.switchModePanel = null;
         this._header = null;
         this._alertMessageBlock = null;
         this.dqWidget = null;
         this.carouselEventEntry = null;
         this._widgetInitialized = false;
         this.prestigeBg.dispose();
         this.prestigeBg = null;
         this._utils.data.cleanupDynamicObject(this._widgetSizes);
         this._widgetSizes = null;
         this._gameInputMgr = null;
         this._toolTipMgr = null;
         this._utils = null;
         this._helpLayout = null;
         this._appStage = null;
         this.carouselContainer.dispose();
         this.carouselContainer = null;
         this._hangarContentHelper.dispose();
         this._hangarContentHelper = null;
         removeChild(this._eventsEntryContainer);
         this._eventsEntryContainer = null;
         this._currentWidgetLayout = 99;
         this._isBRSpaceLoaded = false;
         removeChild(this._carouselEventEntryContainer);
         this._carouselEventEntryContainer = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.tutorialMgr.addListenersToCustomTutorialComponent(this);
         this._appStage.dispatchEvent(new LobbyEvent(LobbyEvent.REGISTER_DRAGGING));
         mouseEnabled = false;
         this.bottomBg.mouseEnabled = false;
         this._gameInputMgr.setKeyHandler(Keyboard.F1,KeyboardEvent.KEY_DOWN,this.showLayoutHandler,true);
         this._gameInputMgr.setKeyHandler(Keyboard.F1,KeyboardEvent.KEY_UP,this.closeLayoutHandler,true);
         this._gameInputMgr.setKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.handleEscapeHandler,true);
         this.ammunitionPanel.addEventListener(Event.RESIZE,this.onAmmunitionPanelResizeHandler);
         this.ammunitionPanel.addEventListener(FocusRequestEvent.REQUEST_FOCUS,this.onAmmunitionPanelRequestFocusHandler);
         this.switchModePanel.addEventListener(ComponentEvent.SHOW,this.onSwitchModePanelShowHandler);
         this.switchModePanel.addEventListener(ComponentEvent.HIDE,this.onSwitchModePanelHideHandler);
         this.vehResearchPanel.addEventListener(Event.RESIZE,this.onVehResearchPanelResizeHandler);
         this.params.addEventListener(Event.RESIZE,this.onParamsResizeHandler);
         this.teaser.addEventListener(TeaserEvent.TEASER_CLICK,this.onTeaserTeaserClickHandler);
         this.teaser.addEventListener(TeaserEvent.HIDE,this.onTeaserHideHandler);
         this.carouselContainer.mouseEnabled = false;
         this._teaserX = -this.teaser.over.width;
         this.prestigeBg.visible = false;
         this.prestigeBg.mouseEnabled = this.prestigeBg.mouseChildren = false;
      }
      
      override protected function allowHandleInput() : Boolean
      {
         return false;
      }
      
      override protected function draw() : void
      {
         var _loc5_:int = 0;
         super.draw();
         var _loc1_:Boolean = isInvalid(ENTRY_CONT_POSITION_INVALID,INVALIDATE_AMMUNITION_PANEL_SIZE);
         var _loc2_:Boolean = isInvalid(PARAMS_POSITION_INVALID);
         var _loc3_:Boolean = false;
         var _loc4_:Boolean = isInvalid(INVALIDATE_PRESTIGE_WIDGET_VISIBILITY);
         if(isInvalid(INVALIDATE_CAROUSEL_SIZE))
         {
            this.carousel.visible = this._carouselVisible;
            this.updateCarouselPosition();
            if(hasEventListener(Event.RESIZE))
            {
               dispatchEvent(new Event(Event.RESIZE));
            }
            this.updateTeaserSize();
            if(this.visible)
            {
               _loc5_ = SM_CAROUSEL_PADDING;
               if(width > SM_THRESHOLD_X)
               {
                  _loc5_ = SM_AMMUNITION_PANEL_PADDING;
               }
               App.systemMessages.dispatchEvent(new NotificationLayoutEvent(NotificationLayoutEvent.UPDATE_LAYOUT,new Point(SM_PADDING_X,height - this.ammunitionPanel.y - _loc5_)));
            }
            this.checkToIfLayoutNeedsUpdate();
            this.updateBRComponentsPos();
            _loc1_ = true;
            _loc3_ = true;
         }
         if(_loc4_)
         {
            this.prestigeBg.visible = this.prestigeProgressInject != null;
         }
         if(_loc4_ || isInvalid(INVALIDATE_COMP7_MODIFIERS_VISIBILITY))
         {
            _loc2_ = true;
         }
         if(isInvalid(INVALIDATE_EVENT_LOOT_BOXES_VISIBLE))
         {
            if(this._carouselEventEntryVisible)
            {
               if(!this.carouselEventEntry)
               {
                  this.carouselEventEntry = new CarouselEventEntry();
                  this._carouselEventEntryContainer.addChild(this.carouselEventEntry);
               }
               if(!isFlashComponentRegisteredS(HANGAR_ALIASES.CAROUSEL_EVENT_ENTRY_HOLDER))
               {
                  registerFlashComponentS(this.carouselEventEntry,HANGAR_ALIASES.CAROUSEL_EVENT_ENTRY_HOLDER);
               }
               this.carouselEventEntry.visible = true;
               this.carouselEventEntry.updateStateS();
            }
            else if(this.carouselEventEntry)
            {
               this.carouselEventEntry.updateStateS();
               if(isFlashComponentRegisteredS(HANGAR_ALIASES.CAROUSEL_EVENT_ENTRY_HOLDER))
               {
                  unregisterFlashComponentS(HANGAR_ALIASES.CAROUSEL_EVENT_ENTRY_HOLDER);
               }
               this._carouselEventEntryContainer.removeChild(this.carouselEventEntry);
               this.carouselEventEntry = null;
            }
            if(this.carousel)
            {
               this.carousel.setRightMargin(!!this._carouselEventEntryVisible ? int(CarouselEventEntry.WIDTH + CAROUSEL_EVENT_ENTRY_X_OFFSET) : int(0));
            }
            this.updateCarouselEventEntryWidgetPosition();
         }
         if(isInvalid(INVALIDATE_CAROUSEL_BANNER_VISIBILITY))
         {
            this.updateCarouselBannerSizeAndPosition();
         }
         if(_loc1_)
         {
            this.updateEntriesPosition();
            _loc2_ = true;
         }
         if(_loc2_)
         {
            this.updateParamsPosition();
            if(!_loc3_)
            {
               this.repositionWidget();
            }
         }
         if(isInvalid(INVALIDATE_HEADER_ANIMATION))
         {
            if(this._battleRoyaleComponents)
            {
               if(this._isBRSpaceLoaded && this._isBRBattleTypeSelectorVisible && !this.header.hasWidget(HANGAR_ALIASES.BATTLE_ROYALE_TOURNAMENT))
               {
                  this._battleRoyaleComponents.showHeader(true);
               }
               else
               {
                  this._battleRoyaleComponents.hideHeader();
               }
            }
         }
      }
      
      override protected function onSetModalFocus(param1:InteractiveObject) : void
      {
         if(param1 == null)
         {
            param1 = this;
         }
         super.onSetModalFocus(param1);
      }
      
      override protected function setupAmmunitionPanel(param1:AmmunitionPanelVO) : void
      {
         this.ammunitionPanel.updateMaintenanceButton(param1.maintenanceVisible,param1.maintenanceEnabled,param1.maintenanceTooltip);
         this.ammunitionPanel.updateTuningButton(param1.customizationVisible,param1.customizationEnabled,param1.customizationTooltip);
         this.ammunitionPanel.updateChangeNationButton(param1.changeNationVisible,param1.changeNationEnable,param1.changeNationTooltip,param1.changeNationIsNew);
      }
      
      override protected function show3DSceneTooltip(param1:String, param2:Array) : void
      {
         this._toolTipMgr.showSpecial.apply(this._toolTipMgr,[param1,null].concat(param2));
      }
      
      override protected function showTeaser(param1:TeaserVO) : void
      {
         this.teaser.setData(param1);
         this._isTeaserShow = true;
         if(!this._tweenTeaser)
         {
            this.teaser.alpha = 0;
            this._tweenTeaser = new Tween(ANIM_SPEED_TIME,this.teaser,{
               "x":this._teaserOffsetX,
               "alpha":1
            },{
               "paused":false,
               "onComplete":this.animationFinished,
               "ease":Quadratic.easeInOut
            });
         }
      }
      
      override protected function updateHangarComponents(param1:Array, param2:Array) : void
      {
         this._hangarContentHelper.updateShowComponents(param1);
         this._hangarContentHelper.updateHideComponents(param2);
      }
      
      public function addAlertMessage() : void
      {
         if(this._alertMessageBlock == null)
         {
            this._alertMessageBlock = this._utils.classFactory.getComponent(Linkages.ALERT_MESSAGE_BLOCK,AlertMessageBlock);
            this._alertMessageBlock.name = HANGAR_ALIASES.ALERT_MESSAGE_BLOCK;
         }
         var _loc1_:Boolean = Boolean(this._alertMessageBlock) ? Boolean(contains(this._alertMessageBlock)) : Boolean(false);
         if(!_loc1_)
         {
            addChildAt(this._alertMessageBlock,getChildIndex(this.ammunitionPanel as DisplayObject) - 1);
         }
         if(!isFlashComponentRegisteredS(HANGAR_ALIASES.ALERT_MESSAGE_BLOCK))
         {
            registerFlashComponentS(this._alertMessageBlock,HANGAR_ALIASES.ALERT_MESSAGE_BLOCK);
         }
         this.updateElementsPosition();
      }
      
      public function addCarouselBanner(param1:String) : void
      {
         if(this._carouselBanner)
         {
            if(this._carouselBanner.alias == param1)
            {
               return;
            }
            this.removeCarouselBanner(this._carouselBanner.alias);
         }
         if(!this._carouselBanner)
         {
            this._carouselBanner = new CarouselBannerInject(param1);
            addChild(this._carouselBanner);
            registerFlashComponentS(this._carouselBanner,param1);
         }
         invalidate(INVALIDATE_CAROUSEL_BANNER_VISIBILITY);
      }
      
      public function addComp7Modifiers() : void
      {
         if(!this._comp7ModifiersPanelInject)
         {
            this._comp7ModifiersPanelInject = new GFInjectComponent();
            this._comp7ModifiersPanelInject.setManageSize(true);
            this._comp7ModifiersPanelInject.width = COMP7_MODIFIERS_PANEL_INJECT_WIDTH;
            this._comp7ModifiersPanelInject.height = COMP7_MODIFIERS_PANEL_INJECT_HEIGHT;
            addChild(this._comp7ModifiersPanelInject);
            registerFlashComponentS(this._comp7ModifiersPanelInject,HANGAR_ALIASES.COMP7_MODIFIERS_PANEL);
            invalidate(INVALIDATE_COMP7_MODIFIERS_VISIBILITY);
         }
      }
      
      public function addPrestigeWidget() : void
      {
         if(!this.prestigeProgressInject)
         {
            this.prestigeProgressInject = PrestigeProgressInject(this._utils.classFactory.getComponent(Linkages.PRESTIGE_HANGAR_WIDGET_UI,PrestigeProgressInject));
            this.prestigeProgressInject.name = PrestigeProgressInject.PRESTIGE_WIDGET_NAME;
            addChildAt(this.prestigeProgressInject,getChildIndex(this.params as DisplayObject) + 1);
            registerFlashComponentS(this.prestigeProgressInject,HANGAR_ALIASES.PRESTIGE_PROGRESS_WIDGET);
            invalidate(INVALIDATE_PRESTIGE_WIDGET_VISIBILITY);
         }
      }
      
      public function as_closeHelpLayout() : void
      {
         this._helpLayout.hide();
      }
      
      public function as_hide3DSceneTooltip() : void
      {
         this.hideTooltip();
      }
      
      public function as_hideTeaserTimer() : void
      {
         this.teaser.hideTimer();
      }
      
      public function as_setBattleRoyaleSpaceLoaded(param1:Boolean) : void
      {
         if(this._battleRoyaleComponents && !this.header.hasWidget(HANGAR_ALIASES.BATTLE_ROYALE_TOURNAMENT))
         {
            this._battleRoyaleComponents.showHeader(!param1);
         }
         this._isBRSpaceLoaded = true;
      }
      
      public function as_setCarousel(param1:String, param2:String) : void
      {
         if(this.carousel != null)
         {
            this.carousel.removeEventListener(Event.RESIZE,this.onCarouselResizeHandler);
            this.carouselContainer.removeChild(this.carousel);
            unregisterFlashComponentS(this._carouselAlias);
         }
         this._carouselAlias = param2;
         this._carousel = this._utils.classFactory.getComponent(param1,TankCarousel);
         this.carousel.visible = false;
         if(this._carouselEventEntryVisible)
         {
            this.carousel.setRightMargin(CarouselEventEntry.WIDTH + CAROUSEL_EVENT_ENTRY_X_OFFSET);
         }
         else if(this._carouselBanner)
         {
            this.carousel.setRightMargin(this._carouselBanner.width);
         }
         this.carousel.addEventListener(Event.RESIZE,this.onCarouselResizeHandler);
         this.carousel.updateStage(_originalWidth,_originalHeight);
         this.carousel.name = CAROUSEL_NAME;
         this.carouselContainer.addChild(this.carousel);
         registerFlashComponentS(this.carousel,this._carouselAlias);
         this.carousel.validateNow();
         invalidate(INVALIDATE_CAROUSEL_SIZE);
      }
      
      public function as_setCarouselBannerVisible(param1:String, param2:Boolean) : void
      {
         if(param2)
         {
            this.addCarouselBanner(param1);
         }
         if(!param2)
         {
            this.removeCarouselBanner(param1);
         }
      }
      
      public function as_setCarouselEnabled(param1:Boolean) : void
      {
         this.carousel.enabled = param1;
      }
      
      public function as_setComp7ModifiersVisible(param1:Boolean) : void
      {
         if(param1 && !this._comp7ModifiersPanelInject)
         {
            this.addComp7Modifiers();
         }
         if(!param1 && this._comp7ModifiersPanelInject)
         {
            this.removeComp7Modifiers();
         }
      }
      
      public function as_setControlsVisible(param1:Boolean) : void
      {
         if(param1 != this.isControlsVisible)
         {
            this._isControlsVisible = param1;
         }
      }
      
      public function as_setDQWidgetLayout(param1:int) : void
      {
         this._forcedWidgetLayout = param1;
      }
      
      public function as_setPrestigeWidgetVisible(param1:Boolean) : void
      {
         if(param1 && this.prestigeProgressInject == null)
         {
            this.addPrestigeWidget();
         }
         if(!param1 && this.prestigeProgressInject != null)
         {
            this.removePrestigeWidget();
         }
      }
      
      public function as_setTeaserTimer(param1:String) : void
      {
         this.teaser.setTime(param1);
      }
      
      public function as_setVisible(param1:Boolean) : void
      {
         this.visible = param1;
      }
      
      public function as_showHelpLayout() : void
      {
         var _loc1_:Number = NaN;
         if(this.params.visible)
         {
            _loc1_ = Math.max(this.params.getHelpLayoutWidth(),this.vehResearchPanel.getHelpLayoutWidth());
            this.params.showHelpLayoutEx(this.vehResearchPanel.x - this.params.x,_loc1_);
         }
         this._helpLayout.show();
      }
      
      public function as_showMiniClientInfo(param1:String, param2:String) : void
      {
         this._miniClient = HangarMiniClientComponent(this._utils.classFactory.getComponent(Linkages.HANGAR_MINI_CLIENT_COMPONENT,HangarMiniClientComponent));
         this._miniClient.update(param1,param2);
         addChild(this._miniClient);
         registerFlashComponentS(this._miniClient,Aliases.MINI_CLIENT_LINKED);
         this.updateElementsPosition();
      }
      
      public function as_showSwitchToAmmunition() : void
      {
         this.initHangarSwitchAnimator();
         this._hangarViewSwitchAnimator.playHideAnimation();
      }
      
      public function as_updateCarouselEventEntryState(param1:Boolean) : void
      {
         if(param1 != this._carouselEventEntryVisible)
         {
            this._carouselEventEntryVisible = param1;
            invalidate(INVALIDATE_EVENT_LOOT_BOXES_VISIBLE);
         }
      }
      
      public function createBattleRoyaleComponents() : void
      {
         var _loc1_:int = 0;
         if(this._battleRoyaleComponents == null)
         {
            this._battleRoyaleComponents = new HangarComponentsContainer();
            this._battleRoyaleComponents.setHeader(this.header);
            _loc1_ = getChildIndex(this.carouselContainer as DisplayObject) + 1;
            addChildAt(this._battleRoyaleComponents,_loc1_);
            this._battleRoyaleComponents.addEventListener(BattleTypeSelectorEvent.BATTLE_TYPE_SELECTOR_VISIBILITY_CHANGED,this.onBattleTypeSelectorVisibilityChangedHandler);
         }
         if(!isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.COMMANDER_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.TECH_PARAMETERS_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.PROXY_CURRENCY_PANEL_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.BOTTOM_PANEL_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.BATTLE_TYPE_SELECTOR))
         {
            registerFlashComponentS(this._battleRoyaleComponents.commander,BATTLEROYALE_ALIASES.COMMANDER_COMPONENT);
            registerFlashComponentS(this._battleRoyaleComponents.techParameters,BATTLEROYALE_ALIASES.TECH_PARAMETERS_COMPONENT);
            registerFlashComponentS(this._battleRoyaleComponents.bottomPanel,BATTLEROYALE_ALIASES.BOTTOM_PANEL_COMPONENT);
            registerFlashComponentS(this._battleRoyaleComponents.proxyCurrencyPanel,BATTLEROYALE_ALIASES.PROXY_CURRENCY_PANEL_COMPONENT);
            registerFlashComponentS(this._battleRoyaleComponents.battleTypeSelector,BATTLEROYALE_ALIASES.BATTLE_TYPE_SELECTOR);
         }
         this.updateBRComponentsPos();
      }
      
      public function generatedUnstoppableEvents() : Boolean
      {
         return true;
      }
      
      public function getTutorialDescriptionName() : String
      {
         return name;
      }
      
      public function needPreventInnerEvents() : Boolean
      {
         return true;
      }
      
      public function removeAlertMessage() : void
      {
         var _loc1_:Boolean = false;
         if(this._alertMessageBlock)
         {
            if(isFlashComponentRegisteredS(HANGAR_ALIASES.ALERT_MESSAGE_BLOCK))
            {
               unregisterFlashComponentS(HANGAR_ALIASES.ALERT_MESSAGE_BLOCK);
            }
            _loc1_ = Boolean(this._alertMessageBlock) ? Boolean(contains(this._alertMessageBlock)) : Boolean(false);
            if(_loc1_)
            {
               removeChild(this._alertMessageBlock);
            }
            this._alertMessageBlock = null;
         }
         this.updateElementsPosition();
      }
      
      public function removeBattleRoyaleComponent(param1:String) : void
      {
         if(isFlashComponentRegisteredS(param1))
         {
            unregisterFlashComponentS(param1);
         }
      }
      
      public function removeBattleRoyaleComponents() : void
      {
         if(!_baseDisposed && this._battleRoyaleComponents != null)
         {
            this.removeBattleRoyaleComponent(BATTLEROYALE_ALIASES.COMMANDER_COMPONENT);
            this.removeBattleRoyaleComponent(BATTLEROYALE_ALIASES.BOTTOM_PANEL_COMPONENT);
            this.removeBattleRoyaleComponent(BATTLEROYALE_ALIASES.PROXY_CURRENCY_PANEL_COMPONENT);
            this.removeBattleRoyaleComponent(BATTLEROYALE_ALIASES.TECH_PARAMETERS_COMPONENT);
            this.removeBattleRoyaleComponent(BATTLEROYALE_ALIASES.BATTLE_TYPE_SELECTOR);
         }
      }
      
      public function removeCarouselBanner(param1:String) : void
      {
         if(this._carouselBanner != null && this._carouselBanner.alias == param1)
         {
            removeChild(this._carouselBanner);
            if(!_baseDisposed && isFlashComponentRegisteredS(this._carouselBanner.alias))
            {
               unregisterFlashComponentS(this._carouselBanner.alias);
            }
            this._carouselBanner = null;
            invalidate(INVALIDATE_CAROUSEL_BANNER_VISIBILITY);
         }
      }
      
      public function removeComp7Modifiers() : void
      {
         this.removeComp7ModifiersPanel();
         invalidate(INVALIDATE_COMP7_MODIFIERS_VISIBILITY);
      }
      
      public function removePrestigeWidget() : void
      {
         this.removePrestigeWidgetPanel();
         invalidate(INVALIDATE_PRESTIGE_WIDGET_VISIBILITY);
      }
      
      public function setAnimatorVisibility(param1:Boolean) : void
      {
         this._isVisibleByAnimator = param1;
         this.resolveVisibility();
      }
      
      public function tryRemoveBattleRoyaleContainer() : void
      {
         this.removeBattleRoyaleComponents();
         if(!_baseDisposed && this._battleRoyaleComponents != null && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.COMMANDER_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.TECH_PARAMETERS_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.PROXY_CURRENCY_PANEL_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.BOTTOM_PANEL_COMPONENT) && !isFlashComponentRegisteredS(BATTLEROYALE_ALIASES.BATTLE_TYPE_SELECTOR))
         {
            removeChild(this._battleRoyaleComponents);
            this._battleRoyaleComponents.removeEventListener(BattleTypeSelectorEvent.BATTLE_TYPE_SELECTOR_VISIBILITY_CHANGED,this.onBattleTypeSelectorVisibilityChangedHandler);
            this._battleRoyaleComponents.dispose();
            this._battleRoyaleComponents = null;
            this._isBRBattleTypeSelectorVisible = false;
            this.updateElementsPosition();
         }
      }
      
      public function updateAmmunitionPanelPosition() : void
      {
         var _loc1_:int = 0;
         if(this.carousel != null)
         {
            this.ammunitionPanel.x = _width - this.ammunitionPanel.width >> 1;
            _loc1_ = this.ammunitionPanel.height + AmmunitionPanel.SLOTS_HEIGHT_AND_OFFSET;
            if(!this.carouselContainer.visible)
            {
               this.ammunitionPanel.y = height - _loc1_ | 0;
            }
            else
            {
               this.ammunitionPanel.y = Math.min(this.carousel.y - _loc1_ + AMMUNITION_PANEL_OFFSET_Y | 0,height - _loc1_ | 0);
            }
            this.ammunitionPanel.updateStage(_width,this.carousel.y);
            this.updateAmmunitionPanelInjectPosition();
         }
         invalidate(PARAMS_POSITION_INVALID);
      }
      
      private function removeComp7ModifiersPanel() : void
      {
         if(this._comp7ModifiersPanelInject != null)
         {
            removeChild(this._comp7ModifiersPanelInject);
            if(!_baseDisposed && isFlashComponentRegisteredS(HANGAR_ALIASES.COMP7_MODIFIERS_PANEL))
            {
               unregisterFlashComponentS(HANGAR_ALIASES.COMP7_MODIFIERS_PANEL);
            }
            this._comp7ModifiersPanelInject = null;
         }
      }
      
      private function removePrestigeWidgetPanel() : void
      {
         if(this.prestigeProgressInject != null)
         {
            removeChild(this.prestigeProgressInject);
            if(!_baseDisposed && isFlashComponentRegisteredS(HANGAR_ALIASES.PRESTIGE_PROGRESS_WIDGET))
            {
               unregisterFlashComponentS(HANGAR_ALIASES.PRESTIGE_PROGRESS_WIDGET);
            }
            this.prestigeProgressInject = null;
         }
      }
      
      private function resolveVisibility() : void
      {
         super.visible = this._isVisibleByAnimator && this._isVisible;
      }
      
      private function initHangarSwitchAnimator() : void
      {
         if(!this._hangarViewSwitchAnimator)
         {
            this._hangarViewSwitchAnimator = new HangarAmunitionSwitchAnimator(this,Vector.<DisplayObject>([this.params,this.crewPanelInject,this.dqWidget,this.teaser,this._alertMessageBlock,this.vehResearchPanel,this.vehResearchBG,this.header,this.ammunitionPanel,this.bottomBg,this._comp7ModifiersPanelInject,this.prestigeBg,this.prestigeProgressInject]),Vector.<DisplayObject>([this.carouselContainer,this._carouselEventEntryContainer]),this.ammunitionPanelInject,height);
         }
      }
      
      private function setupWidgetSizes() : void
      {
         this._widgetSizes = new Dictionary();
         this._widgetSizes[DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_NORMAL] = [340,186];
         this._widgetSizes[DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_MINI] = [190,65];
         this._widgetSizes[DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_MICRO] = [155,55];
         this._widgetSizes[DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_SINGLE] = [340,62];
      }
      
      private function updateEntriesPosition() : void
      {
         var _loc1_:Rectangle = null;
         var _loc4_:Boolean = false;
         var _loc5_:int = 0;
         _loc1_ = this.ammunitionPanelInject.hitRect;
         var _loc2_:Boolean = _loc1_ && _loc1_.width > 0;
         var _loc3_:Boolean = this.carousel && this._eventsEntryContainer.isActive;
         this._eventsEntryContainer.visible = _loc3_;
         if(_loc3_)
         {
            if(_loc2_)
            {
               this._eventsEntryContainer.x = _width - this._eventsEntryContainer.width - this._eventsEntryContainer.margin.width | 0;
               this._eventsEntryContainer.y = this.carousel.y - this._eventsEntryContainer.height | 0;
               _loc4_ = false;
               if(_loc1_ && this.ammunitionPanelInject.visible && _loc1_.width > 0)
               {
                  _loc5_ = AMMUNITION_PANEL_INJECT_FACTOR;
                  if(_loc1_.x + _loc1_.width >= this.ammunitionPanelInject.width)
                  {
                     _loc5_ = AMMUNITION_PANEL_INJECT_FACTOR_X2;
                  }
                  _loc4_ = this.ammunitionPanelInject.x + _loc1_.x / _loc5_ + _loc1_.width + AMMUNITION_PANEL_INJECT_OFFSET_RIGHT > this._eventsEntryContainer.x;
               }
               if(_loc4_)
               {
                  this._eventsEntryContainer.y -= _loc1_.y + (_loc1_.height >> 1);
               }
               else
               {
                  this._eventsEntryContainer.y -= this._eventsEntryContainer.margin.height;
               }
            }
            else
            {
               this._eventsEntryContainer.x = _width - this._eventsEntryContainer.width - this._eventsEntryContainer.margin.width | 0;
               this._eventsEntryContainer.y = this.ammunitionPanel.y;
            }
         }
      }
      
      private function checkToIfLayoutNeedsUpdate() : void
      {
         if(!this._widgetInitialized)
         {
            if(this.dqWidget == null || !isFlashComponentRegisteredS(Aliases.DAILY_QUEST_WIDGET))
            {
               return;
            }
            this.dqWidget.x = DQ_WIDGET_HORIZONTAL_MARGIN;
            this._widgetInitialized = true;
         }
         if(!this._header || !this._carousel)
         {
            return;
         }
         var _loc1_:int = this.determineLayout();
         if(this._currentWidgetLayout != _loc1_)
         {
            this._currentWidgetLayout = _loc1_;
            this.dqWidget.setSize(this._widgetSizes[this._currentWidgetLayout][0],this._widgetSizes[this._currentWidgetLayout][1]);
         }
         this.repositionWidget();
      }
      
      private function repositionWidget() : void
      {
         switch(this._currentWidgetLayout)
         {
            case DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_NORMAL:
               this.dqWidget.y = this.ammunitionPanel.y + WIDGETS_OFFSET_Y - DQ_WIDGET_NORMAL_HEIGHT + DQ_WIDGET_VERTICAL_OFFSET;
               break;
            case DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_MINI:
               this.dqWidget.y = this.ammunitionPanel.y + WIDGETS_OFFSET_Y - DQ_WIDGET_MINI_HEIGHT + DQ_WIDGET_VERTICAL_OFFSET_MINI;
               break;
            case DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_MICRO:
               this.dqWidget.y = this.ammunitionPanel.y + WIDGETS_OFFSET_Y - DQ_WIDGET_MICRO_HEIGHT + DQ_WIDGET_VERTICAL_OFFSET_MICRO;
               break;
            case DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_SINGLE:
               this.dqWidget.y = this.ammunitionPanel.y + WIDGETS_OFFSET_Y - DQ_WIDGET_MICRO_HEIGHT + (!!this.carouselContainer.visible ? DQ_WIDGET_VERTICAL_OFFSET_SINGLE : DQ_WIDGET_VERTICAL_OFFSET_SINGLE_NO_CAROUSEL);
         }
      }
      
      private function determineLayout() : int
      {
         if(this._forcedWidgetLayout != Values.DEFAULT_INT)
         {
            return this._forcedWidgetLayout;
         }
         if(App.appWidth >= DQ_WIDGET_WIDTH_THRESHOLD && this._carousel.y >= DQ_WIDGET_NORMAL_LAYOUT_CAROUSEL_THRESHOLD)
         {
            return DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_NORMAL;
         }
         if(App.appWidth > DQ_WIDGET_WIDTH_THRESHOLD)
         {
            return DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_MINI;
         }
         return DAILY_QUESTS_WIDGET_CONSTANTS.WIDGET_LAYOUT_MICRO;
      }
      
      private function updateBRComponentsPos() : void
      {
         if(this._battleRoyaleComponents != null)
         {
            this._battleRoyaleComponents.y = BR_UNBOUND_HEADER_TOP_MARGIN;
            this._battleRoyaleComponents.updateStage(_width,this.carousel.y - BR_UNBOUND_HEADER_TOP_MARGIN);
            this.updateElementsPosition();
         }
      }
      
      private function updateHeaderMargin() : void
      {
         var _loc2_:int = 0;
         var _loc1_:int = this._topMargin;
         this._topMargin = 0;
         if(_loc1_ != this._topMargin)
         {
            _loc2_ = VEH_RESEARCH_PANEL_Y + this._topMargin;
            this.vehResearchPanel.y = this.vehResearchBG.y = _loc2_;
            this.updateParamsPosition();
         }
      }
      
      private function hideTeaserAnim() : void
      {
         this._isTeaserShow = false;
         this._teaserX = this.teaser.x = -this.teaser.width;
         this.teaser.alpha = 0;
         hideTeaserS();
      }
      
      private function updateTeaserSize() : void
      {
         if(stage.stageWidth <= Teaser.STAGE_WIDTH_BOUNDARY)
         {
            this._teaserOffsetX = TEASER_SHOW_SMALL_X_OFFSET;
            this._teaserX = !!this._isTeaserShow ? int(this._teaserOffsetX) : int(TEASER_HIDE_SMALL_X_OFFSET);
         }
         else
         {
            this._teaserOffsetX = TEASER_SHOW_X_OFFSET;
            this._teaserX = !!this._isTeaserShow ? int(this._teaserOffsetX) : int(-this.teaser.over.width);
         }
         this.teaser.x = this._teaserX;
         this.teaser.y = this._carousel.y - this.teaser.height - TEASER_SHOW_X_OFFSET;
         this.teaser.invalidateSize();
      }
      
      private function animationFinished() : void
      {
         this._tweenTeaser = null;
         this._teaserX = this.teaser.x;
      }
      
      private function updateParamsPosition() : void
      {
         var _loc4_:uint = 0;
         var _loc5_:uint = 0;
         var _loc6_:Rectangle = null;
         this.vehResearchBG.y = VEH_RESEARCH_PANEL_OFFSET + this.vehResearchPanel.offset;
         var _loc1_:int = this.vehResearchBG.y + this.vehResearchBG.height + PARAMS_TOP_MARGIN ^ 0;
         if(this.prestigeProgressInject)
         {
            _loc4_ = PrestigeProgressInject.PRESTIGE_WIDGET_WIDTH;
            _loc5_ = App.appWidth > StageSizeBoundaries.WIDTH_1366 ? uint(PrestigeProgressInject.PRESTIGE_WIDGET_HEIGHT) : uint(PrestigeProgressInject.PRESTIGE_WIDGET_HEIGHT_SMALL);
            this.prestigeProgressInject.setSize(_loc4_,_loc5_);
            this.prestigeBg.height = _loc5_ - 2 * PrestigeProgressInject.PRESTIGE_WIDGET_OFFSET;
            this.prestigeProgressInject.x = _originalWidth - this.prestigeProgressInject.width - RIGHT_MARGIN ^ 0;
            _loc6_ = this.prestigeBg.getBounds(this.prestigeBg);
            this.prestigeBg.x = _originalWidth - _loc6_.x - _loc6_.width - RIGHT_MARGIN >> 0;
            this.prestigeBg.y = _loc1_;
            this.prestigeProgressInject.y = _loc1_ - (PrestigeProgressInject.PRESTIGE_WIDGET_OFFSET >> 1);
            _loc1_ = this.prestigeBg.y + this.prestigeBg.height + PARAMS_TOP_MARGIN ^ 0;
         }
         this.params.x = _originalWidth - this.params.width - RIGHT_MARGIN ^ 0;
         this.params.y = _loc1_;
         var _loc2_:int = _originalWidth <= StageSizeBoundaries.WIDTH_1280 ? int(PARAMS_SMALL_SCREEN_BOTTOM_MARGIN) : int(0);
         var _loc3_:int = this.ammunitionPanel.y - this.params.y + PARAMS_BOTTOM_MARGIN - _loc2_;
         if(this._eventsEntryContainer && this._eventsEntryContainer.isActive && this._eventsEntryContainer.height > 0)
         {
            _loc3_ = this._eventsEntryContainer.y - this.params.y - this._eventsEntryContainer.margin.top;
         }
         if(this._comp7ModifiersPanelInject)
         {
            _loc3_ -= this._comp7ModifiersPanelInject.height + COMP7_MODIFIERS_PANEL_INJECT_OFFSET_Y * 2;
         }
         if(_loc3_ > 0)
         {
            this.params.height = _loc3_;
         }
         this.updateComp7ModifiersPosition();
      }
      
      private function hideTooltip() : void
      {
         this._toolTipMgr.hide();
      }
      
      private function updateCarouselPosition() : void
      {
         this._carousel.updateCarouselPosition(_height - this._carousel.getBottom() ^ 0);
         this.updateCarouselBannerSizeAndPosition();
         this.updateCarouselEventEntryWidgetPosition();
         this.updateAmmunitionPanelPosition();
         if(this._hangarViewSwitchAnimator)
         {
            this._hangarViewSwitchAnimator.updateStage(width,height);
         }
      }
      
      private function updateComp7ModifiersPosition() : void
      {
         if(this._comp7ModifiersPanelInject)
         {
            this._comp7ModifiersPanelInject.y = this.params.y + (this.params.visible && this.params.actualHeight + COMP7_MODIFIERS_PANEL_INJECT_OFFSET_Y) ^ 0;
            this._comp7ModifiersPanelInject.x = this.params.x + this.params.width - this._comp7ModifiersPanelInject.width + COMP7_MODIFIERS_PANEL_INJECT_OFFSET_X ^ 0;
         }
      }
      
      private function updateCarouselEventEntryWidgetPosition() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         if(this.carouselEventEntry && this._carousel)
         {
            _loc1_ = this.carousel.x + this._carousel.rightArrow.x;
            _loc2_ = this._carousel.y + this._carousel.leftArrow.y + (this._carousel.leftArrow.height >> 1);
            _loc1_ += CAROUSEL_EVENT_ENTRY_X_OFFSET;
            _loc2_ -= CAROUSEL_EVENT_ENTRY_Y_OFFSET;
            this.carouselEventEntry.x = _loc1_;
            this.carouselEventEntry.y = _loc2_;
         }
      }
      
      private function updateCarouselBannerSizeAndPosition() : void
      {
         if(!this._carousel)
         {
            return;
         }
         if(this._carouselBanner)
         {
            this._carouselBanner.isExtended = this._carousel.isExtended && App.appHeight >= StageSizeBoundaries.HEIGHT_900;
            this._carousel.setRightMargin(this._carouselBanner.width);
            this._carouselBanner.x = this._carousel.x + this._carousel.rightArrow.x + this._carousel.rightArrow.width + CAROUSEL_BANNER_OFFSET_X | 0;
            this._carouselBanner.y = this._carousel.y + this._carousel.getBottom() - this._carouselBanner.height + CAROUSEL_BANNER_OFFSET_Y | 0;
         }
         else if(!this._carouselEventEntryVisible)
         {
            this._carousel.setRightMargin(0);
         }
      }
      
      private function updateElementsPosition() : void
      {
         var _loc1_:int = TOP_MARGIN;
         if(this._miniClient != null)
         {
            this._miniClient.y = _loc1_;
            _loc1_ += this._miniClient.height + MINI_CLIENT_GAP;
         }
         if(this._alertMessageBlock)
         {
            this._alertMessageBlock.x = _width - this._alertMessageBlock.width >> 1;
            this._alertMessageBlock.y = _loc1_;
            _loc1_ += ALERT_MESSAGE_GAP;
         }
         if(this.header != null)
         {
            this.header.x = _width >> 1;
            if(!this._isBRBattleTypeSelectorVisible || !this._battleRoyaleComponents)
            {
               this.header.y = _loc1_;
            }
         }
         if(this.switchModePanel.visible)
         {
            this.switchModePanel.y = _loc1_;
         }
         if(this.switchModePanel.visible)
         {
            this.switchModePanel.y = _loc1_;
         }
      }
      
      private function alignToCenter(param1:DisplayObject) : void
      {
         if(param1)
         {
            param1.x = width - param1.width >> 1;
         }
      }
      
      private function closeLayoutHandler() : void
      {
         closeHelpLayoutS();
      }
      
      private function updateAmmunitionPanelInjectPosition() : void
      {
         if(this.carousel != null && this.ammunitionPanelInject.width > 0)
         {
            this.ammunitionPanelInject.x = _width - this.ammunitionPanelInject.width >> 1;
            this.ammunitionPanelInject.y = this.ammunitionPanel.y + AMMUNITION_PANEL_INJECT_OFFSET_TOP;
         }
      }
      
      override public function set visible(param1:Boolean) : void
      {
         this._isVisible = param1;
         this.resolveVisibility();
      }
      
      public function get eventsEntryContainer() : HangarEventEntriesContainer
      {
         return this._eventsEntryContainer;
      }
      
      public function get miniClient() : HangarMiniClientComponent
      {
         return this._miniClient;
      }
      
      public function set carouselVisible(param1:Boolean) : void
      {
         this._carouselVisible = param1;
         this.carousel.visible = this._carouselVisible;
      }
      
      public function get carousel() : TankCarousel
      {
         return this._carousel;
      }
      
      public function get header() : HangarHeader
      {
         return this._header;
      }
      
      public function get isControlsVisible() : Boolean
      {
         return this._isControlsVisible;
      }
      
      private function onBattleTypeSelectorVisibilityChangedHandler(param1:BattleTypeSelectorEvent) : void
      {
         this._isBRBattleTypeSelectorVisible = param1.isVisible;
         this.updateElementsPosition();
         invalidate(INVALIDATE_HEADER_ANIMATION);
      }
      
      private function onAmmunitionPanelRequestFocusHandler(param1:FocusRequestEvent) : void
      {
         setFocus(param1.focusContainer.getComponentForFocus());
      }
      
      private function handleEscapeHandler(param1:InputEvent) : void
      {
         if(!this._helpLayout.isShown())
         {
            onEscapeS();
         }
      }
      
      private function showLayoutHandler(param1:InputEvent) : void
      {
         var _loc2_:InputDetails = param1.details;
         if(_loc2_.altKey || _loc2_.ctrlKey || _loc2_.shiftKey)
         {
            return;
         }
         showHelpLayoutS();
      }
      
      private function onSwitchModePanelShowHandler(param1:ComponentEvent) : void
      {
         this.updateElementsPosition();
      }
      
      private function onSwitchModePanelHideHandler(param1:ComponentEvent) : void
      {
         this.updateElementsPosition();
      }
      
      private function onAmmunitionViewHideAnimCompleteHandler(param1:Event) : void
      {
         invalidate(INVALIDATE_CAROUSEL_SIZE);
      }
      
      private function onTeaserTeaserClickHandler(param1:TeaserEvent) : void
      {
         onTeaserClickS();
      }
      
      private function onTeaserHideHandler(param1:TeaserEvent) : void
      {
         this.hideTeaserAnim();
      }
      
      private function onAmmunitionPanelResizeHandler(param1:Event) : void
      {
         invalidate(INVALIDATE_AMMUNITION_PANEL_SIZE);
      }
      
      private function onHangarShowDropDownHandler(param1:CrewDropDownEvent) : void
      {
         var _loc2_:MovieClip = param1.dropDownref;
         var _loc3_:Point = globalToLocal(new Point(_loc2_.x,_loc2_.y));
         addChild(_loc2_);
         _loc2_.x = _loc3_.x;
         _loc2_.y = _loc3_.y;
      }
      
      private function onCarouselResizeHandler(param1:Event) : void
      {
         invalidate(INVALIDATE_CAROUSEL_SIZE);
      }
      
      private function onVehResearchPanelResizeHandler(param1:Event) : void
      {
         this.updateParamsPosition();
      }
      
      private function onParamsResizeHandler(param1:Event) : void
      {
         this.updateComp7ModifiersPosition();
      }
      
      private function onEventsEntryContainerResizeHandler(param1:Event) : void
      {
         invalidate(ENTRY_CONT_POSITION_INVALID);
      }
      
      private function onAmmunitionPanelInjectResizeHandler(param1:Event) : void
      {
         this.updateAmmunitionPanelInjectPosition();
         invalidate(ENTRY_CONT_POSITION_INVALID);
      }
      
      private function onAmmunitionPanelInjectHelpLayoutChangedHandler(param1:Event) : void
      {
         invalidate(ENTRY_CONT_POSITION_INVALID);
      }
   }
}
