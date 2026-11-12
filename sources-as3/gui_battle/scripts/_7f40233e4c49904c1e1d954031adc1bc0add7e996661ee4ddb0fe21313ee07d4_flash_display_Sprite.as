package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7f40233e4c49904c1e1d954031adc1bc0add7e996661ee4ddb0fe21313ee07d4_flash_display_Sprite extends Sprite
   {
       
      
      public function _7f40233e4c49904c1e1d954031adc1bc0add7e996661ee4ddb0fe21313ee07d4_flash_display_Sprite()
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
