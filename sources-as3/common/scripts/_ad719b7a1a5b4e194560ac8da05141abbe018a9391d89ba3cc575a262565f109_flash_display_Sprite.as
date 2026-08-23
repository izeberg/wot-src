package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ad719b7a1a5b4e194560ac8da05141abbe018a9391d89ba3cc575a262565f109_flash_display_Sprite extends Sprite
   {
       
      
      public function _ad719b7a1a5b4e194560ac8da05141abbe018a9391d89ba3cc575a262565f109_flash_display_Sprite()
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
