package net.wg.gui.lobby.vehPostProgression
{
   import fl.motion.BezierEase;
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.geom.Point;
   import flash.geom.Rectangle;
   import flash.ui.Keyboard;
   import net.wg.data.constants.ImageCacheTypes;
   import net.wg.data.constants.generated.HANGAR_ALIASES;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.lobby.components.VehicleTitle;
   import net.wg.gui.lobby.components.data.VehicleTitleVO;
   import net.wg.gui.lobby.vehPostProgression.components.VehParamsPanel;
   import net.wg.gui.lobby.vehPostProgression.components.VehicleBlock;
   import net.wg.gui.lobby.vehPostProgression.data.VehPostProgressionViewVO;
   import net.wg.gui.lobby.vehPostProgression.events.DemountAllBtnEvent;
   import net.wg.infrastructure.base.meta.IVehiclePostProgressionViewBaseMeta;
   import net.wg.infrastructure.base.meta.impl.VehiclePostProgressionViewBaseMeta;
   import net.wg.infrastructure.interfaces.IInnerView;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.InputEvent;
   import scaleform.clik.motion.Tween;
   
   public class VehPostProgressionViewBase extends VehiclePostProgressionViewBaseMeta implements IVehiclePostProgressionViewBaseMeta, IInnerView
   {
      
      private static const TITLE_CENTER_Y_OFFSET:int = -230;
      
      private static const TITLE_MIN_Y_VALUE:int = 80;
      
      private static const TITLE_NEW_MIN_Y_VALUE:int = 30;
      
      private static const TITLE_SIZE_Y_FACTOR:int = 111;
      
      private static const MAX_PARAMS_MARGIN:int = 3;
      
      private static const FLAG_ALPHA:Number = 0.4;
      
      private static const FLAG_SCALE:Number = 0.65;
      
      private static const CONTENT_LEFT_MARGIN:int = 16;
      
      private static const TWEEN_SHOW_TIME:int = 200;
      
      private static const TWEEN_SHOW_DELAY:int = 100;
      
      private static const TWEEN_SHOW_POINTS:Array = [new Point(0.07,0.82),new Point(0.17,1)];
      
      private static const BG_OFFSET_X:int = -1131;
      
      private static const BG_OFFSET_Y:int = -654;
      
      private static const NATION_FLAGS_X_OFFSET:int = -50;
      
      private static const NATION_FLAGS_Y_OFFSET:int = -150;
      
      private static const VEHICLE_BLOCK_NAME:String = "VehicleBlock";
      
      private static const BG_H_MARGIN:int = 10;
       
      
      public var vehParamsPanel:VehParamsPanel = null;
      
      public var background:Image = null;
      
      public var footerBg:Sprite = null;
      
      public var title:VehicleTitle = null;
      
      public var nationFlags:MovieClip;
      
      public var bgColor:Sprite;
      
      protected var _vehicleBlock:VehicleBlock;
      
      protected var _vo:VehPostProgressionViewVO = null;
      
      protected var _topOffset:uint = 0;
      
      protected var _bottomOffset:uint = 0;
      
      private var _injectComponent:VehPostProgressionViewAdaptor;
      
      private var _tweenShow:Tween;
      
      public function VehPostProgressionViewBase()
      {
         this._vehicleBlock = new VehicleBlock();
         this._injectComponent = new VehPostProgressionViewAdaptor();
         super();
         addChild(this.vehParamsPanel);
         addChild(this._injectComponent);
         addChild(this._vehicleBlock);
         this._vehicleBlock.name = VEHICLE_BLOCK_NAME;
         addChild(this.title);
         this.contentAlpha = 0;
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         assertUpdateStageMethod();
      }
      
      override protected function onDispose() : void
      {
         this._vehicleBlock.dispose();
         this._vehicleBlock = null;
         this.title.dispose();
         this.title = null;
         this.footerBg = null;
         this.bgColor = null;
         this.vehParamsPanel.dispose();
         this.vehParamsPanel = null;
         this.background.dispose();
         this.background = null;
         this.nationFlags = null;
         this._injectComponent = null;
         this._vo = null;
         this._tweenShow.dispose();
         this._tweenShow = null;
         super.onDispose();
      }
      
      override protected function onBeforeDispose() : void
      {
         App.gameInputMgr.clearKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.handleEscape);
         this.background.removeEventListener(Event.CHANGE,this.onBackgroundChangeHandler);
         this.vehParamsPanel.removeEventListener(DemountAllBtnEvent.DEMOUNT_ALL_CLICK,this.onDemountAllClickHandler);
         super.onBeforeDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.gameInputMgr.setKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.handleEscape,true);
         this.nationFlags.scaleX = this.nationFlags.scaleY = FLAG_SCALE;
         this.nationFlags.alpha = FLAG_ALPHA;
         this.background.cacheType = ImageCacheTypes.NOT_USE_CACHE;
         this.background.source = RES_ICONS.MAPS_ICONS_VEHPOSTPROGRESSION_VEHICLEPOSTPROGRESSIONVIEW_VEHPROGRESSIONBG;
         this.background.smoothing = true;
         this.background.addEventListener(Event.CHANGE,this.onBackgroundChangeHandler);
         this.vehParamsPanel.addEventListener(DemountAllBtnEvent.DEMOUNT_ALL_CLICK,this.onDemountAllClickHandler);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         registerFlashComponentS(this.vehParamsPanel.params,HANGAR_ALIASES.POST_PROGRESSION_VEHICLE_PARAMS);
         var _loc1_:BezierEase = new BezierEase();
         _loc1_.points = TWEEN_SHOW_POINTS;
         this._tweenShow = new Tween(TWEEN_SHOW_TIME,this,{
            "contentAlpha":1,
            "delay":TWEEN_SHOW_DELAY
         },{
            "ease":_loc1_.getValue,
            "paused":true
         });
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.updateComponentsLayout();
         }
         if(this._vo && isInvalid(InvalidationType.DATA))
         {
            this._vehicleBlock.setButtonData(this._vo.vehicleButton);
            this._vehicleBlock.setVehicleInfo(this._vo.vehicleInfo);
            this._vehicleBlock.setExpBlockVisible(this._vo.showExpBlock);
            this._vehicleBlock.updateWalletStatus();
            this.vehParamsPanel.setDemountAllButtonLabel(this._vo.demountAllButtonLabel);
            if(this.nationFlags.currentFrameLabel != this._vo.nation)
            {
               this.nationFlags.gotoAndStop(this._vo.nation);
            }
         }
      }
      
      override protected function setVehicleTitle(param1:VehicleTitleVO) : void
      {
         this.title.setData(param1);
      }
      
      override protected function setData(param1:VehPostProgressionViewVO) : void
      {
         this._vo = param1;
         this.vehParamsPanel.showDemountAllPairsBtn = this._vo.showDemountAllPairsBtn;
         invalidateData();
      }
      
      public function as_show() : void
      {
         this._tweenShow.reset();
         this._tweenShow.paused = false;
      }
      
      public function isFullScreenModeSupported() : Boolean
      {
         return true;
      }
      
      public function updateStageWithPadding(param1:Number, param2:Number, param3:Rectangle) : void
      {
         this._topOffset = param3.y;
         this._bottomOffset = param3.height;
         setViewSize(param1,param2);
         invalidateSize();
      }
      
      private function updateComponentsLayout() : void
      {
         var _loc4_:int = 0;
         var _loc6_:int = 0;
         var _loc11_:int = 0;
         var _loc1_:uint = _height - this._topOffset - this._bottomOffset | 0;
         var _loc2_:SizeSetting = SizeSettings.extraExtraSmall;
         var _loc3_:int = App.appHeight;
         if(width >= SizeSettings.extraLarge.breakPointX && _loc3_ >= SizeSettings.extraLarge.breakPointY)
         {
            _loc2_ = SizeSettings.extraLarge;
         }
         else if(width >= SizeSettings.large.breakPointX && _loc3_ >= SizeSettings.large.breakPointY)
         {
            _loc2_ = SizeSettings.large;
         }
         else if(width >= SizeSettings.medium.breakPointX && _loc3_ >= SizeSettings.medium.breakPointY)
         {
            _loc2_ = SizeSettings.medium;
         }
         else if(width >= SizeSettings.small.breakPointX && _loc3_ >= SizeSettings.small.breakPointY)
         {
            _loc2_ = SizeSettings.small;
         }
         else if(width >= SizeSettings.extraSmall.breakPointX)
         {
            _loc2_ = SizeSettings.extraSmall;
         }
         this.title.x = width >> 1;
         _loc4_ = (_loc1_ >> 1) + this._topOffset;
         var _loc5_:uint = _loc4_ + TITLE_CENTER_Y_OFFSET >> 1;
         this.title.y = Math.max(_loc5_,TITLE_MIN_Y_VALUE,this._topOffset + TITLE_NEW_MIN_Y_VALUE) | 0;
         this.title.isSmallSized = _loc5_ < TITLE_SIZE_Y_FACTOR;
         this._vehicleBlock.size = _loc2_.sizePrefix;
         _loc6_ = _loc2_.injectCmpWidth;
         var _loc7_:int = _loc2_.injectCmpHeight;
         var _loc8_:Boolean = width < SizeSettings.extraSmall.breakPointX;
         this.vehParamsPanel.y = this._topOffset;
         this.vehParamsPanel.height = _loc1_;
         this.vehParamsPanel.topMargin = this._topOffset;
         this.vehParamsPanel.bottomMargin = this._bottomOffset;
         this.vehParamsPanel.allowHide = _loc8_;
         if(_loc8_)
         {
            addChild(this.vehParamsPanel);
         }
         else
         {
            addChildAt(this.vehParamsPanel,getChildIndex(this._injectComponent));
         }
         var _loc9_:Number = _loc6_ + this.vehParamsPanel.width;
         if(!_loc8_ && width - _loc9_ >= 0)
         {
            _loc11_ = (width - _loc9_ >> 1) + CONTENT_LEFT_MARGIN;
            this.vehParamsPanel.x = _loc11_ + _loc6_ + MAX_PARAMS_MARGIN;
            this._injectComponent.width = _loc6_ + _loc2_.injectCmpXMargin * 2;
            this._injectComponent.x = _loc11_ - _loc2_.injectCmpXMargin;
         }
         else
         {
            this._injectComponent.x = (width - _loc6_ >> 1) - _loc2_.injectCmpXMargin;
            this.vehParamsPanel.x = width - this.vehParamsPanel.width;
            this._injectComponent.width = _loc6_ + _loc2_.injectCmpXMargin * 2;
         }
         var _loc10_:Number = this.title.y + this.title.height - _loc2_.injectCmpTopOffset | 0;
         this._injectComponent.y = Math.max(_loc10_,_height - _loc7_ >> 1) | 0;
         this._injectComponent.height = _height - this._injectComponent.y;
         this._vehicleBlock.x = this._injectComponent.x + (this._injectComponent.width >> 1);
         this._vehicleBlock.y = this._injectComponent.y + (_loc7_ >> 2) + _loc2_.vehicleTopOffset;
         this.vehParamsPanel.setParamsDimensions(this._injectComponent.y - this.vehParamsPanel.y + _loc2_.vehParamsTopOffset,_loc7_ - _loc2_.vehParamsTopOffset);
         this.background.scaleX = this.background.scaleY = _loc2_.bgScale;
         this.background.x = this._vehicleBlock.x + BG_OFFSET_X * _loc2_.bgScale >> 0;
         this.background.y = this._vehicleBlock.y + BG_OFFSET_Y * _loc2_.bgScale >> 0;
         this.footerBg.width = _width;
         this.footerBg.y = _height;
         this.footerBg.visible = this._bottomOffset == 0;
         this.bgColor.x = -BG_H_MARGIN;
         this.bgColor.width = _width + BG_H_MARGIN * 2;
         this.bgColor.height = _height;
         this.nationFlags.x = Math.max(0,this._injectComponent.x + NATION_FLAGS_X_OFFSET);
         this.nationFlags.y = Math.max(0,this._injectComponent.y + NATION_FLAGS_Y_OFFSET);
      }
      
      public function get contentAlpha() : Number
      {
         return this._vehicleBlock.alpha;
      }
      
      public function set contentAlpha(param1:Number) : void
      {
         this._vehicleBlock.alpha = param1;
         this._injectComponent.alpha = param1;
      }
      
      public function get injectComponent() : VehPostProgressionViewAdaptor
      {
         return this._injectComponent;
      }
      
      private function onBackgroundChangeHandler(param1:Event) : void
      {
         invalidateSize();
      }
      
      private function onDemountAllClickHandler(param1:DemountAllBtnEvent) : void
      {
         demountAllPairsS();
      }
      
      private function handleEscape(param1:InputEvent) : void
      {
         if(this.vehParamsPanel.allowHide && this.vehParamsPanel.isPanelShown)
         {
            this.vehParamsPanel.hide();
         }
         else
         {
            onCloseS();
         }
      }
   }
}
