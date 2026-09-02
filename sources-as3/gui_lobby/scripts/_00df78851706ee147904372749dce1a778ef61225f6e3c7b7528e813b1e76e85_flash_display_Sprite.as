package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _00df78851706ee147904372749dce1a778ef61225f6e3c7b7528e813b1e76e85_flash_display_Sprite extends Sprite
   {
       
      
      public function _00df78851706ee147904372749dce1a778ef61225f6e3c7b7528e813b1e76e85_flash_display_Sprite()
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
