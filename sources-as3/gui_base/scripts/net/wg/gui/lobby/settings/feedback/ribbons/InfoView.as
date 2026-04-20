package net.wg.gui.lobby.settings.feedback.ribbons
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.text.TextField;
   import net.wg.gui.components.controls.UILoaderAlt;
   import net.wg.gui.events.UILoaderEvent;
   import net.wg.infrastructure.base.UIComponentEx;
   
   public class InfoView extends UIComponentEx
   {
      
      private static const ALERT_ICON_PADDING_Y:int = 6;
      
      private static const TEXT_FIELD_ADDITIONAL_HEIGHT:int = 4;
       
      
      public var icon:UILoaderAlt = null;
      
      public var message:TextField = null;
      
      public var messageBG:MovieClip = null;
      
      public var hintArea:MovieClip = null;
      
      public function InfoView()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.message.text = SETTINGS.FEEDBACK_TAB_BATTLEEVENTS_INFO;
         this.message.height = this.message.textHeight + TEXT_FIELD_ADDITIONAL_HEIGHT;
         this.icon.addEventListener(UILoaderEvent.COMPLETE,this.onIconCompleteHandler);
         this.icon.source = RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICONFILLEDBIG;
      }
      
      override protected function onDispose() : void
      {
         this.message = null;
         this.messageBG = null;
         this.hintArea = null;
         this.icon.removeEventListener(UILoaderEvent.COMPLETE,this.onIconCompleteHandler);
         this.icon.dispose();
         this.icon = null;
         super.onDispose();
      }
      
      private function onIconCompleteHandler(param1:Event) : void
      {
         var _loc2_:int = this.icon.height + ALERT_ICON_PADDING_Y + this.message.textHeight >> 1;
         this.icon.y = (this.hintArea.height >> 1) - _loc2_;
         this.message.y = this.icon.y + this.icon.height + ALERT_ICON_PADDING_Y;
         this.messageBG.y = this.message.y - (this.messageBG.height - this.message.height >> 1);
      }
   }
}
