package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ae30dcd0537fb29170ab4b6be55b8ec98816e6ae096b70f34e1c8a9421016b0a_flash_display_Sprite extends Sprite
   {
       
      
      public function _ae30dcd0537fb29170ab4b6be55b8ec98816e6ae096b70f34e1c8a9421016b0a_flash_display_Sprite()
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
