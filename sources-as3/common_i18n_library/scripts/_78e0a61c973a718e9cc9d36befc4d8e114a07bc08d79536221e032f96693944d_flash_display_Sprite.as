package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _78e0a61c973a718e9cc9d36befc4d8e114a07bc08d79536221e032f96693944d_flash_display_Sprite extends Sprite
   {
       
      
      public function _78e0a61c973a718e9cc9d36befc4d8e114a07bc08d79536221e032f96693944d_flash_display_Sprite()
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
