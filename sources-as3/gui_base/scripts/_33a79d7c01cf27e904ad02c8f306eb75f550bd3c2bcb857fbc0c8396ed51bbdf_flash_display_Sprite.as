package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _33a79d7c01cf27e904ad02c8f306eb75f550bd3c2bcb857fbc0c8396ed51bbdf_flash_display_Sprite extends Sprite
   {
       
      
      public function _33a79d7c01cf27e904ad02c8f306eb75f550bd3c2bcb857fbc0c8396ed51bbdf_flash_display_Sprite()
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
