package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _75f616082a859e4a6daa1aa741acd18de43c37abd148514ea48827771b60fb03_flash_display_Sprite extends Sprite
   {
       
      
      public function _75f616082a859e4a6daa1aa741acd18de43c37abd148514ea48827771b60fb03_flash_display_Sprite()
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
