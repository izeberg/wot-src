package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5dff7b4ccdf2e9e85b0877719ec8a466f538060838100c88cc9c6a76afb2d0ab_flash_display_Sprite extends Sprite
   {
       
      
      public function _5dff7b4ccdf2e9e85b0877719ec8a466f538060838100c88cc9c6a76afb2d0ab_flash_display_Sprite()
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
