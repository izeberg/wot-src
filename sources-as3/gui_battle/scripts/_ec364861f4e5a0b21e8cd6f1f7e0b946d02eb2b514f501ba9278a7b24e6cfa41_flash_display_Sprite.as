package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ec364861f4e5a0b21e8cd6f1f7e0b946d02eb2b514f501ba9278a7b24e6cfa41_flash_display_Sprite extends Sprite
   {
       
      
      public function _ec364861f4e5a0b21e8cd6f1f7e0b946d02eb2b514f501ba9278a7b24e6cfa41_flash_display_Sprite()
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
