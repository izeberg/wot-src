package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _313785de8ae7790a358a3c8cc15a4f45a0aa8e779b26564af5e86c4327ff8e81_flash_display_Sprite extends Sprite
   {
       
      
      public function _313785de8ae7790a358a3c8cc15a4f45a0aa8e779b26564af5e86c4327ff8e81_flash_display_Sprite()
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
