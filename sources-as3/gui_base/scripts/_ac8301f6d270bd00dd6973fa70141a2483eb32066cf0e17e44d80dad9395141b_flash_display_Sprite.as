package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ac8301f6d270bd00dd6973fa70141a2483eb32066cf0e17e44d80dad9395141b_flash_display_Sprite extends Sprite
   {
       
      
      public function _ac8301f6d270bd00dd6973fa70141a2483eb32066cf0e17e44d80dad9395141b_flash_display_Sprite()
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
