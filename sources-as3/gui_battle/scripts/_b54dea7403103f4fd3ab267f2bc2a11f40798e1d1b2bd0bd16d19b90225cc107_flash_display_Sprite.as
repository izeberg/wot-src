package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b54dea7403103f4fd3ab267f2bc2a11f40798e1d1b2bd0bd16d19b90225cc107_flash_display_Sprite extends Sprite
   {
       
      
      public function _b54dea7403103f4fd3ab267f2bc2a11f40798e1d1b2bd0bd16d19b90225cc107_flash_display_Sprite()
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
