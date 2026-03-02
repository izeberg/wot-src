package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _2a21b42e0827a5e96ccf3c6a17cdd8c2c1a3aac322e36344992a73ef2c3f8fbe_flash_display_Sprite extends Sprite
   {
       
      
      public function _2a21b42e0827a5e96ccf3c6a17cdd8c2c1a3aac322e36344992a73ef2c3f8fbe_flash_display_Sprite()
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
