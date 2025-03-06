package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e1d0edcfd02543597dc16183689d1698862b68fa8aeea5a5f67ac5b09c161f9b_flash_display_Sprite extends Sprite
   {
       
      
      public function _e1d0edcfd02543597dc16183689d1698862b68fa8aeea5a5f67ac5b09c161f9b_flash_display_Sprite()
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
