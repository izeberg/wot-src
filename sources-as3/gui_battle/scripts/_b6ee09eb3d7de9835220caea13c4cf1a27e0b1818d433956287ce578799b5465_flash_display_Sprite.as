package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b6ee09eb3d7de9835220caea13c4cf1a27e0b1818d433956287ce578799b5465_flash_display_Sprite extends Sprite
   {
       
      
      public function _b6ee09eb3d7de9835220caea13c4cf1a27e0b1818d433956287ce578799b5465_flash_display_Sprite()
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
