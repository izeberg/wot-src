package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7b90eb99ce95b31f7d6f61941eeb2f44a34f59ee218ed912be2c41b6a168523b_flash_display_Sprite extends Sprite
   {
       
      
      public function _7b90eb99ce95b31f7d6f61941eeb2f44a34f59ee218ed912be2c41b6a168523b_flash_display_Sprite()
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
