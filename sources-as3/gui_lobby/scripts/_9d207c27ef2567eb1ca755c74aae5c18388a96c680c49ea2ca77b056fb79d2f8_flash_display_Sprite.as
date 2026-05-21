package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9d207c27ef2567eb1ca755c74aae5c18388a96c680c49ea2ca77b056fb79d2f8_flash_display_Sprite extends Sprite
   {
       
      
      public function _9d207c27ef2567eb1ca755c74aae5c18388a96c680c49ea2ca77b056fb79d2f8_flash_display_Sprite()
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
