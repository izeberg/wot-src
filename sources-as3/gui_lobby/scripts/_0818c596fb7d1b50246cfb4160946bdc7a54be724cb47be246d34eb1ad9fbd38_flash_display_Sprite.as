package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0818c596fb7d1b50246cfb4160946bdc7a54be724cb47be246d34eb1ad9fbd38_flash_display_Sprite extends Sprite
   {
       
      
      public function _0818c596fb7d1b50246cfb4160946bdc7a54be724cb47be246d34eb1ad9fbd38_flash_display_Sprite()
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
