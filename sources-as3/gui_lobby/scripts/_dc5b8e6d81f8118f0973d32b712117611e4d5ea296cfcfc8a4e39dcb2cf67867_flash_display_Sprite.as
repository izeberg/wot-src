package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dc5b8e6d81f8118f0973d32b712117611e4d5ea296cfcfc8a4e39dcb2cf67867_flash_display_Sprite extends Sprite
   {
       
      
      public function _dc5b8e6d81f8118f0973d32b712117611e4d5ea296cfcfc8a4e39dcb2cf67867_flash_display_Sprite()
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
