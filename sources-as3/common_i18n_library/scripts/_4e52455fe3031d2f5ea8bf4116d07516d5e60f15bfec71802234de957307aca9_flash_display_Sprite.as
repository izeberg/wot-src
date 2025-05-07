package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4e52455fe3031d2f5ea8bf4116d07516d5e60f15bfec71802234de957307aca9_flash_display_Sprite extends Sprite
   {
       
      
      public function _4e52455fe3031d2f5ea8bf4116d07516d5e60f15bfec71802234de957307aca9_flash_display_Sprite()
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
