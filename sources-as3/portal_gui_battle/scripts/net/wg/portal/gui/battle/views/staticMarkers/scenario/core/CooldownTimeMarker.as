package net.wg.portal.gui.battle.views.staticMarkers.scenario.core
{
   import flash.text.TextField;
   
   public class CooldownTimeMarker extends SimpleMarker
   {
       
      
      public var txtLabel:TextField = null;
      
      public function CooldownTimeMarker()
      {
         super();
         this.txtLabel.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.txtLabel = null;
         super.onDispose();
      }
      
      public function clearCountdown() : void
      {
         this.txtLabel.visible = false;
      }
      
      public function setCountdown(param1:String) : void
      {
         if(!this.txtLabel.visible)
         {
            this.txtLabel.visible = true;
         }
         this.txtLabel.text = param1;
      }
   }
}
