package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1f5c19ca455e07ddcd54a275ea707842a14cf330f5383f037182fe4a0f893cba_flash_display_Sprite extends Sprite
   {
       
      
      public function _1f5c19ca455e07ddcd54a275ea707842a14cf330f5383f037182fe4a0f893cba_flash_display_Sprite()
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
