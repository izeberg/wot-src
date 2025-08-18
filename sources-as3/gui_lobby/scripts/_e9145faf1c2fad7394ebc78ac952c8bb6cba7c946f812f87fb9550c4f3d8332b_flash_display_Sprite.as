package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e9145faf1c2fad7394ebc78ac952c8bb6cba7c946f812f87fb9550c4f3d8332b_flash_display_Sprite extends Sprite
   {
       
      
      public function _e9145faf1c2fad7394ebc78ac952c8bb6cba7c946f812f87fb9550c4f3d8332b_flash_display_Sprite()
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
