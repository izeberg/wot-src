package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _96cdc7f90819e85af581c4d86ebd2dc8836bf575d6f9a75efe1d835fa805c20c_flash_display_Sprite extends Sprite
   {
       
      
      public function _96cdc7f90819e85af581c4d86ebd2dc8836bf575d6f9a75efe1d835fa805c20c_flash_display_Sprite()
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
