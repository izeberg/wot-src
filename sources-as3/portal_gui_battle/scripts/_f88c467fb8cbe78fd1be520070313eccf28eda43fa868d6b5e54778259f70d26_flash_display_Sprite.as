package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f88c467fb8cbe78fd1be520070313eccf28eda43fa868d6b5e54778259f70d26_flash_display_Sprite extends Sprite
   {
       
      
      public function _f88c467fb8cbe78fd1be520070313eccf28eda43fa868d6b5e54778259f70d26_flash_display_Sprite()
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
