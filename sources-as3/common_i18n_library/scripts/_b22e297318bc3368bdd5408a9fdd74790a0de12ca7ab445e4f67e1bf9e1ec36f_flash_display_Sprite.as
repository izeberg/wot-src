package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b22e297318bc3368bdd5408a9fdd74790a0de12ca7ab445e4f67e1bf9e1ec36f_flash_display_Sprite extends Sprite
   {
       
      
      public function _b22e297318bc3368bdd5408a9fdd74790a0de12ca7ab445e4f67e1bf9e1ec36f_flash_display_Sprite()
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
