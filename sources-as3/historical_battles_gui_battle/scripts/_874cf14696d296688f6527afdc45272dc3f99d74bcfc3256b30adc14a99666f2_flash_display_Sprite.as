package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _874cf14696d296688f6527afdc45272dc3f99d74bcfc3256b30adc14a99666f2_flash_display_Sprite extends Sprite
   {
       
      
      public function _874cf14696d296688f6527afdc45272dc3f99d74bcfc3256b30adc14a99666f2_flash_display_Sprite()
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
