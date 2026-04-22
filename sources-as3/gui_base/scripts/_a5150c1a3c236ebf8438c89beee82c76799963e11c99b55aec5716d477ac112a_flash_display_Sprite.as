package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a5150c1a3c236ebf8438c89beee82c76799963e11c99b55aec5716d477ac112a_flash_display_Sprite extends Sprite
   {
       
      
      public function _a5150c1a3c236ebf8438c89beee82c76799963e11c99b55aec5716d477ac112a_flash_display_Sprite()
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
