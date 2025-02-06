package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _189a93e65c4c56dea30b2897012f242d83343897ae889e2fcd011f515be7b1ce_flash_display_Sprite extends Sprite
   {
       
      
      public function _189a93e65c4c56dea30b2897012f242d83343897ae889e2fcd011f515be7b1ce_flash_display_Sprite()
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
