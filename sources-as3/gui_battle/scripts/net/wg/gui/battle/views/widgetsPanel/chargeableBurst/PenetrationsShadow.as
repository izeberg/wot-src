package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import flash.display.Sprite;
   import net.wg.data.constants.Linkages;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class PenetrationsShadow extends Sprite implements IDisposable
   {
      
      private static const ANGLE_ITEM:int = 22;
      
      private static const ANGLE_GAP:int = 4;
      
      private static const ANGLE_STEP:int = ANGLE_ITEM + ANGLE_GAP;
      
      private static const HALF_ANGLE_STEP:int = ANGLE_STEP / 2;
       
      
      private var _disposed:Boolean = false;
      
      private var _items:Vector.<Sprite>;
      
      public function PenetrationsShadow()
      {
         this._items = new Vector.<Sprite>();
         super();
      }
      
      public final function dispose() : void
      {
         this.remove(this._items.length);
         this._items = null;
         this._disposed = true;
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      public function setup(param1:Number) : void
      {
         this.remove(this._items.length - param1);
         this.add(param1 - this._items.length);
         this.layout();
      }
      
      private function remove(param1:int) : void
      {
         var _loc2_:Sprite = null;
         while(param1 > 0)
         {
            _loc2_ = this._items.pop();
            this.removeChild(_loc2_);
            param1--;
         }
         _loc2_ = null;
      }
      
      private function add(param1:int) : void
      {
         var _loc2_:Sprite = null;
         while(param1 > 0)
         {
            _loc2_ = App.utils.classFactory.getComponent(Linkages.CHARGEABLE_BURST_PENETRATION_SHADOW,Sprite);
            this.addChild(_loc2_);
            this._items.push(_loc2_);
            param1--;
         }
      }
      
      private function layout() : void
      {
         var _loc1_:Sprite = null;
         var _loc2_:int = this._items.length - 1;
         var _loc3_:Number = HALF_ANGLE_STEP * _loc2_;
         for each(_loc1_ in this._items)
         {
            _loc1_.rotation = _loc3_;
            _loc3_ -= ANGLE_STEP;
         }
      }
   }
}
