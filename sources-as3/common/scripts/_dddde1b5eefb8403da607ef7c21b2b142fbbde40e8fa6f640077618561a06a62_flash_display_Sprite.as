package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dddde1b5eefb8403da607ef7c21b2b142fbbde40e8fa6f640077618561a06a62_flash_display_Sprite extends Sprite
   {
       
      
      public function _dddde1b5eefb8403da607ef7c21b2b142fbbde40e8fa6f640077618561a06a62_flash_display_Sprite()
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
