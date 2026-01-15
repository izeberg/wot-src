package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _11c33d62717cdf015e14924e8fd35d6ccb19b6230950048d2ce673f18baccc7b_flash_display_Sprite extends Sprite
   {
       
      
      public function _11c33d62717cdf015e14924e8fd35d6ccb19b6230950048d2ce673f18baccc7b_flash_display_Sprite()
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
