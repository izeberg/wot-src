package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _19387f3b54923d5a0477d0a47449b77ba925def1aae82c9abe0d1628b24e4c80_flash_display_Sprite extends Sprite
   {
       
      
      public function _19387f3b54923d5a0477d0a47449b77ba925def1aae82c9abe0d1628b24e4c80_flash_display_Sprite()
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
