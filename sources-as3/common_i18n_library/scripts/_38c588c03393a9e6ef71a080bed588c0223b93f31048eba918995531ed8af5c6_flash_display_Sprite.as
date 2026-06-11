package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _38c588c03393a9e6ef71a080bed588c0223b93f31048eba918995531ed8af5c6_flash_display_Sprite extends Sprite
   {
       
      
      public function _38c588c03393a9e6ef71a080bed588c0223b93f31048eba918995531ed8af5c6_flash_display_Sprite()
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
