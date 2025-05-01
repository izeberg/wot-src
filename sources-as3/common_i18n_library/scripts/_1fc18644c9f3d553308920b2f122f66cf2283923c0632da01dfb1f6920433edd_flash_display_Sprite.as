package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1fc18644c9f3d553308920b2f122f66cf2283923c0632da01dfb1f6920433edd_flash_display_Sprite extends Sprite
   {
       
      
      public function _1fc18644c9f3d553308920b2f122f66cf2283923c0632da01dfb1f6920433edd_flash_display_Sprite()
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
