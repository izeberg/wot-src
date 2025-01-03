package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ca867e481c2ecfa32d96b06477ba0bf9838102385237fb90b58bf33cc0071209_flash_display_Sprite extends Sprite
   {
       
      
      public function _ca867e481c2ecfa32d96b06477ba0bf9838102385237fb90b58bf33cc0071209_flash_display_Sprite()
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
