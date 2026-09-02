package net.wg.gui.lobby.hangar.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class LobbyVisibilityVO extends DAAPIDataClass
   {
       
      
      public var headerIsVisible:Boolean = true;
      
      public var messengerBarVisible:Boolean = true;
      
      public var ignoreTopOffset:Boolean = false;
      
      public function LobbyVisibilityVO(param1:Object)
      {
         super(param1);
      }
   }
}
