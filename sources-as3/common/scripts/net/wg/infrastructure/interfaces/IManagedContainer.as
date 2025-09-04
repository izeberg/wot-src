package net.wg.infrastructure.interfaces
{
   import flash.geom.Rectangle;
   
   public interface IManagedContainer extends ISimpleManagedContainer
   {
       
      
      function updateStage(param1:Number, param2:Number, param3:Rectangle = null) : void;
      
      function tryToSetFocus(param1:Boolean = false, param2:Boolean = false) : Boolean;
      
      function tryToUpdateContent() : void;
      
      function setFocusedView(param1:IManagedContent, param2:Boolean = false) : void;
      
      function getTopmostView(param1:Boolean = false) : IManagedContent;
      
      function allowFocusNextLayer(param1:String) : Boolean;
      
      function get paddings() : Rectangle;
   }
}
