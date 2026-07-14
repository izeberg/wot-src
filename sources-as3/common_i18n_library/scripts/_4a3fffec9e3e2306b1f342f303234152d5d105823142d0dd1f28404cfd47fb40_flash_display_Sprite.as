package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4a3fffec9e3e2306b1f342f303234152d5d105823142d0dd1f28404cfd47fb40_flash_display_Sprite extends Sprite
   {
       
      
      public function _4a3fffec9e3e2306b1f342f303234152d5d105823142d0dd1f28404cfd47fb40_flash_display_Sprite()
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
