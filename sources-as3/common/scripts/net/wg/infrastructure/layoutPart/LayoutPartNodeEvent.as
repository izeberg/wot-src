package net.wg.infrastructure.layoutPart
{
   import flash.events.Event;
   
   public class LayoutPartNodeEvent extends Event
   {
      
      public static const PROPERTIES_UPDATED:String = "transformUpdated";
      
      public static const VISIBILITY_CHANGED:String = "visibilityChanged";
       
      
      private var _name:String;
      
      public function LayoutPartNodeEvent(param1:String, param2:String)
      {
         super(param1,false,false);
         this._name = param2;
      }
      
      public function get name() : String
      {
         return this._name;
      }
   }
}
