package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6f6e233202486c06646c50bd1889ac63c27062e0c81dc315e01dcd4ebff722d1_flash_display_Sprite extends Sprite
   {
       
      
      public function _6f6e233202486c06646c50bd1889ac63c27062e0c81dc315e01dcd4ebff722d1_flash_display_Sprite()
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
