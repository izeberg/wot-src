package net.wg.gui.lobby.hangar.quests
{
   import flash.display.Sprite;
   import flash.events.Event;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.constants.InvalidationType;
   
   public class Comp7Widget extends HangarWidgetInject
   {
      
      private static const WIDTH:int = 300;
      
      private static const HEIGHT:int = 230;
      
      private static const MARGIN_LEFT:int = -75;
      
      private static const MARGIN_LEFT_SMALL:int = -85;
      
      private static const MARGIN_RIGHT:int = -75;
      
      private static const MARGIN_RIGHT_SMALL:int = -85;
      
      private static const MARGIN_TOP:int = 0;
       
      
      public var bgImage:Sprite = null;
      
      private var _isSmall:Boolean = false;
      
      public function Comp7Widget()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         App.stage.addEventListener(Event.RESIZE,this.onStageResizeHandler,false,0,true);
         width = WIDTH;
         height = HEIGHT;
         x = -(WIDTH >> 1);
         this.bgImage.tabEnabled = this.bgImage.mouseEnabled = this.bgImage.mouseChildren = false;
         this.bgImage.hitArea = this;
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
         this.bgImage.hitArea = null;
         this.bgImage = null;
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
