package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7d7ac1b2087d91a2f335d48580dd8ed4a3927ef2da85b8a5eba9c134300ae089_flash_display_Sprite extends Sprite
   {
       
      
      public function _7d7ac1b2087d91a2f335d48580dd8ed4a3927ef2da85b8a5eba9c134300ae089_flash_display_Sprite()
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
