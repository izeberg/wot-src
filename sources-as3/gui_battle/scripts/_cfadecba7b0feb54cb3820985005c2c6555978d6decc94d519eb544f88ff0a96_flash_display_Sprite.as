package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _cfadecba7b0feb54cb3820985005c2c6555978d6decc94d519eb544f88ff0a96_flash_display_Sprite extends Sprite
   {
       
      
      public function _cfadecba7b0feb54cb3820985005c2c6555978d6decc94d519eb544f88ff0a96_flash_display_Sprite()
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
