package net.wg.frontline.gui.battle.views.frontlineInGameRank.events
{
   import flash.events.Event;
   
   public class FrontlineInGameRankEvent extends Event
   {
      
      public static const LEVEL_UP_ANIMATION_COMPLETE:String = "levelUpAnimationComplete";
       
      
      public function FrontlineInGameRankEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new FrontlineInGameRankEvent(type,bubbles,cancelable);
      }
   }
}
