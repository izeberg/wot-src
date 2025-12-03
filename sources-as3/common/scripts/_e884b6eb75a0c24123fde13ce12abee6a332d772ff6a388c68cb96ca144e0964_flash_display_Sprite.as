package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e884b6eb75a0c24123fde13ce12abee6a332d772ff6a388c68cb96ca144e0964_flash_display_Sprite extends Sprite
   {
       
      
      public function _e884b6eb75a0c24123fde13ce12abee6a332d772ff6a388c68cb96ca144e0964_flash_display_Sprite()
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
