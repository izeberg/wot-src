package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8f98a5efe6a9d7a989f5fc22ae1ba360465a40a5ae926549bc2db51076b479ec_flash_display_Sprite extends Sprite
   {
       
      
      public function _8f98a5efe6a9d7a989f5fc22ae1ba360465a40a5ae926549bc2db51076b479ec_flash_display_Sprite()
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
