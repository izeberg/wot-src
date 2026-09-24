package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dee2eaab2691645642e0cc2a8bc405ff24b198e61b88d11c0337272da46919b5_flash_display_Sprite extends Sprite
   {
       
      
      public function _dee2eaab2691645642e0cc2a8bc405ff24b198e61b88d11c0337272da46919b5_flash_display_Sprite()
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
