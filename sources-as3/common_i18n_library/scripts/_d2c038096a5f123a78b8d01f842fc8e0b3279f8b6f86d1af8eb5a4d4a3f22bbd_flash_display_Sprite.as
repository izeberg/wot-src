package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d2c038096a5f123a78b8d01f842fc8e0b3279f8b6f86d1af8eb5a4d4a3f22bbd_flash_display_Sprite extends Sprite
   {
       
      
      public function _d2c038096a5f123a78b8d01f842fc8e0b3279f8b6f86d1af8eb5a4d4a3f22bbd_flash_display_Sprite()
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
