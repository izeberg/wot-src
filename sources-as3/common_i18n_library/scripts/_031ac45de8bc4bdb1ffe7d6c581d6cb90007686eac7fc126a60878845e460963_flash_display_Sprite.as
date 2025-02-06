package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _031ac45de8bc4bdb1ffe7d6c581d6cb90007686eac7fc126a60878845e460963_flash_display_Sprite extends Sprite
   {
       
      
      public function _031ac45de8bc4bdb1ffe7d6c581d6cb90007686eac7fc126a60878845e460963_flash_display_Sprite()
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
