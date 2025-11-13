package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _094b2ee8a620b391fefd8fc6d54855a6e83d985f9f091c5c8c184938c8a34d52_flash_display_Sprite extends Sprite
   {
       
      
      public function _094b2ee8a620b391fefd8fc6d54855a6e83d985f9f091c5c8c184938c8a34d52_flash_display_Sprite()
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
