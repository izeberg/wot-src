package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1ea19f0060b9c34dda4b919469bf75fa4054cfbb1ce76d77bf15a7d245f7e85d_flash_display_Sprite extends Sprite
   {
       
      
      public function _1ea19f0060b9c34dda4b919469bf75fa4054cfbb1ce76d77bf15a7d245f7e85d_flash_display_Sprite()
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
