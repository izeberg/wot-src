package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a4796faa6cd94e319923188bdeb01879eb91c61c37a5c432009010a69643c195_flash_display_Sprite extends Sprite
   {
       
      
      public function _a4796faa6cd94e319923188bdeb01879eb91c61c37a5c432009010a69643c195_flash_display_Sprite()
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
