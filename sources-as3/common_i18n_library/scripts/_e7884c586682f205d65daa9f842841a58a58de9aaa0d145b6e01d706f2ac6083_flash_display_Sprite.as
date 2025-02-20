package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e7884c586682f205d65daa9f842841a58a58de9aaa0d145b6e01d706f2ac6083_flash_display_Sprite extends Sprite
   {
       
      
      public function _e7884c586682f205d65daa9f842841a58a58de9aaa0d145b6e01d706f2ac6083_flash_display_Sprite()
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
