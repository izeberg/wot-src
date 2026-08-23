package net.wg.gui.components.crosshairPanel.components.wt.components
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class IncreaseDamageIndicator extends SimpleDisposable
   {
      
      private static const START:String = "+";
      
      private static const END:String = "%";
      
      private static const PROGRESS_SCALE:uint = 10;
      
      private static const IDLE_FRAME_LBL:String = "idle";
      
      private static const SHOW_FRAME_LBL:String = "show";
      
      private static const UPDATE_FRAME_LBL:String = "update";
      
      private static const FAIL_FRAME_LBL:String = "fail";
      
      private static const END_FRAME_LBL:String = "_end";
       
      
      public var indicator:MovieClip;
      
      public var indicatorFail:MovieClip;
      
      public function IncreaseDamageIndicator()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.indicator = null;
         this.indicatorFail = null;
      }
      
      public function update(param1:uint, param2:Boolean = false, param3:Boolean = false) : void
      {
         if(param1 == 0)
         {
            gotoAndStop(IDLE_FRAME_LBL);
            return;
         }
         this.indicator.textField.text = START + param1 * PROGRESS_SCALE + END;
         if(param2)
         {
            this.indicatorFail.textField.text = START + param1 * PROGRESS_SCALE + END;
            this.gotoFrame(FAIL_FRAME_LBL,param3);
            return;
         }
         if(param1 == 1)
         {
            this.gotoFrame(SHOW_FRAME_LBL,param3);
         }
         else
         {
            this.gotoFrame(UPDATE_FRAME_LBL,param3);
         }
      }
      
      private function gotoFrame(param1:String, param2:Boolean = false) : void
      {
         if(param2)
         {
            gotoAndPlay(param1);
         }
         else
         {
            gotoAndStop(param1 + END_FRAME_LBL);
         }
      }
   }
}
