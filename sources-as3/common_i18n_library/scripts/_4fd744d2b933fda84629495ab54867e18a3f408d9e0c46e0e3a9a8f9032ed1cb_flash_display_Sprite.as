package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4fd744d2b933fda84629495ab54867e18a3f408d9e0c46e0e3a9a8f9032ed1cb_flash_display_Sprite extends Sprite
   {
       
      
      public function _4fd744d2b933fda84629495ab54867e18a3f408d9e0c46e0e3a9a8f9032ed1cb_flash_display_Sprite()
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
