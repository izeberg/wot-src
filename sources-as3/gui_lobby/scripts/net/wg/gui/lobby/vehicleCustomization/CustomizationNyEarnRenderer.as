package net.wg.gui.lobby.vehicleCustomization
{
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.lobby.vehicleCustomization.data.EarnListRendererVO;
   import net.wg.gui.lobby.vehicleCustomization.events.CustomizationEvent;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   import scaleform.clik.controls.ListItemRenderer;
   
   public class CustomizationNyEarnRenderer extends ListItemRenderer implements IUpdatable
   {
      
      private static const TEXT_SIZE:int = 220;
      
      private static const TEXT_SIZE_SMALL:int = 160;
      
      private static const OFFSET:int = 10;
       
      
      public var text:TextField = null;
      
      public var button:SoundButtonEx = null;
      
      private var _vo:EarnListRendererVO = null;
      
      public function CustomizationNyEarnRenderer()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         mouseEnabled = false;
         mouseChildren = true;
         this.text.mouseEnabled = false;
         this.text.autoSize = TextFieldAutoSize.LEFT;
         this.button.useHtmlText = true;
         this.button.addEventListener(MouseEvent.CLICK,this.onButtonClickHandler);
         App.stage.addEventListener(Event.RESIZE,this.handleStageResize);
      }
      
      public function update(param1:Object) : void
      {
         super.data = param1;
         this._vo = EarnListRendererVO(param1);
         this.text.htmlText = this._vo.text;
         this.button.label = this._vo.linkText;
         this.button.enabled = this._vo.enable;
         invalidateData();
         validateNow();
         this.updateSize();
      }
      
      protected function handleStageResize(param1:Event) : void
      {
         this.updateSize();
      }
      
      private function updateSize() : void
      {
         var _loc1_:Boolean = App.appWidth < EmptyStateComponent.MIN_RESOLUTION;
         this.text.width = !!_loc1_ ? Number(TEXT_SIZE_SMALL) : Number(TEXT_SIZE);
         this.button.y = this.text.y + this.text.height + OFFSET;
      }
      
      override public function get width() : Number
      {
         return super.width;
      }
      
      override protected function onDispose() : void
      {
         App.stage.removeEventListener(Event.RESIZE,this.handleStageResize);
         this.button.removeEventListener(MouseEvent.CLICK,this.onButtonClickHandler);
         this._vo.dispose();
         this._vo = null;
         this.button.dispose();
         this.button = null;
         this.text = null;
         super.onDispose();
      }
      
      private function onButtonClickHandler(param1:Event) : void
      {
         dispatchEvent(new CustomizationEvent(this._vo.eventType));
      }
   }
}
