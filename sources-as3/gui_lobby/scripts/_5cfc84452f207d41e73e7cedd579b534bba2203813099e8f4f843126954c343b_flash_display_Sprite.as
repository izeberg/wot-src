package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5cfc84452f207d41e73e7cedd579b534bba2203813099e8f4f843126954c343b_flash_display_Sprite extends Sprite
   {
       
      
      public function _5cfc84452f207d41e73e7cedd579b534bba2203813099e8f4f843126954c343b_flash_display_Sprite()
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
