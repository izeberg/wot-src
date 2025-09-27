package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _176ca1f661df2ba1d3862790f94913e8f0bd8671debb4f563acf0a6224054444_flash_display_Sprite extends Sprite
   {
       
      
      public function _176ca1f661df2ba1d3862790f94913e8f0bd8671debb4f563acf0a6224054444_flash_display_Sprite()
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
