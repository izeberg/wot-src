package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _658455b5b51e655a3e04c13e6927d4d906e74a8fc03125a1ddbad47689d75f8e_flash_display_Sprite extends Sprite
   {
       
      
      public function _658455b5b51e655a3e04c13e6927d4d906e74a8fc03125a1ddbad47689d75f8e_flash_display_Sprite()
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
