package net.wg.gui.lobby.battleResults.components.giftSystem
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.Values;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.controls.CloseButtonText;
   import net.wg.gui.lobby.battleResults.data.GiftStampVO;
   import net.wg.gui.lobby.battleResults.event.BattleResultsViewEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class GiftSystemStamps extends UIComponentEx
   {
      
      private static const ITEMS_HORIZONTAL_OFFSET:uint = 3;
       
      
      public var gotoButton:CloseButtonText = null;
      
      public var bg:MovieClip = null;
      
      public var bgWide:MovieClip = null;
      
      public var labelTF:TextField = null;
      
      public var valueTF:TextField = null;
      
      public var stampIcon:MovieClip = null;
      
      private var _hit:Sprite = null;
      
      private var _data:GiftStampVO = null;
      
      public function GiftSystemStamps()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._hit = new Sprite();
         this._hit.graphics.beginFill(16777215,0);
         this._hit.graphics.drawRect(0,0,1,1);
         this._hit.graphics.endFill();
         this._hit.y = this.valueTF.y;
         this._hit.height = this.valueTF.height | 0;
         addChild(this._hit);
         this.gotoButton.showIcon = false;
         this.gotoButton.label = BATTLE_RESULTS.GIFTSYSTEM_BANNER_STAMPS_BUTTON_NOTAVAILABLE;
         this.gotoButton.addEventListener(ButtonEvent.CLICK,this.onGotoButtonClickHandler);
         this.labelTF.autoSize = TextFieldAutoSize.LEFT;
         this.valueTF.autoSize = TextFieldAutoSize.LEFT;
         this._hit.addEventListener(MouseEvent.ROLL_OVER,this.onStampRollOverHandler);
         this._hit.addEventListener(MouseEvent.ROLL_OUT,this.onStampRollOutHandler);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            if(this._data.count > Values.ZERO)
            {
               this.labelTF.text = BATTLE_RESULTS.GIFTSYSTEM_BANNER_STAMPS_LABEL_AVAILABLE;
               this.valueTF.text = this._data.count.toString();
               this.valueTF.visible = this.stampIcon.visible = this.bg.visible = this._hit.visible = true;
               this.gotoButton.visible = this.bgWide.visible = false;
               this.labelTF.x = this.bg.width - (this.labelTF.width + this.valueTF.width + this.stampIcon.width) >> 1;
               this.valueTF.x = ITEMS_HORIZONTAL_OFFSET + this.labelTF.x + this.labelTF.width | 0;
               this.stampIcon.x = ITEMS_HORIZONTAL_OFFSET * 2 + this.valueTF.x + this.valueTF.width | 0;
               this._hit.x = this.labelTF.x;
               this._hit.width = this.stampIcon.x + this.stampIcon.width - this._hit.x;
            }
            else
            {
               this.labelTF.text = BATTLE_RESULTS.GIFTSYSTEM_BANNER_STAMPS_LABEL_NOTAVAILABLE;
               this.valueTF.visible = this.stampIcon.visible = this.bg.visible = this._hit.visible = false;
               this.gotoButton.visible = this.bgWide.visible = true;
               this.labelTF.x = this.bgWide.width - (this.labelTF.width + this.gotoButton.width) >> 1;
               this.gotoButton.x = ITEMS_HORIZONTAL_OFFSET + this.labelTF.x + this.labelTF.width | 0;
            }
         }
      }
      
      override protected function onDispose() : void
      {
         this.gotoButton.removeEventListener(ButtonEvent.CLICK,this.onGotoButtonClickHandler);
         this.gotoButton.dispose();
         this.gotoButton = null;
         this._hit.removeEventListener(MouseEvent.ROLL_OVER,this.onStampRollOverHandler);
         this._hit.removeEventListener(MouseEvent.ROLL_OUT,this.onStampRollOutHandler);
         this.bg = null;
         this.bgWide = null;
         this.labelTF = null;
         this.valueTF = null;
         this.stampIcon = null;
         this._hit = null;
         this._data = null;
         super.onDispose();
      }
      
      private function onGotoButtonClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new BattleResultsViewEvent(BattleResultsViewEvent.GOTO_GIFT_STAMPS));
      }
      
      private function onStampRollOverHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.showWulfTooltip(TOOLTIPS_CONSTANTS.BIRTHDAY_GIFT_SYSTEM_POSTMARK);
      }
      
      private function onStampRollOutHandler(param1:MouseEvent) : void
      {
         App.toolTipMgr.hide();
      }
      
      public function updateData(param1:GiftStampVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      override public function get width() : Number
      {
         if(this._data && this._data.count <= Values.ZERO)
         {
            return this.bgWide.width;
         }
         return this.bg.width;
      }
   }
}
