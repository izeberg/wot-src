package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _fe22bce52b02fcc10c16d4142ba113e62dba44262766f9eabbd4e54a7be3fda4_flash_display_Sprite extends Sprite
   {
       
      
      public function _fe22bce52b02fcc10c16d4142ba113e62dba44262766f9eabbd4e54a7be3fda4_flash_display_Sprite()
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
