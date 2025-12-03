package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f82e9938c893ecdd44f2265dbc61ef1ad8d82b1cce007e506140cce71ea85f8d_flash_display_Sprite extends Sprite
   {
       
      
      public function _f82e9938c893ecdd44f2265dbc61ef1ad8d82b1cce007e506140cce71ea85f8d_flash_display_Sprite()
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
