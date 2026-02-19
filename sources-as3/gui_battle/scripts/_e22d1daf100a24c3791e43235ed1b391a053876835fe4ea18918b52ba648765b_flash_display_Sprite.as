package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e22d1daf100a24c3791e43235ed1b391a053876835fe4ea18918b52ba648765b_flash_display_Sprite extends Sprite
   {
       
      
      public function _e22d1daf100a24c3791e43235ed1b391a053876835fe4ea18918b52ba648765b_flash_display_Sprite()
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
