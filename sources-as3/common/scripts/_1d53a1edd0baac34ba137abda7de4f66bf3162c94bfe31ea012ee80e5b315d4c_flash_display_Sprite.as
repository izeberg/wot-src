package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1d53a1edd0baac34ba137abda7de4f66bf3162c94bfe31ea012ee80e5b315d4c_flash_display_Sprite extends Sprite
   {
       
      
      public function _1d53a1edd0baac34ba137abda7de4f66bf3162c94bfe31ea012ee80e5b315d4c_flash_display_Sprite()
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
