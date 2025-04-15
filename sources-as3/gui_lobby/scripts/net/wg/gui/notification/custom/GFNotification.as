package net.wg.gui.notification.custom
{
   import flash.events.Event;
   import flash.utils.getTimer;
   import net.wg.gui.notification.ServiceMessageContentBase;
   import net.wg.gui.notification.caches.GFNotificationCache;
   import net.wg.gui.notification.events.NotificationRegisteringEvent;
   import net.wg.gui.notification.interfaces.IGFNotificationCache;
   import scaleform.clik.constants.InvalidationType;
   
   public class GFNotification extends ServiceMessageContentBase
   {
      
      private static const POP_UP_ALIAS_POSTFIX:String = "PopUp";
      
      private static const MIN_HEIGHT:int = 1;
       
      
      private var gfInject:GFNotificationInject = null;
      
      private var alias:String = null;
      
      private var sizeCacheKey:String = null;
      
      private var gfViewName:String = null;
      
      private var isInDOM:Boolean = false;
      
      private var _notificationCache:IGFNotificationCache;
      
      public function GFNotification()
      {
         this._notificationCache = GFNotificationCache.getInstance();
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.gfInject = new GFNotificationInject();
         this.gfInject.addEventListener(Event.RESIZE,this.onInjectResizeHandler);
         addChild(this.gfInject);
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
         if(this.isInjectSizeValid())
         {
            return this.gfInject.height;
         }
         if(this.sizeCacheKey && this._notificationCache.getCachedSize(this.sizeCacheKey))
         {
            return this._notificationCache.getCachedSize(this.sizeCacheKey);
         }
         return MIN_HEIGHT;
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this.isInDOM && !this.alias && isInvalid(InvalidationType.DATA))
         {
            this.registerGFInject();
         }
      }
      
      override protected function onBeforeDispose() : void
      {
         this.gfInject.removeEventListener(Event.RESIZE,this.onInjectResizeHandler);
         if(this.alias)
         {
            if(this.isPopUp)
            {
               App.stage.dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.UNREGISTER_POP_UP,this.alias + POP_UP_ALIAS_POSTFIX,this.gfViewName,null));
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
         removeChild(this.gfInject);
         if(!this.gfInject.isDisposed())
         {
            this.gfInject.dispose();
         }
         this.gfInject = null;
         super.onDispose();
      }
      
      private function registerGFInject() : void
      {
         this.gfViewName = data.messageVO.gfViewName;
         var _loc1_:Object = data.messageVO.linkageData;
         this.alias = this.gfViewName + _loc1_.gfDataID.toString() + data.entityID.toString() + getTimer().toString();
         this.sizeCacheKey = this.gfViewName + _loc1_.gfDataID.toString();
         if(this.isPopUp)
         {
            dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.REGISTER_POP_UP,this.alias + POP_UP_ALIAS_POSTFIX,this.gfViewName,this.gfInject,_loc1_));
         }
         else
         {
            dispatchEvent(new NotificationRegisteringEvent(NotificationRegisteringEvent.REGISTER_SM,this.alias,this.gfViewName,this.gfInject,_loc1_));
         }
         invalidateLayout();
      }
      
      private function onInjectResizeHandler(param1:Event) : void
      {
         if(this.isInjectSizeValid() && this._notificationCache.getCachedSize(this.sizeCacheKey) != this.gfInject.height)
         {
            this._notificationCache.addCachedSize(this.sizeCacheKey,this.gfInject.height);
            dispatchEvent(new Event(Event.RESIZE));
         }
      }
      
      private function isInjectSizeValid() : Boolean
      {
         return this.gfInject.height && this.gfInject.height > MIN_HEIGHT;
      }
   }
}
