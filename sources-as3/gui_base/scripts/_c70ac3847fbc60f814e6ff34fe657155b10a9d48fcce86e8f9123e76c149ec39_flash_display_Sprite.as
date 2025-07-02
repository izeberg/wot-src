package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _c70ac3847fbc60f814e6ff34fe657155b10a9d48fcce86e8f9123e76c149ec39_flash_display_Sprite extends Sprite
   {
       
      
      public function _c70ac3847fbc60f814e6ff34fe657155b10a9d48fcce86e8f9123e76c149ec39_flash_display_Sprite()
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
