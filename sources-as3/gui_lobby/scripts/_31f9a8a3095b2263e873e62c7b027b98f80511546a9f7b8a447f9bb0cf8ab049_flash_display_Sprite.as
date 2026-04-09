package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _31f9a8a3095b2263e873e62c7b027b98f80511546a9f7b8a447f9bb0cf8ab049_flash_display_Sprite extends Sprite
   {
       
      
      public function _31f9a8a3095b2263e873e62c7b027b98f80511546a9f7b8a447f9bb0cf8ab049_flash_display_Sprite()
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
