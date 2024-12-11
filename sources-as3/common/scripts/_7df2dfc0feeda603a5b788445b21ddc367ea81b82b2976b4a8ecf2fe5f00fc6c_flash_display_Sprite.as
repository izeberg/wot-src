package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7df2dfc0feeda603a5b788445b21ddc367ea81b82b2976b4a8ecf2fe5f00fc6c_flash_display_Sprite extends Sprite
   {
       
      
      public function _7df2dfc0feeda603a5b788445b21ddc367ea81b82b2976b4a8ecf2fe5f00fc6c_flash_display_Sprite()
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
