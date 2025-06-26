package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9510270110a1deb26cf902fe97a9b583cbc5af6ccfc6a26d3bcd980152668d6a_flash_display_Sprite extends Sprite
   {
       
      
      public function _9510270110a1deb26cf902fe97a9b583cbc5af6ccfc6a26d3bcd980152668d6a_flash_display_Sprite()
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
