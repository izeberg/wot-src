package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0318a5720afedb008bcded2264edfb287069e5ec560a4b903d1ac1a9e99ebd2a_flash_display_Sprite extends Sprite
   {
       
      
      public function _0318a5720afedb008bcded2264edfb287069e5ec560a4b903d1ac1a9e99ebd2a_flash_display_Sprite()
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
