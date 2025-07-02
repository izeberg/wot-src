package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _417085d6bf6126686a8f81289ef941fe8993d66ec4c0099e690a459a9c53f130_flash_display_Sprite extends Sprite
   {
       
      
      public function _417085d6bf6126686a8f81289ef941fe8993d66ec4c0099e690a459a9c53f130_flash_display_Sprite()
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
