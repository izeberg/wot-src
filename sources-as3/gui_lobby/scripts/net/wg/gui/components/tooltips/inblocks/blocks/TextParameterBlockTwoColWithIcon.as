package net.wg.gui.components.tooltips.inblocks.blocks
{
   import flash.events.Event;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.tooltips.inblocks.data.TextParameterTwoColVO;
   import org.idmedia.as3commons.util.StringUtils;
   
   public class TextParameterBlockTwoColWithIcon extends AbstractTextParameterBlock
   {
       
      
      public var nameTF:TextField;
      
      public var image:Image = null;
      
      private var _defaultNameTFWidth:Number;
      
      public function TextParameterBlockTwoColWithIcon()
      {
         super();
         this._defaultNameTFWidth = valueTF.width;
      }
      
      override public function cleanUp() : void
      {
         this.image.x = this.image.y = 0;
         this.image.source = null;
         this.nameTF.text = null;
         this.nameTF.width = this._defaultNameTFWidth;
         super.cleanUp();
      }
      
      override protected function onSetBlockWidth(param1:int) : void
      {
      }
      
      override protected function getDataClass() : Class
      {
         return TextParameterTwoColVO;
      }
      
      override protected function onDispose() : void
      {
         this.image.removeEventListener(Event.CHANGE,this.onImageChangeHandler);
         this.image.dispose();
         this.image = null;
         this.nameTF = null;
         super.onDispose();
      }
      
      override protected function applyParamName() : void
      {
         var _loc1_:TextParameterTwoColVO = _data as TextParameterTwoColVO;
         if(!_loc1_)
         {
            return;
         }
         this.image.visible = StringUtils.isNotEmpty(_loc1_.icon);
         if(this.image.visible)
         {
            this.image.source = _loc1_.icon;
            this.image.addEventListener(Event.CHANGE,this.onImageChangeHandler);
         }
         if(_loc1_.useHtmlValue)
         {
            valueTF.htmlText = _loc1_.value;
         }
         else
         {
            valueTF.text = _loc1_.value;
         }
         if(_loc1_.valueWidth != -1)
         {
            valueTF.width = _loc1_.valueWidth;
            this.nameTF.width = _loc1_.valueWidth;
         }
         if(_loc1_.useHtmlName)
         {
            this.nameTF.htmlText = _loc1_.name;
         }
         else
         {
            this.nameTF.text = _loc1_.name;
         }
         if(_loc1_.value2Gap != Values.DEFAULT_INT)
         {
            this.nameTF.x = valueTF.x + valueTF.width + _loc1_.value2Gap;
         }
         updateTextFieldHeight(this.nameTF);
         this.invalidateImage();
      }
      
      private function invalidateImage() : void
      {
         var _loc1_:TextParameterTwoColVO = null;
         if(this.image.ready && this.image.visible)
         {
            this.image.x = this.nameTF.x + this.nameTF.width - this.nameTF.textWidth - this.image.width;
            this.image.y = 0;
            _loc1_ = _data as TextParameterTwoColVO;
            if(!_loc1_)
            {
               return;
            }
            if(_loc1_.iconPadding != null)
            {
               this.image.x += _loc1_.iconPadding.left - _loc1_.iconPadding.right;
               this.image.y += _loc1_.iconPadding.top - _loc1_.iconPadding.bottom;
            }
         }
      }
      
      private function onImageChangeHandler(param1:Event) : void
      {
         this.invalidateImage();
      }
   }
}
