package net.wg.gui.lobby.personalMissions.components
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.KeyboardEvent;
   import flash.geom.Rectangle;
   import flash.ui.Keyboard;
   import net.wg.data.constants.LobbyMetrics;
   import net.wg.gui.components.advanced.interfaces.IBackButton;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.components.windows.ScreenBg;
   import net.wg.gui.lobby.personalMissions.components.awardsView.AdditionalAwards;
   import net.wg.gui.lobby.personalMissions.components.awardsView.AwardHeader;
   import net.wg.gui.lobby.personalMissions.components.awardsView.VehicleAward;
   import net.wg.gui.lobby.personalMissions.data.PMAwardHeaderVO;
   import net.wg.gui.lobby.personalMissions.data.PersonalMissionsAwardsViewVO;
   import net.wg.gui.lobby.personalMissions.events.AwardEvent;
   import net.wg.gui.lobby.personalMissions.events.PersonalMissionsItemSlotEvent;
   import net.wg.infrastructure.base.meta.IPersonalMissionsAwardsViewMeta;
   import net.wg.infrastructure.base.meta.impl.PersonalMissionsAwardsViewMeta;
   import net.wg.infrastructure.interfaces.IInnerView;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class PersonalMissionsAwardsView extends PersonalMissionsAwardsViewMeta implements IPersonalMissionsAwardsViewMeta, IInnerView
   {
      
      private static const BACK_BTN_TOP_MARGIN:int = 58;
      
      private static const BACK_BTN_RIGHT_MARGIN:int = 7;
      
      private static const MAIN_AWARDS_X_SHIFT:int = 40;
      
      private static const ADDITIONAL_AWARDS_X_SHIFT:int = 75;
      
      private static const COMPACT_HEIGHT:int = 890;
      
      private static const BG_Y_PADDING:int = 25;
      
      private static const BG_Y_PADDING_COMPACT:int = -15;
      
      private static const BG_WIDTH:int = 1920;
      
      private static const BG_HEIGHT:int = 1056;
      
      private static const VEHICLE_Y_PADDING:int = 0;
      
      private static const VEHICLE_Y_PADDING_COMPACT:int = 40;
      
      private static const SMOKE_OFFSET_Y:int = 203;
      
      private static const HEADER_Y_POS_COMPACT:int = 55;
      
      private static const HEADER_Y_POS:int = 65;
      
      private static const RIBBON_BOTTOM_PADDING:int = -337;
      
      private static const RIBBON_BOTTOM_PADDING_COMPACT:int = -225;
       
      
      public var awardRibbon:Sprite = null;
      
      public var awardHeader:AwardHeader = null;
      
      public var vehicleAward:VehicleAward = null;
      
      public var additionalAwards:AdditionalAwards = null;
      
      public var mainAwards:AdditionalAwards = null;
      
      public var backBtn:IBackButton = null;
      
      public var bg:UILoaderAlt = null;
      
      public var screenBg:ScreenBg = null;
      
      private var _model:PersonalMissionsAwardsViewVO = null;
      
      private var _smokeGenerator:SmokeGenerator;
      
      private var _topOffset:uint = 0;
      
      private var _bottomOffset:uint = 0;
      
      public function PersonalMissionsAwardsView()
      {
         this._smokeGenerator = new SmokeGenerator();
         super();
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         assertUpdateStageMethod();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.gameInputMgr.setKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.onEscapeKeyHandler,true);
         this.vehicleAward.addEventListener(AwardEvent.VEHICLE_PREVIEW,this.onVehicleAwardVehiclePreviewHandler);
         this.backBtn.addEventListener(ButtonEvent.CLICK,this.onBackBtnClickHandler);
         this.backBtn.x = BACK_BTN_RIGHT_MARGIN;
         addEventListener(PersonalMissionsItemSlotEvent.UNLOCK,this.onUnlockHandler);
         addEventListener(PersonalMissionsItemSlotEvent.CLICK,this.onClickHandler);
         addChildAt(this._smokeGenerator,getChildIndex(this.bg) + 1);
      }
      
      override protected function setHeaderData(param1:PMAwardHeaderVO) : void
      {
         this.awardHeader.setData(param1);
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(PersonalMissionsItemSlotEvent.UNLOCK,this.onUnlockHandler);
         removeEventListener(PersonalMissionsItemSlotEvent.CLICK,this.onClickHandler);
         App.gameInputMgr.clearKeyHandler(Keyboard.ESCAPE,KeyboardEvent.KEY_DOWN,this.onEscapeKeyHandler);
         this.vehicleAward.removeEventListener(AwardEvent.VEHICLE_PREVIEW,this.onVehicleAwardVehiclePreviewHandler);
         this.backBtn.removeEventListener(ButtonEvent.CLICK,this.onBackBtnClickHandler);
         this.awardHeader.dispose();
         this.awardHeader = null;
         this.screenBg.dispose();
         this.screenBg = null;
         this.vehicleAward.dispose();
         this.vehicleAward = null;
         this.additionalAwards.dispose();
         this.additionalAwards = null;
         this.mainAwards.dispose();
         this.mainAwards = null;
         this.backBtn.dispose();
         this.backBtn = null;
         this._smokeGenerator.dispose();
         this._smokeGenerator = null;
         this.bg.dispose();
         this.bg = null;
         this.awardRibbon = null;
         this._model = null;
         super.onDispose();
      }
      
      override protected function setData(param1:PersonalMissionsAwardsViewVO) : void
      {
         if(param1 != null && param1 != this._model)
         {
            this._model = param1;
            this.bg.source = this._model.bgIconSource;
            this.additionalAwards.update(this._model.additionalAwards);
            this.mainAwards.update(this._model.mainAwards);
            this.vehicleAward.update(this._model.vehicleAward);
            invalidate(InvalidationType.DATA,InvalidationType.SIZE);
         }
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._model != null && isInvalid(InvalidationType.DATA))
         {
            this.backBtn.label = this._model.backBtnLabel;
            this.backBtn.descrLabel = this._model.backBtnDescrLabel;
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.updateSize();
         }
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
      }
      
      private function updateSize() : void
      {
         var _loc3_:Boolean = false;
         this.backBtn.y = BACK_BTN_TOP_MARGIN + this._topOffset;
         var _loc1_:int = _width >> 1;
         var _loc2_:int = _height + (this._bottomOffset > 0 ? 0 : LobbyMetrics.LOBBY_MESSENGER_HEIGHT);
         _loc3_ = App.appHeight < COMPACT_HEIGHT;
         this.vehicleAward.switchCompact(_loc3_);
         this.screenBg.setSize(_width,_loc2_);
         this.awardHeader.isCompact(_loc3_);
         this.awardHeader.x = _loc1_;
         this.awardHeader.y = !!_loc3_ ? Number(HEADER_Y_POS_COMPACT) : Number(HEADER_Y_POS);
         this.awardHeader.y += this._topOffset;
         var _loc4_:int = _loc2_ + (!!_loc3_ ? RIBBON_BOTTOM_PADDING_COMPACT : RIBBON_BOTTOM_PADDING);
         var _loc5_:int = this.awardHeader.y + this.awardHeader.height;
         var _loc6_:int = _loc4_ - _loc5_;
         var _loc7_:int = _loc5_ + (_loc6_ >> 1);
         this.vehicleAward.y = _loc7_ + (!!_loc3_ ? VEHICLE_Y_PADDING_COMPACT : VEHICLE_Y_PADDING);
         this.vehicleAward.x = _loc1_;
         this.bg.x = _loc1_ - (BG_WIDTH >> 1);
         this.bg.y = _loc7_ + (!!_loc3_ ? BG_Y_PADDING_COMPACT : BG_Y_PADDING) - (BG_HEIGHT >> 1);
         this.awardRibbon.x = _loc1_;
         this.awardRibbon.y = _loc4_;
         this.mainAwards.x = _loc1_ - this.mainAwards.getAwardsWidth() - MAIN_AWARDS_X_SHIFT;
         this.mainAwards.y = _loc4_;
         this.additionalAwards.x = _loc1_ + ADDITIONAL_AWARDS_X_SHIFT;
         this.additionalAwards.y = _loc4_;
         this._smokeGenerator.width = width;
         this._smokeGenerator.y = this.bg.y + SMOKE_OFFSET_Y;
      }
      
      override public function get isModal() : Boolean
      {
         return true;
      }
      
      private function onVehicleAwardVehiclePreviewHandler(param1:AwardEvent) : void
      {
         showVehiclePreviewS();
      }
      
      private function onBackBtnClickHandler(param1:Event) : void
      {
         closeViewS();
      }
      
      private function onEscapeKeyHandler(param1:Event) : void
      {
         closeViewS();
      }
      
      private function onClickHandler(param1:PersonalMissionsItemSlotEvent) : void
      {
         showMissionByVehicleTypeS(param1.vehicleType);
      }
      
      private function onUnlockHandler(param1:PersonalMissionsItemSlotEvent) : void
      {
         setFocus(this);
         buyMissionsByVehicleTypeS(param1.vehicleType);
      }
   }
}
