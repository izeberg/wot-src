package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _006dbfd26c772f94b07c98b95e462d84759b43004d196e59c758aa4e8e7ce506_flash_display_Sprite extends Sprite
   {
       
      
      public function _006dbfd26c772f94b07c98b95e462d84759b43004d196e59c758aa4e8e7ce506_flash_display_Sprite()
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
