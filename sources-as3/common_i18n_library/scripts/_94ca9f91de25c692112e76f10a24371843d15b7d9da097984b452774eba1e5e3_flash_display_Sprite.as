package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _94ca9f91de25c692112e76f10a24371843d15b7d9da097984b452774eba1e5e3_flash_display_Sprite extends Sprite
   {
       
      
      public function _94ca9f91de25c692112e76f10a24371843d15b7d9da097984b452774eba1e5e3_flash_display_Sprite()
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
