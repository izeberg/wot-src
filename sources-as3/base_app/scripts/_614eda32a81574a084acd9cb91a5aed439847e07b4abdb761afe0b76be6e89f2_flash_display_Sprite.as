package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _614eda32a81574a084acd9cb91a5aed439847e07b4abdb761afe0b76be6e89f2_flash_display_Sprite extends Sprite
   {
       
      
      public function _614eda32a81574a084acd9cb91a5aed439847e07b4abdb761afe0b76be6e89f2_flash_display_Sprite()
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
