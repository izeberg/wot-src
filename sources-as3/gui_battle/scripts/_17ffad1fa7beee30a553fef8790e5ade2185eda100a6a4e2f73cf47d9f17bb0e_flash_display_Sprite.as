package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _17ffad1fa7beee30a553fef8790e5ade2185eda100a6a4e2f73cf47d9f17bb0e_flash_display_Sprite extends Sprite
   {
       
      
      public function _17ffad1fa7beee30a553fef8790e5ade2185eda100a6a4e2f73cf47d9f17bb0e_flash_display_Sprite()
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
