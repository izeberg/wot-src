package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4537f18894d97804a588d39118684c3666e1f18dd0cd632fa178173a84785fd1_flash_display_Sprite extends Sprite
   {
       
      
      public function _4537f18894d97804a588d39118684c3666e1f18dd0cd632fa178173a84785fd1_flash_display_Sprite()
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
