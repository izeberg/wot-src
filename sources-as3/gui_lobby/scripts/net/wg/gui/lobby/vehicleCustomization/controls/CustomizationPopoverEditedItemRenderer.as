package net.wg.gui.lobby.vehicleCustomization.controls
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.lobby.vehicleCustomization.data.CustomizationPopoverEditedItemRendererVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationIndicatorEvent;
   import scaleform.clik.constants.InvalidationType;
   
   public class CustomizationPopoverEditedItemRenderer extends CustomizationPopoverItemRenderer
   {
      
      private static const HEIGHT:Number = 48;
       
      
      public var removedTF:TextField = null;
      
      private var _model:CustomizationPopoverEditedItemRendererVO = null;
      
      public function CustomizationPopoverEditedItemRenderer()
      {
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this.removedTF.mouseEnabled = false;
         this.removedTF.autoSize = TextFieldAutoSize.RIGHT;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         isPassive = mouseEnabledOnDisabled = true;
      }
      
      override protected function onDispose() : void
      {
         this.removedTF = null;
         this._model = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._model && isInvalid(InvalidationType.DATA))
         {
            this.removedTF.htmlText = this._model.disabledLabel;
            titleBg.visible = this._model.isTitle;
            if(!this._model.isTitle)
            {
               enabled = !this._model.isDisabled;
               updateDisable(this._model.isDisabled);
               this.removedTF.visible = this._model.isDisabled;
               inStorageIcon.visible = inStorageIcon.visible && !this._model.isDisabled;
               removeBtn.visible = enabled && this._model.isRemovable;
            }
         }
      }
      
      override protected function layoutName(param1:Boolean) : void
      {
         nameTF.visible = !param1;
         if(nameTF.visible)
         {
            super.layoutName(param1);
         }
      }
      
      override protected function updateVisibility(param1:Boolean) : void
      {
         super.updateVisibility(param1);
         this.removedTF.visible = param1;
      }
      
      override protected function removeItem() : void
      {
         dispatchEvent(new CustomizationIndicatorEvent(CustomizationIndicatorEvent.REMOVAL,this._model.id,this._model.itemsList,this._model.seasonType));
      }
      
      override public function setData(param1:Object) : void
      {
         this._model = Boolean(param1) ? CustomizationPopoverEditedItemRendererVO(param1) : null;
         super.setData(param1);
      }
      
      override public function get height() : Number
      {
         return HEIGHT;
      }
   }
}
