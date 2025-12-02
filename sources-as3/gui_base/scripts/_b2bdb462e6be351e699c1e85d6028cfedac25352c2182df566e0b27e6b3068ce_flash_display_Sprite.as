package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b2bdb462e6be351e699c1e85d6028cfedac25352c2182df566e0b27e6b3068ce_flash_display_Sprite extends Sprite
   {
       
      
      public function _b2bdb462e6be351e699c1e85d6028cfedac25352c2182df566e0b27e6b3068ce_flash_display_Sprite()
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
