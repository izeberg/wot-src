package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import flash.display.Sprite;
   import flash.events.Event;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.Values;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class Penetrations extends Sprite implements IDisposable
   {
      
      private static const ANGLE_ITEM:int = 22;
      
      private static const ANGLE_GAP:int = 4;
      
      private static const ANGLE_STEP:int = ANGLE_ITEM + ANGLE_GAP;
      
      private static const HALF_ANGLE_STEP:int = ANGLE_STEP / 2;
       
      
      private var _disposed:Boolean = false;
      
      private var _items:Vector.<PenetrationItem>;
      
      public function Penetrations()
      {
         this._items = new Vector.<PenetrationItem>();
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
      
      public function isFullActivate() : Boolean
      {
         var _loc1_:PenetrationItem = null;
         for each(_loc1_ in this._items)
         {
            if(!_loc1_.isActive)
            {
               return false;
            }
         }
         return true;
      }
      
      public function isFullActivated() : Boolean
      {
         var _loc1_:PenetrationItem = null;
         for each(_loc1_ in this._items)
         {
            if(!_loc1_.isActivated)
            {
               return false;
            }
         }
         return true;
      }
      
      public function maxVisualAngle() : Number
      {
         return this._items.length > 0 ? Number(this._items[0].rotation + (ANGLE_ITEM >> 1)) : Number(Values.ZERO);
      }
      
      public function setup(param1:int) : void
      {
         this.remove(this._items.length - param1);
         this.add(param1 - this._items.length);
         this.layout();
      }
      
      public function update(param1:Number, param2:Boolean, param3:Boolean) : void
      {
         var _loc5_:PenetrationItem = null;
         var _loc4_:int = this._items.length;
         var _loc6_:int = Values.ZERO;
         while(_loc6_ < _loc4_)
         {
            _loc5_ = this._items[_loc6_];
            _loc5_.activate(_loc6_ < param1,param2,param3);
            _loc6_++;
         }
      }
      
      public function updateMode(param1:Boolean, param2:Boolean) : void
      {
         var _loc3_:PenetrationItem = null;
         for each(_loc3_ in this._items)
         {
            _loc3_.anim(param1,param2);
         }
      }
      
      private function remove(param1:int) : void
      {
         var _loc2_:PenetrationItem = null;
         while(param1 > 0)
         {
            _loc2_ = this._items.pop();
            _loc2_.removeEventListener(Event.COMPLETE,this.onItemActivateComplete);
            this.removeChild(_loc2_);
            _loc2_.dispose();
            param1--;
         }
         _loc2_ = null;
      }
      
      private function add(param1:int) : void
      {
         var _loc2_:PenetrationItem = null;
         while(param1 > 0)
         {
            _loc2_ = App.utils.classFactory.getComponent(Linkages.CHARGEABLE_BURST_PENETRATION,PenetrationItem);
            this.addChild(_loc2_);
            this._items.push(_loc2_);
            param1--;
         }
      }
      
      private function layout() : void
      {
         var _loc1_:PenetrationItem = null;
         var _loc2_:int = this._items.length - 1;
         var _loc3_:Number = HALF_ANGLE_STEP * _loc2_;
         var _loc4_:int = 0;
         for each(_loc1_ in this._items)
         {
            _loc1_.init(_loc3_,_loc4_ == _loc2_);
            _loc1_.addEventListener(Event.COMPLETE,this.onItemActivateComplete);
            _loc3_ -= ANGLE_STEP;
            _loc4_++;
         }
      }
      
      private function onItemActivateComplete(param1:Event) : void
      {
         dispatchEvent(new Event(Event.COMPLETE));
      }
   }
}
