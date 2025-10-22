package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _418ab91190ff40be3815ba532b52487fad338d42d236162d82d79d4c703d0587_flash_display_Sprite extends Sprite
   {
       
      
      public function _418ab91190ff40be3815ba532b52487fad338d42d236162d82d79d4c703d0587_flash_display_Sprite()
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
