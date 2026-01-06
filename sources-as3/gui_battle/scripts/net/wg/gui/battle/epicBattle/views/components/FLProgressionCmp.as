package net.wg.gui.battle.epicBattle.views.components
{
   import flash.events.Event;
   import net.wg.infrastructure.base.meta.IFLProgressionCmpMeta;
   import net.wg.infrastructure.base.meta.impl.FLProgressionCmpMeta;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class FLProgressionCmp extends FLProgressionCmpMeta implements IFLProgressionCmpMeta, IDisplayableComponent
   {
      
      public static const EVENT_VISIBILITY_CHANGED:String = "FLProgressionCmp_event_visibility_changed";
       
      
      private var _localVisibility:Boolean = false;
      
      private var _globalVisibility:Boolean = false;
      
      public function FLProgressionCmp()
      {
         super();
         setManageSize(false);
         name = "FLProgressionCmp";
      }
      
      public function as_updateVisibility(param1:Boolean) : void
      {
         this._localVisibility = param1;
         this.updateVisibility();
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         this._globalVisibility = param1;
         this.updateVisibility();
      }
      
      public function isCompVisible() : Boolean
      {
         return this._globalVisibility;
      }
      
      private function updateVisibility() : void
      {
         var _loc1_:Boolean = this._localVisibility && this._globalVisibility;
         if(visible == _loc1_)
         {
            return;
         }
         visible = _loc1_;
         dispatchEvent(new Event(EVENT_VISIBILITY_CHANGED));
      }
   }
}
