package net.wg.infrastructure.events
{
   import flash.events.Event;
   import net.wg.infrastructure.interfaces.ILayoutPart;
   
   public class SharedLayoutRegisterEvent extends Event
   {
      
      public static const REGISTER_LAYOUT_EVENT:String = "registerLayout";
      
      public static const UNREGISTER_LAYOUT_EVENT:String = "unregisterLayout";
       
      
      private var _layoutPart:ILayoutPart;
      
      public function SharedLayoutRegisterEvent(param1:String, param2:ILayoutPart)
      {
         super(param1,false,false);
         this._layoutPart = param2;
      }
      
      public function get layoutPart() : ILayoutPart
      {
         return this._layoutPart;
      }
      
      public function get layoutId() : uint
      {
         return this._layoutPart.layoutId;
      }
   }
}
