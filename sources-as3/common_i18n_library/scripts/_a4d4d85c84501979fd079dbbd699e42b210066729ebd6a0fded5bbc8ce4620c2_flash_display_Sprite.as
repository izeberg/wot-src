package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a4d4d85c84501979fd079dbbd699e42b210066729ebd6a0fded5bbc8ce4620c2_flash_display_Sprite extends Sprite
   {
       
      
      public function _a4d4d85c84501979fd079dbbd699e42b210066729ebd6a0fded5bbc8ce4620c2_flash_display_Sprite()
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
