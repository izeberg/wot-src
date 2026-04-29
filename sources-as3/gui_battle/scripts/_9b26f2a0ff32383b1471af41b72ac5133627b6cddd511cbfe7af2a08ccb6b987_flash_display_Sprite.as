package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9b26f2a0ff32383b1471af41b72ac5133627b6cddd511cbfe7af2a08ccb6b987_flash_display_Sprite extends Sprite
   {
       
      
      public function _9b26f2a0ff32383b1471af41b72ac5133627b6cddd511cbfe7af2a08ccb6b987_flash_display_Sprite()
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
