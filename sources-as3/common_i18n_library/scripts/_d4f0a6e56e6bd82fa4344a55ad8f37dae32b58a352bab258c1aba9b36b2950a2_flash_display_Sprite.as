package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d4f0a6e56e6bd82fa4344a55ad8f37dae32b58a352bab258c1aba9b36b2950a2_flash_display_Sprite extends Sprite
   {
       
      
      public function _d4f0a6e56e6bd82fa4344a55ad8f37dae32b58a352bab258c1aba9b36b2950a2_flash_display_Sprite()
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
