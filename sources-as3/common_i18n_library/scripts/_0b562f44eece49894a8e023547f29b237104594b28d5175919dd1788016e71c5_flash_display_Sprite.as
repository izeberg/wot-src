package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0b562f44eece49894a8e023547f29b237104594b28d5175919dd1788016e71c5_flash_display_Sprite extends Sprite
   {
       
      
      public function _0b562f44eece49894a8e023547f29b237104594b28d5175919dd1788016e71c5_flash_display_Sprite()
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
