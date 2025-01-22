package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6f6ab8fc546b2f75bc4ac1f4f198cda5f2a742f21a59aad3cba09f603702c7ec_flash_display_Sprite extends Sprite
   {
       
      
      public function _6f6ab8fc546b2f75bc4ac1f4f198cda5f2a742f21a59aad3cba09f603702c7ec_flash_display_Sprite()
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
