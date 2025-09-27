package net.wg.portal.gui.battle.components
{
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class PortalShortcutBtn extends BattleUIComponent
   {
      
      private static const TEXT_PADDING:int = 4;
       
      
      public var bg:MovieClip = null;
      
      public var nameTf:TextField = null;
      
      public var descriptionTf:TextField = null;
      
      public function PortalShortcutBtn()
      {
         super();
         this.bg.blendMode = BlendMode.SCREEN;
      }
      
      override protected function onDispose() : void
      {
         this.bg = null;
         this.nameTf = null;
         this.descriptionTf = null;
         super.onDispose();
      }
      
      public function setNameAndDesc(param1:String, param2:String) : void
      {
         this.nameTf.text = param1;
         this.descriptionTf.text = param2;
         App.utils.commons.updateTextFieldSize(this.nameTf,true,false);
         App.utils.commons.updateTextFieldSize(this.descriptionTf,true,false);
         this.bg.width = this.nameTf.x + this.nameTf.width + TEXT_PADDING | 0;
         this.descriptionTf.x = this.bg.width + TEXT_PADDING | 0;
      }
   }
}
