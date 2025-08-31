package net.wg.gui.lobby.menu
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.Values;
   import net.wg.gui.components.controls.BlackButton;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.interfaces.ISoundButtonEx;
   import net.wg.gui.login.impl.components.CopyrightEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class Copyright extends UIComponentEx
   {
      
      private static const LINK_BTN_Y_SHIFT:uint = 10;
      
      private static const TEXT_ALPHA:Number = 0.52;
      
      private static const BUTTONS_GAP:uint = 10;
      
      private static const REPORT_CONTENT_SHIFT_Y:Number = -1;
       
      
      public var textField:TextField = null;
      
      public var legalLink:BlackButton = null;
      
      public var reportCenterLink:BlackButton = null;
      
      private var _copyright:String = null;
      
      private var _reportContent:String = null;
      
      private var _legalInfo:String = null;
      
      private var _tooltipMgr:ITooltipMgr;
      
      private var _defaultTextFieldW:int;
      
      private var _defaultCopyrightW:int;
      
      private var _defaultTextFieldH:int;
      
      private var _btns:Vector.<ISoundButtonEx> = null;
      
      public function Copyright()
      {
         this._tooltipMgr = App.toolTipMgr;
         super();
      }
      
      override protected function initialize() : void
      {
         super.initialize();
         this._defaultTextFieldW = this.textField.width;
         this._defaultCopyrightW = this.legalLink.width;
         this._defaultTextFieldH = this.textField.height;
         this.reportCenterLink.iconSource = RES_ICONS.MAPS_ICONS_LIBRARY_BUYINWEBGRAY;
         this.reportCenterLink.iconShiftY = REPORT_CONTENT_SHIFT_Y;
         this.reportCenterLink.iconAlign = BlackButton.ICON_ALIGN_RIGHT;
         this._btns = new <ISoundButtonEx>[this.legalLink,this.reportCenterLink];
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.textField.alpha = TEXT_ALPHA;
         this.legalLink.addEventListener(MouseEvent.ROLL_OVER,this.onLegalLinkRollOverHandler);
         this.legalLink.addEventListener(MouseEvent.ROLL_OUT,this.onLegalLinkRollOutHandler);
         this.legalLink.addEventListener(ButtonEvent.CLICK,this.onLegalLinkClickHandler);
         this.reportCenterLink.addEventListener(ButtonEvent.CLICK,this.onReportCenterLinkClickHandler);
      }
      
      override protected function draw() : void
      {
         var _loc1_:Boolean = false;
         var _loc2_:uint = 0;
         var _loc3_:SoundButtonEx = null;
         var _loc4_:int = 0;
         super.draw();
         if(isInvalid(InvalidationType.DATA))
         {
            if(StringUtils.isNotEmpty(this._copyright))
            {
               _loc1_ = StringUtils.isEmpty(this._legalInfo);
               if(this.textField.width != this._defaultTextFieldW)
               {
                  this.textField.width = this._defaultTextFieldW;
               }
               if(this.textField.height != this._defaultTextFieldH)
               {
                  this.textField.height = this._defaultTextFieldH;
               }
               this.legalLink.visible = !_loc1_;
               this.legalLink.label = this._legalInfo;
               this.textField.text = this._copyright;
            }
            this.reportCenterLink.label = this._reportContent;
            this.reportCenterLink.visible = StringUtils.isNotEmpty(this._reportContent);
            invalidateLayout();
         }
         if(isInvalid(InvalidationType.LAYOUT))
         {
            this.textField.y = !!_loc1_ ? Number(this.legalLink.y) : Number(this.legalLink.y + this.legalLink.height + LINK_BTN_Y_SHIFT);
            _loc2_ = Values.ZERO;
            _loc3_ = null;
            for each(_loc3_ in this._btns)
            {
               if(_loc3_.visible)
               {
                  _loc2_ += _loc3_.width + BUTTONS_GAP;
               }
            }
            _loc4_ = this.textField.x + (this.textField.width - _loc2_ + BUTTONS_GAP >> 1);
            for each(_loc3_ in this._btns)
            {
               if(_loc3_.visible)
               {
                  _loc3_.x = _loc4_;
                  _loc4_ += _loc3_.width + BUTTONS_GAP;
               }
            }
            dispatchEvent(new Event(Event.CHANGE));
         }
      }
      
      override protected function onDispose() : void
      {
         this.legalLink.removeEventListener(MouseEvent.ROLL_OVER,this.onLegalLinkRollOverHandler);
         this.legalLink.removeEventListener(MouseEvent.ROLL_OUT,this.onLegalLinkRollOutHandler);
         this.legalLink.removeEventListener(ButtonEvent.CLICK,this.onLegalLinkClickHandler);
         this.reportCenterLink.removeEventListener(ButtonEvent.CLICK,this.onReportCenterLinkClickHandler);
         this._btns.splice(0,this._btns.length);
         this._btns = null;
         this.legalLink.dispose();
         this.legalLink = null;
         this.reportCenterLink.dispose();
         this.reportCenterLink = null;
         this.textField = null;
         this._tooltipMgr = null;
         super.onDispose();
      }
      
      public function getWidth() : int
      {
         return Math.max(this.textField.width,this.legalLink.width);
      }
      
      public function getHeight() : int
      {
         return !!this.legalLink.visible ? int(this.textField.height + this.legalLink.height + LINK_BTN_Y_SHIFT) : int(this.textField.height);
      }
      
      public function updateLabel(param1:String, param2:String, param3:String = "") : void
      {
         var _loc4_:Boolean = false;
         if(this._copyright != param1)
         {
            this._copyright = param1;
            _loc4_ = true;
         }
         if(this._legalInfo != param3)
         {
            this._legalInfo = param3;
            _loc4_ = true;
         }
         if(this._reportContent != param2)
         {
            this._reportContent = param2;
            _loc4_ = true;
         }
         if(_loc4_)
         {
            invalidateData();
         }
      }
      
      private function onLegalLinkClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new CopyrightEvent(CopyrightEvent.TO_LEGAL));
      }
      
      private function onLegalLinkRollOutHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.hide();
      }
      
      private function onLegalLinkRollOverHandler(param1:MouseEvent) : void
      {
         this._tooltipMgr.showComplex(TOOLTIPS.LOGIN_LEGAL);
      }
      
      private function onReportCenterLinkClickHandler(param1:ButtonEvent) : void
      {
         dispatchEvent(new CopyrightEvent(CopyrightEvent.TO_REPORT_CONTENT));
      }
   }
}
