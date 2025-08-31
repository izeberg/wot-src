package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _85625b0639e5be6bccaa969caf3c1041f7a5be4709c45dfe499f4c8f2021bd8c_flash_display_Sprite extends Sprite
   {
       
      
      public function _85625b0639e5be6bccaa969caf3c1041f7a5be4709c45dfe499f4c8f2021bd8c_flash_display_Sprite()
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
