package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4b3326ee091bc5dc2ed95f92d7caf22c809aa24d81e4ee95107859f72f6a8cac_flash_display_Sprite extends Sprite
   {
       
      
      public function _4b3326ee091bc5dc2ed95f92d7caf22c809aa24d81e4ee95107859f72f6a8cac_flash_display_Sprite()
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
