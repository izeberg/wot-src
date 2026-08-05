package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b11d3fc2cbd2a73874eb5a6af10088c20b14e71de53dd7f6bd931f7c8d4b6682_flash_display_Sprite extends Sprite
   {
       
      
      public function _b11d3fc2cbd2a73874eb5a6af10088c20b14e71de53dd7f6bd931f7c8d4b6682_flash_display_Sprite()
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
