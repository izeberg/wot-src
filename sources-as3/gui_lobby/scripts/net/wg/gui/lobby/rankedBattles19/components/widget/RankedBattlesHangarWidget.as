package net.wg.gui.lobby.rankedBattles19.components.widget
{
   import flash.events.Event;
   import net.wg.gui.lobby.hangar.quests.HangarWidgetInject;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   
   public class RankedBattlesHangarWidget extends HangarWidgetInject
   {
      
      private static const WIDTH:int = 384;
      
      private static const HEIGHT:int = 160;
      
      private static const MARGIN_LEFT:int = -65;
      
      private static const MARGIN_LEFT_SMALL:int = -72;
      
      private static const MARGIN_RIGHT:int = -75;
      
      private static const MARGIN_RIGHT_SMALL:int = -85;
      
      private static const MARGIN_TOP:int = 0;
       
      
      private var _isSmall:Boolean = false;
      
      public function RankedBattlesHangarWidget()
      {
         super();
         setManageSize(true);
         setSize(WIDTH,HEIGHT);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.stage.addEventListener(Event.RESIZE,this.onStageResizeHandler,false,0,true);
         width = WIDTH;
         height = HEIGHT;
         x = -(WIDTH >> 1);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this._isSmall = App.stage.stageHeight <= StageSizeBoundaries.HEIGHT_900;
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
      
      override protected function onDispose() : void
      {
         App.stage.removeEventListener(Event.RESIZE,this.onStageResizeHandler);
         super.onDispose();
      }
      
      override public function get marginRight() : int
      {
         return !!this._isSmall ? int(MARGIN_RIGHT_SMALL) : int(MARGIN_RIGHT);
      }
      
      override public function get marginLeft() : int
      {
         return !!this._isSmall ? int(MARGIN_LEFT_SMALL) : int(MARGIN_LEFT);
      }
      
      override public function get marginTop() : int
      {
         return MARGIN_TOP;
      }
      
      private function onStageResizeHandler(param1:Event) : void
      {
         invalidateSize();
      }
   }
}
