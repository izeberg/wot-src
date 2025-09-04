package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d6fbeaeb0d6b6f2aa1c2b72118b4670c1f00970bce07f32e169d473a7ece3695_flash_display_Sprite extends Sprite
   {
       
      
      public function _d6fbeaeb0d6b6f2aa1c2b72118b4670c1f00970bce07f32e169d473a7ece3695_flash_display_Sprite()
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
