package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _81cc5c2965935a5d63a886328365a18ea94d5b3ae92f6e940ca0cf2cb5fe069f_flash_display_Sprite extends Sprite
   {
       
      
      public function _81cc5c2965935a5d63a886328365a18ea94d5b3ae92f6e940ca0cf2cb5fe069f_flash_display_Sprite()
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
