package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _46fa482c41c193c0e2651c5e481dc4b354ab23e6e920b1636cbc828158764824_flash_display_Sprite extends Sprite
   {
       
      
      public function _46fa482c41c193c0e2651c5e481dc4b354ab23e6e920b1636cbc828158764824_flash_display_Sprite()
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
