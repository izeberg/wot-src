package net.wg.mock
{
   import flash.events.Event;
   import net.wg.infrastructure.interfaces.ILayoutPart;
   import net.wg.infrastructure.managers.ISharedLayoutManager;
   
   public class MockSharedLayoutManager implements ISharedLayoutManager
   {
       
      
      public function MockSharedLayoutManager()
      {
         super();
      }
      
      public function addEventListener(param1:String, param2:Function, param3:Boolean = false, param4:int = 0, param5:Boolean = false) : void
      {
      }
      
      public function dispose() : void
      {
      }
      
      public function hasEventListener(param1:String) : Boolean
      {
         return false;
      }
      
      public function isDisposed() : Boolean
      {
         return false;
      }
      
      public function notifyLayoutKilled(param1:uint) : void
      {
      }
      
      public function registerLayout(param1:ILayoutPart) : void
      {
      }
      
      public function removeEventListener(param1:String, param2:Function, param3:Boolean = false) : void
      {
      }
      
      public function unregisterLayout(param1:ILayoutPart) : void
      {
      }
      
      public function willTrigger(param1:String) : Boolean
      {
         return false;
      }
      
      public function dispatchEvent(param1:Event) : Boolean
      {
         return false;
      }
   }
}
