package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a834f1258b820fc2fe1482adffcf53a7ddf16f18a8ffa4db26441d7f6320c655_flash_display_Sprite extends Sprite
   {
       
      
      public function _a834f1258b820fc2fe1482adffcf53a7ddf16f18a8ffa4db26441d7f6320c655_flash_display_Sprite()
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
