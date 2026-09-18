package net.wg.gui.lobby.fortifications.cmp.events
{
   import flash.events.Event;
   
   public class FortVehicleSelectorFilterEvent extends Event
   {
      
      public static const FORT_FILTER_CHANGE:String = "fortFiltersChanged";
       
      
      public var isHideFrozen:Boolean;
      
      public function FortVehicleSelectorFilterEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
   }
}
