package net.wg.frontline.gui.battle.components
{
   import flash.events.MouseEvent;
   import net.wg.data.constants.Values;
   import net.wg.data.managers.impl.ToolTipParams;
   import net.wg.gui.components.controls.DropdownMenu;
   import net.wg.gui.components.controls.UILoaderAlt;
   
   public class FrontlineFilterDropDown extends DropdownMenu
   {
      
      private static const TEXT_WIDTH_WARNING:int = 180;
       
      
      public var icon:UILoaderAlt;
      
      private var _tooltipParams:ToolTipParams;
      
      public function FrontlineFilterDropDown()
      {
         this._tooltipParams = new ToolTipParams({},{},null);
         super();
      }
      
      override public function set enabled(param1:Boolean) : void
      {
         super.enabled = param1;
         mouseChildren = true;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(MouseEvent.MOUSE_OVER,this.handleMouseOver,false,0,true);
         addEventListener(MouseEvent.MOUSE_OUT,this.handleMouseOut,false,0,true);
         mouseChildren = true;
         preventAutosizing = true;
         constraintsDisabled = true;
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MouseEvent.ROLL_OVER,this.handleMouseOver);
         removeEventListener(MouseEvent.ROLL_OUT,this.handleMouseOut);
         this._tooltipParams.dispose();
         this._tooltipParams = null;
         if(this.icon)
         {
            this.icon.dispose();
            this.icon = null;
         }
         super.onDispose();
      }
      
      override protected function populateText(param1:Object) : void
      {
         super.populateText(param1);
         if(param1)
         {
            this.icon.mouseEnabled = this.icon.visible = param1.warning;
            this._tooltipParams.header.display = param1.display;
            this._tooltipParams.header.total = param1.total;
         }
      }
      
      override protected function updateText() : void
      {
         if(_label != null && textField != null)
         {
            textField.text = _label;
            this.updateTextField();
         }
      }
      
      protected function updateTextField() : void
      {
         textField.width = !!this.icon.visible ? Number(TEXT_WIDTH_WARNING) : Number(TEXT_WIDTH_WARNING + this.icon.width);
         App.utils.commons.truncateTextFieldText(textField,_label,true,false,Values.THREE_DOTS,2);
      }
      
      private function handleMouseOver(param1:MouseEvent) : void
      {
         if(param1.target == this.icon && this.icon.visible)
         {
            App.toolTipMgr.showComplexWithParams(FL_TOOLTIPS.PLAYLIST_WARNING,this._tooltipParams);
         }
         else if(label != textField.text)
         {
            App.toolTipMgr.show(_label);
         }
      }
      
      private function handleMouseOut(param1:MouseEvent) : void
      {
         this.hideTooltip();
      }
      
      private function hideTooltip() : void
      {
         App.toolTipMgr.hide();
      }
   }
}
