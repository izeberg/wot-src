package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _8e1c17fb4551e5bce3cf8e2a4549a292e6c2c578027173be84ac369cffceb24d_flash_display_Sprite extends Sprite
   {
       
      
      public function _8e1c17fb4551e5bce3cf8e2a4549a292e6c2c578027173be84ac369cffceb24d_flash_display_Sprite()
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
