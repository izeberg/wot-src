package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _32abed84cb606d79971297ff09b5ec769b292fa8d8adadeab9d1c5e201f35fe9_flash_display_Sprite extends Sprite
   {
       
      
      public function _32abed84cb606d79971297ff09b5ec769b292fa8d8adadeab9d1c5e201f35fe9_flash_display_Sprite()
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
