package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e80ff1b67a3e65c8c91ced41ad79ec852d5aea1c6b034a6f83f0c5dc84abaaff_flash_display_Sprite extends Sprite
   {
       
      
      public function _e80ff1b67a3e65c8c91ced41ad79ec852d5aea1c6b034a6f83f0c5dc84abaaff_flash_display_Sprite()
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
