package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4b17b16b2118a005f0d3546dfb2914eb0aad79f104382c8938bcb7e9b5aa73a6_flash_display_Sprite extends Sprite
   {
       
      
      public function _4b17b16b2118a005f0d3546dfb2914eb0aad79f104382c8938bcb7e9b5aa73a6_flash_display_Sprite()
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
