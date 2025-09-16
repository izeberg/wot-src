package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e96611aef91a0b854a5ed566c2e94a7ba89969a515b2cbc4ce5300496b00705a_flash_display_Sprite extends Sprite
   {
       
      
      public function _e96611aef91a0b854a5ed566c2e94a7ba89969a515b2cbc4ce5300496b00705a_flash_display_Sprite()
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
