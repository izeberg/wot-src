package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6ae0c2818c9a3d623f356bef2540f341b8c4ffc67e295b856ec06731c380c614_flash_display_Sprite extends Sprite
   {
       
      
      public function _6ae0c2818c9a3d623f356bef2540f341b8c4ffc67e295b856ec06731c380c614_flash_display_Sprite()
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
