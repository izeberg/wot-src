package net.wg.infrastructure.layoutPart
{
   import flash.display.DisplayObject;
   import flash.events.EventDispatcher;
   import flash.geom.Rectangle;
   import flash.utils.Dictionary;
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.interfaces.ILayoutPart;
   
   public class BaseLayoutPart extends EventDispatcher implements ILayoutPart
   {
       
      
      protected var _nodes:Dictionary;
      
      private var _layoutId:uint = 0;
      
      private var _partId:uint = 0;
      
      public function BaseLayoutPart(param1:uint)
      {
         super();
         this._layoutId = param1;
         this._nodes = new Dictionary();
      }
      
      public function dispose() : void
      {
         if(App.instance)
         {
            App.utils.data.cleanupDynamicObject(this._nodes);
         }
         this._nodes = null;
      }
      
      public function getAlgorithmTypeName() : String
      {
         throw new Error("getAlgorithmTypeName must be overridden in subclass");
      }
      
      public function isDisposed() : Boolean
      {
         return false;
      }
      
      public function notifyAdded(param1:String, param2:uint) : void
      {
         var _loc3_:LayoutPartNode = null;
         if(this._partId != param2)
         {
            if(param1 in this._nodes)
            {
               this.assert(false,param1 + Errors.ALREADY_REGISTERED);
               return;
            }
            _loc3_ = new LayoutPartNode(param1,param2,null);
            _loc3_.visible = true;
            this._nodes[param1] = _loc3_;
         }
         dispatchEvent(new LayoutPartEvent(LayoutPartEvent.LAYOUT_CHANGED_EVENT,this._nodes[param1]));
      }
      
      public function notifyRemoved(param1:String, param2:uint) : void
      {
         if(!(param1 in this._nodes))
         {
            return;
         }
         var _loc3_:LayoutPartNode = this._nodes[param1];
         if(this._partId != param2)
         {
            delete this._nodes[param1];
         }
         dispatchEvent(new LayoutPartEvent(LayoutPartEvent.LAYOUT_CHANGED_EVENT,_loc3_));
      }
      
      public function notifyUpdated(param1:String, param2:uint, param3:Number, param4:Number, param5:Number, param6:Number) : void
      {
         if(!(param1 in this._nodes))
         {
            this.assert(false,param1 + Errors.MUST_REGISTER);
            return;
         }
         var _loc7_:LayoutPartNode = this._nodes[param1];
         _loc7_.calculated.x = param3;
         _loc7_.calculated.y = param4;
         _loc7_.calculated.width = param5;
         _loc7_.calculated.height = param6;
         if(this._partId == param2 && _loc7_.object)
         {
            this.applyLayoutToObject(_loc7_);
         }
         dispatchEvent(new LayoutPartEvent(LayoutPartEvent.LAYOUT_CHANGED_EVENT,_loc7_));
      }
      
      public function register(param1:DisplayObject) : void
      {
         this.doRegister(param1);
      }
      
      public function resendPositions() : void
      {
         var _loc1_:LayoutPartNode = null;
         for each(_loc1_ in this._nodes)
         {
            if(_loc1_.partId == this._partId)
            {
               this.sendUpdate(_loc1_);
            }
         }
      }
      
      public function unregister(param1:DisplayObject) : void
      {
         var _loc2_:String = param1.name;
         if(!(_loc2_ in this._nodes))
         {
            this.assert(false,_loc2_ + Errors.WASNT_UNREGISTERED);
            return;
         }
         param1.removeEventListener(LayoutPartNodeEvent.PROPERTIES_UPDATED,this.onPropertiesUpdatedHandler);
         param1.removeEventListener(LayoutPartNodeEvent.VISIBILITY_CHANGED,this.onVisibilityChangedHandler);
         var _loc3_:LayoutPartNode = this._nodes[_loc2_];
         this.dispatchNodeEvent(LayoutPartEvent.REMOVED_EVENT,_loc3_);
         delete this._nodes[_loc2_];
      }
      
      protected function doRegister(param1:DisplayObject, param2:Object = null) : void
      {
         var _loc5_:Object = null;
         var _loc3_:String = param1.name;
         this.assert(this._partId > 0,_loc3_ + " cannot add. Part is not connected: ");
         this.assert(!(_loc3_ in this._nodes),_loc3_ + Errors.ALREADY_REGISTERED);
         if(this._partId == 0 || _loc3_ in this._nodes)
         {
            return;
         }
         var _loc4_:LayoutPartNode = new LayoutPartNode(_loc3_,this._partId,param1);
         _loc4_.config = param2;
         this._nodes[_loc4_.name] = _loc4_;
         if(_loc4_.visible)
         {
            _loc5_ = this.makePayload(_loc4_);
            this.dispatchNodeEvent(LayoutPartEvent.ADDED_EVENT,_loc4_,_loc5_);
         }
         param1.addEventListener(LayoutPartNodeEvent.PROPERTIES_UPDATED,this.onPropertiesUpdatedHandler,false,0,true);
         param1.addEventListener(LayoutPartNodeEvent.VISIBILITY_CHANGED,this.onVisibilityChangedHandler,false,0,true);
      }
      
      protected function getLayoutBounds(param1:DisplayObject) : LayoutBounds
      {
         if(param1 is ILayoutBoundsProvider)
         {
            return ILayoutBoundsProvider(param1).getLayoutBounds();
         }
         return null;
      }
      
      protected function applyLayoutToObject(param1:LayoutPartNode) : void
      {
         var _loc2_:DisplayObject = param1.object;
         if(_loc2_ is ILayoutPositionable)
         {
            ILayoutPositionable(_loc2_).applyLayoutPosition(param1.calculated);
         }
         else
         {
            this.applyDefaultPosition(_loc2_,param1.calculated);
            this.applyDefaultSize(_loc2_,param1.calculated);
         }
      }
      
      protected function applyDefaultPosition(param1:DisplayObject, param2:Rectangle) : void
      {
         param1.x = param2.x;
         param1.y = param2.y;
      }
      
      protected function applyDefaultSize(param1:DisplayObject, param2:Rectangle) : void
      {
         if(param2.width != param1.width || param2.height != param1.height)
         {
            param1.width = param2.width;
            param1.height = param2.height;
         }
      }
      
      protected function makePayload(param1:LayoutPartNode) : Object
      {
         throw new Error("makePayload must be overridden in subclass");
      }
      
      protected function dispatchNodeEvent(param1:String, param2:LayoutPartNode, param3:Object = null) : void
      {
         var _loc4_:LayoutPartEvent = new LayoutPartEvent(param1,param2);
         if(param3)
         {
            _loc4_.payload = param3;
         }
         dispatchEvent(_loc4_);
      }
      
      private function assert(param1:Boolean, param2:String) : void
      {
         if(App.instance)
         {
            App.utils.asserter.assert(param1,param2);
         }
         else if(!param1)
         {
            DebugUtils.LOG_ERROR(param2);
         }
      }
      
      private function sendUpdate(param1:LayoutPartNode) : void
      {
         var _loc2_:Object = null;
         if(param1.object.visible)
         {
            _loc2_ = this.makePayload(param1);
            this.dispatchNodeEvent(LayoutPartEvent.UPDATE_EVENT,param1,_loc2_);
         }
      }
      
      public function get nodes() : Dictionary
      {
         return this._nodes;
      }
      
      public function get layoutId() : uint
      {
         return this._layoutId;
      }
      
      public function get partId() : uint
      {
         return this._partId;
      }
      
      public function set partId(param1:uint) : void
      {
         this._partId = param1;
         dispatchEvent(new LayoutPartEvent(LayoutPartEvent.LAYOUT_CHANGED_EVENT,null));
      }
      
      private function onPropertiesUpdatedHandler(param1:LayoutPartNodeEvent) : void
      {
         var _loc2_:String = param1.name;
         if(!(_loc2_ in this._nodes))
         {
            DebugUtils.LOG_ERROR("BaseLayoutPart | component is not registered: " + _loc2_);
            return;
         }
         var _loc3_:LayoutPartNode = this._nodes[_loc2_];
         this.sendUpdate(_loc3_);
      }
      
      private function onVisibilityChangedHandler(param1:LayoutPartNodeEvent) : void
      {
         var _loc4_:Object = null;
         var _loc2_:String = param1.name;
         if(!(_loc2_ in this._nodes))
         {
            DebugUtils.LOG_ERROR("BaseLayoutPart | component is not registered: " + _loc2_);
            return;
         }
         var _loc3_:LayoutPartNode = this._nodes[_loc2_];
         if(_loc3_.visible == _loc3_.object.visible)
         {
            return;
         }
         _loc3_.visible = _loc3_.object.visible;
         if(_loc3_.visible)
         {
            _loc4_ = this.makePayload(_loc3_);
            this.dispatchNodeEvent(LayoutPartEvent.ADDED_EVENT,_loc3_,_loc4_);
         }
         else
         {
            this.dispatchNodeEvent(LayoutPartEvent.REMOVED_EVENT,_loc3_);
         }
      }
   }
}
