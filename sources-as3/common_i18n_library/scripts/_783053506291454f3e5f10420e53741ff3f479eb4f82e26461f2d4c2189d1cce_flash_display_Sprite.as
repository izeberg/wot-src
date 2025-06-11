package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _783053506291454f3e5f10420e53741ff3f479eb4f82e26461f2d4c2189d1cce_flash_display_Sprite extends Sprite
   {
       
      
      public function _783053506291454f3e5f10420e53741ff3f479eb4f82e26461f2d4c2189d1cce_flash_display_Sprite()
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
