package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dbff31d0aea4bb5c4ad46c2153b96bdcc507f3ac3011357ead579d0067f745e7_flash_display_Sprite extends Sprite
   {
       
      
      public function _dbff31d0aea4bb5c4ad46c2153b96bdcc507f3ac3011357ead579d0067f745e7_flash_display_Sprite()
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
