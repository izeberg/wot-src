package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _01c91acaab4818a5e57af2398700c3c94ec8af7fcdf192805e65c045cb7c85e4_flash_display_Sprite extends Sprite
   {
       
      
      public function _01c91acaab4818a5e57af2398700c3c94ec8af7fcdf192805e65c045cb7c85e4_flash_display_Sprite()
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
