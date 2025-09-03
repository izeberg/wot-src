package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _6d1d4ee312dd786dba8d3ff1e9786872716acc5ca3e7d8006d089c10f37bee9b_flash_display_Sprite extends Sprite
   {
       
      
      public function _6d1d4ee312dd786dba8d3ff1e9786872716acc5ca3e7d8006d089c10f37bee9b_flash_display_Sprite()
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
