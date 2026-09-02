package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _eddcae08227995caeec82760b71b79b652ff61ecbbf85fa05dc41455c63810e5_flash_display_Sprite extends Sprite
   {
       
      
      public function _eddcae08227995caeec82760b71b79b652ff61ecbbf85fa05dc41455c63810e5_flash_display_Sprite()
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
