package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a6f77cc41a1ed5a9fc068b7d22804227cdb52dc7d0c703333bfefaf59a554b6b_flash_display_Sprite extends Sprite
   {
       
      
      public function _a6f77cc41a1ed5a9fc068b7d22804227cdb52dc7d0c703333bfefaf59a554b6b_flash_display_Sprite()
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
