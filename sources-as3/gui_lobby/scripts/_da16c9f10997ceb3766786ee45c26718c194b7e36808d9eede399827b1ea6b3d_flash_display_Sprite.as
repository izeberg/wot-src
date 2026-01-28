package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _da16c9f10997ceb3766786ee45c26718c194b7e36808d9eede399827b1ea6b3d_flash_display_Sprite extends Sprite
   {
       
      
      public function _da16c9f10997ceb3766786ee45c26718c194b7e36808d9eede399827b1ea6b3d_flash_display_Sprite()
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
