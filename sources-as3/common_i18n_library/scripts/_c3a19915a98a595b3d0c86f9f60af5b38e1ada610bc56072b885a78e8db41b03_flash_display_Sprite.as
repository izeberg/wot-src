package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c3a19915a98a595b3d0c86f9f60af5b38e1ada610bc56072b885a78e8db41b03_flash_display_Sprite extends Sprite
   {
       
      
      public function _c3a19915a98a595b3d0c86f9f60af5b38e1ada610bc56072b885a78e8db41b03_flash_display_Sprite()
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
