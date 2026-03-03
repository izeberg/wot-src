package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4916b4ce352414ad119e6432203906234c058d8dd304418b14bec29e1fb18a29_flash_display_Sprite extends Sprite
   {
       
      
      public function _4916b4ce352414ad119e6432203906234c058d8dd304418b14bec29e1fb18a29_flash_display_Sprite()
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
