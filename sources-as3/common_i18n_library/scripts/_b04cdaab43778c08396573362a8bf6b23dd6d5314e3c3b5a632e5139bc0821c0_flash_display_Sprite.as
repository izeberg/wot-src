package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b04cdaab43778c08396573362a8bf6b23dd6d5314e3c3b5a632e5139bc0821c0_flash_display_Sprite extends Sprite
   {
       
      
      public function _b04cdaab43778c08396573362a8bf6b23dd6d5314e3c3b5a632e5139bc0821c0_flash_display_Sprite()
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
