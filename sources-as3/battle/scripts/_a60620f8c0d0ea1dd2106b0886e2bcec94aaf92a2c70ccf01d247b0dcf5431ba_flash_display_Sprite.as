package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a60620f8c0d0ea1dd2106b0886e2bcec94aaf92a2c70ccf01d247b0dcf5431ba_flash_display_Sprite extends Sprite
   {
       
      
      public function _a60620f8c0d0ea1dd2106b0886e2bcec94aaf92a2c70ccf01d247b0dcf5431ba_flash_display_Sprite()
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
