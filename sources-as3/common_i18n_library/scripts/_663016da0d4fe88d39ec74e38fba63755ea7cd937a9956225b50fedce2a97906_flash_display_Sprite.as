package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _663016da0d4fe88d39ec74e38fba63755ea7cd937a9956225b50fedce2a97906_flash_display_Sprite extends Sprite
   {
       
      
      public function _663016da0d4fe88d39ec74e38fba63755ea7cd937a9956225b50fedce2a97906_flash_display_Sprite()
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
