package net.wg.data.constants.generated
{
   public class PILLBOX_SIEGE_WIDGET_CONST
   {
      
      public static const EMPTY:String = "empty";
      
      public static const IDLE:String = "idle";
      
      public static const SIEDGE:String = "siege";
      
      public static const PILLBOX:String = "pillbox";
      
      public static const IDLE_TO_SIEDGE:String = "idle_to_siege";
      
      public static const IDLE_TO_PILLBOX:String = "idle_to_pillbox";
      
      public static const SIEDGE_TO_IDLE:String = "siege_to_idle";
      
      public static const SIEDGE_TO_PILLBOX:String = "siege_to_pillbox";
      
      public static const PILLBOX_TO_IDLE:String = "pillbox_to_idle";
      
      public static const PILLBOX_TO_SIEDGE:String = "pillbox_to_siege";
      
      public static const PILLBOX_SIEGE_MECHANICS_WIDGET_STATE:Array = [IDLE,SIEDGE,PILLBOX,IDLE_TO_SIEDGE,IDLE_TO_PILLBOX,SIEDGE_TO_IDLE,SIEDGE_TO_PILLBOX,PILLBOX_TO_IDLE,PILLBOX_TO_SIEDGE];
      
      public static const PILLBOX_SIEGE_TRANSITIONS_STATE:Array = [IDLE_TO_SIEDGE,IDLE_TO_PILLBOX,SIEDGE_TO_IDLE,SIEDGE_TO_PILLBOX,PILLBOX_TO_IDLE,PILLBOX_TO_SIEDGE];
      
      public static const CONDITION_NORMAL:String = "normal";
      
      public static const CONDITION_WARNING:String = "warning";
      
      public static const CONDITION_CRITICAL:String = "critical";
      
      public static const PILLBOX_SIEGE_MECHANICS_WIDGET_CONDITION:Array = [CONDITION_NORMAL,CONDITION_WARNING,CONDITION_CRITICAL];
      
      public static const DEVICE_STATE_CRITICAL:String = "critical";
      
      public static const DEVICE_STATE_DESTROYED:String = "destroyed";
      
      public static const DEVICE_NONE:String = "None";
      
      public static const DEVICE_CHASSIS:String = "chassis";
      
      public static const DEVICE_ENGINE:String = "engine";
      
      public static const DEVICES:Array = [DEVICE_NONE,DEVICE_CHASSIS,DEVICE_ENGINE];
       
      
      public function PILLBOX_SIEGE_WIDGET_CONST()
      {
         super();
      }
   }
}
