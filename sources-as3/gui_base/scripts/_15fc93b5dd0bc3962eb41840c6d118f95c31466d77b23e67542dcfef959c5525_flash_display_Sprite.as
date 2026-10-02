package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _15fc93b5dd0bc3962eb41840c6d118f95c31466d77b23e67542dcfef959c5525_flash_display_Sprite extends Sprite
   {
       
      
      public function _15fc93b5dd0bc3962eb41840c6d118f95c31466d77b23e67542dcfef959c5525_flash_display_Sprite()
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
