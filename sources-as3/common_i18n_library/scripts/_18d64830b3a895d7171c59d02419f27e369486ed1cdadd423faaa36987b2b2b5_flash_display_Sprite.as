package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _18d64830b3a895d7171c59d02419f27e369486ed1cdadd423faaa36987b2b2b5_flash_display_Sprite extends Sprite
   {
       
      
      public function _18d64830b3a895d7171c59d02419f27e369486ed1cdadd423faaa36987b2b2b5_flash_display_Sprite()
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
