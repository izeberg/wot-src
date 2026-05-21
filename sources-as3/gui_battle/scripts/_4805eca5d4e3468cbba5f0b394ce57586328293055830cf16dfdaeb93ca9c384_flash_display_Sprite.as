package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4805eca5d4e3468cbba5f0b394ce57586328293055830cf16dfdaeb93ca9c384_flash_display_Sprite extends Sprite
   {
       
      
      public function _4805eca5d4e3468cbba5f0b394ce57586328293055830cf16dfdaeb93ca9c384_flash_display_Sprite()
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
