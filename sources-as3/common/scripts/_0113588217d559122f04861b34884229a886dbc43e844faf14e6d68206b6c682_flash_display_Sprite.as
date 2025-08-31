package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0113588217d559122f04861b34884229a886dbc43e844faf14e6d68206b6c682_flash_display_Sprite extends Sprite
   {
       
      
      public function _0113588217d559122f04861b34884229a886dbc43e844faf14e6d68206b6c682_flash_display_Sprite()
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
