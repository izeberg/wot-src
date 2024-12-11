package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d4177f6aabeb32e7d33eebd68a9f630cd3bc018ddc225a98a210a63fee883886_flash_display_Sprite extends Sprite
   {
       
      
      public function _d4177f6aabeb32e7d33eebd68a9f630cd3bc018ddc225a98a210a63fee883886_flash_display_Sprite()
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
