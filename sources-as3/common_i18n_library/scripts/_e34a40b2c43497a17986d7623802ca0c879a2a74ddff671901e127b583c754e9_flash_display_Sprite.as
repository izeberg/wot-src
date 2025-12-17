package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e34a40b2c43497a17986d7623802ca0c879a2a74ddff671901e127b583c754e9_flash_display_Sprite extends Sprite
   {
       
      
      public function _e34a40b2c43497a17986d7623802ca0c879a2a74ddff671901e127b583c754e9_flash_display_Sprite()
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
