package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _853210fdd57c76fc4530b244168e9a09f05396bb3cb396635833a6f6bd50286f_flash_display_Sprite extends Sprite
   {
       
      
      public function _853210fdd57c76fc4530b244168e9a09f05396bb3cb396635833a6f6bd50286f_flash_display_Sprite()
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
