package net.wg.gui.components.crosshairPanel.components.wt
{
   import flash.display.MovieClip;
   import net.wg.gui.components.crosshairPanel.components.wt.components.IncreaseDamageIndicator;
   import net.wg.gui.components.crosshairPanel.components.wt.components.IncreaseDamageProgress;
   import net.wg.gui.components.crosshairPanel.components.wt.events.IncreaseDamageEvent;
   import net.wg.infrastructure.base.SimpleDisposable;
   
   public class IncreaseDamage extends SimpleDisposable
   {
      
      public static const MAX_PROGRESS:uint = 5;
      
      private static const SHOW_FRAME_LBL:String = "show";
      
      private static const HIDE_FRAME_LBL:String = "hide";
      
      private static const END_FRAME_LBL:String = "_end";
      
      private static const LINE_ALPHA:Number = 0.52;
      
      private static const LINE_FAIL_ALPHA:Number = 0.28;
      
      private static const LINE_FINAL_ALPHA:Number = 1;
       
      
      public var leftProgress:IncreaseDamageProgress;
      
      public var rightProgress:IncreaseDamageProgress;
      
      public var indicator:IncreaseDamageIndicator;
      
      public var line:MovieClip;
      
      private var _curProgress:uint = 0;
      
      private var _isFail:Boolean = false;
      
      private var _totalFrames:int = 0;
      
      private var _line:MovieClip;
      
      public function IncreaseDamage()
      {
         super();
         this._totalFrames = totalFrames;
         addFrameScript(this._totalFrames - 1,this.onHideComplete);
         this._line = this.line.line;
      }
      
      override protected function onDispose() : void
      {
         addFrameScript(this._totalFrames - 1,null);
         this.leftProgress.dispose();
         this.leftProgress = null;
         this.rightProgress.dispose();
         this.rightProgress = null;
         this.indicator.dispose();
         this.indicator = null;
         this.line = null;
         this._line = null;
      }
      
      public function hide(param1:Boolean) : void
      {
         if(param1)
         {
            gotoAndPlay(HIDE_FRAME_LBL);
         }
         else
         {
            this.onHideComplete();
         }
      }
      
      public function show(param1:Boolean) : void
      {
         this._curProgress = 0;
         this._isFail = false;
         this.leftProgress.update(0);
         this.rightProgress.update(0);
         this.indicator.update(0);
         this._line.alpha = LINE_ALPHA;
         visible = true;
         if(param1)
         {
            gotoAndPlay(SHOW_FRAME_LBL);
         }
         else
         {
            gotoAndStop(SHOW_FRAME_LBL + END_FRAME_LBL);
         }
      }
      
      public function update(param1:uint, param2:Boolean, param3:Boolean) : void
      {
         if(param1 > MAX_PROGRESS)
         {
            return;
         }
         if(param1 == MAX_PROGRESS)
         {
            this._line.alpha = LINE_FINAL_ALPHA;
         }
         if(param2)
         {
            this._line.alpha = LINE_FAIL_ALPHA;
         }
         if(this._curProgress != param1 || this._isFail != param2)
         {
            this._curProgress = param1;
            this._isFail = param2;
            this.leftProgress.update(param1,param2,param3);
            this.rightProgress.update(param1,param2,param3);
            this.indicator.update(param1,param2,param3);
         }
      }
      
      private function onHideComplete() : void
      {
         visible = false;
         dispatchEvent(new IncreaseDamageEvent(IncreaseDamageEvent.HIDE_COMPLETE));
      }
   }
}
