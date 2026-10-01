package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e5b38e573878547d53ea745cee1290860604fac912cf8ee0cbe5893d7bfa271c_flash_display_Sprite extends Sprite
   {
       
      
      public function _e5b38e573878547d53ea745cee1290860604fac912cf8ee0cbe5893d7bfa271c_flash_display_Sprite()
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
