package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8c27d08cf7d676c2cad13a954239e4d1875e549e5fc6f1b730abfe5deb3e9f46_flash_display_Sprite extends Sprite
   {
       
      
      public function _8c27d08cf7d676c2cad13a954239e4d1875e549e5fc6f1b730abfe5deb3e9f46_flash_display_Sprite()
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
