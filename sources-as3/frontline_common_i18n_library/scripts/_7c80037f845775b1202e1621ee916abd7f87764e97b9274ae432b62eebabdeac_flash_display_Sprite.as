package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7c80037f845775b1202e1621ee916abd7f87764e97b9274ae432b62eebabdeac_flash_display_Sprite extends Sprite
   {
       
      
      public function _7c80037f845775b1202e1621ee916abd7f87764e97b9274ae432b62eebabdeac_flash_display_Sprite()
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
