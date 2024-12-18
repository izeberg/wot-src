package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8b9242c1c083de7f9ea863c9992405f53a228f67b7fe85c76b56893cfd404c82_flash_display_Sprite extends Sprite
   {
       
      
      public function _8b9242c1c083de7f9ea863c9992405f53a228f67b7fe85c76b56893cfd404c82_flash_display_Sprite()
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
