package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a46411baa3f3d5fd13720405a3b5c90221af3e8bb62281834cca1ae5feafd764_flash_display_Sprite extends Sprite
   {
       
      
      public function _a46411baa3f3d5fd13720405a3b5c90221af3e8bb62281834cca1ae5feafd764_flash_display_Sprite()
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
