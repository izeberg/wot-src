package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e63f02fcab1d1cae31ee1144dfa0e503caf6749668cf1ee032c79f41125b67a6_flash_display_Sprite extends Sprite
   {
       
      
      public function _e63f02fcab1d1cae31ee1144dfa0e503caf6749668cf1ee032c79f41125b67a6_flash_display_Sprite()
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
