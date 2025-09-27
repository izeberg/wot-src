package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _61cec7e824f69f24f74896ef2ed9dbde7d79de7ae1c0550dd9469cb89c2ad714_flash_display_Sprite extends Sprite
   {
       
      
      public function _61cec7e824f69f24f74896ef2ed9dbde7d79de7ae1c0550dd9469cb89c2ad714_flash_display_Sprite()
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
