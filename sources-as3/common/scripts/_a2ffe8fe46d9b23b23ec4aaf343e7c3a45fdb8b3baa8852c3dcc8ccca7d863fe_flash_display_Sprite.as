package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a2ffe8fe46d9b23b23ec4aaf343e7c3a45fdb8b3baa8852c3dcc8ccca7d863fe_flash_display_Sprite extends Sprite
   {
       
      
      public function _a2ffe8fe46d9b23b23ec4aaf343e7c3a45fdb8b3baa8852c3dcc8ccca7d863fe_flash_display_Sprite()
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
