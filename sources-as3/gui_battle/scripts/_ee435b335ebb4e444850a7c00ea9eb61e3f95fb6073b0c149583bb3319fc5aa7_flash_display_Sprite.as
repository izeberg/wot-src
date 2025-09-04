package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ee435b335ebb4e444850a7c00ea9eb61e3f95fb6073b0c149583bb3319fc5aa7_flash_display_Sprite extends Sprite
   {
       
      
      public function _ee435b335ebb4e444850a7c00ea9eb61e3f95fb6073b0c149583bb3319fc5aa7_flash_display_Sprite()
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
