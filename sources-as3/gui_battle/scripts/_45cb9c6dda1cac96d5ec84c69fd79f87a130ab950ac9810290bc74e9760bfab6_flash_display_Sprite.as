package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _45cb9c6dda1cac96d5ec84c69fd79f87a130ab950ac9810290bc74e9760bfab6_flash_display_Sprite extends Sprite
   {
       
      
      public function _45cb9c6dda1cac96d5ec84c69fd79f87a130ab950ac9810290bc74e9760bfab6_flash_display_Sprite()
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
