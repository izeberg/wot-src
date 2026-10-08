package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _25715aab44b5354944da2298e7a30e4dae26dbe1f0ea684c5f1f654123b61914_flash_display_Sprite extends Sprite
   {
       
      
      public function _25715aab44b5354944da2298e7a30e4dae26dbe1f0ea684c5f1f654123b61914_flash_display_Sprite()
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
