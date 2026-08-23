package net.wg.gui.components.crosshairPanel.components.wt.components
{
   import flash.display.MovieClip;
   import net.wg.gui.components.crosshairPanel.components.wt.IncreaseDamage;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class IncreaseDamageProgress extends SimpleDisposable
   {
      
      private static const PROGRESS_FRAME_LBL:String = "progress";
      
      private static const SHOW_FRAME_LBL:String = "show";
      
      private static const END_FRAME_LBL:String = "_end";
       
      
      public var progress:MovieClip;
      
      public var progressGlow:MovieClip;
      
      public var finalGlow:MovieClip;
      
      public var failGlow:MovieClip;
      
      public var fail:MovieClip;
      
      public function IncreaseDamageProgress()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.progress = null;
         this.progressGlow = null;
         this.finalGlow = null;
         this.failGlow = null;
         this.fail = null;
      }
      
      public function update(param1:uint, param2:Boolean = false, param3:Boolean = false) : void
      {
         if(param2 && param1 > 0)
         {
            this.fail.visible = true;
            this.failGlow.visible = true;
            this.fail.gotoAndStop(param1);
            this.failGlow.gotoAndStop(param1);
            return;
         }
         this.fail.visible = false;
         this.failGlow.visible = false;
         this.gotoFrame(this.progress,PROGRESS_FRAME_LBL + param1,param3);
         this.gotoFrame(this.progressGlow,PROGRESS_FRAME_LBL + param1,param3);
         var _loc4_:Boolean = param1 == IncreaseDamage.MAX_PROGRESS;
         this.finalGlow.visible = _loc4_;
         if(_loc4_)
         {
            this.gotoFrame(this.finalGlow,SHOW_FRAME_LBL,param3);
         }
      }
      
      private function gotoFrame(param1:MovieClip, param2:String, param3:Boolean = false) : void
      {
         if(param3)
         {
            param1.gotoAndPlay(param2);
         }
         else
         {
            param1.gotoAndStop(param2 + END_FRAME_LBL);
         }
      }
   }
}
