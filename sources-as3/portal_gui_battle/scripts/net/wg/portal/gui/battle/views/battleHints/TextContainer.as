package net.wg.portal.gui.battle.views.battleHints
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.battle.components.BattleDisplayable;
   
   public class TextContainer extends BattleDisplayable
   {
      
      private static const WITH_ICON_OFFSET:uint = 10;
       
      
      public var txt:TextField = null;
      
      private var _useWithIconAlignment:Boolean = false;
      
      public function TextContainer()
      {
         super();
         this.txt.wordWrap = true;
         this.txt.autoSize = TextFieldAutoSize.CENTER;
      }
      
      override protected function onDispose() : void
      {
         this.txt = null;
         super.onDispose();
      }
      
      public function setText(param1:String) : void
      {
         this.txt.htmlText = param1;
         this.updateTxtY();
      }
      
      private function updateTxtY() : void
      {
         if(this._useWithIconAlignment)
         {
            this.txt.y = 0;
         }
         else
         {
            this.txt.y = -(this.txt.textHeight >> 1) + WITH_ICON_OFFSET;
         }
      }
      
      public function set useWithIconAlignment(param1:Boolean) : void
      {
         this._useWithIconAlignment = param1;
         this.updateTxtY();
      }
   }
}
