package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4b506e384f9d4c15c40d43912223f672576b82992cdd4496e8236c6846aa976e_flash_display_Sprite extends Sprite
   {
       
      
      public function _4b506e384f9d4c15c40d43912223f672576b82992cdd4496e8236c6846aa976e_flash_display_Sprite()
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
