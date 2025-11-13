package net.wg.gui.components.crosshairPanel.components.hitIndicator
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class HitArrow extends SimpleDisposable
   {
      
      private static const FRAME_SHOW_ANIMATION:int = 2;
       
      
      public var arrow:MovieClip;
      
      public function HitArrow()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.arrow = null;
         super.onDispose();
      }
      
      public function show(param1:String) : void
      {
         gotoAndPlay(FRAME_SHOW_ANIMATION);
         if(this.arrow.currentLabel != param1)
         {
            this.arrow.gotoAndStop(param1);
         }
      }
   }
}
