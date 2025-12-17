package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _fcc6291562dbfbe7488bd42e042c5b2b130726ba860ad67796d462bbe8062742_flash_display_Sprite extends Sprite
   {
       
      
      public function _fcc6291562dbfbe7488bd42e042c5b2b130726ba860ad67796d462bbe8062742_flash_display_Sprite()
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
