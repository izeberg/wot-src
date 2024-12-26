package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _eeceb6378127677210b3e06c93118a3dbfe02bed575265860f03b94bbc754be2_flash_display_Sprite extends Sprite
   {
       
      
      public function _eeceb6378127677210b3e06c93118a3dbfe02bed575265860f03b94bbc754be2_flash_display_Sprite()
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
