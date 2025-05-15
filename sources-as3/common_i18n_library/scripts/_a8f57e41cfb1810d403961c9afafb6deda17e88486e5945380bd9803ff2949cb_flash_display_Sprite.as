package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a8f57e41cfb1810d403961c9afafb6deda17e88486e5945380bd9803ff2949cb_flash_display_Sprite extends Sprite
   {
       
      
      public function _a8f57e41cfb1810d403961c9afafb6deda17e88486e5945380bd9803ff2949cb_flash_display_Sprite()
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
