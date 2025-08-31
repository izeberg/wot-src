package net.wg.gui.battle.windows.vo
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class IngameDetailsKeyVO extends DAAPIDataClass
   {
       
      
      public var vKey:String = "";
      
      public var keyName:String = "";
      
      public var isLong:Boolean = false;
      
      public function IngameDetailsKeyVO(param1:Object = null)
      {
         super(param1);
      }
      
      public function isEqual(param1:IngameDetailsKeyVO) : Boolean
      {
         return this.vKey == param1.vKey && this.keyName == param1.keyName && this.isLong == param1.isLong;
      }
   }
}
