package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a4afa0422fbfcdcf68cff7dbcb5a2142a4573a5efd9aaa5bcd480b413eca2a05_flash_display_Sprite extends Sprite
   {
       
      
      public function _a4afa0422fbfcdcf68cff7dbcb5a2142a4573a5efd9aaa5bcd480b413eca2a05_flash_display_Sprite()
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
