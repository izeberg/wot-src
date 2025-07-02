package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1daeb750c75c71c95632134a9d9f71b5869e82a2f64d9512ff35c5381443e343_flash_display_Sprite extends Sprite
   {
       
      
      public function _1daeb750c75c71c95632134a9d9f71b5869e82a2f64d9512ff35c5381443e343_flash_display_Sprite()
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
