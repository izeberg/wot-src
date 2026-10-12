package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5ee87df2545742a201ff0f54f2148b5f7d48a6beea63221373ece42b9ffe7e51_flash_display_Sprite extends Sprite
   {
       
      
      public function _5ee87df2545742a201ff0f54f2148b5f7d48a6beea63221373ece42b9ffe7e51_flash_display_Sprite()
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
