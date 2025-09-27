package net.wg.gui.components.crosshairPanel.constants
{
   import flash.filters.ColorMatrixFilter;
   
   public class CrosshairConsts
   {
      
      public static const RELOADING_INIT:String = "reloadingInit";
      
      public static const RELOADING_PROGRESS:String = "reloadingProgress";
      
      public static const RELOADING_END:String = "reloadingEnd";
      
      public static const RELOADING_ENDED:String = "reloadingEnded";
      
      public static const RELOADING_IMPOSSIBLE_AMMO_ENDED:String = "reloadingImpossibleAmmoEnded";
      
      public static const PROGRESS_TOTAL_FRAMES_COUNT:int = 60;
      
      public static const MS_IN_SECOND:Number = 1000;
      
      public static const COUNTER_UPDATE_TICK:Number = 90;
      
      public static const ANIMATION_UPDATE_TICK:Number = 50;
      
      public static const MAX_HEALTH:Number = 1;
      
      public static const GRAYSCALE_FILTER:ColorMatrixFilter = new ColorMatrixFilter([0.2225,0.7169,0.0606,0,0,0.2225,0.7169,0.0606,0,0,0.2225,0.7169,0.0606,0,0,0,0,0,1,0]);
       
      
      public function CrosshairConsts()
      {
         super();
      }
   }
}
