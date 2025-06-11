package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _cafa7501008b7edc344b4676d303876fef3d1514337d99734b178d56e18536cf_flash_display_Sprite extends Sprite
   {
       
      
      public function _cafa7501008b7edc344b4676d303876fef3d1514337d99734b178d56e18536cf_flash_display_Sprite()
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
