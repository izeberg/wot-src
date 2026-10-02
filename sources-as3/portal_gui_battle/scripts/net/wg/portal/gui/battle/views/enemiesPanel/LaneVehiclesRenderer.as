package net.wg.portal.gui.battle.views.enemiesPanel
{
   import fl.motion.easing.Cubic;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.VehicleTypes;
   import net.wg.gui.battle.components.BattleDisplayable;
   import scaleform.clik.motion.Tween;
   
   public class LaneVehiclesRenderer extends BattleDisplayable
   {
      
      private static const UNDER_ATTACK_BG_FRAME_INDEX:uint = 1;
      
      private static const PROTECTED_BG_FRAME_INDEX:uint = 2;
      
      private static const INV_VEH_AMOUNT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const FLAG_HEAVY_VEH_AMOUNT:uint = 1 << 0;
      
      private static const FLAG_MEDIUM_VEH_AMOUNT:uint = 1 << 1;
      
      private static const FLAG_LIGHT_VEH_AMOUNT:uint = 1 << 2;
      
      private static const FLAG_SPG_VEH_AMOUNT:uint = 1 << 3;
      
      private static const FLAG_AT_SPG_VEH_AMOUNT:uint = 1 << 4;
      
      private static const APPEARANCE_TWEEN_DURATION:uint = 500;
      
      private static const SLIDE_DOWN_TWEEN_DURATION:uint = 300;
      
      private static const APPEARANCE_TWEEN_OFFSET_Y:uint = 30;
      
      private static const VEH_AMOUNT_START_X:uint = 170;
      
      private static const VEH_AMOUNT_OFFSET_X:uint = 45;
       
      
      public var atSpgVehAmount:VehicleTypesAmount = null;
      
      public var heavyVehAmount:VehicleTypesAmount = null;
      
      public var mediumVehAmount:VehicleTypesAmount = null;
      
      public var lightVehAmount:VehicleTypesAmount = null;
      
      public var spgVehAmount:VehicleTypesAmount = null;
      
      public var laneNameTf:TextField = null;
      
      public var laneStatusTf:TextField = null;
      
      public var bg:MovieClip = null;
      
      private var _hasInfo:Boolean = false;
      
      private var _isProtected:Boolean = false;
      
      private var _appearanceTween:Tween = null;
      
      private var _slideDownTween:Tween = null;
      
      private var _visibleVehicleTypesAmounts:Array;
      
      private var _readyVehAmountFlags:uint = 0;
      
      public function LaneVehiclesRenderer()
      {
         this._visibleVehicleTypesAmounts = [];
         super();
      }
      
      override protected function onDispose() : void
      {
         this.clearAppearanceTween();
         this.clearSlideDownTweenTween();
         this.atSpgVehAmount.dispose();
         this.atSpgVehAmount = null;
         this.heavyVehAmount.dispose();
         this.heavyVehAmount = null;
         this.mediumVehAmount.dispose();
         this.mediumVehAmount = null;
         this.lightVehAmount.dispose();
         this.lightVehAmount = null;
         this.spgVehAmount.dispose();
         this.spgVehAmount = null;
         this.laneNameTf = null;
         this.laneStatusTf = null;
         this.bg = null;
         this._visibleVehicleTypesAmounts.length = 0;
         this._visibleVehicleTypesAmounts = null;
         super.onDispose();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.laneStatusTf.text = PORTAL_EVENT.BATTLE_LANE_STATUS_PROTECTED;
         this.laneStatusTf.visible = false;
         this.setIsProtected(false);
         this.initVehAmount(this.atSpgVehAmount,VehicleTypes.AT_SPG,5);
         this.initVehAmount(this.heavyVehAmount,VehicleTypes.HEAVY_TANK,3);
         this.initVehAmount(this.mediumVehAmount,VehicleTypes.MEDIUM_TANK,2);
         this.initVehAmount(this.lightVehAmount,VehicleTypes.LIGHT_TANK,1);
         this.initVehAmount(this.spgVehAmount,VehicleTypes.SPG,4);
      }
      
      override protected function draw() : void
      {
         if(isInvalid(INV_VEH_AMOUNT))
         {
            this.drawVehAmount(this.atSpgVehAmount,FLAG_AT_SPG_VEH_AMOUNT);
            this.drawVehAmount(this.heavyVehAmount,FLAG_HEAVY_VEH_AMOUNT);
            this.drawVehAmount(this.mediumVehAmount,FLAG_MEDIUM_VEH_AMOUNT);
            this.drawVehAmount(this.lightVehAmount,FLAG_LIGHT_VEH_AMOUNT);
            this.drawVehAmount(this.spgVehAmount,FLAG_SPG_VEH_AMOUNT);
         }
         super.draw();
      }
      
      public function playAppearanceTween() : void
      {
         var _loc1_:int = y;
         this.clearAppearanceTween();
         alpha = 0;
         this.y = y - APPEARANCE_TWEEN_OFFSET_Y;
         this._appearanceTween = new Tween(APPEARANCE_TWEEN_DURATION,this,{
            "alpha":1,
            "y":_loc1_
         },{"ease":Cubic.easeInOut});
      }
      
      public function reset() : void
      {
         this._hasInfo = false;
         this.setIsProtected(false);
      }
      
      public function setNameLabel(param1:String) : void
      {
         this.laneNameTf.text = param1;
      }
      
      public function setVehicleInfo(param1:int, param2:int, param3:int, param4:int, param5:int) : void
      {
         var _loc6_:uint = this.toUint(param1) + this.toUint(param2) + this.toUint(param3) + this.toUint(param4) + this.toUint(param5);
         if(_loc6_ > 0)
         {
            invalidate(INV_VEH_AMOUNT);
            this.setupVehAmount(this.atSpgVehAmount,FLAG_AT_SPG_VEH_AMOUNT,param5);
            this.setupVehAmount(this.heavyVehAmount,FLAG_HEAVY_VEH_AMOUNT,param1);
            this.setupVehAmount(this.mediumVehAmount,FLAG_MEDIUM_VEH_AMOUNT,param2);
            this.setupVehAmount(this.lightVehAmount,FLAG_LIGHT_VEH_AMOUNT,param3);
            this.setupVehAmount(this.spgVehAmount,FLAG_SPG_VEH_AMOUNT,param4);
            this.atSpgVehAmount.count = param5;
            this.heavyVehAmount.count = param1;
            this.mediumVehAmount.count = param2;
            this.lightVehAmount.count = param3;
            this.spgVehAmount.count = param4;
            this.setIsProtected(false);
         }
         else
         {
            this.setIsProtected(true);
         }
         this._hasInfo = true;
      }
      
      private function setupVehAmount(param1:VehicleTypesAmount, param2:uint, param3:int) : void
      {
         if(param3 > 0 && !param1.visible)
         {
            this._readyVehAmountFlags |= param2;
         }
      }
      
      private function drawVehAmount(param1:VehicleTypesAmount, param2:uint) : void
      {
         if(param1.count >= 0 && (this._readyVehAmountFlags & param2) > 0)
         {
            this._readyVehAmountFlags &= ~param2;
            param1.visible = true;
            this._visibleVehicleTypesAmounts.push(param1);
            this.updateVehAmountsX();
         }
      }
      
      private function initVehAmount(param1:VehicleTypesAmount, param2:String, param3:int) : void
      {
         param1.vehicleType = param2;
         param1.visible = false;
         param1.priority = param3;
      }
      
      private function playSlideDownTween(param1:int) : void
      {
         this.clearAppearanceTween();
         this.clearSlideDownTweenTween();
         this._slideDownTween = new Tween(SLIDE_DOWN_TWEEN_DURATION,this,{
            "y":param1,
            "alpha":1
         },{"ease":Cubic.easeInOut});
      }
      
      private function setIsProtected(param1:Boolean) : void
      {
         if(this._isProtected == param1)
         {
            return;
         }
         this._isProtected = param1;
         this.laneStatusTf.visible = this._isProtected;
         this.bg.gotoAndStop(!!this._isProtected ? PROTECTED_BG_FRAME_INDEX : UNDER_ATTACK_BG_FRAME_INDEX);
         if(this._isProtected)
         {
            this._readyVehAmountFlags = 0;
            this.resetVehAmountToDefault(this.atSpgVehAmount);
            this.resetVehAmountToDefault(this.heavyVehAmount);
            this.resetVehAmountToDefault(this.mediumVehAmount);
            this.resetVehAmountToDefault(this.lightVehAmount);
            this.resetVehAmountToDefault(this.spgVehAmount);
            this._visibleVehicleTypesAmounts.length = 0;
         }
      }
      
      private function resetVehAmountToDefault(param1:VehicleTypesAmount) : void
      {
         param1.count = Values.DEFAULT_INT;
         param1.visible = false;
      }
      
      private function toUint(param1:int) : uint
      {
         if(param1 > 0)
         {
            return param1;
         }
         return 0;
      }
      
      private function updateVehAmountsX() : void
      {
         this._visibleVehicleTypesAmounts.sort(this.compareByPriority);
         var _loc1_:uint = this._visibleVehicleTypesAmounts.length;
         var _loc2_:VehicleTypesAmount = null;
         var _loc3_:int = VEH_AMOUNT_START_X;
         var _loc4_:uint = 0;
         while(_loc4_ < _loc1_)
         {
            _loc2_ = this._visibleVehicleTypesAmounts[_loc4_];
            _loc2_.x = _loc3_;
            _loc3_ -= VEH_AMOUNT_OFFSET_X;
            _loc4_++;
         }
      }
      
      private function compareByPriority(param1:VehicleTypesAmount, param2:VehicleTypesAmount) : int
      {
         var _loc3_:int = param1.priority;
         var _loc4_:int = param2.priority;
         if(_loc3_ > _loc4_)
         {
            return -1;
         }
         if(_loc3_ < _loc4_)
         {
            return 1;
         }
         return 0;
      }
      
      private function clearAppearanceTween() : void
      {
         if(this._appearanceTween)
         {
            this._appearanceTween.dispose();
            this._appearanceTween = null;
         }
      }
      
      private function clearSlideDownTweenTween() : void
      {
         if(this._slideDownTween)
         {
            this._slideDownTween.dispose();
            this._slideDownTween = null;
         }
      }
      
      override public function set y(param1:Number) : void
      {
         if(y < param1)
         {
            this.playSlideDownTween(param1);
         }
         else
         {
            super.y = param1;
         }
      }
      
      public function get hasInfo() : Boolean
      {
         return this._hasInfo;
      }
   }
}
