package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6ea7070305288ba4adafced09d3f6c7916c85f3893f4b8533f5773c29742e7bf_flash_display_Sprite extends Sprite
   {
       
      
      public function _6ea7070305288ba4adafced09d3f6c7916c85f3893f4b8533f5773c29742e7bf_flash_display_Sprite()
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
