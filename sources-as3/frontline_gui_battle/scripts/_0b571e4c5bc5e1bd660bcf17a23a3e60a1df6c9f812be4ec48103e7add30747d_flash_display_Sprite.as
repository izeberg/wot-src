package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _0b571e4c5bc5e1bd660bcf17a23a3e60a1df6c9f812be4ec48103e7add30747d_flash_display_Sprite extends Sprite
   {
       
      
      public function _0b571e4c5bc5e1bd660bcf17a23a3e60a1df6c9f812be4ec48103e7add30747d_flash_display_Sprite()
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
