package net.wg.gui.lobby.missions.components
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFormat;
   import net.wg.data.constants.Fonts;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.gui.lobby.missions.event.MissionViewEvent;
   import net.wg.infrastructure.base.BaseDAAPIComponent;
   import net.wg.utils.IUtils;
   
   public class NYMissionsBanner extends BaseDAAPIComponent
   {
      
      private static const BG_OFFSET_Y:int = 15;
      
      private static const BG_OFFSET_Y_SMALL:int = -7;
      
      private static const MESSAGE_BTN_GAP:int = 14;
      
      private static const MESSAGE_BTN_GAP_SMALL:int = 11;
      
      private static const MESSAGE_Y:int = 130;
      
      private static const MESSAGE_Y_SMALL:int = 100;
      
      private static const SIZE_CHANGE_POINT:int = 900;
      
      private static const BG_SIZE_BIG:String = "big";
      
      private static const BG_SIZE_SMALL:String = "small";
      
      private static const BTN_PADDING:int = 10;
      
      private static const BTN_PADDING_SMALL:int = 5;
      
      private static const BTN_WIDTH:int = 236;
      
      private static const BTN_WIDTH_SMALL:int = 202;
      
      private static const BOTTOM_GAP:int = 25;
      
      private static const BOTTOM_GAP_SMALL:int = -21;
      
      private static const BTN_ICON_TEXT_OFFSET:int = 4;
      
      private static const BTN_ICON_TEXT_OFFSET_SMALL:int = -1;
      
      private static const NY_TF_FONTSIZE_BIG:uint = 16;
      
      private static const NY_TF_FONTSIZE_SMALL:uint = 14;
      
      private static const NY_TF_FONTSIZE_LINEHEIGHT_OFFSET:uint = 1;
      
      private static const INV_BUTTON_SIZE:String = "invButtonSize";
       
      
      public var toDailyQuestsBtn:UniversalBtn = null;
      
      public var messageTF:TextField = null;
      
      public var bg:MovieClip = null;
      
      private var _isBigSize:Boolean = false;
      
      private var _currentHeight:int = -1;
      
      private var _currentWidth:int = -1;
      
      public function NYMissionsBanner()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.bg.buttonMode = true;
         this.bg.useHandCursor = true;
         this.messageTF.mouseEnabled = false;
         this.toDailyQuestsBtn.currentFont = Fonts.FIELD_FONT;
         this.addEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.toDailyQuestsBtn.addEventListener(Event.RESIZE,this.onBtnResizeHandler);
         this.toDailyQuestsBtn.placeIconFromBorder = true;
         this.toDailyQuestsBtn.iconOffsetX = 1;
         this.toDailyQuestsBtn.label = "#ny_legacy:nyMissionsBanner/buttons/toNyQuestsBtn";
         this.isSizeChanged();
         this.rebuildHorizontal();
         this.rebuildVerticalAndTexts();
      }
      
      override protected function onDispose() : void
      {
         this.removeEventListener(MouseEvent.CLICK,this.onClickHandler);
         this.toDailyQuestsBtn.removeEventListener(Event.RESIZE,this.onBtnResizeHandler);
         this.toDailyQuestsBtn.dispose();
         this.toDailyQuestsBtn = null;
         this.messageTF = null;
         this.bg = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INV_BUTTON_SIZE))
         {
            this.rebuildHorizontal();
         }
      }
      
      public function getMaxHeight(param1:int, param2:int) : int
      {
         this._currentWidth = param1;
         var _loc3_:Boolean = this.isSizeChanged();
         this.rebuildHorizontal();
         if(!_loc3_)
         {
            return this._currentHeight;
         }
         this.rebuildVerticalAndTexts();
         return this._currentHeight;
      }
      
      protected function getMessage() : String
      {
         return "#ny_legacy:nyMissionsBanner/message";
      }
      
      private function rebuildVerticalAndTexts() : void
      {
         var _loc1_:IUtils = App.utils;
         var _loc2_:TextFormat = this.messageTF.getTextFormat();
         _loc2_.size = !!this._isBigSize ? NY_TF_FONTSIZE_BIG : NY_TF_FONTSIZE_SMALL;
         _loc2_.leading = NY_TF_FONTSIZE_LINEHEIGHT_OFFSET;
         this.messageTF.setTextFormat(_loc2_);
         this.messageTF.text = this.getMessage();
         _loc1_.commons.updateTextFieldSize(this.messageTF,false,true);
         this.bg.gotoAndStop(!!this._isBigSize ? BG_SIZE_BIG : BG_SIZE_SMALL);
         var _loc3_:int = this.bg.y = !!this._isBigSize ? Number(BG_OFFSET_Y) : Number(BG_OFFSET_Y_SMALL);
         this.toDailyQuestsBtn.y = _loc3_ = (this.messageTF.y = int(_loc3_ + (!!this._isBigSize ? MESSAGE_Y : MESSAGE_Y_SMALL))) + (this.messageTF.height + (!!this._isBigSize ? MESSAGE_BTN_GAP : MESSAGE_BTN_GAP_SMALL) | 0);
         var _loc4_:String = !!this._isBigSize ? UniversalBtnStylesConst.STYLE_HEAVY_NY_TRANSPARENT : UniversalBtnStylesConst.STYLE_SLIM_NY_TRANSPARENT;
         _loc1_.universalBtnStyles.setStyle(this.toDailyQuestsBtn,_loc4_);
         this.toDailyQuestsBtn.iconSource = !!this._isBigSize ? RES_ICONS.MAPS_ICONS_NY_LEGACY_NY_QUEST : RES_ICONS.MAPS_ICONS_NY_LEGACY_NY_QUEST_SMALL;
         this.toDailyQuestsBtn.iconOffsetText = !!this._isBigSize ? int(BTN_ICON_TEXT_OFFSET) : int(BTN_ICON_TEXT_OFFSET_SMALL);
         this._currentHeight = _loc3_ + this.toDailyQuestsBtn.height + (!!this._isBigSize ? BOTTOM_GAP : BOTTOM_GAP_SMALL);
      }
      
      private function rebuildHorizontal() : void
      {
         this.bg.x = this._currentWidth - this.bg.width >> 1;
         this.messageTF.x = this._currentWidth - this.messageTF.width >> 1;
         this.toDailyQuestsBtn.paddingHorizontal = !!this._isBigSize ? Number(BTN_PADDING) : Number(BTN_PADDING_SMALL);
         this.toDailyQuestsBtn.width = !!this._isBigSize ? Number(BTN_WIDTH) : Number(BTN_WIDTH_SMALL);
         this.toDailyQuestsBtn.x = this._currentWidth - this.toDailyQuestsBtn.width >> 1;
      }
      
      private function isSizeChanged() : Boolean
      {
         var _loc1_:Boolean = App.appHeight >= SIZE_CHANGE_POINT;
         var _loc2_:Boolean = _loc1_ == this._isBigSize;
         this._isBigSize = _loc1_;
         return _loc2_;
      }
      
      override public function get height() : Number
      {
         return this._currentHeight;
      }
      
      private function onBtnResizeHandler(param1:Event) : void
      {
         param1.stopImmediatePropagation();
         invalidate(INV_BUTTON_SIZE);
      }
      
      private function onClickHandler(param1:MouseEvent) : void
      {
         dispatchEvent(new MissionViewEvent(MissionViewEvent.GOTO_NY_QUESTS,true));
      }
   }
}
