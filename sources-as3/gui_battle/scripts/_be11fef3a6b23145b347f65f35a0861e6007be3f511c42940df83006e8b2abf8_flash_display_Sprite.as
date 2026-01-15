package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _be11fef3a6b23145b347f65f35a0861e6007be3f511c42940df83006e8b2abf8_flash_display_Sprite extends Sprite
   {
       
      
      public function _be11fef3a6b23145b347f65f35a0861e6007be3f511c42940df83006e8b2abf8_flash_display_Sprite()
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
