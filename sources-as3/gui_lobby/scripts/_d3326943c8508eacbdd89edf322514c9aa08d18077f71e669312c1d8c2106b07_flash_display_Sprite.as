package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d3326943c8508eacbdd89edf322514c9aa08d18077f71e669312c1d8c2106b07_flash_display_Sprite extends Sprite
   {
       
      
      public function _d3326943c8508eacbdd89edf322514c9aa08d18077f71e669312c1d8c2106b07_flash_display_Sprite()
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
