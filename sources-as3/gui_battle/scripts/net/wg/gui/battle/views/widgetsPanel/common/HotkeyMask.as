package net.wg.gui.battle.views.widgetsPanel.common
{
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class HotkeyMask extends Sprite implements IDisposable
   {
      
      private static const CENTRAL_SIDE_WIDTH:int = 28;
       
      
      public var leftSide:Sprite = null;
      
      public var rightSide:Sprite = null;
      
      public var centerSide:Sprite = null;
      
      private var _isDisposable:Boolean = false;
      
      public function HotkeyMask()
      {
         super();
      }
      
      public final function dispose() : void
      {
         this.leftSide = null;
         this.rightSide = null;
         this.centerSide = null;
         this._isDisposable = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposable;
      }
      
      public function setSize(param1:int) : void
      {
         var _loc2_:int = 0;
         _loc2_ = param1 - CENTRAL_SIDE_WIDTH >> 1;
         this.leftSide.width = _loc2_;
         this.rightSide.width = _loc2_;
         this.centerSide.x = _loc2_;
         this.rightSide.x = _loc2_ + CENTRAL_SIDE_WIDTH;
      }
   }
}
