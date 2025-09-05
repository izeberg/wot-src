package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8a658f12dbe5d2008252c7a3ab2f614d66089af5584079427e1851b5bf2d359b_flash_display_Sprite extends Sprite
   {
       
      
      public function _8a658f12dbe5d2008252c7a3ab2f614d66089af5584079427e1851b5bf2d359b_flash_display_Sprite()
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
