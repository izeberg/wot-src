package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dd15ec61cb5929591e1908f2fbc10e7b8c738c7da32c4643cac9a085d6f11a7c_flash_display_Sprite extends Sprite
   {
       
      
      public function _dd15ec61cb5929591e1908f2fbc10e7b8c738c7da32c4643cac9a085d6f11a7c_flash_display_Sprite()
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
