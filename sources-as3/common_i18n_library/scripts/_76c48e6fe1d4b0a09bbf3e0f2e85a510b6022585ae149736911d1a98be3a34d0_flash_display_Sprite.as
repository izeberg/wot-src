package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _76c48e6fe1d4b0a09bbf3e0f2e85a510b6022585ae149736911d1a98be3a34d0_flash_display_Sprite extends Sprite
   {
       
      
      public function _76c48e6fe1d4b0a09bbf3e0f2e85a510b6022585ae149736911d1a98be3a34d0_flash_display_Sprite()
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
