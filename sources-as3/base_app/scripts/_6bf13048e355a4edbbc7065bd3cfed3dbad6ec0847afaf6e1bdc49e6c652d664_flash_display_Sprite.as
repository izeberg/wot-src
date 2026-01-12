package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6bf13048e355a4edbbc7065bd3cfed3dbad6ec0847afaf6e1bdc49e6c652d664_flash_display_Sprite extends Sprite
   {
       
      
      public function _6bf13048e355a4edbbc7065bd3cfed3dbad6ec0847afaf6e1bdc49e6c652d664_flash_display_Sprite()
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
