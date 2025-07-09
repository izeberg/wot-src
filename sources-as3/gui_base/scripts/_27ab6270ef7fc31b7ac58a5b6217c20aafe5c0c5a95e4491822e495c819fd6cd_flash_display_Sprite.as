package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _27ab6270ef7fc31b7ac58a5b6217c20aafe5c0c5a95e4491822e495c819fd6cd_flash_display_Sprite extends Sprite
   {
       
      
      public function _27ab6270ef7fc31b7ac58a5b6217c20aafe5c0c5a95e4491822e495c819fd6cd_flash_display_Sprite()
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
