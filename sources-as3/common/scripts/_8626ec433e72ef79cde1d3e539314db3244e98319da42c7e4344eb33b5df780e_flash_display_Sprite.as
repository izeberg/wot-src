package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8626ec433e72ef79cde1d3e539314db3244e98319da42c7e4344eb33b5df780e_flash_display_Sprite extends Sprite
   {
       
      
      public function _8626ec433e72ef79cde1d3e539314db3244e98319da42c7e4344eb33b5df780e_flash_display_Sprite()
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
