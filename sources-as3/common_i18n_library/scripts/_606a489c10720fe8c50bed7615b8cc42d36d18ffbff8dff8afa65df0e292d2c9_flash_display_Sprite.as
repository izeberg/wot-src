package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _606a489c10720fe8c50bed7615b8cc42d36d18ffbff8dff8afa65df0e292d2c9_flash_display_Sprite extends Sprite
   {
       
      
      public function _606a489c10720fe8c50bed7615b8cc42d36d18ffbff8dff8afa65df0e292d2c9_flash_display_Sprite()
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
