package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ca8e169fbec5250ec688a170bf73309911b16867d1da483cd1360ee8c2b37dea_flash_display_Sprite extends Sprite
   {
       
      
      public function _ca8e169fbec5250ec688a170bf73309911b16867d1da483cd1360ee8c2b37dea_flash_display_Sprite()
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
