package net.wg.gui.battle.views.thermalVisionPanel
{
   import flash.display.MovieClip;
   import net.wg.gui.battle.views.rocketAcceleratorPanel.RocketAcceleratorPanel;
   
   public class ThermalVisionPanel extends RocketAcceleratorPanel
   {
      
      private static const PROGRESS_Y:int = 21;
      
      private static const PROGRESS_H_FULL:int = PROGRESS_Y - 3;
      
      private static const OFFSET_X:int = 35;
      
      private static const OFFSET_Y:int = 40;
      
      private static const TIMER_PRECISION:int = 1;
       
      
      public var count:MovieClip;
      
      public var timer:MovieClip;
      
      public function ThermalVisionPanel()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         countTF = this.count.countTF;
         timerTF = this.timer.timerTF;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         progressMask.y = PROGRESS_Y;
      }
      
      override protected function onDispose() : void
      {
         this.count = null;
         this.timer = null;
         super.onDispose();
      }
      
      override public function as_setActiveTime(param1:Number) : void
      {
         if(_time == param1)
         {
            return;
         }
         _time = param1;
         timerTF.visible = param1 > 0;
         if(timerTF.visible)
         {
            timerTF.text = param1.toFixed(TIMER_PRECISION);
         }
      }
      
      override public function as_setProgress(param1:Number) : void
      {
         progressMask.y = PROGRESS_Y - PROGRESS_H_FULL * param1 | 0;
      }
      
      override public function as_updateLayout(param1:Number, param2:Number) : void
      {
         this.x = param1 + OFFSET_X | 0;
         this.y = param2 + OFFSET_Y | 0;
      }
   }
}
