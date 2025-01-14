package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1395b7e81f8f67a61f70c1d1bb93e4cfcc7dfeab056ff81e8e684e0335bde961_flash_display_Sprite extends Sprite
   {
       
      
      public function _1395b7e81f8f67a61f70c1d1bb93e4cfcc7dfeab056ff81e8e684e0335bde961_flash_display_Sprite()
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
