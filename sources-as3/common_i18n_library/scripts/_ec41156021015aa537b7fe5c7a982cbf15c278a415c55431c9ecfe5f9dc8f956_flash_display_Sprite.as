package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ec41156021015aa537b7fe5c7a982cbf15c278a415c55431c9ecfe5f9dc8f956_flash_display_Sprite extends Sprite
   {
       
      
      public function _ec41156021015aa537b7fe5c7a982cbf15c278a415c55431c9ecfe5f9dc8f956_flash_display_Sprite()
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
