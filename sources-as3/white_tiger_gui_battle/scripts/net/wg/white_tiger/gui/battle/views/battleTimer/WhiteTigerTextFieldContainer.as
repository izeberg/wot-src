package net.wg.white_tiger.gui.battle.views.battleTimer
{
   import net.wg.gui.components.controls.TextFieldContainer;
   
   public class WhiteTigerTextFieldContainer extends TextFieldContainer
   {
       
      
      public function WhiteTigerTextFieldContainer()
      {
         super();
      }
      
      override protected function updateSize() : void
      {
         super.updateSize();
         textField.x = -textField.width | 0;
         textField.y = -textField.height >> 1;
      }
   }
}
