package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ad569e27563a59842582270522c5adabdf027e0e41e2e1da54f5aa82a9200be1_flash_display_Sprite extends Sprite
   {
       
      
      public function _ad569e27563a59842582270522c5adabdf027e0e41e2e1da54f5aa82a9200be1_flash_display_Sprite()
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
