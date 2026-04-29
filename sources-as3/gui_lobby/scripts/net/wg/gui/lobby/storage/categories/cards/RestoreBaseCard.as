package net.wg.gui.lobby.storage.categories.cards
{
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.controls.Image;
   import scaleform.clik.constants.InvalidationType;
   
   public class RestoreBaseCard extends BaseCard
   {
       
      
      public var timerTF:TextField = null;
      
      public var timerImage:Image = null;
      
      public function RestoreBaseCard()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.timerTF.autoSize = TextFieldAutoSize.LEFT;
         this.timerTF.mouseEnabled = this.timerTF.mouseWheelEnabled = false;
         this.timerImage.mouseEnabled = this.timerImage.mouseChildren = false;
      }
      
      override protected function onDispose() : void
      {
         this.timerTF = null;
         this.timerImage.dispose();
         this.timerImage = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         var _loc1_:RestoreBaseCardVO = null;
         super.draw();
         if(_data && isInvalid(InvalidationType.DATA))
         {
            sellButton.visible = true;
            sellButton.enabled = _data.enabled;
            _loc1_ = RestoreBaseCardVO(_data);
            if(_loc1_.timerText)
            {
               this.timerTF.text = _loc1_.timerText;
               this.timerImage.source = _loc1_.timerIcon;
               this.timerTF.visible = this.timerImage.visible = true;
            }
            else
            {
               this.timerImage.visible = this.timerTF.visible = false;
            }
         }
      }
   }
}
