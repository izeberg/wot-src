package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f5ed2b27e479e7293fddc1834cb6d13780621a469dcada1a54d50ebb0e3f9e27_flash_display_Sprite extends Sprite
   {
       
      
      public function _f5ed2b27e479e7293fddc1834cb6d13780621a469dcada1a54d50ebb0e3f9e27_flash_display_Sprite()
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
