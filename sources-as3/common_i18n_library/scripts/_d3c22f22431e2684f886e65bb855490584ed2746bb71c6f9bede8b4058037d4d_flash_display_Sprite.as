package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d3c22f22431e2684f886e65bb855490584ed2746bb71c6f9bede8b4058037d4d_flash_display_Sprite extends Sprite
   {
       
      
      public function _d3c22f22431e2684f886e65bb855490584ed2746bb71c6f9bede8b4058037d4d_flash_display_Sprite()
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
