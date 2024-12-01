package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e8e547de9575f043b4145bcd78b92107871b6a6af0c0337b13e52ca2beec8098_flash_display_Sprite extends Sprite
   {
       
      
      public function _e8e547de9575f043b4145bcd78b92107871b6a6af0c0337b13e52ca2beec8098_flash_display_Sprite()
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
