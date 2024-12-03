package net.wg.gui.lobby.vehicleCustomization
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.containers.HorizontalGroupLayout;
   import net.wg.gui.components.containers.IGroupEx;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.lobby.vehicleCustomization.data.EarnListRendererVO;
   import net.wg.gui.lobby.vehicleCustomization.data.FilterFallbackDataVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.data.DataProvider;
   
   public class EmptyStateComponent extends UIComponentEx
   {
      
      private static const BTN_OFFSET:int = 100;
      
      private static const BTN_OFFSET_SMALL:int = 40;
      
      private static const TEXT_POSITION:int = 70;
      
      private static const TEXT_POSITION_SMALL:int = 100;
      
      private static const LINK_OFFSET_X:int = 0;
      
      private static const LINK_OFFSET_Y:int = 7;
      
      private static const LBL_OFFSET_X:int = 20;
      
      public static const MIN_RESOLUTION:int = 1800;
      
      private static const RENDERER_LINKAGE:String = "NyEarnRendererUI";
      
      private static const HOR_GAP:int = 12;
      
      private static const HOR_GAP_SMALL:int = -10;
      
      private static const EARN_LIST_OFFSET:int = 60;
      
      private static const EARN_LIST_OFFSET_LIST:int = 30;
      
      private static const MESSAGE_OFFSET_Y:int = 10;
      
      private static const SMALL_OFFSET_NY:int = -180;
      
      private static const LARGE_OFFSET_NY:int = -326;
      
      private static const LBL_MSG_SMALL_NY:int = 95;
       
      
      public var lblMessage:TextField = null;
      
      public var videoButton:SoundButtonEx = null;
      
      public var actionButton:SoundButtonEx = null;
      
      public var nyEarnTypes:IGroupEx = null;
      
      private var _data:FilterFallbackDataVO = null;
      
      private var _earnDataProvider:DataProvider = null;
      
      public function EmptyStateComponent()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.lblMessage.autoSize = TextFieldAutoSize.LEFT;
         this.videoButton.addEventListener(MouseEvent.CLICK,this.onVideoButtonClickHandler);
         this.actionButton.addEventListener(MouseEvent.CLICK,this.onActionButtonButtonClickHandler);
         this.nyEarnTypes.layout = new HorizontalGroupLayout(HOR_GAP);
         this.nyEarnTypes.itemRendererLinkage = RENDERER_LINKAGE;
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:int = 0;
         var _loc3_:Number = NaN;
         super.draw();
         if(this._data != null && isInvalid(InvalidationType.DATA))
         {
            this.lblMessage.htmlText = this._data.message;
            this.actionButton.visible = this._data.actionButtonVisible;
            this.nyEarnTypes.visible = this._data.nySpecial;
            this.actionButton.label = !!this._data.nySpecial ? VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EMPTYSTATE_VIDEO : VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EMPTYSTATE_ATTACHMENTS;
            this._earnDataProvider = new DataProvider([new EarnListRendererVO({
               "text":VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EARN_LOOTBOX_DESCRIPTION,
               "linkText":VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EARN_LOOTBOX_BUTTON,
               "eventType":CustomizationEvent.NY_GOTO_LOOTBOXES
            }),new EarnListRendererVO({
               "text":VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EARN_CHALLENGE_DESCRIPTION,
               "linkText":VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EARN_CHALLENGE_BUTTON,
               "eventType":CustomizationEvent.NY_GOTO_CHALLENGE
            })]);
            if(this._data.grinchEnable)
            {
               this._earnDataProvider.push(new EarnListRendererVO({
                  "text":VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EARN_RAID_DESCRIPTION,
                  "linkText":VEHICLE_CUSTOMIZATION.CUSTOMIZATION_EARN_RAID_BUTTON,
                  "eventType":CustomizationEvent.NY_GOTO_BOARDGAME
               }));
            }
            this._earnDataProvider.dataProvider = this._earnDataProvider;
            this.nyEarnTypes.dataProvider = this._earnDataProvider;
            invalidateLayout();
         }
         if(InvalidationType.LAYOUT)
         {
            _loc1_ = App.appWidth < MIN_RESOLUTION;
            _loc2_ = !!this._data.nySpecial ? (!!_loc1_ ? int(SMALL_OFFSET_NY) : int(LARGE_OFFSET_NY)) : int(0);
            this.videoButton.visible = !!this._data.nySpecial ? this._data.hasVideo && !_loc1_ : Boolean(this._data.hasVideo);
            this.actionButton.visible = !!this._data.nySpecial ? Boolean(!this.videoButton.visible) : Boolean(this.actionButton.visible);
            if(this._data.hasVideo)
            {
               this.lblMessage.x = !!_loc1_ ? Number(TEXT_POSITION_SMALL) : Number(TEXT_POSITION);
               this.lblMessage.x += _loc2_;
               this.videoButton.x = this.lblMessage.x + this.lblMessage.textWidth;
               this.videoButton.x += !!_loc1_ ? BTN_OFFSET_SMALL : BTN_OFFSET;
               this.lblMessage.width = this.videoButton.x - this.lblMessage.x - LBL_OFFSET_X;
               _loc3_ = this.lblMessage.height;
               _loc3_ += !!this.actionButton.visible ? this.actionButton.height : 0;
               this.lblMessage.y = !!this.videoButton.visible ? Number(this.videoButton.y + MESSAGE_OFFSET_Y + (this.videoButton.height - _loc3_) / 2) : Number(LBL_MSG_SMALL_NY);
            }
            else
            {
               this.lblMessage.x = width - this.lblMessage.textWidth >> 1;
            }
            if(this._data.nySpecial)
            {
               this.nyEarnTypes.visible = this._data.nySpecial;
               this.nyEarnTypes.x = !!this.videoButton.visible ? Number(this.videoButton.width + this.videoButton.x + EARN_LIST_OFFSET) : Number(this.lblMessage.width + this.lblMessage.x + EARN_LIST_OFFSET_LIST);
            }
            this.nyEarnTypes.layout = new HorizontalGroupLayout(!!_loc1_ ? int(HOR_GAP_SMALL) : int(HOR_GAP));
            this.actionButton.x = this.lblMessage.x + LINK_OFFSET_X;
            this.actionButton.y = this.lblMessage.y + this.lblMessage.textHeight + LINK_OFFSET_Y;
         }
      }
      
      public function setData(param1:FilterFallbackDataVO) : void
      {
         if(param1 != null && this._data != param1)
         {
            this._data = param1;
         }
         invalidateData();
      }
      
      private function onVideoButtonClickHandler(param1:Event) : void
      {
         dispatchEvent(new CustomizationEvent(CustomizationEvent.SHOW_ATTACHMENTS_VIDEO));
      }
      
      private function onActionButtonButtonClickHandler(param1:Event) : void
      {
         if(this._data.nySpecial)
         {
            dispatchEvent(new CustomizationEvent(CustomizationEvent.SHOW_ATTACHMENTS_VIDEO));
         }
         else
         {
            dispatchEvent(new CustomizationEvent(CustomizationEvent.EMPTY_STATE_ACTION));
         }
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IDisposable = null;
         this.videoButton.addEventListener(MouseEvent.CLICK,this.onVideoButtonClickHandler);
         this.actionButton.addEventListener(MouseEvent.CLICK,this.onActionButtonButtonClickHandler);
         this.actionButton.dispose();
         this.actionButton = null;
         this.videoButton.dispose();
         this.videoButton = null;
         this.nyEarnTypes.dispose();
         this.nyEarnTypes = null;
         for each(_loc1_ in this._earnDataProvider)
         {
            _loc1_.dispose();
         }
         this._earnDataProvider.cleanUp();
         this._earnDataProvider = null;
         this.lblMessage = null;
         super.onDispose();
      }
   }
}
