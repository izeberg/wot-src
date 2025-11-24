package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _11ec7ed382018a3195af2b342e8aed683a9a48644c09a60c2fe86b712703adf6_flash_display_Sprite extends Sprite
   {
       
      
      public function _11ec7ed382018a3195af2b342e8aed683a9a48644c09a60c2fe86b712703adf6_flash_display_Sprite()
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
