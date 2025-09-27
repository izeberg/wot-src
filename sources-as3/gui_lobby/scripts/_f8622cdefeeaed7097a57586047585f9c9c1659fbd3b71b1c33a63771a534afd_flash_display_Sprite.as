package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f8622cdefeeaed7097a57586047585f9c9c1659fbd3b71b1c33a63771a534afd_flash_display_Sprite extends Sprite
   {
       
      
      public function _f8622cdefeeaed7097a57586047585f9c9c1659fbd3b71b1c33a63771a534afd_flash_display_Sprite()
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
