package net.wg.gui.battle.views.minimap.interfaces
{
   import flash.display.DisplayObject;
   import flash.geom.Point;
   import net.wg.infrastructure.interfaces.IDisplayObject;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public interface IHoverableEntity extends IDisplayObject, IDisposable
   {
       
      
      function onRollOver(param1:Point) : void;
      
      function onRollOut(param1:Point) : void;
      
      function onClick(param1:Point) : void;
      
      function get hitTestTarget() : DisplayObject;
   }
}
