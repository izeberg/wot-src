package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _555dfc78939240d91230bae78f53f9866220b7d51b01e8903bc91cf98835dc40_flash_display_Sprite extends Sprite
   {
       
      
      public function _555dfc78939240d91230bae78f53f9866220b7d51b01e8903bc91cf98835dc40_flash_display_Sprite()
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
