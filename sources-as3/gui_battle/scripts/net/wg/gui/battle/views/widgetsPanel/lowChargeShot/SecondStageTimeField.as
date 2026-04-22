package net.wg.gui.battle.views.widgetsPanel.lowChargeShot
{
   import com.gskinner.motion.GTweener;
   import com.gskinner.motion.easing.Cubic;
   
   public class SecondStageTimeField extends TimeField
   {
      
      private static const POSITION_NORMAL_SHORT:int = 37;
      
      private static const POSITION_NORMAL_LONG:int = 31;
      
      private static const POSITION_HIDDEN:int = 60;
      
      private static const LONG_TEXT_LENGTH:int = 4;
       
      
      private var _position:Number = 37;
      
      public function SecondStageTimeField()
      {
         super();
      }
      
      override public function setValue(param1:Number, param2:Boolean = true) : void
      {
         super.setValue(param1,param2);
         this.position = this.positionNormal;
      }
      
      override protected function playAlmostFinished() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "position":this.positionNormal,
            "opacity":ALPHA_NORMAL,
            "textColor":_colorsProvider.textColorNotCompleted
         },{"ease":Cubic.easeOut});
         updateShadow(false);
      }
      
      override protected function playFullCharge() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "position":POSITION_HIDDEN,
            "opacity":ALPHA_HIDDEN
         },{"ease":Cubic.easeIn});
         updateShadow(true);
      }
      
      override protected function playInitial() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "position":this.positionNormal,
            "opacity":ALPHA_FADED,
            "textColor":_colorsProvider.colorBlockDisabled
         },{"ease":Cubic.easeIn});
         updateShadow(true);
      }
      
      override protected function playLowCharge() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{
            "position":this.positionNormal,
            "opacity":ALPHA_NORMAL,
            "textColor":_colorsProvider.textColorNotCompleted
         },{"ease":Cubic.easeOut});
         updateShadow(false);
      }
      
      override protected function playQuickReload() : void
      {
         GTweener.removeTweens(this);
         GTweener.to(this,DURATION_QUICK,{"opacity":ALPHA_HIDDEN},{"ease":Cubic.easeIn});
         updateShadow(true);
      }
      
      public function get position() : Number
      {
         return this._position;
      }
      
      public function set position(param1:Number) : void
      {
         this._position = param1;
         textField.x = this._position;
      }
      
      private function get positionNormal() : uint
      {
         return textField.text.length >= LONG_TEXT_LENGTH ? uint(POSITION_NORMAL_LONG) : uint(POSITION_NORMAL_SHORT);
      }
   }
}
