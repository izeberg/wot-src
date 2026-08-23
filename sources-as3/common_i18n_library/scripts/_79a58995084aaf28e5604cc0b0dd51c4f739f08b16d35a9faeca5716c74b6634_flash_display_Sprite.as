package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _79a58995084aaf28e5604cc0b0dd51c4f739f08b16d35a9faeca5716c74b6634_flash_display_Sprite extends Sprite
   {
       
      
      public function _79a58995084aaf28e5604cc0b0dd51c4f739f08b16d35a9faeca5716c74b6634_flash_display_Sprite()
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
