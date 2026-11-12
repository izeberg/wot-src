package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _55d4697dc0a141dea82610e957dbb9a04ba8ab52a363c6cbdd485e87257ed5a3_flash_display_Sprite extends Sprite
   {
       
      
      public function _55d4697dc0a141dea82610e957dbb9a04ba8ab52a363c6cbdd485e87257ed5a3_flash_display_Sprite()
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
