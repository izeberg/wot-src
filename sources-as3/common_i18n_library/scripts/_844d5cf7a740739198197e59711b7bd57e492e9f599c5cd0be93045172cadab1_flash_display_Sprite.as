package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _844d5cf7a740739198197e59711b7bd57e492e9f599c5cd0be93045172cadab1_flash_display_Sprite extends Sprite
   {
       
      
      public function _844d5cf7a740739198197e59711b7bd57e492e9f599c5cd0be93045172cadab1_flash_display_Sprite()
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
