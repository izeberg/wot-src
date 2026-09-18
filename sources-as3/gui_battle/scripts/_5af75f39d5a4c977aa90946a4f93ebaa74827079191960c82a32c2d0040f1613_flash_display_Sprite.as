package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5af75f39d5a4c977aa90946a4f93ebaa74827079191960c82a32c2d0040f1613_flash_display_Sprite extends Sprite
   {
       
      
      public function _5af75f39d5a4c977aa90946a4f93ebaa74827079191960c82a32c2d0040f1613_flash_display_Sprite()
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
