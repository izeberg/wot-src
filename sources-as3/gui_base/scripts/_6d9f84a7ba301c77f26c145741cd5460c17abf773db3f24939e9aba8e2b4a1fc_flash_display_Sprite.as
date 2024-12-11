package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6d9f84a7ba301c77f26c145741cd5460c17abf773db3f24939e9aba8e2b4a1fc_flash_display_Sprite extends Sprite
   {
       
      
      public function _6d9f84a7ba301c77f26c145741cd5460c17abf773db3f24939e9aba8e2b4a1fc_flash_display_Sprite()
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
