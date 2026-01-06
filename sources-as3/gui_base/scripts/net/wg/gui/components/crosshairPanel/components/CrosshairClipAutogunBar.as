package net.wg.gui.components.crosshairPanel.components
{
   import flash.display.Graphics;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class CrosshairClipAutogunBar extends CrosshairClipQuantityBar
   {
      
      private static const ZERO_VALUE_ALPHA:Number = 0.5;
      
      private static const UNAVAILABLE_NUM:String = "X ";
      
      private static const ZERO_STRING:String = "0";
       
      
      public var valueTF:TextField = null;
      
      public var valueBG:MovieClip = null;
      
      public var maskMC:MovieClip = null;
      
      private var _initClipCapacityNumsCount:int = 0;
      
      public function CrosshairClipAutogunBar()
      {
         super();
      }
      
      override public function initialize(param1:String, param2:Number, param3:Number, param4:Number, param5:Boolean) : void
      {
         super.initialize(param1,param2,param3,param4,param5);
         this._initClipCapacityNumsCount = param2.toString().length;
      }
      
      override public function dispose() : void
      {
         this.valueTF = null;
         this.valueBG = null;
         this.maskMC = null;
         super.dispose();
      }
      
      override public function updateInfo(param1:Number, param2:String, param3:Boolean) : void
      {
         var _loc5_:uint = 0;
         quantityInClipBar.gotoAndStop(param2);
         this.valueTF.alpha = param1 > Values.ZERO ? Number(Values.DEFAULT_ALPHA) : Number(ZERO_VALUE_ALPHA);
         var _loc4_:String = Values.EMPTY_STR;
         if(param1 < Values.ZERO)
         {
            _loc5_ = 0;
            while(_loc5_ < this._initClipCapacityNumsCount)
            {
               _loc4_ += UNAVAILABLE_NUM;
               _loc5_++;
            }
         }
         else
         {
            _loc4_ = StringUtils.leftPadChar(param1.toString(),this._initClipCapacityNumsCount,ZERO_STRING).split("").join(" ");
         }
         this.valueTF.text = _loc4_;
         this.valueBG.gotoAndStop(this._initClipCapacityNumsCount);
         this.drawMask(param1 / _initClipCapacity);
      }
      
      private function drawMask(param1:Number) : void
      {
         var _loc2_:Number = NaN;
         var _loc3_:Number = NaN;
         var _loc15_:Number = NaN;
         var _loc16_:uint = 0;
         _loc2_ = 0.542;
         _loc3_ = 0.664;
         var _loc4_:Number = (_loc3_ - _loc2_) * param1 + _loc2_;
         var _loc5_:uint = 3;
         var _loc6_:Number = 6.2831;
         var _loc7_:uint = 40;
         var _loc8_:uint = 170;
         var _loc9_:Number = 0.5;
         var _loc10_:Number = _loc9_ * _loc6_;
         var _loc11_:Number = _loc4_ * _loc6_ - _loc10_;
         var _loc12_:Graphics = this.maskMC.graphics;
         _loc12_.clear();
         _loc12_.beginFill(16711935,1);
         _loc12_.moveTo(Math.sin(_loc10_) * _loc8_,-Math.cos(_loc10_) * _loc8_);
         var _loc13_:Number = _loc8_ - _loc7_;
         var _loc14_:uint = Math.round(_loc11_ * _loc5_);
         _loc16_ = 0;
         while(_loc16_ <= _loc14_)
         {
            _loc15_ = _loc16_ / _loc14_ * _loc11_ + _loc10_;
            _loc12_.lineTo(Math.sin(_loc15_) * _loc8_,-Math.cos(_loc15_) * _loc8_);
            _loc16_++;
         }
         _loc16_ = 0;
         while(_loc16_ <= _loc14_)
         {
            _loc15_ = (_loc14_ - _loc16_) / _loc14_ * _loc11_ + _loc10_;
            _loc12_.lineTo(Math.sin(_loc15_) * _loc13_,-Math.cos(_loc15_) * _loc13_);
            _loc16_++;
         }
         _loc12_.endFill();
      }
   }
}
