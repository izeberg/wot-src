package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.geom.Point;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.utils.IAssertable;
   
   public class HotkeySettings implements IDisposable
   {
      
      public static const DIRECTION_FORWARD:String = "straightForward";
      
      public static const DIRECTION_BACKWARD:String = "straightBackward";
      
      public static const DIRECTION_UP:String = "straightUp";
      
      public static const DIRECTION_DOWN:String = "straightDown";
      
      private static const ASSERT_INIT_MSG:String = "HotkeySettings: items size must be inited before getting anchorX, anchorY";
       
      
      private var _gapX:uint = 0;
      
      private var _gapY:uint = 0;
      
      private var _direction:String = null;
      
      private var _anchorCenter:Boolean = false;
      
      private var _anchor:Point = null;
      
      private var _horizontalShift:int = 0;
      
      private var _verticalShift:int = 0;
      
      private var _wasInited:Boolean = false;
      
      private var _isDisposed:Boolean = false;
      
      private var _asserter:IAssertable;
      
      public function HotkeySettings(param1:Point, param2:Boolean, param3:String, param4:uint, param5:uint)
      {
         this._asserter = App.utils.asserter;
         super();
         this._anchor = param1;
         this._anchorCenter = param2;
         this._direction = param3;
         this._gapX = param4;
         this._gapY = param5;
      }
      
      protected function onDispose() : void
      {
         this._anchor = null;
         this._asserter = null;
      }
      
      public final function dispose() : void
      {
         if(this._isDisposed)
         {
            return;
         }
         this.onDispose();
         this._isDisposed = true;
      }
      
      public final function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function calcHorizontalStep(param1:uint) : int
      {
         if(this.isVertical)
         {
            return Values.ZERO;
         }
         param1 += this._gapX;
         if(this._direction == DIRECTION_BACKWARD)
         {
            return -param1;
         }
         return param1;
      }
      
      public function calcVerticalStep(param1:uint) : int
      {
         if(this.isHorizontal)
         {
            return Values.ZERO;
         }
         param1 += this._gapY;
         if(this._direction == DIRECTION_UP)
         {
            return -param1;
         }
         return param1;
      }
      
      public function initItemsSize(param1:uint, param2:uint, param3:uint) : void
      {
         if(this._anchorCenter)
         {
            if(this._direction == HotkeySettings.DIRECTION_FORWARD)
            {
               this._horizontalShift = -(param1 + (param3 - 1) * this._gapX >> 1);
            }
            else if(this._direction == HotkeySettings.DIRECTION_BACKWARD)
            {
               this._horizontalShift = param1 + (param3 - 1) * this._gapX >> 1;
            }
            else if(this._direction == HotkeySettings.DIRECTION_DOWN)
            {
               this._verticalShift = -(param2 + (param3 - 1) * this._gapY >> 1);
            }
            else if(this._direction == HotkeySettings.DIRECTION_UP)
            {
               this._verticalShift = param2 + (param3 - 1) * this._gapY >> 1;
            }
         }
         this._wasInited = true;
      }
      
      public function get anchorX() : int
      {
         this._asserter.assert(this._wasInited,ASSERT_INIT_MSG);
         return this._anchor.x + this._horizontalShift;
      }
      
      public function get anchorY() : int
      {
         this._asserter.assert(this._wasInited,ASSERT_INIT_MSG);
         return this._anchor.y + this._verticalShift;
      }
      
      private function get isHorizontal() : Boolean
      {
         return this._direction == DIRECTION_FORWARD || this._direction == DIRECTION_BACKWARD;
      }
      
      private function get isVertical() : Boolean
      {
         return this._direction == DIRECTION_UP || this._direction == DIRECTION_DOWN;
      }
   }
}
