package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4cc719cf65ece3c3c2a77d93bbc2db6d41f6c992f3550d3d351fedfa96b4f313_flash_display_Sprite extends Sprite
   {
       
      
      public function _4cc719cf65ece3c3c2a77d93bbc2db6d41f6c992f3550d3d351fedfa96b4f313_flash_display_Sprite()
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
