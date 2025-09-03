package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _66b33ed8e0500a073e69649b45a1ccfd943936479d65d16082ea0c0812aeeeae_flash_display_Sprite extends Sprite
   {
       
      
      public function _66b33ed8e0500a073e69649b45a1ccfd943936479d65d16082ea0c0812aeeeae_flash_display_Sprite()
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
