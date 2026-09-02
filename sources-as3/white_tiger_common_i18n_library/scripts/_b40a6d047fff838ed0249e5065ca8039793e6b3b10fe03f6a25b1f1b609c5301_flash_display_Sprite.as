package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b40a6d047fff838ed0249e5065ca8039793e6b3b10fe03f6a25b1f1b609c5301_flash_display_Sprite extends Sprite
   {
       
      
      public function _b40a6d047fff838ed0249e5065ca8039793e6b3b10fe03f6a25b1f1b609c5301_flash_display_Sprite()
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
