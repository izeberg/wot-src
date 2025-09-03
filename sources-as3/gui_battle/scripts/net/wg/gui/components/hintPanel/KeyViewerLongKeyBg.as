package net.wg.gui.components.hintPanel
{
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class KeyViewerLongKeyBg extends Sprite implements IDisposable
   {
       
      
      public var leftSide:Sprite = null;
      
      public var rightSide:Sprite = null;
      
      public var center:Sprite = null;
      
      public var lid:Sprite = null;
      
      private var _isDisposed:Boolean = false;
      
      private var _minWidth:int = 0;
      
      public function KeyViewerLongKeyBg()
      {
         super();
         this._minWidth = this.leftSide.width + this.rightSide.width + this.center.width;
      }
      
      public final function dispose() : void
      {
         this.lid = null;
         this.leftSide = null;
         this.rightSide = null;
         this.center = null;
         this._isDisposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._isDisposed;
      }
      
      public function setWidth(param1:int) : void
      {
         param1 = Math.max(this._minWidth,param1);
         this.lid.x = param1 >> 1;
         var _loc2_:int = param1 - this.center.width >> 1;
         this.leftSide.width = this.rightSide.width = _loc2_;
         this.center.x = _loc2_;
         this.rightSide.x = _loc2_ + this.center.width;
      }
   }
}
