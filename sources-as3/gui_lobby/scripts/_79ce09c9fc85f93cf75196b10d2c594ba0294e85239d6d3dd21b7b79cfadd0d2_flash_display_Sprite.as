package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _79ce09c9fc85f93cf75196b10d2c594ba0294e85239d6d3dd21b7b79cfadd0d2_flash_display_Sprite extends Sprite
   {
       
      
      public function _79ce09c9fc85f93cf75196b10d2c594ba0294e85239d6d3dd21b7b79cfadd0d2_flash_display_Sprite()
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
