package net.wg.gui.lobby.settings.components
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.controls.InfoIcon;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.lobby.settings.components.evnts.WarningMessageEvent;
   import net.wg.gui.lobby.settings.vo.MessageBlockDataVO;
   import net.wg.infrastructure.base.UIComponentEx;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class WarningMessageBlock extends UIComponentEx
   {
      
      private static const INFO_ICON_X_PADDING:int = 10;
      
      private static const MAX_TOOLTIP_WIDTH:uint = 270;
       
      
      public var descTf:TextField = null;
      
      public var infoIcon:InfoIcon = null;
      
      public var actionBtn:SoundButtonEx = null;
      
      public var lip:MovieClip = null;
      
      private var _data:MessageBlockDataVO = null;
      
      public function WarningMessageBlock()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.descTf.autoSize = TextFieldAutoSize.CENTER;
         this.infoIcon.tooltipMaxWidth = MAX_TOOLTIP_WIDTH;
         this.actionBtn.addEventListener(ButtonEvent.CLICK,this.onActionBtnClickHandler,false,0,true);
         this.lip.mouseChildren = this.lip.mouseEnabled = false;
         mouseEnabled = false;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data != null && isInvalid(InvalidationType.DATA))
         {
            this.actionBtn.label = this._data.buttonLabel;
            this.descTf.text = this._data.message;
            this.infoIcon.icoType = this._data.infoIconType;
            this.infoIcon.tooltip = this._data.tooltip;
            this.infoIcon.x = this.descTf.x + this.descTf.textWidth + INFO_ICON_X_PADDING;
         }
      }
      
      override protected function onDispose() : void
      {
         this.descTf = null;
         this.infoIcon.dispose();
         this.infoIcon = null;
         this.actionBtn.removeEventListener(ButtonEvent.CLICK,this.onActionBtnClickHandler);
         this.actionBtn.dispose();
         this.actionBtn = null;
         this.lip = null;
         if(this._data)
         {
            this._data = null;
         }
         super.onDispose();
      }
      
      public function setData(param1:MessageBlockDataVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      private function onActionBtnClickHandler(param1:ButtonEvent) : void
      {
         var _loc2_:String = this._data.actionName;
         if(StringUtils.isNotEmpty(_loc2_))
         {
            dispatchEvent(new WarningMessageEvent(_loc2_,true));
         }
      }
   }
}
