package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _25c4412da1c373ffa509a3952671dea811b28351956fc8da0434c64da9dad7b8_flash_display_Sprite extends Sprite
   {
       
      
      public function _25c4412da1c373ffa509a3952671dea811b28351956fc8da0434c64da9dad7b8_flash_display_Sprite()
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
