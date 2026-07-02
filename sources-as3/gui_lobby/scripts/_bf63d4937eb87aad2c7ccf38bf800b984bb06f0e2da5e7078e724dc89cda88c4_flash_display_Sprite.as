package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _bf63d4937eb87aad2c7ccf38bf800b984bb06f0e2da5e7078e724dc89cda88c4_flash_display_Sprite extends Sprite
   {
       
      
      public function _bf63d4937eb87aad2c7ccf38bf800b984bb06f0e2da5e7078e724dc89cda88c4_flash_display_Sprite()
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
