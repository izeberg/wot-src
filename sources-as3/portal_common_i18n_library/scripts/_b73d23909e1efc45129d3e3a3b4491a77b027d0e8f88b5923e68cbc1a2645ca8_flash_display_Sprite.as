package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b73d23909e1efc45129d3e3a3b4491a77b027d0e8f88b5923e68cbc1a2645ca8_flash_display_Sprite extends Sprite
   {
       
      
      public function _b73d23909e1efc45129d3e3a3b4491a77b027d0e8f88b5923e68cbc1a2645ca8_flash_display_Sprite()
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
