package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6c4c1e192156e48911bc764ecc1842bab82a5d0c2934c818b5ded0b680f628df_flash_display_Sprite extends Sprite
   {
       
      
      public function _6c4c1e192156e48911bc764ecc1842bab82a5d0c2934c818b5ded0b680f628df_flash_display_Sprite()
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
