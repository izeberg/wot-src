package net.wg.portal.gui.battle.components
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import net.wg.gui.battle.components.BattleUIComponent;
   
   public class KeyShortcut extends BattleUIComponent
   {
      
      public static const DESCRIPTION_TF_PADDING:uint = 10;
      
      public static const MOUSE_LEFT_KEY:String = "mouseLeftKey";
      
      public static const SPACE_KEY:String = "spaceKey";
       
      
      public var descriptionTf:TextField = null;
      
      public var keyIcon:MovieClip = null;
      
      public function KeyShortcut()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.keyIcon = null;
         this.descriptionTf = null;
         super.onDispose();
      }
      
      public function setKeyAndDesc(param1:String, param2:String) : void
      {
         this.keyIcon.gotoAndStop(param1);
         this.descriptionTf.text = param2;
         App.utils.commons.updateTextFieldSize(this.descriptionTf,true,false);
         this.descriptionTf.x = this.keyIcon.x + this.keyIcon.width + DESCRIPTION_TF_PADDING;
      }
   }
}
