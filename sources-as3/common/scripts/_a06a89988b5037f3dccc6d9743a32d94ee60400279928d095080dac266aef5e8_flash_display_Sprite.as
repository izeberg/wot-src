package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a06a89988b5037f3dccc6d9743a32d94ee60400279928d095080dac266aef5e8_flash_display_Sprite extends Sprite
   {
       
      
      public function _a06a89988b5037f3dccc6d9743a32d94ee60400279928d095080dac266aef5e8_flash_display_Sprite()
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
