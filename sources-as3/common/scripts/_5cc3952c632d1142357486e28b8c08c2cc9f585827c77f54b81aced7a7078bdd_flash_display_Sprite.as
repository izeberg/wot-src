package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5cc3952c632d1142357486e28b8c08c2cc9f585827c77f54b81aced7a7078bdd_flash_display_Sprite extends Sprite
   {
       
      
      public function _5cc3952c632d1142357486e28b8c08c2cc9f585827c77f54b81aced7a7078bdd_flash_display_Sprite()
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
