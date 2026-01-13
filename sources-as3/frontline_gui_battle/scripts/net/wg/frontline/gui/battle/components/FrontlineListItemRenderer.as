package net.wg.frontline.gui.battle.components
{
   import flash.events.MouseEvent;
   import net.wg.data.constants.Values;
   import net.wg.data.managers.impl.ToolTipParams;
   import net.wg.gui.components.controls.DropDownListItemRendererSound;
   import net.wg.gui.components.controls.UILoaderAlt;
   import scaleform.clik.constants.InvalidationType;
   
   public class FrontlineListItemRenderer extends DropDownListItemRendererSound
   {
      
      private static const TEXT_WIDTH:int = 195;
       
      
      public var icon:UILoaderAlt;
      
      private var _tooltipParams:ToolTipParams;
      
      public function FrontlineListItemRenderer()
      {
         this._tooltipParams = new ToolTipParams({},{},null);
         super();
      }
      
      override public function set enabled(param1:Boolean) : void
      {
         super.enabled = param1;
         mouseChildren = true;
      }
      
      override public function setData(param1:Object) : void
      {
         super.setData(param1);
         invalidateData();
      }
      
      override protected function preInitialize() : void
      {
         super.preInitialize();
         preventAutosizing = true;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         addEventListener(MouseEvent.MOUSE_OVER,this.handleMouseOver,false,0,true);
         addEventListener(MouseEvent.MOUSE_OUT,this.handleMouseOut,false,0,true);
         mouseChildren = true;
         this.icon.mouseChildren = this.icon.mouseEnabled = this.icon.visible = false;
         if(data)
         {
            this.validateDate();
         }
      }
      
      override protected function onDispose() : void
      {
         removeEventListener(MouseEvent.ROLL_OVER,this.handleMouseOver);
         removeEventListener(MouseEvent.ROLL_OUT,this.handleMouseOut);
         this._tooltipParams.dispose();
         this._tooltipParams = null;
         this.icon.dispose();
         this.icon = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(enabled && isInvalid(InvalidationType.DATA))
         {
            this.validateDate();
         }
         if(isInvalid(InvalidationType.SIZE))
         {
            this.validateSize();
         }
      }
      
      override protected function hideTooltip() : void
      {
         App.toolTipMgr.hide();
      }
      
      private function validateDate() : void
      {
         if(data)
         {
            this.icon.mouseEnabled = this.icon.visible = data.warning;
            this._tooltipParams.header.display = data.display;
            this._tooltipParams.header.total = data.total;
            textField.text = data.label;
         }
      }
      
      private function validateSize() : void
      {
         textField.width = !!this.icon.visible ? Number(TEXT_WIDTH) : Number(TEXT_WIDTH + this.icon.width);
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
   }
}
