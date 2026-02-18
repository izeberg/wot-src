package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _551d73e8d14fb5d0d862b51a23e423a5da08b9125b26e711ed04b0f8a6164db1_flash_display_Sprite extends Sprite
   {
       
      
      public function _551d73e8d14fb5d0d862b51a23e423a5da08b9125b26e711ed04b0f8a6164db1_flash_display_Sprite()
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
