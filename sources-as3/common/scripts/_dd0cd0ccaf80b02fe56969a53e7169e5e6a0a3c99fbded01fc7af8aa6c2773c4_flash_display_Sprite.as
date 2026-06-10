package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dd0cd0ccaf80b02fe56969a53e7169e5e6a0a3c99fbded01fc7af8aa6c2773c4_flash_display_Sprite extends Sprite
   {
       
      
      public function _dd0cd0ccaf80b02fe56969a53e7169e5e6a0a3c99fbded01fc7af8aa6c2773c4_flash_display_Sprite()
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
