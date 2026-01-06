package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2bdaff7b4b04c037c218686cd09bc1b9588e2fd1571cef44501d980e1439bc54_flash_display_Sprite extends Sprite
   {
       
      
      public function _2bdaff7b4b04c037c218686cd09bc1b9588e2fd1571cef44501d980e1439bc54_flash_display_Sprite()
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
