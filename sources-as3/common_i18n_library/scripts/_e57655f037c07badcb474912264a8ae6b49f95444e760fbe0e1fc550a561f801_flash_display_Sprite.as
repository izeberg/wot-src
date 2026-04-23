package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _e57655f037c07badcb474912264a8ae6b49f95444e760fbe0e1fc550a561f801_flash_display_Sprite extends Sprite
   {
       
      
      public function _e57655f037c07badcb474912264a8ae6b49f95444e760fbe0e1fc550a561f801_flash_display_Sprite()
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
