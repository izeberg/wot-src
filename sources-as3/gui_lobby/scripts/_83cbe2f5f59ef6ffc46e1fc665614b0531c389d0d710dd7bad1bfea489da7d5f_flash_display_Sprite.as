package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _83cbe2f5f59ef6ffc46e1fc665614b0531c389d0d710dd7bad1bfea489da7d5f_flash_display_Sprite extends Sprite
   {
       
      
      public function _83cbe2f5f59ef6ffc46e1fc665614b0531c389d0d710dd7bad1bfea489da7d5f_flash_display_Sprite()
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
