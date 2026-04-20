package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _18746728478ae6ad95d8b2f489791fd0c5d2308de511d7e71b6ca6baa31f665f_flash_display_Sprite extends Sprite
   {
       
      
      public function _18746728478ae6ad95d8b2f489791fd0c5d2308de511d7e71b6ca6baa31f665f_flash_display_Sprite()
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
