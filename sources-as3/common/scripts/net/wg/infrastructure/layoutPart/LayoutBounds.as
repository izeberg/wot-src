package net.wg.infrastructure.layoutPart
{
   public class LayoutBounds
   {
       
      
      public var width:Number;
      
      public var height:Number;
      
      public var pivotX:Number;
      
      public var pivotY:Number;
      
      public function LayoutBounds(param1:Number = 0, param2:Number = 0, param3:Number = 0, param4:Number = 0)
      {
         super();
         this.width = param1;
         this.height = param2;
         this.pivotX = param3;
         this.pivotY = param4;
      }
   }
}
