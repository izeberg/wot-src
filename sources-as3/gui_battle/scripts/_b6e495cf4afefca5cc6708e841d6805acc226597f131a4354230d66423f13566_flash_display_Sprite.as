package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b6e495cf4afefca5cc6708e841d6805acc226597f131a4354230d66423f13566_flash_display_Sprite extends Sprite
   {
       
      
      public function _b6e495cf4afefca5cc6708e841d6805acc226597f131a4354230d66423f13566_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
