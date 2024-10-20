package net.wg.gui.battle.epicBattle.views.upgradePanel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class EpicChoiceInfoPanelVO extends DAAPIDataClass
   {
      
      private static const FIRST_ITEM_LBL:String = "firstItem";
      
      private static const SECOND_ITEM_LBL:String = "secondItem";
       
      
      public var firstItem:EpicModuleInfoVO = null;
      
      public var secondItem:EpicModuleInfoVO = null;
      
      public function EpicChoiceInfoPanelVO(param1:Object = null)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == FIRST_ITEM_LBL || param1 == SECOND_ITEM_LBL)
         {
            if(this[param1])
            {
               this[param1].dispose();
            }
            this[param1] = new EpicModuleInfoVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         this.firstItem.dispose();
         this.firstItem = null;
         this.secondItem.dispose();
         this.secondItem = null;
         super.onDispose();
      }
   }
}
