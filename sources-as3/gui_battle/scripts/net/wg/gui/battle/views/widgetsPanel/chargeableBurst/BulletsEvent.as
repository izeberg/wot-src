package net.wg.gui.battle.views.widgetsPanel.chargeableBurst
{
   import flash.events.Event;
   
   public class BulletsEvent extends Event
   {
      
      public static const RELOADING_ANIM_CHANGE:String = "onReloadingAnimChange";
      
      public static const BURST_SHOT_ANIM_COMPLETED:String = "onBurstShotAnimCompleted";
       
      
      private var _isAnimInReloadingState:Boolean = false;
      
      public function BulletsEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this._isAnimInReloadingState = param2;
      }
      
      public function get isAnimInReloadingState() : Boolean
      {
         return this._isAnimInReloadingState;
      }
   }
}
