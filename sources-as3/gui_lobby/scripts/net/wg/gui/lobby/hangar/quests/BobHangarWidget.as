package net.wg.gui.lobby.hangar.quests
{
   import flash.events.Event;
   import scaleform.clik.constants.InvalidationType;
   
   public class BobHangarWidget extends HangarWidgetInject
   {
      
      private static const WIDTH:int = 320;
      
      private static const HEIGHT:int = 240;
      
      private static const MARGIN_X:int = -(WIDTH >> 1);
       
      
      public function BobHangarWidget()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
      }
      
      override protected function configUI() : void
      {
         setSize(WIDTH,HEIGHT);
      }
      
      override public function get marginRight() : int
      {
         return MARGIN_X;
      }
      
      override public function get marginLeft() : int
      {
         return MARGIN_X;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            x = MARGIN_X;
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
      
      private function onStageResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
   }
}
