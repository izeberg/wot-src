package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5f11ef06179aa71a63b52eca808338f2b86508d2b5c1deab210c199678168f48_flash_display_Sprite extends Sprite
   {
       
      
      public function _5f11ef06179aa71a63b52eca808338f2b86508d2b5c1deab210c199678168f48_flash_display_Sprite()
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
