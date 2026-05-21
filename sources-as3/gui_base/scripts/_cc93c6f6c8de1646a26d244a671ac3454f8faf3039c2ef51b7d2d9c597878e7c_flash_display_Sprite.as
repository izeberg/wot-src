package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _cc93c6f6c8de1646a26d244a671ac3454f8faf3039c2ef51b7d2d9c597878e7c_flash_display_Sprite extends Sprite
   {
       
      
      public function _cc93c6f6c8de1646a26d244a671ac3454f8faf3039c2ef51b7d2d9c597878e7c_flash_display_Sprite()
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
