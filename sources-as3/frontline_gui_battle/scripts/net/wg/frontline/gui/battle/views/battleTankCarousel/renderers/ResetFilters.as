package net.wg.frontline.gui.battle.views.battleTankCarousel.renderers
{
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.components.controls.SoundButtonEx;
   
   public class ResetFilters extends BattleUIComponent
   {
       
      
      public var textField:TextField = null;
      
      public var resetButton:SoundButtonEx = null;
      
      public function ResetFilters()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.textField.text = FL_COMMON.BATTLECAROUSEL_RESETFILTERS_TITLE;
         this.resetButton.label = FL_COMMON.BATTLECAROUSEL_RESETFILTERS_BUTTON;
         this.validateSize();
      }
      
      override protected function draw() : void
      {
         if(isInvalid(InvalidationType.SIZE))
         {
            this.validateSize();
         }
      }
      
      private function validateSize() : void
      {
         this.textField.x = -this.textField.width >> 1;
         this.resetButton.x = -this.resetButton.width >> 1;
         this.resetButton.y = this.textField.y + this.textField.textHeight + 10;
      }
      
      override protected function onDispose() : void
      {
         this.resetButton.dispose();
         this.resetButton = null;
         this.textField = null;
         super.onDispose();
      }
   }
}
