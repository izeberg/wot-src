package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1568fb8b745926a380565e546bc7a74ffd3afb91a3a32e59751c510bc57d076b_flash_display_Sprite extends Sprite
   {
       
      
      public function _1568fb8b745926a380565e546bc7a74ffd3afb91a3a32e59751c510bc57d076b_flash_display_Sprite()
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
