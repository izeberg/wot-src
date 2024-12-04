package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0cd3db5f1dca10a39610dbd28928ccc996dba584f39ed7311be5ec37a3079aa0_flash_display_Sprite extends Sprite
   {
       
      
      public function _0cd3db5f1dca10a39610dbd28928ccc996dba584f39ed7311be5ec37a3079aa0_flash_display_Sprite()
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
