package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b1e30b6a43cc532381e13a0a32cde473945163f04515f50830d70f407d3d2804_flash_display_Sprite extends Sprite
   {
       
      
      public function _b1e30b6a43cc532381e13a0a32cde473945163f04515f50830d70f407d3d2804_flash_display_Sprite()
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
