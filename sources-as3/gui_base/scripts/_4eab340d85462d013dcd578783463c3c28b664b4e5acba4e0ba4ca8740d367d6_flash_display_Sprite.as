package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4eab340d85462d013dcd578783463c3c28b664b4e5acba4e0ba4ca8740d367d6_flash_display_Sprite extends Sprite
   {
       
      
      public function _4eab340d85462d013dcd578783463c3c28b664b4e5acba4e0ba4ca8740d367d6_flash_display_Sprite()
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
