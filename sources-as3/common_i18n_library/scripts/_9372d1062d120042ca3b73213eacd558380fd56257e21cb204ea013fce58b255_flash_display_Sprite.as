package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9372d1062d120042ca3b73213eacd558380fd56257e21cb204ea013fce58b255_flash_display_Sprite extends Sprite
   {
       
      
      public function _9372d1062d120042ca3b73213eacd558380fd56257e21cb204ea013fce58b255_flash_display_Sprite()
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
