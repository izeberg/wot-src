package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4f63781f8a942418a2469bb651d0fb4cb19e81bffc172a7827250c527b62e878_flash_display_Sprite extends Sprite
   {
       
      
      public function _4f63781f8a942418a2469bb651d0fb4cb19e81bffc172a7827250c527b62e878_flash_display_Sprite()
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
