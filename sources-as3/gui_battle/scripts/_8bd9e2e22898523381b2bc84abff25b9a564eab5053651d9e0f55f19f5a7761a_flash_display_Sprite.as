package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8bd9e2e22898523381b2bc84abff25b9a564eab5053651d9e0f55f19f5a7761a_flash_display_Sprite extends Sprite
   {
       
      
      public function _8bd9e2e22898523381b2bc84abff25b9a564eab5053651d9e0f55f19f5a7761a_flash_display_Sprite()
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
