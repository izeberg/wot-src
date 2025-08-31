package net.wg.gui.lobby.components
{
   import flash.geom.Rectangle;
   import net.wg.infrastructure.interfaces.IViewStackContent;
   
   public interface IResizableContent extends IViewStackContent
   {
       
      
      function setViewSize(param1:Number, param2:Number, param3:Rectangle = null) : void;
      
      function get centerOffset() : int;
      
      function set centerOffset(param1:int) : void;
      
      function get active() : Boolean;
      
      function set active(param1:Boolean) : void;
   }
}
