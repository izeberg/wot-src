package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _bdee07fbaf5dd375c8ac6e357f856c1b3f6bf7af51bf81a40aea3f60382c9c22_flash_display_Sprite extends Sprite
   {
       
      
      public function _bdee07fbaf5dd375c8ac6e357f856c1b3f6bf7af51bf81a40aea3f60382c9c22_flash_display_Sprite()
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
