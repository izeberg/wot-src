package net.wg.infrastructure.layoutPart
{
   import flash.events.Event;
   
   public class LayoutPartEvent extends Event
   {
      
      public static const ADDED_EVENT:String = "nodeAdded";
      
      public static const UPDATE_EVENT:String = "nodeUpdated";
      
      public static const REMOVED_EVENT:String = "nodeRemoved";
      
      public static const LAYOUT_CHANGED_EVENT:String = "layoutChanged";
       
      
      public var payload:Object = null;
      
      private var _node:LayoutPartNode;
      
      public function LayoutPartEvent(param1:String, param2:LayoutPartNode)
      {
         super(param1,false,false);
         this._node = param2;
      }
      
      public function get name() : String
      {
         return this._node.name;
      }
      
      public function get properties() : Object
      {
         return this.payload;
      }
      
      public function get node() : LayoutPartNode
      {
         return this._node;
      }
   }
}
