package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _5ee31dc8d2daeebe1cfed7816a3f49c199797cde7d79cfd5072391381e26eedd_flash_display_Sprite extends Sprite
   {
       
      
      public function _5ee31dc8d2daeebe1cfed7816a3f49c199797cde7d79cfd5072391381e26eedd_flash_display_Sprite()
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
