package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _70a9e2495bb2d3950a225ed1eef1cc66e82451bf7bf3980f4f8486e6f8f23255_flash_display_Sprite extends Sprite
   {
       
      
      public function _70a9e2495bb2d3950a225ed1eef1cc66e82451bf7bf3980f4f8486e6f8f23255_flash_display_Sprite()
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
