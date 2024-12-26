package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _fc08f610a0aa0356b83f19dcb103739af7ab3df13839a47543ed9f09f3d0816b_flash_display_Sprite extends Sprite
   {
       
      
      public function _fc08f610a0aa0356b83f19dcb103739af7ab3df13839a47543ed9f09f3d0816b_flash_display_Sprite()
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
