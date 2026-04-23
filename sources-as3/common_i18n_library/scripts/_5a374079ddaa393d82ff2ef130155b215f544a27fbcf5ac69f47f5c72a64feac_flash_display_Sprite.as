package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5a374079ddaa393d82ff2ef130155b215f544a27fbcf5ac69f47f5c72a64feac_flash_display_Sprite extends Sprite
   {
       
      
      public function _5a374079ddaa393d82ff2ef130155b215f544a27fbcf5ac69f47f5c72a64feac_flash_display_Sprite()
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
