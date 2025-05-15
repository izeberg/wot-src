package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b5df638fc1744c6b774fe7e340ec3d30161e7febbb3bb4e78fd4f7415f5862c7_flash_display_Sprite extends Sprite
   {
       
      
      public function _b5df638fc1744c6b774fe7e340ec3d30161e7febbb3bb4e78fd4f7415f5862c7_flash_display_Sprite()
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
