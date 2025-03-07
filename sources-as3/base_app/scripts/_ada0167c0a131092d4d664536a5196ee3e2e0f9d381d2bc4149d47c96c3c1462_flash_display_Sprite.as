package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ada0167c0a131092d4d664536a5196ee3e2e0f9d381d2bc4149d47c96c3c1462_flash_display_Sprite extends Sprite
   {
       
      
      public function _ada0167c0a131092d4d664536a5196ee3e2e0f9d381d2bc4149d47c96c3c1462_flash_display_Sprite()
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
