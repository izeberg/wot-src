package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4e3bb917b77cc6eb010a649b4585ec0af50f32f8ab0864d74349d4a74b592a77_flash_display_Sprite extends Sprite
   {
       
      
      public function _4e3bb917b77cc6eb010a649b4585ec0af50f32f8ab0864d74349d4a74b592a77_flash_display_Sprite()
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
