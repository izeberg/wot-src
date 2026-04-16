package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7353fe6a08a58f2ab4833129c593eb36fecba19aa9e3f676d9e31509de626f09_flash_display_Sprite extends Sprite
   {
       
      
      public function _7353fe6a08a58f2ab4833129c593eb36fecba19aa9e3f676d9e31509de626f09_flash_display_Sprite()
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
