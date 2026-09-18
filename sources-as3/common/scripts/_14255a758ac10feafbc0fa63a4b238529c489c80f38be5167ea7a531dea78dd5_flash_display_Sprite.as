package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _14255a758ac10feafbc0fa63a4b238529c489c80f38be5167ea7a531dea78dd5_flash_display_Sprite extends Sprite
   {
       
      
      public function _14255a758ac10feafbc0fa63a4b238529c489c80f38be5167ea7a531dea78dd5_flash_display_Sprite()
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
