package net.wg.gui.crewOperations
{
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.ToggleRenderer;
   import net.wg.gui.components.controls.VO.SimpleRendererVO;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   
   public class CrewOperationIRToggleBlock extends UIComponentEx
   {
      
      private static const OFFSET_BETWEEN_TEXT_AND_ITEM:uint = 17;
      
      private static const PADDING_BOTTOM_ERROR:uint = 7;
      
      private static const PADDING_BOTTOM_TOGGLE:uint = 19;
       
      
      public var toggle:ToggleRenderer = null;
      
      public var descriptionText:TextField;
      
      public var errorText:TextField;
      
      private var _data:CrewOperationInfoVO;
      
      public function CrewOperationIRToggleBlock()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.descriptionText.mouseEnabled = this.errorText.mouseEnabled = false;
         this.errorText.visible = false;
         this.toggle.visible = false;
      }
      
      override protected function onDispose() : void
      {
         this.toggle.dispose();
         this.toggle = null;
         this._data = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:SimpleRendererVO = null;
         super.draw();
         if(isInvalid(InvalidationType.DATA) && this._data)
         {
            this.descriptionText.text = this._data.toggleBlockDescription;
            App.utils.commons.updateTextFieldSize(this.descriptionText,false);
            _loc1_ = this._data.toggleBlockError != Values.EMPTY_STR;
            if(_loc1_)
            {
               this.errorText.visible = true;
               this.errorText.text = this._data.toggleBlockError;
               App.utils.commons.updateTextFieldSize(this.errorText,false);
               this.errorText.y = this.descriptionText.y + this.descriptionText.height + OFFSET_BETWEEN_TEXT_AND_ITEM;
               _height = this.errorText.y + this.errorText.height + PADDING_BOTTOM_ERROR >> 0;
            }
            else
            {
               _loc2_ = new SimpleRendererVO({});
               _loc2_.enabled = true;
               _loc2_.selected = this._data.isToggleSelected;
               this.toggle.setData(_loc2_);
               this.toggle.visible = true;
               this.toggle.btn.label = this._data.toggleBlockToggleLabel;
               this.toggle.y = this.descriptionText.y + this.descriptionText.height + OFFSET_BETWEEN_TEXT_AND_ITEM;
               _height = this.toggle.y + this.toggle.height + PADDING_BOTTOM_TOGGLE >> 0;
            }
         }
      }
      
      public function get data() : CrewOperationInfoVO
      {
         return this._data;
      }
      
      public function set data(param1:CrewOperationInfoVO) : void
      {
         this._data = param1;
         invalidateData();
      }
   }
}
