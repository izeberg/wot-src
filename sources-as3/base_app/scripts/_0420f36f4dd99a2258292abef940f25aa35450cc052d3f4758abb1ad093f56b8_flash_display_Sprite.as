package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0420f36f4dd99a2258292abef940f25aa35450cc052d3f4758abb1ad093f56b8_flash_display_Sprite extends Sprite
   {
       
      
      public function _0420f36f4dd99a2258292abef940f25aa35450cc052d3f4758abb1ad093f56b8_flash_display_Sprite()
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
