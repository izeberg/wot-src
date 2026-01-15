package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ef359f17a978cafe73033ccf3ddb06e3fe36d8e4ae5411757d8873530e578b39_flash_display_Sprite extends Sprite
   {
       
      
      public function _ef359f17a978cafe73033ccf3ddb06e3fe36d8e4ae5411757d8873530e578b39_flash_display_Sprite()
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
