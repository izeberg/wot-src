package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _47cf40f50fb99cec07762caa37fc847ca7e62637b1fe73e054b3a0b628c0e9a5_flash_display_Sprite extends Sprite
   {
       
      
      public function _47cf40f50fb99cec07762caa37fc847ca7e62637b1fe73e054b3a0b628c0e9a5_flash_display_Sprite()
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
