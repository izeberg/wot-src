package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _458e6e727bc5fe2af5a22fb3c899d18d7108315ac1a89f558b88dc81fd0c5a9d_flash_display_Sprite extends Sprite
   {
       
      
      public function _458e6e727bc5fe2af5a22fb3c899d18d7108315ac1a89f558b88dc81fd0c5a9d_flash_display_Sprite()
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
