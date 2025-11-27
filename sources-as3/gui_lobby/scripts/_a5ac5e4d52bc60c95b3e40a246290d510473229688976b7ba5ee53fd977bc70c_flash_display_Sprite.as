package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a5ac5e4d52bc60c95b3e40a246290d510473229688976b7ba5ee53fd977bc70c_flash_display_Sprite extends Sprite
   {
       
      
      public function _a5ac5e4d52bc60c95b3e40a246290d510473229688976b7ba5ee53fd977bc70c_flash_display_Sprite()
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
