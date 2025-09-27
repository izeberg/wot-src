package net.wg.gui.lobby.notify_center
{
   import flash.events.MouseEvent;
   import flash.events.TextEvent;
   import net.wg.infrastructure.base.meta.INotifyCenterDialogMeta;
   import net.wg.infrastructure.base.meta.impl.NotifyCenterDialogMeta;
   
   public class NotifyCenterDialog extends NotifyCenterDialogMeta implements INotifyCenterDialogMeta
   {
       
      
      private var _isTFClickedByMBR:Boolean = false;
      
      public function NotifyCenterDialog()
      {
         super();
      }
      
      override protected function onPopulate() : void
      {
         textField.addEventListener(TextEvent.LINK,this.onMessageLinkClickHandler);
         textField.addEventListener(MouseEvent.CLICK,this.onMessageTextClickHandler);
         App.utils.styleSheetManager.setLinkStyle(textField);
         super.onPopulate();
      }
      
      override protected function onDispose() : void
      {
         textField.removeEventListener(TextEvent.LINK,this.onMessageLinkClickHandler);
         textField.removeEventListener(MouseEvent.CLICK,this.onMessageTextClickHandler);
         super.onDispose();
      }
      
      private function doActionFn(param1:String, param2:Boolean) : void
      {
         assertNotNull(param1,"Button has not unique action (actionID)");
         doActionS(param1,param2);
      }
      
      override protected function onBtnClick(param1:Object) : void
      {
         var _loc2_:String = param1.action;
         this.doActionFn(_loc2_,true);
      }
      
      private function onMessageTextClickHandler(param1:MouseEvent) : void
      {
         this._isTFClickedByMBR = App.utils.commons.isRightButton(param1);
      }
      
      private function onMessageLinkClickHandler(param1:TextEvent) : void
      {
         if(this._isTFClickedByMBR)
         {
            return;
         }
         this.doActionFn(param1.text,false);
      }
   }
}
