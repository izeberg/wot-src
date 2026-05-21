package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2b63c623994eaf31c39139b1d299a29c4a72c6fdba5be863e40c04f23cda3a2a_flash_display_Sprite extends Sprite
   {
       
      
      public function _2b63c623994eaf31c39139b1d299a29c4a72c6fdba5be863e40c04f23cda3a2a_flash_display_Sprite()
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
