package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _fe493bb7b7440e3f0e2c51a455b7970166504c0204907409c2939424b0105757_flash_display_Sprite extends Sprite
   {
       
      
      public function _fe493bb7b7440e3f0e2c51a455b7970166504c0204907409c2939424b0105757_flash_display_Sprite()
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
