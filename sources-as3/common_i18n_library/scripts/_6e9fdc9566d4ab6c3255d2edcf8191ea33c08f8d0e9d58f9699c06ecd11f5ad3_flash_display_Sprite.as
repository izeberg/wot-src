package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6e9fdc9566d4ab6c3255d2edcf8191ea33c08f8d0e9d58f9699c06ecd11f5ad3_flash_display_Sprite extends Sprite
   {
       
      
      public function _6e9fdc9566d4ab6c3255d2edcf8191ea33c08f8d0e9d58f9699c06ecd11f5ad3_flash_display_Sprite()
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
