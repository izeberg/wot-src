package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8c771ce6e78065da3c931596b26ba568ce7030babb17f66d9c2ac5bf71160d92_flash_display_Sprite extends Sprite
   {
       
      
      public function _8c771ce6e78065da3c931596b26ba568ce7030babb17f66d9c2ac5bf71160d92_flash_display_Sprite()
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
