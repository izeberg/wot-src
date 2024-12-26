package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _bf783f42f7599e1ce225f702113ec8ea5dd8f3d3453dd16d643ded8631a73e76_flash_display_Sprite extends Sprite
   {
       
      
      public function _bf783f42f7599e1ce225f702113ec8ea5dd8f3d3453dd16d643ded8631a73e76_flash_display_Sprite()
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
