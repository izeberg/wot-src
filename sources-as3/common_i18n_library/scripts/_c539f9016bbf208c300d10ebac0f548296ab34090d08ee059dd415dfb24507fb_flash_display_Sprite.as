package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c539f9016bbf208c300d10ebac0f548296ab34090d08ee059dd415dfb24507fb_flash_display_Sprite extends Sprite
   {
       
      
      public function _c539f9016bbf208c300d10ebac0f548296ab34090d08ee059dd415dfb24507fb_flash_display_Sprite()
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
