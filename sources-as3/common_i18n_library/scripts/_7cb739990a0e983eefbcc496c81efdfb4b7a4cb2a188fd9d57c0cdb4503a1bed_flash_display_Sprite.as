package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7cb739990a0e983eefbcc496c81efdfb4b7a4cb2a188fd9d57c0cdb4503a1bed_flash_display_Sprite extends Sprite
   {
       
      
      public function _7cb739990a0e983eefbcc496c81efdfb4b7a4cb2a188fd9d57c0cdb4503a1bed_flash_display_Sprite()
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
