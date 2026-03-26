package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _93c595eb8ae347870e5a11b7fb591589749c33a1d14e10d614d50eb80cea955c_flash_display_Sprite extends Sprite
   {
       
      
      public function _93c595eb8ae347870e5a11b7fb591589749c33a1d14e10d614d50eb80cea955c_flash_display_Sprite()
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
