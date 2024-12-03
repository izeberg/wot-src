package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _687b5d25d470965a0f8efba49753777e5db1d2538d98d20e6e3b549404acfde0_flash_display_Sprite extends Sprite
   {
       
      
      public function _687b5d25d470965a0f8efba49753777e5db1d2538d98d20e6e3b549404acfde0_flash_display_Sprite()
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
