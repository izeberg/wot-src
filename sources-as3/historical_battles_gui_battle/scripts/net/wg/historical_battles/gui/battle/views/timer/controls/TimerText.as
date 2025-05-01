package net.wg.historical_battles.gui.battle.views.timer.controls
{
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.bootcamp.containers.AnimatedTextContainer;
   
   public class TimerText extends AnimatedTextContainer
   {
       
      
      public function TimerText()
      {
         super();
         textField.autoSize = TextFieldAutoSize.CENTER;
      }
   }
}
