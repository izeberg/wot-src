package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _45c57e806b0c8c042c8c83a80e581f10b4f6d4ec6f7a88a906239c9459774f7b_flash_display_Sprite extends Sprite
   {
       
      
      public function _45c57e806b0c8c042c8c83a80e581f10b4f6d4ec6f7a88a906239c9459774f7b_flash_display_Sprite()
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
