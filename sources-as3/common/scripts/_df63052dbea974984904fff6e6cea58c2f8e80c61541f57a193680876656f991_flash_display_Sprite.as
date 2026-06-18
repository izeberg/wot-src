package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _df63052dbea974984904fff6e6cea58c2f8e80c61541f57a193680876656f991_flash_display_Sprite extends Sprite
   {
       
      
      public function _df63052dbea974984904fff6e6cea58c2f8e80c61541f57a193680876656f991_flash_display_Sprite()
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
