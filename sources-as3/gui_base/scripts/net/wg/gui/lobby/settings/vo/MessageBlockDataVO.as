package net.wg.gui.lobby.settings.vo
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class MessageBlockDataVO extends DAAPIDataClass
   {
       
      
      public var message:String = "";
      
      public var actionName:String = "";
      
      public var buttonLabel:String = "";
      
      public var infoIconType:String = "";
      
      public var tooltip:String = "";
      
      public function MessageBlockDataVO(param1:Object)
      {
         super(param1);
      }
   }
}
