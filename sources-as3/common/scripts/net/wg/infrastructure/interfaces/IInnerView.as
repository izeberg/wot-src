package net.wg.infrastructure.interfaces
{
   import flash.geom.Rectangle;
   
   public interface IInnerView
   {
       
      
      function updateStageWithPadding(param1:Number, param2:Number, param3:Rectangle) : void;
      
      function isFullScreenModeSupported() : Boolean;
   }
}
