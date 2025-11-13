package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4624243c937ac90a6fe85687250342fc9e1ac78c21e84ed47b83fb1c744feba7_flash_display_Sprite extends Sprite
   {
       
      
      public function _4624243c937ac90a6fe85687250342fc9e1ac78c21e84ed47b83fb1c744feba7_flash_display_Sprite()
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
