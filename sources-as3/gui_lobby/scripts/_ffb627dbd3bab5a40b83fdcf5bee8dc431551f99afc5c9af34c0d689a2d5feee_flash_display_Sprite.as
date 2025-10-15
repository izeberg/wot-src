package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ffb627dbd3bab5a40b83fdcf5bee8dc431551f99afc5c9af34c0d689a2d5feee_flash_display_Sprite extends Sprite
   {
       
      
      public function _ffb627dbd3bab5a40b83fdcf5bee8dc431551f99afc5c9af34c0d689a2d5feee_flash_display_Sprite()
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
