package net.wg.gui.battle.pveBase.views.postmortemPanel.events
{
   import flash.events.Event;
   
   public class PvePostmortemPanelEvent extends Event
   {
      
      public static const UPDATE_TIME:String = "updateTime";
       
      
      private var _strTime:String = "";
      
      public function PvePostmortemPanelEvent(param1:String, param2:String, param3:Boolean = false, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this._strTime = param2;
      }
      
      override public function clone() : Event
      {
         return new PvePostmortemPanelEvent(type,this._strTime,bubbles,cancelable);
      }
      
      public function get strTime() : String
      {
         return this._strTime;
      }
   }
}
