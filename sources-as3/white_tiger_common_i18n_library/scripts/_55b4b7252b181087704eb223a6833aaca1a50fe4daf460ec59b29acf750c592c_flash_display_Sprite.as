package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _55b4b7252b181087704eb223a6833aaca1a50fe4daf460ec59b29acf750c592c_flash_display_Sprite extends Sprite
   {
       
      
      public function _55b4b7252b181087704eb223a6833aaca1a50fe4daf460ec59b29acf750c592c_flash_display_Sprite()
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
