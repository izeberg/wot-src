package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _d52af507c2ee8d5f12192be701fd7a60b8654f907e1204b4c4afd0c03adfb81b_flash_display_Sprite extends Sprite
   {
       
      
      public function _d52af507c2ee8d5f12192be701fd7a60b8654f907e1204b4c4afd0c03adfb81b_flash_display_Sprite()
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
