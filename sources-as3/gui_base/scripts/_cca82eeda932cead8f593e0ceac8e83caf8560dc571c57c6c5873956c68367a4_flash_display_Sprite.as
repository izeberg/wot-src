package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _cca82eeda932cead8f593e0ceac8e83caf8560dc571c57c6c5873956c68367a4_flash_display_Sprite extends Sprite
   {
       
      
      public function _cca82eeda932cead8f593e0ceac8e83caf8560dc571c57c6c5873956c68367a4_flash_display_Sprite()
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
