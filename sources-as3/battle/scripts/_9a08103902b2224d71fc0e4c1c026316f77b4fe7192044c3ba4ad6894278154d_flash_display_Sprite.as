package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9a08103902b2224d71fc0e4c1c026316f77b4fe7192044c3ba4ad6894278154d_flash_display_Sprite extends Sprite
   {
       
      
      public function _9a08103902b2224d71fc0e4c1c026316f77b4fe7192044c3ba4ad6894278154d_flash_display_Sprite()
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
