package net.wg.infrastructure.managers.impl
{
   import flash.events.EventDispatcher;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.events.SharedLayoutRegisterEvent;
   import net.wg.infrastructure.interfaces.ILayoutPart;
   import net.wg.infrastructure.managers.ISharedLayoutManager;
   
   public final class SharedLayoutManager extends EventDispatcher implements ISharedLayoutManager
   {
       
      
      private var _layoutParts:Dictionary;
      
      public function SharedLayoutManager()
      {
         this._layoutParts = new Dictionary();
         super();
      }
      
      public function dispose() : void
      {
         var _loc1_:ILayoutPart = null;
         for each(_loc1_ in this._layoutParts)
         {
            this.removeHandler(_loc1_);
         }
         this._layoutParts = null;
      }
      
      public function isDisposed() : Boolean
      {
         return false;
      }
      
      public function notifyLayoutKilled(param1:uint) : void
      {
         DebugUtils.LOG_WARNING("Layout " + param1 + " is killed from logic side");
         if(param1 in this._layoutParts)
         {
            delete this._layoutParts[param1];
         }
      }
      
      public function registerLayout(param1:ILayoutPart) : void
      {
         var _loc2_:String = null;
         if(param1.layoutId in this._layoutParts)
         {
            _loc2_ = "Layout " + param1.layoutId + Errors.ALREADY_REGISTERED;
            if(App.instance)
            {
               App.utils.asserter.assert(!(param1.layoutId in this._layoutParts),_loc2_);
            }
            else
            {
               DebugUtils.LOG_ERROR(_loc2_);
            }
            return;
         }
         this._layoutParts[param1.layoutId] = param1;
         dispatchEvent(new SharedLayoutRegisterEvent(SharedLayoutRegisterEvent.REGISTER_LAYOUT_EVENT,param1));
      }
      
      public function unregisterLayout(param1:ILayoutPart) : void
      {
         if(param1.layoutId in this._layoutParts)
         {
            this.removeHandler(param1);
            delete this._layoutParts[param1.layoutId];
         }
      }
      
      private function removeHandler(param1:ILayoutPart) : void
      {
         dispatchEvent(new SharedLayoutRegisterEvent(SharedLayoutRegisterEvent.UNREGISTER_LAYOUT_EVENT,param1));
      }
   }
}
