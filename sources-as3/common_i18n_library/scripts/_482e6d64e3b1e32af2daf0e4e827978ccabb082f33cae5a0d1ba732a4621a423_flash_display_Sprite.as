package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _482e6d64e3b1e32af2daf0e4e827978ccabb082f33cae5a0d1ba732a4621a423_flash_display_Sprite extends Sprite
   {
       
      
      public function _482e6d64e3b1e32af2daf0e4e827978ccabb082f33cae5a0d1ba732a4621a423_flash_display_Sprite()
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
