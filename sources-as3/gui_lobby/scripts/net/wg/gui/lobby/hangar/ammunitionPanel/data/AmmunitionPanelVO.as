package net.wg.gui.lobby.hangar.ammunitionPanel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class AmmunitionPanelVO extends DAAPIDataClass
   {
      
      public static const MAINTENANCE:String = "maintenance";
      
      public static const CUSTOMIZATION:String = "customization";
      
      public static const CHANGE_NATION:String = "changeNation";
      
      public static const EASY_TANK_EQUIP:String = "easyTankEquip";
      
      private static const BTNS_IDS:Vector.<String> = new <String>[MAINTENANCE,CUSTOMIZATION,CHANGE_NATION,EASY_TANK_EQUIP];
       
      
      private var _btnsData:Object = null;
      
      public function AmmunitionPanelVO(param1:Object)
      {
         this._btnsData = {};
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(BTNS_IDS.indexOf(param1) != -1 && param2 != null)
         {
            this._btnsData[param1] = new AmmunitionPanelBtnVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         this._btnsData = App.utils.data.cleanupDynamicObject(this._btnsData);
         super.onDispose();
      }
      
      public function getBtnData(param1:String) : AmmunitionPanelBtnVO
      {
         if(this._btnsData.hasOwnProperty(param1))
         {
            return this._btnsData[param1];
         }
         return null;
      }
      
      public function get isAnyButtonVisible() : Boolean
      {
         var _loc1_:AmmunitionPanelBtnVO = null;
         for each(_loc1_ in this._btnsData)
         {
            if(_loc1_.visible)
            {
               return true;
            }
         }
         return false;
      }
   }
}
