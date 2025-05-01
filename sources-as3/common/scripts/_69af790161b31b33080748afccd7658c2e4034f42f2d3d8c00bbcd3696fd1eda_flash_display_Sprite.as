package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _69af790161b31b33080748afccd7658c2e4034f42f2d3d8c00bbcd3696fd1eda_flash_display_Sprite extends Sprite
   {
       
      
      public function _69af790161b31b33080748afccd7658c2e4034f42f2d3d8c00bbcd3696fd1eda_flash_display_Sprite()
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
