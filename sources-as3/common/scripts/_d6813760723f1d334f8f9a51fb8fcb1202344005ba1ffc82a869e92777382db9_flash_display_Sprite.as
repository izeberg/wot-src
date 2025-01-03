package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d6813760723f1d334f8f9a51fb8fcb1202344005ba1ffc82a869e92777382db9_flash_display_Sprite extends Sprite
   {
       
      
      public function _d6813760723f1d334f8f9a51fb8fcb1202344005ba1ffc82a869e92777382db9_flash_display_Sprite()
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
