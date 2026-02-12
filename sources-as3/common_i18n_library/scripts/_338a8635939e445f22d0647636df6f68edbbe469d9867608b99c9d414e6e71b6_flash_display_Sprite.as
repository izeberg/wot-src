package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _338a8635939e445f22d0647636df6f68edbbe469d9867608b99c9d414e6e71b6_flash_display_Sprite extends Sprite
   {
       
      
      public function _338a8635939e445f22d0647636df6f68edbbe469d9867608b99c9d414e6e71b6_flash_display_Sprite()
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
