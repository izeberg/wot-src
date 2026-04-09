package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _03473888fb3fadde4742e55ef22e7d2fa6309155414e743dd53dda93673b7202_flash_display_Sprite extends Sprite
   {
       
      
      public function _03473888fb3fadde4742e55ef22e7d2fa6309155414e743dd53dda93673b7202_flash_display_Sprite()
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
