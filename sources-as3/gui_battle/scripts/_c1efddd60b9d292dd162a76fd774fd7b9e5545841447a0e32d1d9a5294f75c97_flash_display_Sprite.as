package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c1efddd60b9d292dd162a76fd774fd7b9e5545841447a0e32d1d9a5294f75c97_flash_display_Sprite extends Sprite
   {
       
      
      public function _c1efddd60b9d292dd162a76fd774fd7b9e5545841447a0e32d1d9a5294f75c97_flash_display_Sprite()
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
