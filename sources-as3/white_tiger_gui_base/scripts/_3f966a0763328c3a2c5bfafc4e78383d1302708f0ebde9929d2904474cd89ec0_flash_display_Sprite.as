package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _3f966a0763328c3a2c5bfafc4e78383d1302708f0ebde9929d2904474cd89ec0_flash_display_Sprite extends Sprite
   {
       
      
      public function _3f966a0763328c3a2c5bfafc4e78383d1302708f0ebde9929d2904474cd89ec0_flash_display_Sprite()
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
