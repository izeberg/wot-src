package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e3995ea28a350bd40991142d1b7cf4330597215c7c3f58652fbe1477a07a910f_flash_display_Sprite extends Sprite
   {
       
      
      public function _e3995ea28a350bd40991142d1b7cf4330597215c7c3f58652fbe1477a07a910f_flash_display_Sprite()
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
