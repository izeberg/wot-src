package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8204f42c056ce7d5481191a6b5e20ef8e3029f9e04a4657a799ff61b941dd06f_flash_display_Sprite extends Sprite
   {
       
      
      public function _8204f42c056ce7d5481191a6b5e20ef8e3029f9e04a4657a799ff61b941dd06f_flash_display_Sprite()
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
