package net.wg.gui.lobby.hangar
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.generated.TEXT_MANAGER_STYLES;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.lobby.hangar.data.EconomyWidgetVO;
   import net.wg.gui.lobby.hangar.quests.HeaderQuestsFlags;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import scaleform.clik.constants.InvalidationType;
   
   public class EconomyWidget extends UIComponentEx
   {
      
      private static const LBL_BIG:String = "big";
      
      private static const LBL_SMALL:String = "small";
      
      private static const IMG_TAG_BIG:String = "<img src=\'img://gui/maps/icons/library/economyBonus_big.png\' width=\'40\' height=\'20\' vspace=\'-4\' hspace=\'0\'/>";
      
      private static const IMG_TAG_SMALL:String = "<img src=\'img://gui/maps/icons/library/economyBonus_small.png\' width=\'28\' height=\'15\' vspace=\'-3\' hspace=\'0\'/>";
       
      
      public var valueField:TextField = null;
      
      private var _data:EconomyWidgetVO = null;
      
      private var _isSmall:Boolean = false;
      
      private var _isTooltipShown:Boolean;
      
      private var _toolTipMgr:ITooltipMgr;
      
      public function EconomyWidget()
      {
         super();
         this._toolTipMgr = App.toolTipMgr;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(MouseEvent.ROLL_OVER,this.onMouseRollOverHandler);
         addEventListener(MouseEvent.ROLL_OUT,this.onMouseRollOutHandler);
         mouseEnabled = true;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._data && isInvalid(InvalidationType.DATA))
         {
            this.visible = this._data.isVisible;
            this.updateValue();
            dispatchEvent(new Event(HeaderQuestsFlags.ENTRY_POINT_RESIZE));
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            gotoAndStop(!!this._isSmall ? LBL_SMALL : LBL_BIG);
            this.updateValue();
            dispatchEvent(new Event(HeaderQuestsFlags.ENTRY_POINT_RESIZE));
         }
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MouseEvent.ROLL_OVER,this.onMouseRollOverHandler);
         removeEventListener(MouseEvent.ROLL_OUT,this.onMouseRollOutHandler);
         this.valueField = null;
         this._toolTipMgr = null;
         this._data = null;
         super.onDispose();
      }
      
      public function updateData(param1:EconomyWidgetVO) : void
      {
         this._data = param1;
         invalidateData();
      }
      
      private function updateValue() : void
      {
         if(!this._data)
         {
            return;
         }
         this.valueField.htmlText = (!!this._isSmall ? IMG_TAG_SMALL : IMG_TAG_BIG) + App.textMgr.getTextStyleById(!!this._isSmall ? TEXT_MANAGER_STYLES.WHITE_TITLE_12 : TEXT_MANAGER_STYLES.WHITE_TITLE_15,this._data.bonusValue);
         App.utils.commons.updateTextFieldSize(this.valueField,true,false);
         this.valueField.x = -this.valueField.width >> 1;
      }
      
      private function showTooltip() : void
      {
         this._isTooltipShown = true;
         this._toolTipMgr.showWulfTooltip(TOOLTIPS_CONSTANTS.ECONOMY_BONUS_TOOLTIP);
      }
      
      private function hideTooltip() : void
      {
         if(this._isTooltipShown)
         {
            this._isTooltipShown = false;
            this._toolTipMgr.hide();
         }
      }
      
      public function get isSmall() : Boolean
      {
         return this._isSmall;
      }
      
      public function set isSmall(param1:Boolean) : void
      {
         if(this._isSmall != param1)
         {
            this._isSmall = param1;
            invalidateSize();
         }
      }
      
      private function onMouseRollOverHandler(param1:MouseEvent) : void
      {
         this.showTooltip();
      }
      
      private function onMouseRollOutHandler(param1:MouseEvent) : void
      {
         this.hideTooltip();
      }
   }
}
