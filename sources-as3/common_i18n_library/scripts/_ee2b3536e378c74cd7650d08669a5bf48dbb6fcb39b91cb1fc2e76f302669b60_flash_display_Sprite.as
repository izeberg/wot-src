package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ee2b3536e378c74cd7650d08669a5bf48dbb6fcb39b91cb1fc2e76f302669b60_flash_display_Sprite extends Sprite
   {
       
      
      public function _ee2b3536e378c74cd7650d08669a5bf48dbb6fcb39b91cb1fc2e76f302669b60_flash_display_Sprite()
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
