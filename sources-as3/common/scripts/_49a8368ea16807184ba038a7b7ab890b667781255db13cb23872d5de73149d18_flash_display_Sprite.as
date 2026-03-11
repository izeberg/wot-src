package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _49a8368ea16807184ba038a7b7ab890b667781255db13cb23872d5de73149d18_flash_display_Sprite extends Sprite
   {
       
      
      public function _49a8368ea16807184ba038a7b7ab890b667781255db13cb23872d5de73149d18_flash_display_Sprite()
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
