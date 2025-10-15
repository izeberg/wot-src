package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _77e99431506e4fb3759527140d924c6792c283c4925401f4970635329d32644c_flash_display_Sprite extends Sprite
   {
       
      
      public function _77e99431506e4fb3759527140d924c6792c283c4925401f4970635329d32644c_flash_display_Sprite()
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
