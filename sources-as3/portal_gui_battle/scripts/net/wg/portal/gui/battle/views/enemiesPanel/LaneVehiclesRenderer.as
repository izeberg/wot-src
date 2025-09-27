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
      
      private static const HEAVY_VEH_AMOUNT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const MEDIUM_VEH_AMOUNT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 2;
      
      private static const LIGHT_VEH_AMOUNT:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 3;
      
      private static const APPEARANCE_TWEEN_DURATION:uint = 500;
      
      private static const SLIDE_DOWN_TWEEN_DURATION:uint = 300;
      
      private static const APPEARANCE_TWEEN_OFFSET_Y:uint = 30;
       
      
      public var heavyVehAmount:VehicleTypesAmount = null;
      
      public var mediumVehAmount:VehicleTypesAmount = null;
      
      public var lightVehAmount:VehicleTypesAmount = null;
      
      public var vehiclesAmountTf:TextField = null;
      
      public var laneNameTf:TextField = null;
      
      public var laneStatusTf:TextField = null;
      
      public var bg:MovieClip = null;
      
      private var _hasInfo:Boolean = false;
      
      private var _isProtected:Boolean = false;
      
      private var _mediumVehAmountOriginX:int = 0;
      
      private var _lightVehAmountOriginX:int = 0;
      
      private var _appearanceTween:Tween = null;
      
      private var _slideDownTween:Tween = null;
      
      public function LaneVehiclesRenderer()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this._mediumVehAmountOriginX = this.mediumVehAmount.x;
         this._lightVehAmountOriginX = this.lightVehAmount.x;
      }
      
      override protected function onDispose() : void
      {
         this.clearAppearanceTween();
         this.clearSlideDownTweenTween();
         this.heavyVehAmount.dispose();
         this.heavyVehAmount = null;
         this.mediumVehAmount.dispose();
         this.mediumVehAmount = null;
         this.lightVehAmount.dispose();
         this.lightVehAmount = null;
         this.vehiclesAmountTf = null;
         this.laneNameTf = null;
         this.laneStatusTf = null;
         this.bg = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.laneStatusTf.text = PORTAL_EVENT.BATTLE_LANE_STATUS_PROTECTED;
         this.laneStatusTf.visible = false;
         this.setIsProtected(false);
         this.heavyVehAmount.vehicleType = VehicleTypes.HEAVY_TANK;
         this.heavyVehAmount.visible = false;
         this.mediumVehAmount.vehicleType = VehicleTypes.MEDIUM_TANK;
         this.mediumVehAmount.visible = false;
         this.lightVehAmount.vehicleType = VehicleTypes.LIGHT_TANK;
         this.lightVehAmount.visible = false;
      }
      
      override protected function draw() : void
      {
         if(this.heavyVehAmount.count >= 0 && isInvalid(HEAVY_VEH_AMOUNT))
         {
            this.heavyVehAmount.visible = true;
            this.updateVehAmountsX();
         }
         if(this.mediumVehAmount.count >= 0 && isInvalid(MEDIUM_VEH_AMOUNT))
         {
            this.mediumVehAmount.visible = true;
            this.updateVehAmountsX();
         }
         if(this.lightVehAmount.count >= 0 && isInvalid(LIGHT_VEH_AMOUNT))
         {
            this.lightVehAmount.visible = true;
            this.updateVehAmountsX();
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
      
      public function setVehicleInfo(param1:int, param2:int, param3:int) : void
      {
         var _loc4_:uint = this.toUint(param1) + this.toUint(param2) + this.toUint(param3);
         if(_loc4_ > 0)
         {
            if(param1 > 0 && !this.heavyVehAmount.visible)
            {
               invalidate(HEAVY_VEH_AMOUNT);
            }
            if(param2 > 0 && !this.mediumVehAmount.visible)
            {
               invalidate(MEDIUM_VEH_AMOUNT);
            }
            if(param3 > 0 && !this.lightVehAmount.visible)
            {
               invalidate(LIGHT_VEH_AMOUNT);
            }
            this.heavyVehAmount.count = param1;
            this.mediumVehAmount.count = param2;
            this.lightVehAmount.count = param3;
            this.vehiclesAmountTf.text = _loc4_.toString();
            this.setIsProtected(false);
         }
         else
         {
            this.setIsProtected(true);
         }
         this._hasInfo = true;
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
         this.vehiclesAmountTf.visible = !this._isProtected;
         this.laneStatusTf.visible = this._isProtected;
         this.bg.gotoAndStop(!!this._isProtected ? PROTECTED_BG_FRAME_INDEX : UNDER_ATTACK_BG_FRAME_INDEX);
         if(this._isProtected)
         {
            this.heavyVehAmount.count = Values.DEFAULT_INT;
            this.heavyVehAmount.visible = false;
            this.mediumVehAmount.count = Values.DEFAULT_INT;
            this.mediumVehAmount.visible = false;
            this.lightVehAmount.count = Values.DEFAULT_INT;
            this.lightVehAmount.visible = false;
         }
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
         if(this.heavyVehAmount.visible && this.mediumVehAmount.visible && this.lightVehAmount.visible)
         {
            this.mediumVehAmount.x = this._mediumVehAmountOriginX;
            this.lightVehAmount.x = this._lightVehAmountOriginX;
         }
         else if(this.heavyVehAmount.visible && this.mediumVehAmount.visible)
         {
            this.mediumVehAmount.x = this._mediumVehAmountOriginX;
         }
         else if(this.heavyVehAmount.visible && this.lightVehAmount.visible)
         {
            this.lightVehAmount.x = this._mediumVehAmountOriginX;
         }
         else if(this.mediumVehAmount.visible && this.lightVehAmount.visible)
         {
            this.mediumVehAmount.x = this.heavyVehAmount.x;
            this.lightVehAmount.x = this._mediumVehAmountOriginX;
         }
         else if(this.mediumVehAmount.visible)
         {
            this.mediumVehAmount.x = this.heavyVehAmount.x;
         }
         else if(this.lightVehAmount.visible)
         {
            this.lightVehAmount.x = this.heavyVehAmount.x;
         }
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
