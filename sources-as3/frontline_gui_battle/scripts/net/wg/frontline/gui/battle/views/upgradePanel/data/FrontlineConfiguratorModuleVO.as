package net.wg.frontline.gui.battle.views.upgradePanel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class FrontlineConfiguratorModuleVO extends DAAPIDataClass
   {
       
      
      public var icon:String = "";
      
      public var level:int = -1;
      
      public var intCD:int = 0;
      
      public var selected:Boolean = false;
      
      public var available:Boolean = false;
      
      public var gap:int = 0;
      
      public function FrontlineConfiguratorModuleVO(param1:Object)
      {
         super(param1);
      }
      
      public function update(param1:FrontlineConfiguratorModuleVO) : void
      {
         this.selected = param1.selected;
         this.available = param1.available;
         this.level = param1.level;
      }
   }
}
