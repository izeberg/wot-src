package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _379d1ea20e8629c3437ab30cca3a4da181f5d9deceb45ea0862e87d00ad5b9e3_flash_display_Sprite extends Sprite
   {
       
      
      public function _379d1ea20e8629c3437ab30cca3a4da181f5d9deceb45ea0862e87d00ad5b9e3_flash_display_Sprite()
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
