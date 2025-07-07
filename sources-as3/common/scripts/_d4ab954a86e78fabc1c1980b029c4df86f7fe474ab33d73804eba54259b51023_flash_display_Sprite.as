package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d4ab954a86e78fabc1c1980b029c4df86f7fe474ab33d73804eba54259b51023_flash_display_Sprite extends Sprite
   {
       
      
      public function _d4ab954a86e78fabc1c1980b029c4df86f7fe474ab33d73804eba54259b51023_flash_display_Sprite()
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
