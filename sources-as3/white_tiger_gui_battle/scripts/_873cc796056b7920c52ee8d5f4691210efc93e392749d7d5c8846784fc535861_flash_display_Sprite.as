package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _873cc796056b7920c52ee8d5f4691210efc93e392749d7d5c8846784fc535861_flash_display_Sprite extends Sprite
   {
       
      
      public function _873cc796056b7920c52ee8d5f4691210efc93e392749d7d5c8846784fc535861_flash_display_Sprite()
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
