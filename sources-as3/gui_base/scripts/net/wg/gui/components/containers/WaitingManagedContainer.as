package net.wg.gui.components.containers
{
   import flash.display.DisplayObject;
   import flash.events.Event;
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.events.ChildVisibilityEvent;
   import net.wg.infrastructure.events.ContainerManagerEvent;
   import net.wg.infrastructure.interfaces.IView;
   import net.wg.infrastructure.managers.IWaitingView;
   import net.wg.utils.IAssertable;
   
   public class WaitingManagedContainer extends ManagedContainer
   {
       
      
      private var _waiting:IWaitingView = null;
      
      private var _prevModalFocus:IView;
      
      public function WaitingManagedContainer(param1:String)
      {
         super(param1);
         enabled = false;
         mouseEnabled = true;
      }
      
      override public function addChild(param1:DisplayObject) : DisplayObject
      {
         var _loc2_:String = "WaitingManagerContainer must be contain only waiting view!";
         var _loc3_:IAssertable = App.utils.asserter;
         _loc3_.assert(param1 is IWaitingView,_loc2_);
         _loc3_.assertNull(this._waiting,_loc2_);
         this._waiting = param1 as IWaitingView;
         this._waiting.visible = false;
         this._waiting.addEventListener(ChildVisibilityEvent.CHILD_HIDDEN,this.onWaitingHiddenHandler);
         this._waiting.addEventListener(ChildVisibilityEvent.CHILD_SHOWN,this.onWaitingShownHandler);
         super.addChild(param1);
         App.containerMgr.addEventListener(ContainerManagerEvent.VIEW_REMOVED,this.onContainerMgrViewRemovedHandler,false,0,true);
         IWaitingView(this._waiting).validateNow();
         return param1;
      }
      
      override public function canFocusNextLayer(param1:String) : Boolean
      {
         return !this._waiting.isActive;
      }
      
      override protected function onDispose() : void
      {
         this._prevModalFocus = null;
         if(this._waiting)
         {
            this._waiting.removeEventListener(ChildVisibilityEvent.CHILD_HIDDEN,this.onWaitingHiddenHandler);
            this._waiting.removeEventListener(ChildVisibilityEvent.CHILD_SHOWN,this.onWaitingShownHandler);
            if(this.contains(this._waiting as DisplayObject))
            {
               removeChild(this._waiting as DisplayObject);
            }
            this._waiting = null;
         }
         super.onDispose();
      }
      
      override protected function updateModalFocus(param1:Event) : void
      {
      }
      
      private function onContainerMgrViewRemovedHandler(param1:ContainerManagerEvent) : void
      {
         if(this._prevModalFocus == param1.view)
         {
            this._prevModalFocus = null;
         }
      }
      
      private function onWaitingShownHandler(param1:ChildVisibilityEvent) : void
      {
         DebugUtils.LOG_TRACE("Show waiting");
         App.utils.asserter.assertNotNull(this._waiting,"_waiting" + Errors.CANT_NULL);
         this._prevModalFocus = App.containerMgr.lastFocusedView;
         this._waiting.visible = true;
         setFocusedView(this._waiting as IView);
         this._waiting.validateNow();
      }
      
      private function onWaitingHiddenHandler(param1:ChildVisibilityEvent) : void
      {
         DebugUtils.LOG_TRACE("Hide waiting");
         App.utils.asserter.assertNotNull(this._waiting,"_waiting" + Errors.CANT_NULL);
         this._waiting.visible = false;
         var _loc2_:IView = this._prevModalFocus;
         this._prevModalFocus = null;
         if(!_loc2_ || !App.containerMgr.tryFocusView(_loc2_))
         {
            App.containerMgr.updateFocus();
         }
      }
   }
}
