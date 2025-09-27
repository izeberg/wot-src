package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _29fb1aee5c597a38e8a564b78e1e05c7fa661fdfcae5743b9ed7d425c8716ad1_flash_display_Sprite extends Sprite
   {
       
      
      public function _29fb1aee5c597a38e8a564b78e1e05c7fa661fdfcae5743b9ed7d425c8716ad1_flash_display_Sprite()
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
