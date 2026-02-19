package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e7a5a27cc7b9437c2daf3e462c0d9d076104f07186da937c546d778483edb55a_flash_display_Sprite extends Sprite
   {
       
      
      public function _e7a5a27cc7b9437c2daf3e462c0d9d076104f07186da937c546d778483edb55a_flash_display_Sprite()
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
