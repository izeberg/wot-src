package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ad858139d204efadad0284d1b2d95071a1fee931f23c2647874c4503f7b33320_flash_display_Sprite extends Sprite
   {
       
      
      public function _ad858139d204efadad0284d1b2d95071a1fee931f23c2647874c4503f7b33320_flash_display_Sprite()
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
