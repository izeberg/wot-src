package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _575e74ea76e2ca0ae65605f68c2420b2576e7d3fdfd33d828e256d9a163de120_flash_display_Sprite extends Sprite
   {
       
      
      public function _575e74ea76e2ca0ae65605f68c2420b2576e7d3fdfd33d828e256d9a163de120_flash_display_Sprite()
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
