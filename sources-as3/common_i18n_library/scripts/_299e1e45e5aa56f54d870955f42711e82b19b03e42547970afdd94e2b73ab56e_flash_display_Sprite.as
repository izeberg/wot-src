package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _299e1e45e5aa56f54d870955f42711e82b19b03e42547970afdd94e2b73ab56e_flash_display_Sprite extends Sprite
   {
       
      
      public function _299e1e45e5aa56f54d870955f42711e82b19b03e42547970afdd94e2b73ab56e_flash_display_Sprite()
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
