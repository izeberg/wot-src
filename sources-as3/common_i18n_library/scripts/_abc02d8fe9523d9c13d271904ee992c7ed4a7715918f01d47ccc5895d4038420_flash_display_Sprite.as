package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _abc02d8fe9523d9c13d271904ee992c7ed4a7715918f01d47ccc5895d4038420_flash_display_Sprite extends Sprite
   {
       
      
      public function _abc02d8fe9523d9c13d271904ee992c7ed4a7715918f01d47ccc5895d4038420_flash_display_Sprite()
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
