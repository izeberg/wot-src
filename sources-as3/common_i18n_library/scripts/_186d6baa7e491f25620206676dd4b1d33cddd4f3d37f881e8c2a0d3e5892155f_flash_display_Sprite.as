package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _186d6baa7e491f25620206676dd4b1d33cddd4f3d37f881e8c2a0d3e5892155f_flash_display_Sprite extends Sprite
   {
       
      
      public function _186d6baa7e491f25620206676dd4b1d33cddd4f3d37f881e8c2a0d3e5892155f_flash_display_Sprite()
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
