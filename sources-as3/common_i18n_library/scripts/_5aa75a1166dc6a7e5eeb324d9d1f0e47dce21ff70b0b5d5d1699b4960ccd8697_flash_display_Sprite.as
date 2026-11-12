package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5aa75a1166dc6a7e5eeb324d9d1f0e47dce21ff70b0b5d5d1699b4960ccd8697_flash_display_Sprite extends Sprite
   {
       
      
      public function _5aa75a1166dc6a7e5eeb324d9d1f0e47dce21ff70b0b5d5d1699b4960ccd8697_flash_display_Sprite()
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
