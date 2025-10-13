package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1763387bf6e2260dedb6955201c221660eb9b2ff623585abd517ff391094af85_flash_display_Sprite extends Sprite
   {
       
      
      public function _1763387bf6e2260dedb6955201c221660eb9b2ff623585abd517ff391094af85_flash_display_Sprite()
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
