package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4119c2f959efd92a905c7634276bdbd0b792309d5cd05b50d2ab224240ae6baf_flash_display_Sprite extends Sprite
   {
       
      
      public function _4119c2f959efd92a905c7634276bdbd0b792309d5cd05b50d2ab224240ae6baf_flash_display_Sprite()
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
