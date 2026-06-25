package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _948f3f920a2f9a256d40e1ef3c9a126f3c06689fc9f38b49f8544ea0d566747e_flash_display_Sprite extends Sprite
   {
       
      
      public function _948f3f920a2f9a256d40e1ef3c9a126f3c06689fc9f38b49f8544ea0d566747e_flash_display_Sprite()
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
