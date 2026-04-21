package net.wg.gui.battle.views.widgetsPanel.lowChargeShot
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   
   public class FirstStageTimeField extends TimeField
   {
       
      
      public function FirstStageTimeField()
      {
         super();
      }
      
      override protected function playAlmostFinished() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "opacity":ALPHA_FADED,
            "textColor":_colorsProvider.colorBlockDisabled
         },{"ease":Cubic.easeIn});
         updateShadow(true);
      }
      
      override protected function playFullCharge() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "opacity":ALPHA_NORMAL,
            "textColor":_colorsProvider.textColorCompleted
         },{"ease":Cubic.easeOut});
         updateShadow(false);
      }
      
      override protected function playInitial() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "opacity":ALPHA_NORMAL,
            "textColor":_colorsProvider.textColorNotCompleted
         },{"ease":Cubic.easeOut});
         updateShadow(false);
      }
      
      override protected function playLowCharge() : void
      {
         opacity = ALPHA_NORMAL;
         textColor = _colorsProvider.glowColor;
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_LONG,{"textColor":_colorsProvider.textColorCompleted},{"ease":Cubic.easeIn});
         updateShadow(false);
      }
      
      override protected function playQuickReload() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "opacity":ALPHA_NORMAL,
            "textColor":_colorsProvider.textColorNotCompleted
         },{"ease":Cubic.easeOut});
         updateShadow(false);
      }
   }
}
