package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _338edbfa4713580cd6f490475db9f329645ec7267e8258fb49b7172ebd60038d_flash_display_Sprite extends Sprite
   {
       
      
      public function _338edbfa4713580cd6f490475db9f329645ec7267e8258fb49b7172ebd60038d_flash_display_Sprite()
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
