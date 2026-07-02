package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a6647ebcb9c884ec80247a1e233e2b48f5b49e38703b5551453d9394237754a5_flash_display_Sprite extends Sprite
   {
       
      
      public function _a6647ebcb9c884ec80247a1e233e2b48f5b49e38703b5551453d9394237754a5_flash_display_Sprite()
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
