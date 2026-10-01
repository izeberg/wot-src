package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _b650342b741072579956765a78080e402f46d9445eda16df243e0d50be5d5876_flash_display_Sprite extends Sprite
   {
       
      
      public function _b650342b741072579956765a78080e402f46d9445eda16df243e0d50be5d5876_flash_display_Sprite()
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
