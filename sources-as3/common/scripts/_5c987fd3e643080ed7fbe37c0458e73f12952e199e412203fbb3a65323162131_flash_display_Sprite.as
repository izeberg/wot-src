package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5c987fd3e643080ed7fbe37c0458e73f12952e199e412203fbb3a65323162131_flash_display_Sprite extends Sprite
   {
       
      
      public function _5c987fd3e643080ed7fbe37c0458e73f12952e199e412203fbb3a65323162131_flash_display_Sprite()
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
