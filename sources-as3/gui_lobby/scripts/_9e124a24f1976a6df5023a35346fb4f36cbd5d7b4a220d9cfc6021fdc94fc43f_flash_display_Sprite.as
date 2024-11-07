package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9e124a24f1976a6df5023a35346fb4f36cbd5d7b4a220d9cfc6021fdc94fc43f_flash_display_Sprite extends Sprite
   {
       
      
      public function _9e124a24f1976a6df5023a35346fb4f36cbd5d7b4a220d9cfc6021fdc94fc43f_flash_display_Sprite()
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
