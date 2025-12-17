package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _3c19cb9ade37fd77ec0d10992343d4acf7f866f2020144450ff1961046cf0ead_flash_display_Sprite extends Sprite
   {
       
      
      public function _3c19cb9ade37fd77ec0d10992343d4acf7f866f2020144450ff1961046cf0ead_flash_display_Sprite()
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
