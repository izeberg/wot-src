package net.wg.gui.lobby.battleResults.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class GiftStampVO extends DAAPIDataClass
   {
       
      
      public var name:String = "";
      
      public var count:int = 0;
      
      public function GiftStampVO(param1:Object)
      {
         super(param1);
      }
   }
}
