package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2e492f68ecd1689a0cd1668577ca01764857804ba88ee70a5469ff6076881ebd_flash_display_Sprite extends Sprite
   {
       
      
      public function _2e492f68ecd1689a0cd1668577ca01764857804ba88ee70a5469ff6076881ebd_flash_display_Sprite()
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
