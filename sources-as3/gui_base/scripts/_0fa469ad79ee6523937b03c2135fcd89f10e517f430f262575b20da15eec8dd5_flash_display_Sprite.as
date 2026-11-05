package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0fa469ad79ee6523937b03c2135fcd89f10e517f430f262575b20da15eec8dd5_flash_display_Sprite extends Sprite
   {
       
      
      public function _0fa469ad79ee6523937b03c2135fcd89f10e517f430f262575b20da15eec8dd5_flash_display_Sprite()
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
