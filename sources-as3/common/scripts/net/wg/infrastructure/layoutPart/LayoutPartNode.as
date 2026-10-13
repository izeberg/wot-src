package net.wg.infrastructure.layoutPart
{
   import flash.display.DisplayObject;
   import flash.geom.Rectangle;
   
   public class LayoutPartNode
   {
       
      
      public var name:String;
      
      public var partId:uint;
      
      public var object:DisplayObject;
      
      public var config:Object;
      
      public var visible:Boolean;
      
      public var calculated:Rectangle;
      
      public function LayoutPartNode(param1:String, param2:uint, param3:DisplayObject)
      {
         this.calculated = new Rectangle();
         super();
         this.name = param1;
         this.partId = param2;
         this.object = param3;
         this.config = null;
         this.visible = param3 && param3.visible;
      }
   }
}
