package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1cdbbaaa597230a9354609c91c457dc2423a9ab3d63252cafe5e89073b48d97b_flash_display_Sprite extends Sprite
   {
       
      
      public function _1cdbbaaa597230a9354609c91c457dc2423a9ab3d63252cafe5e89073b48d97b_flash_display_Sprite()
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
