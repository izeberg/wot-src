package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _4e38118193dde9b0891cf87b228dba32eca205fb53f4ccdf3ae74f0393fb844c_flash_display_Sprite extends Sprite
   {
       
      
      public function _4e38118193dde9b0891cf87b228dba32eca205fb53f4ccdf3ae74f0393fb844c_flash_display_Sprite()
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
