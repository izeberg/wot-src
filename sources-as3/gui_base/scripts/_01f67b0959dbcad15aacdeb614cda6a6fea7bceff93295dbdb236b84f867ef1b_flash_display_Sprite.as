package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _01f67b0959dbcad15aacdeb614cda6a6fea7bceff93295dbdb236b84f867ef1b_flash_display_Sprite extends Sprite
   {
       
      
      public function _01f67b0959dbcad15aacdeb614cda6a6fea7bceff93295dbdb236b84f867ef1b_flash_display_Sprite()
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
