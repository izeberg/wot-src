package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _719d8de0adbde7685cc04a821f94a726db94625503172b5de806f4328a7db676_flash_display_Sprite extends Sprite
   {
       
      
      public function _719d8de0adbde7685cc04a821f94a726db94625503172b5de806f4328a7db676_flash_display_Sprite()
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
