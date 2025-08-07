package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _f61037e7d5995344b25ee01777c9cfcae32f136afab3cc9eab6b303225f2fd73_flash_display_Sprite extends Sprite
   {
       
      
      public function _f61037e7d5995344b25ee01777c9cfcae32f136afab3cc9eab6b303225f2fd73_flash_display_Sprite()
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
