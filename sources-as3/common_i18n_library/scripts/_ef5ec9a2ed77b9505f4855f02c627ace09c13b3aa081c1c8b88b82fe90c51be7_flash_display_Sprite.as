package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ef5ec9a2ed77b9505f4855f02c627ace09c13b3aa081c1c8b88b82fe90c51be7_flash_display_Sprite extends Sprite
   {
       
      
      public function _ef5ec9a2ed77b9505f4855f02c627ace09c13b3aa081c1c8b88b82fe90c51be7_flash_display_Sprite()
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
