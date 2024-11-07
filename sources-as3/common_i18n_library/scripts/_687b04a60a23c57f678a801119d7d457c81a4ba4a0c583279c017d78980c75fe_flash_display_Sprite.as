package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _687b04a60a23c57f678a801119d7d457c81a4ba4a0c583279c017d78980c75fe_flash_display_Sprite extends Sprite
   {
       
      
      public function _687b04a60a23c57f678a801119d7d457c81a4ba4a0c583279c017d78980c75fe_flash_display_Sprite()
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
