package net.wg.gui.lobby.battleResults.components
{
   import flash.text.TextField;
   import flash.text.TextFormat;
   import flash.text.TextFormatAlign;
   import net.wg.infrastructure.base.UIComponentEx;
   
   public class PersonalCondition extends UIComponentEx
   {
      
      private static const TEXT_HEIGHT:int = 6;
       
      
      public var conditionTF:TextField;
      
      public var statusTF:TextField;
      
      private var _isMain:Boolean = false;
      
      public function PersonalCondition()
      {
         super();
      }
      
      public function setData(param1:String, param2:String, param3:Boolean) : void
      {
         var _loc4_:TextFormat = new TextFormat();
         _loc4_.align = TextFormatAlign.RIGHT;
         this.conditionTF.htmlText = param1;
         this.statusTF.htmlText = param2;
         this.conditionTF.height = this.conditionTF.textHeight + TEXT_HEIGHT | 0;
         this.statusTF.height = this.statusTF.textHeight + TEXT_HEIGHT | 0;
         this.statusTF.setTextFormat(_loc4_);
         this._isMain = param3;
      }
      
      public function getTextHeight() : int
      {
         return this.conditionTF.textHeight;
      }
      
      public function isMainQuest() : Boolean
      {
         return this._isMain;
      }
      
      override protected function onDispose() : void
      {
         this.conditionTF = null;
         this.statusTF = null;
         super.onDispose();
      }
   }
}
