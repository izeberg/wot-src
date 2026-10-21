package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _43501b743bc11e27458b54940269f96d0979520c13e31c04800d9f4b73d98526_flash_display_Sprite extends Sprite
   {
       
      
      public function _43501b743bc11e27458b54940269f96d0979520c13e31c04800d9f4b73d98526_flash_display_Sprite()
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
