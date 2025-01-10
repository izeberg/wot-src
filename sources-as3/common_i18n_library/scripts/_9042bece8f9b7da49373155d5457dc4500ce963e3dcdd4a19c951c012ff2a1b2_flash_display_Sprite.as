package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9042bece8f9b7da49373155d5457dc4500ce963e3dcdd4a19c951c012ff2a1b2_flash_display_Sprite extends Sprite
   {
       
      
      public function _9042bece8f9b7da49373155d5457dc4500ce963e3dcdd4a19c951c012ff2a1b2_flash_display_Sprite()
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
