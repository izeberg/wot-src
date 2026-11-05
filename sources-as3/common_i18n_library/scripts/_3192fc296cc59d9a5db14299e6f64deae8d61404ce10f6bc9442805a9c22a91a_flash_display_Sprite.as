package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _3192fc296cc59d9a5db14299e6f64deae8d61404ce10f6bc9442805a9c22a91a_flash_display_Sprite extends Sprite
   {
       
      
      public function _3192fc296cc59d9a5db14299e6f64deae8d61404ce10f6bc9442805a9c22a91a_flash_display_Sprite()
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
