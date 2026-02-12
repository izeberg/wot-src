package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c1ee5de1395d97369fd65c449b785dd974d8b3b8284ed2315c21c1f75114f7ad_flash_display_Sprite extends Sprite
   {
       
      
      public function _c1ee5de1395d97369fd65c449b785dd974d8b3b8284ed2315c21c1f75114f7ad_flash_display_Sprite()
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
