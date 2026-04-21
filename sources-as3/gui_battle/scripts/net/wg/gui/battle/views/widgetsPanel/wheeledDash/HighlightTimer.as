package net.wg.gui.battle.views.widgetsPanel.wheeledDash
{
   import flash.display.MovieClip;
   import flashx.textLayout.formats.TextAlign;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.widgetsPanel.common.Timer;
   
   public class HighlightTimer extends Timer
   {
      
      private static const FRAME_STATE_ACTIVE:String = "active";
      
      private static const FRAME_STATE_INACTIVE:String = "inactive";
      
      private static const GLOW__SHIFT_X:int = 4;
       
      
      public var glow:MovieClip;
      
      private var _isHighlighted:Boolean = false;
      
      public function HighlightTimer()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         stop();
         this.glow = null;
         super.onDispose();
      }
      
      public function set highlight(param1:Boolean) : void
      {
         if(this._isHighlighted == param1)
         {
            return;
         }
         var _loc2_:String = label.text;
         var _loc3_:String = !!param1 ? FRAME_STATE_ACTIVE : FRAME_STATE_INACTIVE;
         gotoAndPlay(_loc3_);
         label.text = _loc2_;
         this._isHighlighted = param1;
      }
      
      override public function setLabel(param1:Number) : void
      {
         super.setLabel(param1);
         if(label.getTextFormat().align == TextAlign.CENTER)
         {
            this.glow.img.x = Values.ZERO;
         }
         else
         {
            this.glow.img.x = label.textWidth + GLOW__SHIFT_X >> 1;
         }
      }
   }
}
