package net.wg.gui.components.tooltips.inblocks.blocks
{
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.tooltips.inblocks.data.TextParameterTwoColVO;
   
   public class TextParameterBlockTwoCol extends TextParameterBlock
   {
       
      
      public var value2TF:TextField = null;
      
      private var _defaultValue2TFWidth:int = -1;
      
      public function TextParameterBlockTwoCol()
      {
         super();
         this._defaultValue2TFWidth = this.value2TF.width;
      }
      
      override public function cleanUp() : void
      {
         this.value2TF.text = this.value2TF.htmlText = null;
         this.value2TF.width = this._defaultValue2TFWidth;
         super.cleanUp();
      }
      
      override protected function getDataClass() : Class
      {
         return TextParameterTwoColVO;
      }
      
      override protected function onDispose() : void
      {
         this.value2TF = null;
         super.onDispose();
      }
      
      override protected function applyParamName() : void
      {
         var _loc1_:TextParameterTwoColVO = _data as TextParameterTwoColVO;
         if(!_loc1_)
         {
            return;
         }
         if(_loc1_.useHtmlName)
         {
            nameTF.htmlText = _loc1_.name;
         }
         else
         {
            nameTF.text = _loc1_.name;
         }
         if(_loc1_.useHtmlValue2)
         {
            this.value2TF.htmlText = _loc1_.value2;
         }
         else
         {
            this.value2TF.text = _loc1_.value2;
         }
         if(_loc1_.value2Gap != Values.DEFAULT_INT)
         {
            this.value2TF.x = valueTF.x + valueTF.width + _loc1_.value2Gap;
         }
         if(_loc1_.valueWidth != Values.DEFAULT_INT)
         {
            this.value2TF.width = _loc1_.valueWidth;
         }
         if(_loc1_.gap != Values.DEFAULT_INT)
         {
            nameTF.x = this.value2TF.x + this.value2TF.width + _loc1_.gap;
         }
         updateTextFieldHeight(nameTF);
         updateTextFieldHeight(this.value2TF);
      }
   }
}
