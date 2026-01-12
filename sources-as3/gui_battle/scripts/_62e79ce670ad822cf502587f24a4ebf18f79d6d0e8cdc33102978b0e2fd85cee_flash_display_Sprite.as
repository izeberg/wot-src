package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _62e79ce670ad822cf502587f24a4ebf18f79d6d0e8cdc33102978b0e2fd85cee_flash_display_Sprite extends Sprite
   {
       
      
      public function _62e79ce670ad822cf502587f24a4ebf18f79d6d0e8cdc33102978b0e2fd85cee_flash_display_Sprite()
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
