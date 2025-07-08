package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9b47a22ffe8e9f9d73f29b5aef168fcf9b3c1e0859b7a4bcc6dd53a3455917a0_flash_display_Sprite extends Sprite
   {
       
      
      public function _9b47a22ffe8e9f9d73f29b5aef168fcf9b3c1e0859b7a4bcc6dd53a3455917a0_flash_display_Sprite()
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
