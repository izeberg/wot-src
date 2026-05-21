package net.wg.gui.lobby.missions.components.headerComponents
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.generated.QUESTS_ALIASES;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.gui.lobby.missions.event.MissionHeaderEvent;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class SummerSaleHeaderDescBlock extends HeaderDescBlock
   {
      
      private static const SHOP_BTN_NAME:String = "gotoShopBtn";
      
      private static const EVENT_BTN_NAME:String = "gotoEventBtn";
      
      private static const TF1_NAME:String = "captionTF1";
      
      private static const TF2_NAME:String = "captionTF2";
      
      private static const TF3_NAME:String = "captionTF3";
      
      private static const DISABLED_TF_NAME:String = "captionDisabledTF";
      
      private static const BUTTONS_MIN_WIDTH:int = 160;
      
      private static const BUTTONS_PADDING_TOP:int = 8;
       
      
      public var captionContainer:MovieClip;
      
      public var disabledContainer:MovieClip;
      
      public var infoBtn:SoundButtonEx;
      
      private var _gotoShopBtn:UniversalBtn;
      
      private var _gotoEventBtn:UniversalBtn;
      
      private var _captionTF1:TextField;
      
      private var _captionTF2:TextField;
      
      private var _captionTF3:TextField;
      
      private var _captionDisabledTF:TextField;
      
      private var _isEnabled:Boolean;
      
      public function SummerSaleHeaderDescBlock()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         this.infoBtn.removeEventListener(MouseEvent.CLICK,this.onInfoMouseButtonClick);
         this.infoBtn.dispose();
         this.infoBtn = null;
         this._gotoShopBtn.removeEventListener(ButtonEvent.CLICK,this.onGotoShopBtnClickHandler);
         this._gotoShopBtn.dispose();
         this._gotoShopBtn = null;
         this._gotoEventBtn.removeEventListener(ButtonEvent.CLICK,this.onGotoEventBtnClickHandler);
         this._gotoEventBtn.dispose();
         this._gotoEventBtn = null;
         this.captionContainer = null;
         this._captionTF1 = null;
         this._captionTF2 = null;
         this._captionTF3 = null;
         this.disabledContainer = null;
         this._captionDisabledTF = null;
         super.onDispose();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.infoBtn.constraintsDisabled = true;
         this.infoBtn.buttonMode = true;
         this.infoBtn.addEventListener(MouseEvent.CLICK,this.onInfoMouseButtonClick);
         this.infoBtn.label = QUESTS.SUMMERSALE_MISSIONS_HEADER_INFO;
         this._gotoShopBtn = this.captionContainer.getChildByName(SHOP_BTN_NAME) as UniversalBtn;
         this._gotoEventBtn = this.captionContainer.getChildByName(EVENT_BTN_NAME) as UniversalBtn;
         App.utils.universalBtnStyles.setStyle(this._gotoShopBtn,UniversalBtnStylesConst.STYLE_HEAVY_ORANGE);
         App.utils.universalBtnStyles.setStyle(this._gotoEventBtn,UniversalBtnStylesConst.STYLE_HEAVY_GREEN);
         this._gotoShopBtn.minWidth = this._gotoEventBtn.minWidth = BUTTONS_MIN_WIDTH;
         this._gotoShopBtn.autoSize = this._gotoEventBtn.autoSize = TextFieldAutoSize.LEFT;
         this._gotoShopBtn.label = QUESTS.SUMMERSALE_MISSIONS_HEADER_BUTTON_GOTOSHOP;
         this._gotoEventBtn.label = QUESTS.SUMMERSALE_MISSIONS_HEADER_BUTTON_GOTOEVENT;
         this._gotoShopBtn.addEventListener(ButtonEvent.CLICK,this.onGotoShopBtnClickHandler);
         this._gotoEventBtn.addEventListener(ButtonEvent.CLICK,this.onGotoEventBtnClickHandler);
         this._captionTF1 = this.captionContainer.getChildByName(TF1_NAME) as TextField;
         this._captionTF2 = this.captionContainer.getChildByName(TF2_NAME) as TextField;
         this._captionTF3 = this.captionContainer.getChildByName(TF3_NAME) as TextField;
         this._captionDisabledTF = this.disabledContainer.getChildByName(DISABLED_TF_NAME) as TextField;
         this._captionTF1.text = QUESTS.SUMMERSALE_MISSIONS_HEADER_CAPTION1;
         this._captionTF2.text = QUESTS.SUMMERSALE_MISSIONS_HEADER_CAPTION2;
         this._captionTF3.text = QUESTS.SUMMERSALE_MISSIONS_HEADER_CAPTION3;
         App.utils.commons.updateTextFieldSize(this._captionTF1,false);
         App.utils.commons.updateTextFieldSize(this._captionTF2,false);
         App.utils.commons.updateTextFieldSize(this._captionTF3,false);
         this._captionDisabledTF.text = QUESTS.SUMMERSALE_MISSIONS_HEADER_DISABLED;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            this.captionContainer.visible = this.infoBtn.visible = calendar.visible = descText.visible = this._isEnabled;
            this.disabledContainer.visible = !this._isEnabled;
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.captionContainer.x = width - this.captionContainer.width >> 1;
            this.disabledContainer.x = width - this.disabledContainer.width >> 1;
            this.infoBtn.x = this.captionContainer.x;
            this._gotoShopBtn.x = this._captionTF1.x + (this._captionTF1.width - this._gotoShopBtn.width >> 1);
            this._gotoShopBtn.y = this._captionTF1.y + this._captionTF1.height + BUTTONS_PADDING_TOP;
            this._gotoEventBtn.x = this._captionTF3.x + (this._captionTF3.width - this._gotoEventBtn.width >> 1);
            this._gotoEventBtn.y = this._captionTF3.y + this._captionTF3.height + BUTTONS_PADDING_TOP;
         }
      }
      
      public function set isEnabled(param1:Boolean) : void
      {
         if(this._isEnabled != param1)
         {
            this._isEnabled = param1;
            invalidateData();
         }
      }
      
      private function onInfoMouseButtonClick(param1:MouseEvent) : void
      {
         var _loc2_:MissionHeaderEvent = new MissionHeaderEvent(MissionHeaderEvent.OPEN_INFO_PAGE,true);
         _loc2_.actionId = QUESTS_ALIASES.SUMMER_SALE_EVENT;
         dispatchEvent(_loc2_);
      }
      
      private function onGotoShopBtnClickHandler(param1:ButtonEvent) : void
      {
         var _loc2_:MissionHeaderEvent = new MissionHeaderEvent(MissionHeaderEvent.OPEN_SHOP_PAGE,true);
         _loc2_.actionId = QUESTS_ALIASES.SUMMER_SALE_EVENT;
         dispatchEvent(_loc2_);
      }
      
      private function onGotoEventBtnClickHandler(param1:ButtonEvent) : void
      {
         var _loc2_:MissionHeaderEvent = new MissionHeaderEvent(MissionHeaderEvent.OPEN_EVENT_PAGE,true);
         _loc2_.actionId = QUESTS_ALIASES.SUMMER_SALE_EVENT;
         dispatchEvent(_loc2_);
      }
   }
}
