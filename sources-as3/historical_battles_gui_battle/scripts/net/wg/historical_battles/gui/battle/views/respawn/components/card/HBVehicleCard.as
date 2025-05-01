package net.wg.historical_battles.gui.battle.views.respawn.components.card
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.historical_battles.data.constants.generated.HB_VEHICLE_CARD_STATE;
   import net.wg.historical_battles.gui.battle.views.respawn.constants.HB_VEHICLE_CARD_PROPS;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBVehicleCardVO;
   import net.wg.historical_battles.gui.battle.views.respawn.events.HBVehicleCardEvent;
   import net.wg.infrastructure.interfaces.IImage;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   import scaleform.clik.events.ButtonEvent;
   import scaleform.clik.motion.Tween;
   
   public class HBVehicleCard extends BattleUIComponent implements IUpdatable
   {
      
      private static const EMBLEM_ALPHA:Number = 0.05;
      
      private static const MASK_EXTRA_HEIGHT:int = 20;
      
      private static const SYMBOL_TOP:int = -3;
      
      private static const TWEEN_DURATION:Number = 300;
       
      
      public var vehImg:HBVehicleImage = null;
      
      public var vehName:HBVehicleName = null;
      
      public var emblemIcon:IImage = null;
      
      public var border:MovieClip = null;
      
      public var fg:MovieClip = null;
      
      public var maskMC:MovieClip = null;
      
      public var pickBtn:UniversalBtn = null;
      
      public var vehState:HBVehicleState = null;
      
      public var bg:MovieClip = null;
      
      public var smoke:MovieClip = null;
      
      public var glow:MovieClip = null;
      
      public var symbol:MovieClip = null;
      
      public var shadow:MovieClip = null;
      
      public var header:MovieClip = null;
      
      public var separator:MovieClip = null;
      
      private var _data:HBVehicleCardVO = null;
      
      private var _state:uint = 1;
      
      private var _prevState:uint = 1;
      
      private var _size:uint = 0;
      
      private var _tweensState:Vector.<Tween>;
      
      private var _tweensLayout:Vector.<Tween>;
      
      private var _hasStateAnim:Boolean = false;
      
      private var _hasLayoutAnim:Boolean = false;
      
      public function HBVehicleCard()
      {
         this._tweensState = new Vector.<Tween>(0);
         this._tweensLayout = new Vector.<Tween>(0);
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.pickBtn.addEventListener(ButtonEvent.CLICK,this.onPickBtnClickHandler);
         this.pickBtn.dynamicSizeByText = true;
         this.pickBtn.label = HB_BATTLE.RESPAWN_CARD_PICK;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.emblemIcon.alpha = EMBLEM_ALPHA;
         mask = this.maskMC;
         mouseChildren = false;
         buttonMode = useHandCursor = true;
         addEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         addEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         addEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.vehState.visible = false;
         this.vehState.label = HB_BATTLE.RESPAWN_CARD_DEAD;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.validateData();
               invalidateState();
               invalidateSize();
            }
            if(isInvalid(InvalidationType.STATE))
            {
               this.validateState();
               invalidateSize();
               this._hasStateAnim = false;
            }
            if(isInvalid(InvalidationType.SIZE))
            {
               this.validateLayout();
               this._hasLayoutAnim = false;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearTweens(this._tweensLayout);
         this.clearTweens(this._tweensState);
         removeEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         removeEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         removeEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.vehImg.dispose();
         this.vehImg = null;
         this.emblemIcon.dispose();
         this.emblemIcon = null;
         this.vehName.dispose();
         this.vehName = null;
         this.vehState.dispose();
         this.vehState = null;
         this.pickBtn.removeEventListener(ButtonEvent.CLICK,this.onPickBtnClickHandler);
         this.pickBtn.dispose();
         this.pickBtn = null;
         this.border = null;
         this.fg = null;
         this.bg = null;
         this.maskMC = null;
         this.symbol = null;
         this.glow = null;
         this.smoke = null;
         this.shadow = null;
         this.header = null;
         this.separator = null;
         this._data = null;
         this._tweensLayout = null;
         this._tweensState = null;
         super.onDispose();
      }
      
      public function update(param1:Object) : void
      {
         if(this._data != param1)
         {
            this._data = HBVehicleCardVO(param1);
            this.state = this._data.state;
            this._hasStateAnim = false;
            this._hasLayoutAnim = false;
            invalidateData();
         }
      }
      
      public function updateSize(param1:uint) : void
      {
         if(this._size != param1)
         {
            this._size = param1;
            this.pickBtn.paddingHorizontal = HB_VEHICLE_CARD_PROPS.getPickBtnPaddingHor(this._size);
            App.utils.universalBtnStyles.setStyle(this.pickBtn,UniversalBtnStylesConst.STYLE_SLIM_GREEN);
            App.utils.universalBtnStyles.setStyle(this.pickBtn,HB_VEHICLE_CARD_PROPS.getPickBtnStyle(this._size));
            this.pickBtn.validateNow();
            invalidateSize();
         }
      }
      
      private function validateData() : void
      {
         this.vehImg.source = this._data.vehicleSrc;
         this.emblemIcon.source = this._data.emblemSrc;
         this.vehName.label = this._data.vehicleName;
         this.vehName.typeSrc = this._data.vehicleTypeSrc;
         this.border.gotoAndStop(this._data.frontName);
         this.header.gotoAndStop(this._data.frontName);
         this.glow.gotoAndStop(this._data.frontName);
         this.separator.gotoAndStop(this._data.frontName);
         this.smoke.gotoAndStop(this._data.frontName);
      }
      
      private function validateState() : void
      {
         mouseChildren = false;
         buttonMode = useHandCursor = false;
         this.vehState.visible = false;
         this.fg.visible = false;
         this.vehName.alpha = 1;
         switch(this._state)
         {
            case HB_VEHICLE_CARD_STATE.DEFAULT:
               buttonMode = useHandCursor = true;
               break;
            case HB_VEHICLE_CARD_STATE.PICKED:
               mouseChildren = true;
               break;
            case HB_VEHICLE_CARD_STATE.DEAD:
               this.vehState.visible = true;
               this.fg.visible = true;
               this.vehName.alpha = HB_VEHICLE_CARD_PROPS.VEH_NAME_DEAD_ALPHA;
         }
         var _loc1_:int = HB_VEHICLE_CARD_PROPS.getPickedAlpha(this._state);
         var _loc2_:int = HB_VEHICLE_CARD_PROPS.getPickedAlpha(this._prevState);
         if(this._hasStateAnim)
         {
            this.vehImg.alpha = HB_VEHICLE_CARD_PROPS.getVehImgAlpha(this._prevState);
            this._tweensState.push(new Tween(TWEEN_DURATION,this.vehImg,{"alpha":HB_VEHICLE_CARD_PROPS.getVehImgAlpha(this._state)}));
            this.glow.alpha = HB_VEHICLE_CARD_PROPS.getGlowAlpha(this._prevState);
            this._tweensState.push(new Tween(TWEEN_DURATION,this.glow,{"alpha":HB_VEHICLE_CARD_PROPS.getGlowAlpha(this._state)}));
            this.smoke.alpha = HB_VEHICLE_CARD_PROPS.getSmokeAlpha(this._prevState);
            this._tweensState.push(new Tween(TWEEN_DURATION,this.smoke,{"alpha":HB_VEHICLE_CARD_PROPS.getSmokeAlpha(this._state)}));
            this.symbol.alpha = _loc2_;
            this.header.alpha = _loc2_;
            this.pickBtn.alpha = _loc2_;
            this.border.alpha = _loc2_;
            if(_loc2_ != _loc1_)
            {
               this._tweensState.push(new Tween(TWEEN_DURATION,this.symbol,{"alpha":_loc1_}));
               this._tweensState.push(new Tween(TWEEN_DURATION,this.header,{"alpha":_loc1_}));
               this._tweensState.push(new Tween(TWEEN_DURATION,this.pickBtn,{"alpha":_loc1_}));
               this._tweensState.push(new Tween(TWEEN_DURATION,this.border,{"alpha":_loc1_}));
            }
         }
         else
         {
            this.vehImg.alpha = HB_VEHICLE_CARD_PROPS.getVehImgAlpha(this._state);
            this.glow.alpha = HB_VEHICLE_CARD_PROPS.getGlowAlpha(this._state);
            this.smoke.alpha = HB_VEHICLE_CARD_PROPS.getSmokeAlpha(this._state);
            this.symbol.alpha = _loc1_;
            this.header.alpha = _loc1_;
            this.pickBtn.alpha = _loc1_;
            this.border.alpha = _loc1_;
         }
      }
      
      private function validateLayout() : void
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc1_:uint = HB_VEHICLE_CARD_PROPS.getWidthWide(this._size);
         var _loc2_:uint = !!this.isPickedState ? uint(_loc1_) : uint(HB_VEHICLE_CARD_PROPS.getWidth(this._size));
         var _loc3_:uint = HB_VEHICLE_CARD_PROPS.getHeight(this._size);
         this.maskMC.y = -MASK_EXTRA_HEIGHT;
         this.maskMC.height = _loc3_ + MASK_EXTRA_HEIGHT;
         this.vehImg.updateSize(this._size);
         this.vehImg.y = HB_VEHICLE_CARD_PROPS.getVehImgY(this._size);
         this.emblemIcon.scaleX = this.emblemIcon.scaleY = HB_VEHICLE_CARD_PROPS.getEmblemScale(this._size);
         this.emblemIcon.y = HB_VEHICLE_CARD_PROPS.getEmblemY(this._size);
         this.vehName.updateSize(this._size);
         var _loc4_:int = !!this.isPickedState ? int(HB_VEHICLE_CARD_PROPS.getVehNameExtraY(this._size)) : int(0);
         this.vehState.updateSize(this._size);
         this.vehState.x = _loc2_ - this.vehState.width >> 1;
         this.vehState.y = HB_VEHICLE_CARD_PROPS.getVehStateY(this._size);
         this.border.width = _loc1_;
         this.border.height = _loc3_;
         this.bg.width = _loc1_;
         this.bg.height = _loc3_;
         this.fg.width = _loc1_;
         this.fg.height = _loc3_;
         this.pickBtn.x = _loc1_ - this.pickBtn.width >> 1;
         this.pickBtn.y = _loc3_ - this.pickBtn.height - HB_VEHICLE_CARD_PROPS.getPickBtnBottomOffset(this._size);
         this.glow.width = _loc1_;
         this.glow.height = _loc3_;
         this.smoke.width = _loc1_;
         this.smoke.height = _loc3_;
         this.symbol.scaleX = this.symbol.scaleY = HB_VEHICLE_CARD_PROPS.getScale(this._size);
         this.symbol.x = _loc1_ - this.symbol.width >> 1;
         this.symbol.y = (-this.symbol.height >> 1) + SYMBOL_TOP * HB_VEHICLE_CARD_PROPS.getScale(this._size);
         this.separator.height = _loc3_;
         this.shadow.height = _loc3_;
         if(this._hasLayoutAnim && (this.isPickedState || this._prevState == HB_VEHICLE_CARD_STATE.PICKED))
         {
            _loc5_ = HB_VEHICLE_CARD_PROPS.getAnimStartWidth(this._size,this.isPickedState);
            _loc6_ = HB_VEHICLE_CARD_PROPS.getAnimEndWidth(this._size,this.isPickedState);
            this.maskMC.width = _loc5_;
            this._tweensLayout.push(new Tween(TWEEN_DURATION,this.maskMC,{"width":_loc6_}));
            this.shadow.x = _loc5_;
            this._tweensLayout.push(new Tween(TWEEN_DURATION,this.shadow,{"x":_loc6_}));
            this._tweensLayout.push(new Tween(TWEEN_DURATION,this.emblemIcon,{"x":_loc2_ - this.emblemIcon.width >> 1}));
            this._tweensLayout.push(new Tween(TWEEN_DURATION,this.vehName,{
               "x":_loc2_ - this.vehName.width >> 1,
               "y":HB_VEHICLE_CARD_PROPS.getVehNameY(this._size) + _loc4_
            }));
         }
         else
         {
            this.maskMC.width = _loc2_;
            this.shadow.x = _loc2_;
            this.emblemIcon.x = _loc2_ - this.emblemIcon.width >> 1;
            this.vehName.x = _loc2_ - this.vehName.width >> 1;
            this.vehName.y = HB_VEHICLE_CARD_PROPS.getVehNameY(this._size) + _loc4_;
         }
      }
      
      private function clearTweens(param1:Vector.<Tween>) : void
      {
         var _loc2_:Tween = null;
         if(param1 && param1.length)
         {
            for each(_loc2_ in param1)
            {
               _loc2_.dispose();
            }
            param1.length = 0;
         }
      }
      
      public function set state(param1:uint) : void
      {
         if(this._state != param1)
         {
            this._prevState = this._state;
            this._state = param1;
            this.clearTweens(this._tweensState);
            this.clearTweens(this._tweensLayout);
            this._hasStateAnim = true;
            this._hasLayoutAnim = true;
            invalidateState();
         }
      }
      
      public function get vehicleId() : int
      {
         return Boolean(this._data) ? int(this._data.vehicleId) : int(Values.DEFAULT_INT);
      }
      
      public function get isPickedState() : Boolean
      {
         return this._state == HB_VEHICLE_CARD_STATE.PICKED;
      }
      
      public function get isDeadState() : Boolean
      {
         return this._state == HB_VEHICLE_CARD_STATE.DEAD;
      }
      
      private function onRollOverHandler(param1:Event) : void
      {
         if(this._state == HB_VEHICLE_CARD_STATE.DEFAULT)
         {
            this.state = HB_VEHICLE_CARD_STATE.HOVER;
            this._hasLayoutAnim = false;
         }
      }
      
      private function onRollOutHandler(param1:Event) : void
      {
         if(this._state == HB_VEHICLE_CARD_STATE.HOVER)
         {
            this.state = HB_VEHICLE_CARD_STATE.DEFAULT;
            this._hasLayoutAnim = false;
         }
      }
      
      private function onClickHandler(param1:Event) : void
      {
         if(this._state == HB_VEHICLE_CARD_STATE.HOVER)
         {
            this.state = HB_VEHICLE_CARD_STATE.PICKED;
            dispatchEvent(new HBVehicleCardEvent(HBVehicleCardEvent.VEHICLE_PICK,this._data.vehicleId));
         }
      }
      
      private function onPickBtnClickHandler(param1:Event) : void
      {
         dispatchEvent(new HBVehicleCardEvent(HBVehicleCardEvent.VEHICLE_SELECT,this._data.vehicleId));
      }
   }
}
