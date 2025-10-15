package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _daf12dd4bb3ed044df8a04a8eca2e2c2c9ca54dbcc1b72661c1146d152bde271_flash_display_Sprite extends Sprite
   {
       
      
      public function _daf12dd4bb3ed044df8a04a8eca2e2c2c9ca54dbcc1b72661c1146d152bde271_flash_display_Sprite()
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
