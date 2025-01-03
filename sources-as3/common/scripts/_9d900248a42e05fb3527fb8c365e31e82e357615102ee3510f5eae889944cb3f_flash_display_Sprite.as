package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9d900248a42e05fb3527fb8c365e31e82e357615102ee3510f5eae889944cb3f_flash_display_Sprite extends Sprite
   {
       
      
      public function _9d900248a42e05fb3527fb8c365e31e82e357615102ee3510f5eae889944cb3f_flash_display_Sprite()
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
