package net.wg.frontline.gui.battle.views.upgradePanel
{
   import flash.display.DisplayObject;
   import flash.geom.Rectangle;
   import net.wg.frontline.gui.battle.views.upgradePanel.data.FrontlineConfiguratorModuleVO;
   import net.wg.infrastructure.interfaces.IDisplayObject;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public interface IFrontlineConfiguratorRenderer extends IDisplayObject, IDisposable
   {
       
      
      function setIndex(param1:uint, param2:uint) : void;
      
      function setData(param1:FrontlineConfiguratorModuleVO) : void;
      
      function makeUpState() : void;
      
      function makeOverState() : void;
      
      function get moduleIntCD() : uint;
      
      function get moduleIdx() : int;
      
      function get columnIdx() : int;
      
      function getNodeBounds(param1:DisplayObject) : Rectangle;
   }
}
