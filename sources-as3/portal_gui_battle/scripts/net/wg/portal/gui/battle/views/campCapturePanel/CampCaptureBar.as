package net.wg.portal.gui.battle.views.campCapturePanel
{
   import flash.display.MovieClip;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class CampCaptureBar extends CaptureBar
   {
       
      
      public var campIcon:MovieClip = null;
      
      public var timerIcon:MovieClip = null;
      
      public var tankIcon:MovieClip = null;
      
      public function CampCaptureBar()
      {
         super();
      }
      
      override public function setData(param1:Number, param2:Number, param3:String, param4:String, param5:Number, param6:String, param7:String, param8:Boolean = false) : void
      {
         super.setData(param1,param2,param3,param4,param5,param6,param7,param8);
         this.campIcon.gotoAndStop(param1 + 1);
      }
      
      override protected function onDispose() : void
      {
         this.campIcon = null;
         this.timerIcon = null;
         this.tankIcon = null;
         super.onDispose();
      }
      
      override protected function getEaseArray(param1:Number) : Array
      {
         return TWEEN_EASE_NONE;
      }
      
      override protected function updateTitle(param1:String) : void
      {
         super.updateTitle(param1);
         this.campIcon.x = textField.x + (textField.width - textField.textWidth >> 1) | 0;
         this.tankIcon.visible = this.timerIcon.visible = this.campIcon.visible = StringUtils.isNotEmpty(param1);
      }
   }
}
