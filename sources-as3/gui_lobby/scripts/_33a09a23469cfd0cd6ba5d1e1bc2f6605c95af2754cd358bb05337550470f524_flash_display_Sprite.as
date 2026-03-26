package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _33a09a23469cfd0cd6ba5d1e1bc2f6605c95af2754cd358bb05337550470f524_flash_display_Sprite extends Sprite
   {
       
      
      public function _33a09a23469cfd0cd6ba5d1e1bc2f6605c95af2754cd358bb05337550470f524_flash_display_Sprite()
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
