package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a0775e9857e1045b8dea39e53ca8631842ac91cc61a0767a3e85ba605e19568d_flash_display_Sprite extends Sprite
   {
       
      
      public function _a0775e9857e1045b8dea39e53ca8631842ac91cc61a0767a3e85ba605e19568d_flash_display_Sprite()
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
