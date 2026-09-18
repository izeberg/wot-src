package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b8c64caabbe63b1159c343116f98ddcf009b0b42fb0a238b058a3b8339028e33_flash_display_Sprite extends Sprite
   {
       
      
      public function _b8c64caabbe63b1159c343116f98ddcf009b0b42fb0a238b058a3b8339028e33_flash_display_Sprite()
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
