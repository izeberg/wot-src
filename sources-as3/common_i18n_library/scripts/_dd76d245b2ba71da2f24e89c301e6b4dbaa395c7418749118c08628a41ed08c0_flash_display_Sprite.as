package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dd76d245b2ba71da2f24e89c301e6b4dbaa395c7418749118c08628a41ed08c0_flash_display_Sprite extends Sprite
   {
       
      
      public function _dd76d245b2ba71da2f24e89c301e6b4dbaa395c7418749118c08628a41ed08c0_flash_display_Sprite()
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
