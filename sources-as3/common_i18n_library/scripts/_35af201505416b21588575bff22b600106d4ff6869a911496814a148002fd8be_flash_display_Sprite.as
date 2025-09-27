package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _35af201505416b21588575bff22b600106d4ff6869a911496814a148002fd8be_flash_display_Sprite extends Sprite
   {
       
      
      public function _35af201505416b21588575bff22b600106d4ff6869a911496814a148002fd8be_flash_display_Sprite()
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
