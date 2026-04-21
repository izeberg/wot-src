package net.wg.gui.battle.views.widgetsPanel.lowChargeShot
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   
   public class QuickReloadTimeField extends TimeField
   {
       
      
      public function QuickReloadTimeField()
      {
         super();
      }
      
      override public function setValue(param1:Number, param2:Boolean = true) : void
      {
         super.setValue(param1,param2);
         visible = param1 != 0;
      }
      
      override protected function playAlmostFinished() : void
      {
         this.hide();
      }
      
      override protected function playFullCharge() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{"opacity":ALPHA_NORMAL},{"ease":Cubic.easeOut});
      }
      
      override protected function playInitial() : void
      {
         this.hide();
      }
      
      override protected function playLowCharge() : void
      {
         this.hide();
      }
      
      override protected function playQuickReload() : void
      {
         this.hide();
      }
      
      private function hide() : void
      {
         GTweener.removeTweens(this);
         opacity = ALPHA_HIDDEN;
      }
   }
}
