package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c9d3cb8f3977f74828d0c2baf09d49140f915b26e593c80f562855b4220374e0_flash_display_Sprite extends Sprite
   {
       
      
      public function _c9d3cb8f3977f74828d0c2baf09d49140f915b26e593c80f562855b4220374e0_flash_display_Sprite()
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
