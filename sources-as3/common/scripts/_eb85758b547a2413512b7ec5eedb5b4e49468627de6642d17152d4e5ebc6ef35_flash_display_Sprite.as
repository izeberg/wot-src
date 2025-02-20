package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _eb85758b547a2413512b7ec5eedb5b4e49468627de6642d17152d4e5ebc6ef35_flash_display_Sprite extends Sprite
   {
       
      
      public function _eb85758b547a2413512b7ec5eedb5b4e49468627de6642d17152d4e5ebc6ef35_flash_display_Sprite()
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
