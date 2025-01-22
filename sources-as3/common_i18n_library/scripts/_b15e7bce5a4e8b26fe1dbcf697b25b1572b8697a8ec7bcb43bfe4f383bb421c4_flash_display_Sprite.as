package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b15e7bce5a4e8b26fe1dbcf697b25b1572b8697a8ec7bcb43bfe4f383bb421c4_flash_display_Sprite extends Sprite
   {
       
      
      public function _b15e7bce5a4e8b26fe1dbcf697b25b1572b8697a8ec7bcb43bfe4f383bb421c4_flash_display_Sprite()
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
