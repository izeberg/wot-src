package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import flash.display.Sprite;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class BulletsShadow extends Sprite implements IDisposable
   {
      
      private static const MIN_BULLETS_COUNT:int = 2;
      
      private static const BULLET_WIDTH:int = 6;
       
      
      public var shadow:Sprite = null;
      
      private var _shadowMinWidth:int = 0;
      
      private var _disposed:Boolean = false;
      
      public function BulletsShadow()
      {
         super();
         this._shadowMinWidth = this.shadow.width;
      }
      
      public final function dispose() : void
      {
         this.shadow = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setup(param1:Number) : void
      {
         var _loc2_:int = Values.ZERO;
         if(param1 > MIN_BULLETS_COUNT)
         {
            _loc2_ = (param1 - MIN_BULLETS_COUNT) * BULLET_WIDTH;
            this.shadow.width = this._shadowMinWidth + _loc2_;
         }
      }
   }
}
