package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _3b59594666cda2f14f3792550409008a7c82b492ec9c47907c921d273c5a9464_flash_display_Sprite extends Sprite
   {
       
      
      public function _3b59594666cda2f14f3792550409008a7c82b492ec9c47907c921d273c5a9464_flash_display_Sprite()
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
