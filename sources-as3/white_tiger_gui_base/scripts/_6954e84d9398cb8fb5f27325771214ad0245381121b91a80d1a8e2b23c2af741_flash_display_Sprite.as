package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6954e84d9398cb8fb5f27325771214ad0245381121b91a80d1a8e2b23c2af741_flash_display_Sprite extends Sprite
   {
       
      
      public function _6954e84d9398cb8fb5f27325771214ad0245381121b91a80d1a8e2b23c2af741_flash_display_Sprite()
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
