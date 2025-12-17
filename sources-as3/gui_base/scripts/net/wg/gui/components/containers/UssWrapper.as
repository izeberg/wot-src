package net.wg.gui.components.containers
{
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.InteractiveObject;
   
   public class UssWrapper extends BaseWrapper
   {
       
      
      public function UssWrapper()
      {
         super();
      }
      
      override public function isFullScreenModeSupported() : Boolean
      {
         return true;
      }
      
      override public function getComponentForFocus() : InteractiveObject
      {
         return this.findComponentToFocus(this) || this;
      }
      
      private function findComponentToFocus(param1:DisplayObjectContainer) : InteractiveObject
      {
         var _loc3_:DisplayObject = null;
         var _loc4_:DisplayObjectContainer = null;
         var _loc5_:InteractiveObject = null;
         var _loc2_:int = 0;
         while(_loc2_ != param1.numChildren)
         {
            _loc3_ = param1.getChildAt(_loc2_);
            if(_loc3_ is DisplayObjectContainer)
            {
               _loc4_ = DisplayObjectContainer(_loc3_);
               if(_loc4_.tabEnabled)
               {
                  App.utils.focusHandler.setFocus(_loc4_);
                  return _loc4_;
               }
            }
            _loc2_++;
         }
         _loc2_ = 0;
         while(_loc2_ != param1.numChildren)
         {
            _loc3_ = param1.getChildAt(_loc2_);
            if(_loc3_ is DisplayObjectContainer)
            {
               _loc4_ = DisplayObjectContainer(_loc3_);
               _loc5_ = this.findComponentToFocus(_loc4_);
               if(_loc5_)
               {
                  return _loc5_;
               }
            }
            _loc2_++;
         }
         return null;
      }
   }
}
