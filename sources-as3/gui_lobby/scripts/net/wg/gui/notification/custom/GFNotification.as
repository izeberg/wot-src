package net.wg.gui.notification.custom
{
   import flash.events.Event;
   import flash.utils.getTimer;
   import net.wg.gui.notification.ServiceMessageContentBase;
   import net.wg.gui.notification.events.NotificationRegisteringEvent;
   import scaleform.clik.constants.InvalidationType;
   
   public class GFNotification extends ServiceMessageContentBase
   {
      
      private static const WIDTH:int = 288;
      
      private static const POP_UP_WIDTH:int = 301;
      
      private static const GF_NOTIFICATION_ALIAS_POSTFIX:String = "PopUp";
       
      
      public var gfInject:GFNotificationInject = null;
      
      private var alias:String = null;
      
      private var gfViewName:String = null;
      
      private var isInDOM:Boolean = false;
      
      private var linkageData:Object = null;
      
      public function GFNotification()
      {
         super();
      }
      
      override protected function addedToStage(param1:Event) : void
      {
         this.isInDOM = true;
         if(data && !this.alias)
         {
            this.registerGFInject();
         }
         super.addedToStage(param1);
      }
      
      override public function get height() : Number
      {
         return this.gfInject.height;
      }
      
      override public function get width() : Number
      {
         if(this.isPopUp)
         {
            return POP_UP_WIDTH;
         }
         return WIDTH;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.LAYOUT))
         {
            if(this.isPopUp)
            {
               this.gfInject.setViewSize(data.messageVO.gfViewPopUpWidth,data.messageVO.gfViewPopUpHeight);
            }
            else
            {
               this.gfInject.setViewSize(data.messageVO.gfViewWidth,data.messageVO.gfViewHeight);
            }
         }
         if(isInvalid(InvalidationType.DATA))
         {
            if(this.isInDOM && !this.alias)
            {
               this.registerGFInject();
            }
         }
      }
      
      override protected function onBeforeDispose() : void
      {
         if(this.alias)
         {
            if(this.isPopUp)
            {
               App.stage.dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.UNREGISTER_POP_UP,this.alias,this.gfViewName,null));
            }
            else
            {
               App.stage.dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.UNREGISTER_SM,this.alias,this.gfViewName,null));
            }
         }
         super.onBeforeDispose();
      }
      
      override protected function onDispose() : void
      {
         this.removeChild(this.gfInject);
         this.gfInject = null;
         this.linkageData = null;
         super.onDispose();
      }
      
      private function registerGFInject() : void
      {
         this.gfViewName = data.messageVO.gfViewName;
         this.linkageData = data.messageVO.linkageData;
         this.alias = this.createAlias();
         if(this.isPopUp)
         {
            this.alias += GF_NOTIFICATION_ALIAS_POSTFIX;
            dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.REGISTER_POP_UP,this.alias,this.gfViewName,this.gfInject,this.linkageData));
         }
         else
         {
            dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.REGISTER_SM,this.alias,this.gfViewName,this.gfInject,this.linkageData));
         }
         invalidateLayout();
      }
      
      private function createAlias() : String
      {
         return this.gfViewName + data.entityID.toString() + getTimer().toString();
      }
   }
}
