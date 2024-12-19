package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5d528b3a0e122ac5a18a87edf656e3797824ed54aee80c94434f7ccd78f392c9_flash_display_Sprite extends Sprite
   {
       
      
      public function _5d528b3a0e122ac5a18a87edf656e3797824ed54aee80c94434f7ccd78f392c9_flash_display_Sprite()
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
