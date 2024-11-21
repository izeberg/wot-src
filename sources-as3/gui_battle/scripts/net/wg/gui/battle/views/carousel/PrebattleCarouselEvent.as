package net.wg.gui.battle.views.carousel
{
   import flash.events.Event;
   
   public class PrebattleCarouselEvent extends Event
   {
      
      public static const VIEW_HIDDEN:String = "onViewHidden";
      
      public static const VIEW_SHOWN:String = "onViewShown";
      
      public static const STATE_CHANGED:String = "onStateChanged";
       
      
      public var useAnim:Boolean = false;
      
      public function PrebattleCarouselEvent(param1:String, param2:Boolean = false, param3:Boolean = false, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this.useAnim = param2;
      }
      
      override public function clone() : Event
      {
         return new PrebattleCarouselEvent(type,this.useAnim,bubbles,cancelable);
      }
   }
}
