package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0356ffdb0bcaac69a18e1524806664b99e19e759fe0a0590bbf006104510daed_flash_display_Sprite extends Sprite
   {
       
      
      public function _0356ffdb0bcaac69a18e1524806664b99e19e759fe0a0590bbf006104510daed_flash_display_Sprite()
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
