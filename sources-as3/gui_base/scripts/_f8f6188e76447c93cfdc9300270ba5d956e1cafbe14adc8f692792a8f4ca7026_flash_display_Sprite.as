package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f8f6188e76447c93cfdc9300270ba5d956e1cafbe14adc8f692792a8f4ca7026_flash_display_Sprite extends Sprite
   {
       
      
      public function _f8f6188e76447c93cfdc9300270ba5d956e1cafbe14adc8f692792a8f4ca7026_flash_display_Sprite()
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
