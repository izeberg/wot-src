package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _82c2e4b6524ec6033f73836b4063b68268b33fb89666da077988eabd4f705100_flash_display_Sprite extends Sprite
   {
       
      
      public function _82c2e4b6524ec6033f73836b4063b68268b33fb89666da077988eabd4f705100_flash_display_Sprite()
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
