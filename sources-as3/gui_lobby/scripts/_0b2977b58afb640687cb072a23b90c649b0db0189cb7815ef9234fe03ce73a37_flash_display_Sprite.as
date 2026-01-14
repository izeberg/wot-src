package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0b2977b58afb640687cb072a23b90c649b0db0189cb7815ef9234fe03ce73a37_flash_display_Sprite extends Sprite
   {
       
      
      public function _0b2977b58afb640687cb072a23b90c649b0db0189cb7815ef9234fe03ce73a37_flash_display_Sprite()
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
