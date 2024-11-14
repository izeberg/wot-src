package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7c7b3dd799b718ec341fa21afe31ce4fd382dd6ee13cb070aa185ef482e0e52f_flash_display_Sprite extends Sprite
   {
       
      
      public function _7c7b3dd799b718ec341fa21afe31ce4fd382dd6ee13cb070aa185ef482e0e52f_flash_display_Sprite()
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
