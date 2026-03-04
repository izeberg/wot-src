package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _daa48df7171ca37cca20d3c2adc82849981ddb067bc4d6b5f9ff30e0814c6e40_flash_display_Sprite extends Sprite
   {
       
      
      public function _daa48df7171ca37cca20d3c2adc82849981ddb067bc4d6b5f9ff30e0814c6e40_flash_display_Sprite()
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
