package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _837bd02d4127d4d857df271cc8438146b92abbc7616681c6f65da3ad2ff23756_flash_display_Sprite extends Sprite
   {
       
      
      public function _837bd02d4127d4d857df271cc8438146b92abbc7616681c6f65da3ad2ff23756_flash_display_Sprite()
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
