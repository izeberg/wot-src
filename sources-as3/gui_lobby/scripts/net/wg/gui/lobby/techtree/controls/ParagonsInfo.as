package net.wg.gui.lobby.techtree.controls
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.lobby.techtree.constants.ParagonsTypeStrings;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   
   public class ParagonsInfo extends UIComponentEx
   {
       
      
      public var paragonsLabel:TextField;
      
      public var paragonsField:TextField;
      
      private var _paragonsValue:String = "";
      
      private var _paragonsType:String = "research";
      
      public function ParagonsInfo()
      {
         super();
         this.paragonsLabel.autoSize = TextFieldAutoSize.LEFT;
      }
      
      override protected function draw() : void
      {
         if(isInvalid(InvalidationType.DATA))
         {
            this.paragonsField.text = this._paragonsValue;
            this.paragonsLabel.text = this._paragonsType == ParagonsTypeStrings.FIRST_RESEARCH_TYPE ? PARAGONS.RESEARCHPAGE_FIRSTRESEARCH : PARAGONS.RESEARCHPAGE_FIRSTWIN;
         }
      }
      
      override protected function onDispose() : void
      {
         this.paragonsLabel = null;
         this.paragonsField = null;
         super.onDispose();
      }
      
      public function setData(param1:String, param2:String) : void
      {
         this._paragonsValue = param1;
         this._paragonsType = param2;
         invalidateData();
      }
   }
}
