package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dedc5f970451bf2b21f73d3cf5017f3669ef12c309bece8d725016a9fc1af7ab_flash_display_Sprite extends Sprite
   {
       
      
      public function _dedc5f970451bf2b21f73d3cf5017f3669ef12c309bece8d725016a9fc1af7ab_flash_display_Sprite()
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
