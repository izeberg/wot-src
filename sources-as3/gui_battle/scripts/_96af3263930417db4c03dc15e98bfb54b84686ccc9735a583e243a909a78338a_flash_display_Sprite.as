package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _96af3263930417db4c03dc15e98bfb54b84686ccc9735a583e243a909a78338a_flash_display_Sprite extends Sprite
   {
       
      
      public function _96af3263930417db4c03dc15e98bfb54b84686ccc9735a583e243a909a78338a_flash_display_Sprite()
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
