package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _83183d2dcba704b8da7e51a64ed62a4a4fb4d7d7e849640b4d40ffb4560b4af7_flash_display_Sprite extends Sprite
   {
       
      
      public function _83183d2dcba704b8da7e51a64ed62a4a4fb4d7d7e849640b4d40ffb4560b4af7_flash_display_Sprite()
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
