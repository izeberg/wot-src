package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _7f6832a45f0b959f3b800a68dca543063d73211c1616557ac480a03f56627456_flash_display_Sprite extends Sprite
   {
       
      
      public function _7f6832a45f0b959f3b800a68dca543063d73211c1616557ac480a03f56627456_flash_display_Sprite()
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
