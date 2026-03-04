package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _dbca62d56741148d609b2201e9f359007d5d8ef25ad5adabc66de332dfb450a7_flash_display_Sprite extends Sprite
   {
       
      
      public function _dbca62d56741148d609b2201e9f359007d5d8ef25ad5adabc66de332dfb450a7_flash_display_Sprite()
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
