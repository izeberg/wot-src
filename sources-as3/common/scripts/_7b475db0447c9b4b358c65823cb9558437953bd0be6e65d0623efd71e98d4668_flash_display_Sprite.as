package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7b475db0447c9b4b358c65823cb9558437953bd0be6e65d0623efd71e98d4668_flash_display_Sprite extends Sprite
   {
       
      
      public function _7b475db0447c9b4b358c65823cb9558437953bd0be6e65d0623efd71e98d4668_flash_display_Sprite()
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
