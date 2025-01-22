package net.wg.gui.lobby.personalMissions.components
{
   import flash.display.InteractiveObject;
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.infrastructure.interfaces.IViewStackExContent;
   
   public class PM3Operations extends GFInjectComponent implements IViewStackExContent
   {
       
      
      public function PM3Operations()
      {
         super();
         setManageSize(true);
      }
      
      public function canShowAutomatically() : Boolean
      {
         return true;
      }
      
      public function getComponentForFocus() : InteractiveObject
      {
         return undefined;
      }
      
      public function setActive(param1:Boolean) : void
      {
      }
      
      public function update(param1:Object) : void
      {
      }
   }
}
