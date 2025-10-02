package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _429f0c851d62369c9ede3cbc3cb46de48b7273b03665c4ae52cbd5aea21e3ffd_flash_display_Sprite extends Sprite
   {
       
      
      public function _429f0c851d62369c9ede3cbc3cb46de48b7273b03665c4ae52cbd5aea21e3ffd_flash_display_Sprite()
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
