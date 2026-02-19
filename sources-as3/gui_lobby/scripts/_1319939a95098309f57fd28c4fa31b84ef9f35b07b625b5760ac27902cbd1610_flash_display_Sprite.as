package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1319939a95098309f57fd28c4fa31b84ef9f35b07b625b5760ac27902cbd1610_flash_display_Sprite extends Sprite
   {
       
      
      public function _1319939a95098309f57fd28c4fa31b84ef9f35b07b625b5760ac27902cbd1610_flash_display_Sprite()
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
