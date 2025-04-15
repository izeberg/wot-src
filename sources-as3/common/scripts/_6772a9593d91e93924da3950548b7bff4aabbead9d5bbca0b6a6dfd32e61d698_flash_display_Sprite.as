package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6772a9593d91e93924da3950548b7bff4aabbead9d5bbca0b6a6dfd32e61d698_flash_display_Sprite extends Sprite
   {
       
      
      public function _6772a9593d91e93924da3950548b7bff4aabbead9d5bbca0b6a6dfd32e61d698_flash_display_Sprite()
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
