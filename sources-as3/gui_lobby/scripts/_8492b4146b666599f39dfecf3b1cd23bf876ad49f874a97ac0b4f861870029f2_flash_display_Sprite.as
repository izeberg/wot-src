package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8492b4146b666599f39dfecf3b1cd23bf876ad49f874a97ac0b4f861870029f2_flash_display_Sprite extends Sprite
   {
       
      
      public function _8492b4146b666599f39dfecf3b1cd23bf876ad49f874a97ac0b4f861870029f2_flash_display_Sprite()
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
