package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0009b9492a7ecafdd5e14378e8f7bed66147f00ff51d51ecc5e42ce908fe183c_flash_display_Sprite extends Sprite
   {
       
      
      public function _0009b9492a7ecafdd5e14378e8f7bed66147f00ff51d51ecc5e42ce908fe183c_flash_display_Sprite()
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
