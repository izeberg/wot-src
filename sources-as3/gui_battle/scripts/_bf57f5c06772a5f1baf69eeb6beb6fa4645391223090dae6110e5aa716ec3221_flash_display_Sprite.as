package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _bf57f5c06772a5f1baf69eeb6beb6fa4645391223090dae6110e5aa716ec3221_flash_display_Sprite extends Sprite
   {
       
      
      public function _bf57f5c06772a5f1baf69eeb6beb6fa4645391223090dae6110e5aa716ec3221_flash_display_Sprite()
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
