package net.wg.gui.battle.views.widgetsPanel
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import net.wg.gui.battle.views.decorativeCrosshair.shared.TextWrapper;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class StanceDanceSpeedWidget extends MovieClip implements IDisposable
   {
      
      private static const COLOR_BASE:uint = 16711680;
      
      private static const COLOR_UNAVAILABLE:uint = 65280;
      
      private static const COLOR_CHARGE:uint = 16711935;
      
      private static const COLOR_CHARGE_ACTIVE:uint = 255;
      
      private static const ARC_START:Number = Math.PI * 0.75;
      
      private static const ARC_LENGTH:Number = Math.PI * 1.5;
      
      private static const RADIUS:Number = 70;
      
      private static const STEPS:int = 100;
      
      private static const MAX_POINTER_STEPS:int = 100;
      
      private static const IDLE_FRAME:int = 1;
      
      private static const ACTIVE_FRAME:int = 2;
       
      
      public var baseSpeed:Sprite = null;
      
      public var passiveActive:MovieClip = null;
      
      public var baseSpeedActive:MovieClip = null;
      
      public var chargeZone:Sprite = null;
      
      public var chargeZoneActive:Sprite = null;
      
      public var unavailableSpeed:Sprite = null;
      
      public var unavailableTurboSpeed:MovieClip = null;
      
      public var switchTimer:Timer = null;
      
      public var pointer:MovieClip = null;
      
      public var pointerTurbo:MovieClip = null;
      
      public var pointerActive:MovieClip = null;
      
      public var text:TextWrapper = null;
      
      public var textActive:TextWrapper = null;
      
      private var _baseSpeedMask:Sprite = null;
      
      private var _baseSpeedActiveMask:Sprite = null;
      
      private var _chargeZoneMask:Sprite = null;
      
      private var _chargeZoneActiveMask:Sprite = null;
      
      private var _unavailableMask:Sprite = null;
      
      private var _unavailableTurboMask:Sprite = null;
      
      private var _passiveActiveMask:Sprite = null;
      
      private var _maxSpeed:int = 0;
      
      private var _maxActiveSpeed:int = 0;
      
      private var _maxPassiveSpeed:int = 0;
      
      private var _totalMaxSpeed:int = 0;
      
      private var _chargeZoneStart:int = 0;
      
      private var _isDisposed:Boolean = false;
      
      public function StanceDanceSpeedWidget()
      {
         super();
         this._unavailableMask = this.createMask("unavailableMask");
         this._unavailableTurboMask = this.createMask("unavailableTurboMask");
         this._baseSpeedMask = this.createMask("baseMask");
         this._chargeZoneMask = this.createMask("chargeZoneMask");
         this._baseSpeedActiveMask = this.createMask("baseSpeedActiveMask");
         this._chargeZoneActiveMask = this.createMask("chargeZoneActiveMask");
         this._passiveActiveMask = this.createMask("passiveActiveMask");
         this.baseSpeed.mask = this._baseSpeedMask;
         this.unavailableSpeed.mask = this._unavailableMask;
         this.unavailableTurboSpeed.mask = this._unavailableTurboMask;
         this.chargeZone.mask = this._chargeZoneMask;
         this.passiveActive.mask = this._passiveActiveMask;
         this.baseSpeedActive.mask = this._baseSpeedActiveMask;
         this.chargeZoneActive.mask = this._chargeZoneActiveMask;
         this.chargeZoneActive.visible = false;
      }
      
      private static function drawSector(param1:Sprite, param2:Sprite, param3:Number, param4:Number, param5:uint) : void
      {
         var _loc9_:Number = NaN;
         var _loc10_:Number = NaN;
         var _loc11_:Number = NaN;
         var _loc12_:Number = NaN;
         var _loc6_:Number = param2.width / 2;
         var _loc7_:Number = param2.height / 2;
         param1.graphics.clear();
         param1.graphics.beginFill(param5);
         param1.graphics.moveTo(_loc6_,_loc7_);
         var _loc8_:int = 0;
         while(_loc8_ <= STEPS)
         {
            _loc9_ = _loc8_ / STEPS;
            _loc10_ = param3 + param4 * _loc9_;
            _loc11_ = _loc6_ + Math.cos(_loc10_) * RADIUS;
            _loc12_ = _loc7_ + Math.sin(_loc10_) * RADIUS;
            param1.graphics.lineTo(_loc11_,_loc12_);
            _loc8_++;
         }
         param1.graphics.lineTo(_loc6_,_loc7_);
         param1.graphics.endFill();
         param1.x = param2.x;
         param1.y = param2.y;
      }
      
      private function createMask(param1:String) : Sprite
      {
         var _loc2_:Sprite = new Sprite();
         _loc2_.name = param1;
         addChild(_loc2_);
         return _loc2_;
      }
      
      public function draw(param1:Number, param2:Number, param3:Number, param4:Number) : void
      {
         this._maxSpeed = param1;
         this._maxActiveSpeed = param2;
         this._maxPassiveSpeed = param3;
         this._chargeZoneStart = param4;
         this._totalMaxSpeed = this._maxSpeed + this._maxActiveSpeed + this._maxPassiveSpeed;
         this.drawBaseMask();
         this.drawBaseActiveMask();
         this.drawChargeZoneMask();
         this.drawChargeZoneActiveMask();
         this.drawUnavailableMask();
         this.drawUnavailableTurboMask();
         this.drawPassiveActiveMask();
      }
      
      public function setTransitionTimer(param1:Number) : void
      {
         this.switchTimer.setLabel(param1);
      }
      
      public function setSpeed(param1:Number, param2:Boolean) : void
      {
         var _loc3_:String = Math.abs(param1).toString();
         this.text.setText(_loc3_);
         this.textActive.setText(_loc3_);
         this.chargeZoneActive.visible = param1 > this._chargeZoneStart;
         this.baseSpeedActive.gotoAndStop(!!param2 ? ACTIVE_FRAME : IDLE_FRAME);
         this.unavailableTurboSpeed.gotoAndStop(!!param2 ? ACTIVE_FRAME : IDLE_FRAME);
         var _loc4_:Number = Math.abs(param1 / this._totalMaxSpeed);
         this.pointer.gotoAndStop(MAX_POINTER_STEPS * _loc4_);
         this.pointerTurbo.gotoAndStop(MAX_POINTER_STEPS * _loc4_);
         this.pointerActive.gotoAndStop(MAX_POINTER_STEPS * _loc4_);
      }
      
      private function drawBaseMask() : void
      {
         var _loc1_:Number = (this._maxSpeed + this._maxPassiveSpeed) / this._totalMaxSpeed;
         drawSector(this._baseSpeedMask,this.baseSpeed,ARC_START,ARC_LENGTH * _loc1_,COLOR_BASE);
      }
      
      private function drawUnavailableMask() : void
      {
         var _loc1_:Number = this._maxSpeed / this._totalMaxSpeed;
         drawSector(this._unavailableMask,this.unavailableSpeed,ARC_START,ARC_LENGTH * _loc1_,COLOR_UNAVAILABLE);
      }
      
      private function drawUnavailableTurboMask() : void
      {
         var _loc1_:Number = (this._maxSpeed + this._maxPassiveSpeed) / this._totalMaxSpeed;
         drawSector(this._unavailableTurboMask,this.unavailableTurboSpeed,ARC_START + ARC_LENGTH * _loc1_,ARC_LENGTH * (1 - _loc1_),255);
      }
      
      private function drawChargeZoneMask() : void
      {
         var _loc1_:Number = this._chargeZoneStart / this._totalMaxSpeed;
         var _loc2_:Number = (this._maxSpeed + this._maxPassiveSpeed) / this._totalMaxSpeed;
         drawSector(this._chargeZoneMask,this.chargeZone,ARC_START + ARC_LENGTH * _loc1_,ARC_LENGTH * (_loc2_ - _loc1_),COLOR_CHARGE);
      }
      
      private function drawChargeZoneActiveMask() : void
      {
         var _loc1_:Number = this._chargeZoneStart / this._totalMaxSpeed;
         var _loc2_:Number = (this._maxSpeed + this._maxPassiveSpeed) / this._totalMaxSpeed;
         drawSector(this._chargeZoneActiveMask,this.chargeZoneActive,ARC_START + ARC_LENGTH * _loc1_,ARC_LENGTH * (_loc2_ - _loc1_),COLOR_CHARGE_ACTIVE);
      }
      
      private function drawBaseActiveMask() : void
      {
         var _loc1_:Number = (this._maxSpeed + this._maxPassiveSpeed) / this._totalMaxSpeed;
         drawSector(this._baseSpeedActiveMask,this.baseSpeedActive,ARC_START,ARC_LENGTH * _loc1_,COLOR_BASE);
      }
      
      private function drawPassiveActiveMask() : void
      {
         var _loc1_:Number = (this._maxSpeed + this._maxPassiveSpeed) / this._totalMaxSpeed;
         drawSector(this._passiveActiveMask,this.passiveActive,ARC_START,ARC_LENGTH * _loc1_,COLOR_BASE);
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function dispose() : void
      {
         this._isDisposed = true;
         this._baseSpeedMask = null;
         this._baseSpeedActiveMask = null;
         this._chargeZoneMask = null;
         this._chargeZoneActiveMask = null;
         this._unavailableMask = null;
         this._unavailableTurboMask = null;
         this.baseSpeed = null;
         this.baseSpeedActive = null;
         this.chargeZone = null;
         this.chargeZoneActive = null;
         this.unavailableSpeed = null;
         this.unavailableTurboSpeed = null;
         this.switchTimer.dispose();
         this.switchTimer = null;
      }
   }
}
