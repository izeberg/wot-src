package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _631e307a03d39a88cc3d6e236a5da06ea7466904535e1a1c9a0f62da5735f643_flash_display_Sprite extends Sprite
   {
       
      
      public function _631e307a03d39a88cc3d6e236a5da06ea7466904535e1a1c9a0f62da5735f643_flash_display_Sprite()
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
