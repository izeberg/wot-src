package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ad28463aa188eade5ee86298f6ead5e9db1f0495e7a7cf51ca892a33cdccf624_flash_display_Sprite extends Sprite
   {
       
      
      public function _ad28463aa188eade5ee86298f6ead5e9db1f0495e7a7cf51ca892a33cdccf624_flash_display_Sprite()
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
