package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2a7196dc64c2973a2af47be3b95c79ac61bbfaf71552aff8c428e262b15489b2_flash_display_Sprite extends Sprite
   {
       
      
      public function _2a7196dc64c2973a2af47be3b95c79ac61bbfaf71552aff8c428e262b15489b2_flash_display_Sprite()
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
