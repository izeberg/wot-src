package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _bbad7a4309e7269f458a960263e83c1a232ea79c28129a2524ffea2a4914e834_flash_display_Sprite extends Sprite
   {
       
      
      public function _bbad7a4309e7269f458a960263e83c1a232ea79c28129a2524ffea2a4914e834_flash_display_Sprite()
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
