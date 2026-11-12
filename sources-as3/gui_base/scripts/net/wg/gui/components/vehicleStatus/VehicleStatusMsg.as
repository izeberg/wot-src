package net.wg.gui.components.vehicleStatus
{
   import flash.display.Sprite;
   import flash.text.TextField;
   import net.wg.infrastructure.base.UIComponentEx;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   
   public class VehicleStatusMsg extends UIComponentEx
   {
       
      
      public var textField:TextField = null;
      
      public var hitMc:Sprite = null;
      
      public var messageBg:Sprite = null;
      
      private var _message:String = null;
      
      public function VehicleStatusMsg()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         hitArea = this.hitMc;
         this.messageBg.mouseEnabled = this.messageBg.mouseChildren = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._message != null)
         {
            if(isInvalid(InvalidationType.DATA))
            {
               this.textField.htmlText = this._message;
               App.utils.commons.updateTextFieldSize(this.textField);
            }
         }
         if(isInvalid(InvalidationType.DATA,InvalidationType.SIZE))
         {
            this.messageBg.x = this.textField.x;
            this.messageBg.y = this.textField.y;
            this.messageBg.width = this.width;
            this.messageBg.height = this.height;
         }
      }
      
      override protected function onDispose() : void
      {
         hitArea = null;
         this.textField = null;
         this.hitMc = null;
         this.messageBg = null;
         super.onDispose();
      }
      
      public function setMessage(param1:String) : void
      {
         if(this._message != param1 && StringUtils.isNotEmpty(param1))
         {
            this._message = param1;
            invalidateData();
         }
      }
      
      override public function get width() : Number
      {
         return this.textField.width;
      }
      
      override public function get height() : Number
      {
         return this.textField.height;
      }
   }
}
