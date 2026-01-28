package net.wg.gui.lobby.epicBattles.components
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import net.wg.data.constants.Values;
   
   public class EpicBattlesWidgetIntroButton extends EpicBattlesWidgetBaseButton
   {
      
      private static const FRAME_LABEL_SMALL_POSTFIX:String = "_small";
       
      
      public var widget:MovieClip = null;
      
      public var hitMc:MovieClip = null;
      
      public function EpicBattlesWidgetIntroButton()
      {
         super();
      }
      
      override protected function init() : void
      {
         this.updateOverState(false);
         this.widget.mouseEnabled = this.widget.mouseChildren = false;
         this.hitMc.buttonMode = true;
         this.hitMc.addEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.hitMc.addEventListener(MouseEvent.ROLL_OVER,onRollOverHandler);
         this.hitMc.addEventListener(MouseEvent.ROLL_OUT,onRollOutHandler);
      }
      
      override protected function onDispose() : void
      {
         this.hitMc.removeEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.hitMc.removeEventListener(MouseEvent.ROLL_OVER,onRollOverHandler);
         this.hitMc.removeEventListener(MouseEvent.ROLL_OUT,onRollOutHandler);
         this.hitMc = null;
         this.widget = null;
         super.onDispose();
      }
      
      override protected function updateOverState(param1:Boolean, param2:Boolean = false) : void
      {
         var _loc3_:String = !!isSmallHeight ? FRAME_LABEL_SMALL_POSTFIX : Values.EMPTY_STR;
         if(param2)
         {
            this.widget.gotoAndStop((!!param1 ? OUT : OVER) + _loc3_);
         }
         else
         {
            this.widget.gotoAndPlay((!!param1 ? OVER : OUT) + _loc3_);
         }
      }
      
      private function onClickHandler(param1:MouseEvent) : void
      {
         if(param1.target == this.hitMc && App.utils.commons.isLeftButton(param1))
         {
            dispatchClickEvent();
         }
      }
      
      override public function updateSize() : void
      {
         this.updateOverState(false,true);
      }
   }
}
