package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _82b9b0ecd6f072df5c98cb6dc7b9a3866f8f026ebe429cea4d31c464c5057283_flash_display_Sprite extends Sprite
   {
       
      
      public function _82b9b0ecd6f072df5c98cb6dc7b9a3866f8f026ebe429cea4d31c464c5057283_flash_display_Sprite()
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
