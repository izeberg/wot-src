package net.wg.white_tiger.gui.battle.views.vehicleMarkers
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.battle.views.vehicleMarkers.DamageLabel;
   import scaleform.gfx.TextFieldEx;
   
   public class WhiteTigerDamageLabel extends DamageLabel
   {
       
      
      public var hunter:TextField = null;
      
      public var wt_red:TextField = null;
      
      public var plasmaDamage:TextField = null;
      
      public function WhiteTigerDamageLabel()
      {
         super();
         this.hunter.visible = false;
         this.wt_red.visible = false;
         this.plasmaDamage.visible = false;
         TextFieldEx.setNoTranslate(this.hunter,true);
         TextFieldEx.setNoTranslate(this.wt_red,true);
         TextFieldEx.setNoTranslate(this.plasmaDamage,true);
         this.hunter.autoSize = TextFieldAutoSize.LEFT;
         this.wt_red.autoSize = TextFieldAutoSize.LEFT;
         this.plasmaDamage.autoSize = TextFieldAutoSize.LEFT;
         tfMap["hunter"] = this.hunter;
         tfMap["wt_red"] = this.wt_red;
         tfMap["plasmaDamage"] = this.plasmaDamage;
      }
      
      override public function dispose() : void
      {
         this.hunter = null;
         this.wt_red = null;
         this.plasmaDamage = null;
         tfMap["white"] = null;
         tfMap["hunter"] = null;
         tfMap["plasmaDamage"] = null;
         super.dispose();
      }
   }
}
