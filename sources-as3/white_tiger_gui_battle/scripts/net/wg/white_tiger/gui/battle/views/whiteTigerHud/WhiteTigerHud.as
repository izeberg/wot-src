package net.wg.white_tiger.gui.battle.views.whiteTigerHud
{
   import net.wg.gui.components.containers.inject.GFInjectComponent;
   import net.wg.infrastructure.interfaces.entity.IDisplayableComponent;
   
   public class WhiteTigerHud extends GFInjectComponent implements IDisplayableComponent
   {
       
      
      public function WhiteTigerHud()
      {
         super();
         setManageSize(true);
      }
      
      public function updateStage(param1:Number, param2:Number) : void
      {
         x = y = 0;
         setSize(param1,param2);
         invalidateSize();
      }
      
      public function setCompVisible(param1:Boolean) : void
      {
         visible = param1;
      }
      
      public function isCompVisible() : Boolean
      {
         return visible;
      }
   }
}
