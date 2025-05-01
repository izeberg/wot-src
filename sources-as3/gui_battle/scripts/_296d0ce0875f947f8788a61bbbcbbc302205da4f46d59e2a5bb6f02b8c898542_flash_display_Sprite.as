package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _296d0ce0875f947f8788a61bbbcbbc302205da4f46d59e2a5bb6f02b8c898542_flash_display_Sprite extends Sprite
   {
       
      
      public function _296d0ce0875f947f8788a61bbbcbbc302205da4f46d59e2a5bb6f02b8c898542_flash_display_Sprite()
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
