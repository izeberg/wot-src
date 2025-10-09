package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2220f34b921c3dcd565f91e56952875adb797ba5d8eadff7615b435f6d304529_flash_display_Sprite extends Sprite
   {
       
      
      public function _2220f34b921c3dcd565f91e56952875adb797ba5d8eadff7615b435f6d304529_flash_display_Sprite()
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
